import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

model=LogisticRegression()

df=pd.read_csv("student.csv")
print(df.head())
print(df.tail())
print(df.columns)
print(df.describe())
print(df.info())
print(df.shape)
x=df[["StudyHours", "Attendance"]]
y=df["Performance"]
train_x, test_x, train_y, test_y = train_test_split(x,
 y, test_size=0.2, random_state=42)
print("training data")
print(train_x)
print("test data")
print(test_x)
print("training labels")
print(train_y)
print("test labels")
print(test_y)
model.fit(train_x, train_y)
print("model trained successfully")
study_hours = float(input("Enter Study Hours: "))
attendance = float(input("Enter Attendance (%): "))

new_student = pd.DataFrame({
    "StudyHours": [study_hours],
    "Attendance": [attendance]
})

prediction = model.predict(new_student)

if prediction[0] == 1:
    print("Prediction: Pass")
else:
    print("Prediction: Fail")

accuracy = model.score(test_x, test_y)
print("Accuracy:", accuracy)

