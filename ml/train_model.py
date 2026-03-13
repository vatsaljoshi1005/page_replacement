import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

data=pd.read_csv("../data/ml_dataset.csv")
X=data[["frame1","frame2","frame3","next_page"]]
y=data["evict_page"]

model=RandomForestClassifier(n_estimators=100)
model.fit(X,y)
joblib.dump(model, "model.pkl")