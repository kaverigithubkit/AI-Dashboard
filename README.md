AI Dashboard (Python Flask + Pandas + Plotly)

This project is an interactive AI-style data dashboard built using Python, Flask, Pandas, and Plotly.
Users can upload a CSV file, and the system automatically generates KPIs and visual charts such as Monthly Sales, Store Sales, Holiday Sales, and Temperature Correlation.

Features:
- CSV upload via web interface
- Automatic data processing with Pandas
- Interactive charts using Plotly
- KPIs: Total Sales, Total Stores, Avg Order Value, Holiday Sales
- Dashboard template rendered with Flask and Jinja
- Fully responsive HTML dashboard

Tech Stack:
Backend: Python, Flask
Data Processing: Pandas
Charts: Plotly
Frontend: HTML, CSS, Bootstrap
Upload Handling: Flask File Upload

How It Works:
1. User uploads a CSV file
2. File is stored in the uploads folder
3. Pandas loads and processes data
4. KPIs are calculated
5. Plotly generates chart HTML
6. Dashboard displays KPIs and charts

How to Run:
1. Install libraries:
   pip install flask pandas plotly
2. Run application:
   python app.py
3. Open in browser:
   http://127.0.0.1:5000
4. Upload a CSV to generate dashboard

Project Structure:
app.py
templates/
   upload.html
   dashboard.html
uploads/
static/

Charts Generated:
- Monthly Sales (Bar)
- Sales by Store (Bar)
- Holiday vs Non-Holiday (Pie)
- Temperature vs Weekly Sales (Scatter)

Future Enhancements:
- AI forecasting with Prophet or LSTM
- Login authentication
- Multi-file comparison
- Export charts
- Cloud deployment

Author:
Your Name
Your Email
LinkedIn Profile Link
