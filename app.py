import os
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load dataset dynamically
df = None


def create_charts(df):
    # Convert Date column
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors="coerce")
    df["Month"] = df["Date"].dt.strftime("%B")


    # KPIs
    total_sales = df["Weekly_Sales"].sum()
    total_orders = df["Store"].nunique()
    avg_order_value = total_sales / total_orders
    holiday_sales = df[df["Holiday_Flag"] == 1]["Weekly_Sales"].sum()

    # --- Charts ---
    # 1. Monthly Sales
    monthly = df.groupby("Month")["Weekly_Sales"].sum().reset_index()
    fig_month = px.bar(monthly, x="Month", y="Weekly_Sales", title="Monthly Sales",
                       color="Weekly_Sales", color_continuous_scale="Blues")

    # 2. Sales by Store
    store_sales = df.groupby("Store")["Weekly_Sales"].sum().reset_index()
    fig_store = px.bar(store_sales, x="Store", y="Weekly_Sales",
                       title="Sales by Store", color="Weekly_Sales")

    # 3. Sales on Holidays vs Non-Holidays
    holiday_sales_df = df.groupby("Holiday_Flag")["Weekly_Sales"].sum().reset_index()
    holiday_sales_df["Holiday_Flag"] = holiday_sales_df["Holiday_Flag"].map({0: "Non-Holiday", 1: "Holiday"})
    fig_holiday = px.pie(holiday_sales_df, names="Holiday_Flag", values="Weekly_Sales",
                         title="Holiday vs Non-Holiday Sales", hole=0.4)

    # 4. Correlation with Temperature
    fig_temp = px.scatter(df, x="Temperature", y="Weekly_Sales", size="Fuel_Price",
                          color="Unemployment", hover_data=["Store"],
                          title="Sales vs Temperature")

    charts = {
        "month_chart": pio.to_html(fig_month, full_html=False),
        "store_chart": pio.to_html(fig_store, full_html=False),
        "holiday_chart": pio.to_html(fig_holiday, full_html=False),
        "temp_chart": pio.to_html(fig_temp, full_html=False),
    }

    return total_sales, total_orders, avg_order_value, holiday_sales, charts


@app.route("/", methods=["GET", "POST"])
def index():
    global df
    if request.method == "POST":
        file = request.files["file"]
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            df = pd.read_csv(filepath)
            return redirect(url_for("dashboard"))
    return render_template("upload.html")


@app.route("/dashboard")
def dashboard():
    global df
    if df is None:
        return redirect(url_for("index"))

    total_sales, total_orders, avg_order_value, holiday_sales, charts = create_charts(df)

    return render_template("dashboard.html",
                           total_sales=total_sales,
                           total_orders=total_orders,
                           avg_order_value=avg_order_value,
                           holiday_sales=holiday_sales,
                           **charts)


if __name__ == "__main__":
    app.run(debug=True)
