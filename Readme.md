# 💰 Salary Prediction Using Machine Learning

## 📌 Project Overview

This project predicts the **estimated salary of a person** based on different factors such as **Age, Gender, Education Level, Job Title, and Years of Experience**.
The system uses a **Machine Learning Regression model** and a **Flask web application** to provide an interactive interface for users to input their details and get a salary prediction.

---

## 🚀 Features

* Predict salary using Machine Learning
* User-friendly web interface
* Input fields for:

  * Age
  * Gender
  * Education Level
  * Job Title
  * Years of Experience
* Real-time salary prediction
* Error handling for unknown inputs
* Offline dataset support

---

## 🛠 Technologies Used

* **Python**
* **Flask**
* **NumPy**
* **Pandas**
* **Scikit-learn**
* **HTML**
* **CSS**

---

## 📂 Project Structure

```
Salary_Prediction_Using_Regression
│
├── app.py                # Flask application
├── train_model.py        # Machine learning model training script
├── model.pkl             # Trained ML model
├── gender.pkl            # Gender encoder
├── edu.pkl               # Education encoder
├── job.pkl               # Job title encoder
├── Salary Data.csv       # Dataset
│
├── templates
│   └── index.html        # Frontend UI
│
└── README.md
```

---

## 📊 Dataset

The dataset contains the following features:

* Age
* Gender
* Education Level
* Job Title
* Years of Experience
* Salary (Target Variable)

The dataset is used to train a **Linear Regression model** for predicting salary.

---

## ⚙️ How to Run the Project

### 1️⃣ Clone the repository

```
git clone https://github.com/yourusername/Salary-Prediction-ML.git
```

### 2️⃣ Navigate to project folder

```
cd Salary-Prediction-ML
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Train the model (optional)

```
python train_model.py
```

### 5️⃣ Run the Flask app

```
python app.py
```

### 6️⃣ Open in browser

```
http://127.0.0.1:5000/
```

---

## 🧠 Machine Learning Model

The project uses **Linear Regression** to predict salary based on multiple input features.
Categorical features such as Gender, Education Level, and Job Title are encoded using label encoders.

---

## 📸 Project Output

The user enters details in the web form and the system returns:

```
Estimated Salary : ₹ XXXXX
```

---

## 👨‍💻 Author

**Mohd Nazim**
B.Tech CSE (AI & ML)

---

## 📜 License

This project is created for **educational and learning purposes**.
