# KidneyHealthWatch
A machine learning project to predict and prevent chronic kidney disease.
Project Overview
Kidney Health Watch is an API-based Chronic Kidney Disease (CKD) risk prediction system. This project utilizes machine learning to predict the likelihood of CKD based on patient health parameters. It is designed to assist healthcare professionals and individuals in early detection and preventive care.

Live API: https://kidneyhealthwatch-1.onrender.com/docs

📜 Table of Contents
Features
Tech Stack
Installation
Endpoints
Deployment
Contributing

🌟 Features
✅ Predict CKD risk based on user input parameters.
✅ Uses machine learning models for high accuracy.
✅ Provides an API-based approach for easy integration with web & mobile apps.
✅ FastAPI for performance and auto-generated Swagger UI documentation.
✅ Dockerized for seamless deployment.
✅ Hosted on Render for cloud accessibility.

🛠 Tech Stack
Backend: FastAPI
Machine Learning: Scikit-Learn
Database: PostgreSQL (Planned for Future Integration)
Containerization: Docker
Deployment: Render
Version Control: Git & GitHub

💻 Installation
🔹 Prerequisites
Ensure you have the following installed on your system:
✅ Python 3.8+
✅ Git
✅ Virtualenv (pip install virtualenv)
✅ Docker (optional for containerization)

📡 API Endpoints
Method	   Endpoint	         Description
GET	           /	        Welcome message
GET	         /docs	      OpenAPI documentation
POST	    /predict	   Predict CKD risk

🎯 Deployment
🔹 Deploying on Render
The project is already deployed on Render at:
🔗 https://kidneyhealthwatch-1.onrender.com/docs

To redeploy:

Push your latest changes to GitHub.
Render will automatically pull and deploy changes.
If needed, trigger a manual redeploy from Render dashboard.

🤝 Contributing
Contributions are welcome! To contribute:

Fork the repository
Create a new branch (feature-xyz)
Commit changes and push to your fork
Open a pull request