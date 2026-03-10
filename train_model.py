import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score

# load dataset
df = pd.read_csv("Salary Data.csv")

# remove missing values
df = df.dropna()

# encoders
gender_encoder = LabelEncoder()
edu_encoder = LabelEncoder()
job_encoder = LabelEncoder()

# encode categorical columns
df["Gender"] = gender_encoder.fit_transform(df["Gender"])
df["Education Level"] = edu_encoder.fit_transform(df["Education Level"])
df["Job Title"] = job_encoder.fit_transform(df["Job Title"])

# features
X = df[["Age","Gender","Education Level","Job Title","Years of Experience"]]
y = df["Salary"]

# split dataset
X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)

# train model
model = LinearRegression()
model.fit(X_train,y_train)

# prediction for accuracy
y_pred = model.predict(X_test)

score = r2_score(y_test,y_pred)

print("Model Accuracy (R2 Score):",score)

# save model
pickle.dump(model,open("model.pkl","wb"))
pickle.dump(gender_encoder,open("gender.pkl","wb"))
pickle.dump(edu_encoder,open("edu.pkl","wb"))
pickle.dump(job_encoder,open("job.pkl","wb"))

print("Model saved successfully")