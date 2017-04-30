from sklearn.preprocessing import MinMaxScaler
import pickle
import pandas as pd

def preprocess(X):
    min_max_scaler = MinMaxScaler()
    return min_max_scaler.fit_transform(X)

def predict(X):
    clf2 = pickle.load(open("best_radiation.pkl", "rb"))
    X= pd.Series({"barometric": X[0], "humidity": X[1],
                  "speed": X[2], "temp": X[3], "direction":X[4]})
    return clf2.predict(X)

def calculate(radiation, panel_area, efficiency):
    return radiation * panel_area * efficiency

def do_all(X,panel_area, efficiency):
    return calculate(predict(preprocess(X)), panel_area, efficiency)
