import pandas as pd
import yfinance as yf

atvi = yf.Ticker("atvi")


# get historical market data
hist = atvi.history(period="3y")
hist1 = atvi.history(period="1mo")

hist["difference"] = hist["Close"] - hist["Open"]
hist.loc[hist["difference"] > 0, "futureOpen"] = 1
hist.loc[hist["difference"] <= 0, "futureOpen"] = 0

hist1["difference"] = hist1["Close"] - hist1["Open"]
hist1.loc[hist1["difference"] > 0, "futureOpen"] = 1
hist1.loc[hist1["difference"] <= 0, "futureOpen"] = 0

hist.to_csv("yfinanceData3yr.csv")
hist1.to_csv("yfinanceData1month.csv")






