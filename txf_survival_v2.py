
import yfinance as yf
import pandas as pd
import numpy as np

def calculate_vwap(data):
    """Calculate Volume Weighted Average Price"""
    vwap = (data['Close'] * data['Volume']).cumsum() / data['Volume'].cumsum()
    return vwap

def calculate_atr(data, window=14):
    """Calculate Average True Range"""
    high_low = data['High'] - data['Low']
    high_close = np.abs(data['High'] - data['Close'].shift(1))
    low_close = np.abs(data['Low'] - data['Close'].shift(1))
    ranges = pd.concat([high_low, high_close, low_close], axis=1)
    true_range = ranges.max(axis=1)
    atr = true_range.ewm(span=window, adjust=False).mean()
    return atr

def main():
    # Get ^TWII data
    twii_data = yf.download('^TWII', period='1y')

    # Ensure max_contracts is an integer
    max_contracts = int(10)

    # Calculate VWAP and ATR
    twii_data['VWAP'] = calculate_vwap(twii_data)
    twii_data['ATR'] = calculate_atr(twii_data)

    # Format output as Markdown table
    output = []
    for index, row in twii_data.iterrows():
        if not np.isnan(row['VWAP']) and not np.isnan(row['ATR']):
            output.append([index, row['Close'], row['VWAP'], row['ATR']])

    print("| Date | Close | VWAP | ATR |")
    print("| --- | --- | --- | --- |")
    for row in output:
        print(f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} |")

if __name__ == "__main__":
    main()
