# -*- coding: utf-8 -*-
"""Codsoft_task_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d6w0YscI7LoiYUATmxo9NiKAlxGeTMnX
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import xgboost as xgb
from sklearn.metrics import mean_squared_error, r2_score

df=pd.read_csv('advertising.csv')

df

X = df[['TV', 'Radio', 'Newspaper']]
y = df['Sales']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = Sequential()
model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='linear'))

model.compile(loss='mean_squared_error', optimizer='adam')

model.fit(X_train, y_train, epochs=100, batch_size=32, verbose=1)

mse = model.evaluate(X_test, y_test, verbose=0)
print(f"Mean Squared Error: {mse}")

new_data = pd.DataFrame({
    'TV': [250],
    'Radio': [40],
    'Newspaper': [20]
})

new_data_scaled = scaler.transform(new_data)

predicted_sales = model.predict(new_data_scaled)
print(f"Predicted Sales for New Data: {predicted_sales[0][0]}")

model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

plt.scatter(y_test, y_pred)
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs. Predicted Sales (XGBoost Regression)")
plt.show()

new_data = pd.DataFrame({
    'TV': [250],
    'Radio': [40],
    'Newspaper': [20]
})

predicted_sales = model.predict(new_data)
print(f"Predicted Sales for New Data: {predicted_sales[0]}")