from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sklearn import svm
import pandas as pd
import numpy as np

# Train classifier
train_set = pd.read_csv("./train-set.csv", usecols=["EMA_diff", "SMA_diff"])
train_label = pd.read_csv("./train-set.csv", usecols=["is_profitable"])
X = train_set.values.tolist()
y = train_label.values.tolist()
y = np.ravel(y)
clf = svm.SVC()
clf.fit(X, y)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def get_prediction(ema_diff: int, sma_diff: int):
    
    sample = [[ema_diff, sma_diff]]
    print(sample)
    prediction = clf.predict(sample)

    return prediction[0]

