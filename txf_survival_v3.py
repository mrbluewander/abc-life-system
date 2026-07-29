
import pandas as pd

def calculate_vwap(df):
    """Calculate VWAP"""
    try:
        vwap = df['VWAP'].dropna().iloc[-1]
        return vwap
    except IndexError:
        return None

def calculate_atr(df):
    """Calculate ATR"""
    try:
        atr = df['ATR'].dropna().iloc[-1]
        return atr
    except IndexError:
        return None

def calculate_max_contracts(df):
    """Calculate max contracts"""
    try:
        max_contracts = int(df['Contracts'].dropna().max())
        return max_contracts
    except (IndexError, ValueError):
        return 0

def main():
    # Sample dataframe
    data = {
        'VWAP': [10.0, 11.0, float('nan'), 12.0],
        'ATR': [1.0, 2.0, 3.0, float('nan')],
        'Contracts': [10, 20, float('nan'), 30]
    }
    df = pd.DataFrame(data)

    vwap = calculate_vwap(df)
    atr = calculate_atr(df)
    max_contracts = calculate_max_contracts(df)

    print(f"VWAP: {vwap}, ATR: {atr}, Max Contracts: {max_contracts}")

if __name__ == "__main__":
    main()
