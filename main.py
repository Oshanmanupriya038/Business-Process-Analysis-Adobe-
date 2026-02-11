import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

ticker = 'ADBE'
print(f"Downloading data for {ticker}...")

try:
    df = yf.download(ticker, start='2023-01-01', end='2025-12-31')
    
    if df.empty:
        print(f"Error: No data found for {ticker}.")
    else:
        df = df[['Close']]
        df['Date_Index'] = np.arange(len(df))

        X = df[['Date_Index']] 
        y = df['Close']      

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
        
        model = LinearRegression()
        model.fit(X_train, y_train)

        plt.figure(figsize=(12,6))
        plt.plot(df.index, df['Close'], label='Actual Price')
        plt.plot(df.index, model.predict(X), label='Linear Trend', color='red')
        plt.title(f'Adobe (ADBE) Stock Price Analysis & Prediction')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.legend()
        plt.show()

        df.to_csv('adobe_stock_data.csv')
        print(f"Successfully processed {ticker} data.")
        print("CSV file 'adobe_stock_data.csv' has been saved.")

except Exception as e:
    print(f"An error occurred: {e}")

    