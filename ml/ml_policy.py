import joblib
import pandas as pd

model=joblib.load("ml/model.pkl")

def ml_replace(frames,page):
    features=pd.DataFrame(
        [[frames[0],frames[1],frames[2],page]],
        columns=["frame1","frame2","frame3","next_page"]
    )
    prediction=model.predict(features)
    return prediction[0]