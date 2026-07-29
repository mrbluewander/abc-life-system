import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def calculate_vwap(high, low, close, volume):
    typical_price = (high + low + close) / 3
    vwap = typical_price.groupby(typical_price.index.date).apply(lambda x: (x * volume).cumsum() / volume.cumsum())
    return vwap

def calculate_atr(high, low, close, window=14):
    hl = high - low
    hc = np.abs(high - close.shift(1))
    lc = np.abs(low - close.shift(1))
    tr = np.maximum(hl, np.maximum(hc, lc))
    atr = tr.rolling(window).mean()
    return atr

def calculate_dynamic_stop_loss(atr):
    return atr * 1.5

def calculate_max_contracts(margin_cap, max_risk, price, atr):
    dynamic_stop_loss = calculate_dynamic_stop_loss(atr)
    max_contracts = (margin_cap * max_risk) / (price * dynamic_stop_loss)
    return max_contracts

def main():
    ticker = "^TWII"
    data = yf.download(ticker, period="5d", interval="1m")
    data['typical_price'] = (data['High'] + data['Low'] + data['Close']) / 3
    vwap = calculate_vwap(data['High'], data['Low'], data['Close'], data['Volume'])

    atr = calculate_atr(data['High'], data['Low'], data['Close'])

    margin_cap = 600000
    max_risk = 0.02
    price = data['Close'].iloc[-1]
    dynamic_stop_loss = calculate_dynamic_stop_loss(atr.iloc[-1])
    max_contracts = calculate_max_contracts(margin_cap, max_risk, price, atr.iloc[-1])

    report = f"### TWII Survival Report\n"
    report += f"#### VWAP: {vwap.iloc[-1]}\n"
    report += f"#### ATR: {atr.iloc[-1]}\n"
    report += f"#### Dynamic Stop Loss: {dynamic_stop_loss}\n"
    report += f"#### Max Contracts: {max_contracts}\n"
    report += f"#### Margin Cap: {margin_cap}\n"
    report += f"#### Max Risk: {max_risk * 100}%\n"

    with open("txf_survival_report.md", "w") as f:
        f.write(report)

    print(report)

if __name__ == "__main__":
    main()