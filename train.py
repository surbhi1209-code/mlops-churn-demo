import pandas as pd
import joblib
import os
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("s3://mlops-free-demo/raw/churn.csv")

X = df.drop("churn", axis=1)
y = df["churn"]

model = RandomForestClassifier()
model.fit(X, y)

os.makedirs("/opt/ml/model", exist_ok=True)
joblib.dump(model, "/opt/ml/model/model.joblib")
