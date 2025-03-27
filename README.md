# Employee Retention Prediction

## Overview
Employee retention is a crucial aspect of workforce management. This project leverages Machine Learning to predict whether an employee is likely to stay or leave the company based on various factors. The application is built using Flask for the backend and JavaScript, HTML, and CSS for the frontend.

## Features
- Predicts employee retention based on input parameters
- User-friendly web interface
- Interactive visualizations to display predictions
- REST API for model inference

## Tech Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn

## Installation
### Prerequisites
- Python 3.x
- Flask
- Virtual environment (optional but recommended)

### Setup Instructions
1. Clone the repository:
   ```sh
   git clone https://github.com/vi-m-al-si-n-gh/Employee_Retention.git
   cd Employee_Retention
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Flask application:
   ```sh
   python app.py
   ```
5. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## Usage
1. Enter employee details into the web form.
2. Click "Predict" to get the retention prediction.
3. View results and suggestions based on the prediction.

## Project Structure
```
Employee_Retention/
│── static/          # CSS, JS, images
│── templates/       # HTML files
│── model/           # Machine learning model
│── app.py           # Flask application
│── requirements.txt # Dependencies
│── README.md        # Project documentation
```

## Future Enhancements
- Improve prediction accuracy with advanced ML models
- Add database integration for storing employee data
- Deploy the project on a cloud platform

## Contributors
- **Kumar Vimal Kirti Singh**
