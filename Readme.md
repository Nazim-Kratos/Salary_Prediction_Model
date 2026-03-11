💰 Salary Prediction Using Machine Learning

👨‍💻 Author

Mohd Nazim

B.Tech Computer Science Engineering (AI & ML)

📌 Project Title

Salary Prediction Using Machine Learning

📖 Project Description

This project predicts the estimated salary of an individual based on several factors such as Age, Gender, Education Level, Job Title, and Years of Experience.

The system uses a Machine Learning regression model to analyze these features and predict salary. A web interface built using Flask and HTML/CSS allows users to enter their information and receive a predicted salary instantly.

The goal of this project is to demonstrate how Machine Learning models can be integrated with web applications to create practical and interactive systems.

⚙️ Methodology

The project follows the following steps:

1️⃣ Data Collection

A dataset containing the following features is used:

Age

Gender

Education Level

Job Title

Years of Experience

Salary (Target Variable)

2️⃣ Data Preprocessing

Handling categorical variables using Label Encoding

Separating features (X) and target variable (Y)

3️⃣ Model Training

A Linear Regression model is trained using the dataset.

Libraries used:

NumPy

Pandas

Scikit-learn

The trained model is saved using Pickle (.pkl) for later use in the web application.

4️⃣ Model Deployment

The trained model is integrated with a Flask web application.

User workflow:

User enters input data in the web form

Flask sends the data to the trained ML model

The model processes the input

The predicted salary is returned and displayed on the webpage

📊 Results

The system successfully predicts the estimated salary based on the user inputs.

Example Output:

Estimated Salary : ₹ 8,50,000

The project demonstrates how machine learning models can be deployed in real-world applications using a web interface.

🛠 Technologies Used

Python

Flask

NumPy

Pandas

Scikit-learn

HTML

CSS

📂 Project Structure

Salary_Prediction_Using_Regression

│

├── app.py

├── train_model.py

├── model.pkl

├── gender.pkl

├── edu.pkl

├── job.pkl

├── Salary Data.csv

│

├── templates

│   └── index.html

│

└── README.md

🚀 How to Run the Project

1. Clone Repository
git clone https://github.com/yourusername/Salary-Prediction-ML.git
2. Go to Project Folder
cd Salary-Prediction-ML
3. Install Required Libraries
pip install -r requirements.txt
4. Train Model (Optional)
python train_model.py
5. Run Flask App
python app.py
6. Open Browser
http://127.0.0.1:5000/

📜 License


This project is developed for educational and learning purposes.
