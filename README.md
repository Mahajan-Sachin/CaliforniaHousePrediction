## 🏠 California House Price Prediction

This project is a complete End-to-End Machine Learning Pipeline built using Python, Flask, and Scikit-learn.
It predicts California housing prices based on various input features like median income, average rooms, population, etc.

-------

🚀 Project Overview

This project demonstrates the full ML lifecycle, from data preprocessing and model training to deployment using Flask.
It provides both a web interface (HTML form) and a REST API endpoint for predictions.

-------

📂 Project Structure

CaliforniaHousePrediction/

│

├── static/

│   └── style.css               # Styling for the frontend
│

├── templates/

│   └── home.html               # Frontend HTML form for input
│

├── house.pkl                   # Trained regression model

├── scaler.pkl                  # Scaler for input normalization

│

├── app.py                      # Flask app – handles routes and predictions

├── Dockerfile                  # For containerization and deployment

├── requirements.txt             # Dependencies list
│
└── README.md                   # Project documentation (you’re reading it)

-----

⚙️ Tech Stack

Layer	Technology Used

Language	Python

Framework	Flask

Libraries	Scikit-learn, NumPy, Pandas, Pickle

Deployment	Flask App (locally / Railway / Render / Docker)

Frontend	HTML, CSS (Jinja templates)

------

💡 Features

✅ Predict California house prices using user input
✅ Simple and clean web interface
✅ REST API endpoint for external integrations
✅ Scalable and production-ready Flask structure
✅ Docker-ready for container deployment

------

🧠 Model Details

The model is trained on the California Housing Dataset from Scikit-learn.
It uses a Linear Regression algorithm after scaling input features.

Input Features:

Median Income

House Age

Average Rooms

Average Bedrooms

Population

Average Occupancy

Latitude

Longitude

-------

🌐 Web App Routes

Route	Method	Description
/	GET	Renders the home page (form UI)
/predict	POST	Handles form data and returns prediction on web
/predict_api	POST	Handles raw JSON data for API requests


🧩 Example Usage


▶️ 1. Using the Web App

Enter the required values in the form and click Predict — the model will return the estimated house price.

▶️ 2. Using the API (via Postman or curl)

POST Request:

POST http://localhost:8080/predict_api
Content-Type: application/json
{
    "data": {
        "MedInc": 8.3252,
        "HouseAge": 41,
        "AveRooms": 6.9841,
        "AveBedrms": 1.0238,
        "Population": 322,
        "AveOccup": 2.5556,
        "Latitude": 37.88,
        "Longitude": -122.23
    }
}


Response:

{
    "prediction": 4.526
}

🐳 Run with Docker
# Build image
docker build -t california-house-app .

# Run container
docker run -p 8080:8080 california-house-app

--------

⚡ Deployment

You can deploy this project easily on:

Railway.app (recommended for free hosting)

Render.com

Heroku (legacy option)

Docker Hub + any VPS

----------

👨‍💻 Author

Sachin Mahajan
🎓 B.Tech CSE (AI/ML Specialization) | LPU
5. [![Deploy to Railway](https://github.com/Mahajan-Sachin/CaliforniaHousePrediction/actions/workflows/deploy_railway.yml/badge.svg)](https://github.com/Mahajan-Sachin/CaliforniaHousePrediction/actions/workflows/deploy_railway.yml)
