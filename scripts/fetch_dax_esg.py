from datetime import datetime
from pathlib import Path
import json
import polars as pl
import yfinance as yf
# TODO make auto create list from XETRA or wiki
DAX_TICKERS = [
    "ADS.DE", "ALV.DE", "BAS.DE", "BAYN.DE", "BEI.DE", "BMW.DE",
    "CON.DE", "1COV.DE", "DAI.DE", "DB1.DE", "DBK.DE", "DPW.DE",
    "DTE.DE", "EOAN.DE", "FME.DE", "FRE.DE", "HEI.DE", "HEN3.DE",
    "IFX.DE", "LIN.DE", "MRK.DE", "MTX.DE", "MUV2.DE", "PUM.DE",
    "QIA.DE", "RWE.DE", "SAP.DE", "SIE.DE", "VNA.DE", "VOW3.DE"
]

def fetch_esg_data(tickers):
    records = []
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker) # TODO check response structure to find "esg"
            info = stock.info
            if 'esgScores' in info:
                esg = info['esgScores']
                record = {
                    "company": info.get("longName", ticker),
                    "ticker": ticker,
                    "industry": info.get("industry", "N/A"),
                    "esg_score": {
                        "environment": esg.get("environmentScore"),
                        "social": esg.get("socialScore"),
                        "governance": esg.get("governanceScore"),
                        "total": esg.get("totalEsg"),
                    },
                    "controversy_level": esg.get("peerCount"),
                    "source": "yfinance",
                    "retrieved_at": datetime.utcnow().isoformat()
                }
                records.append(record)
                print(f'Fetched ESG for {ticker}')
            else:
                print(f'No ESG data for {ticker}')
        except Exception as e:
            print(f'[x] Error for {ticker}: {e}')
    return records

def save_data(records, output_dir='data/raw/'):
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    json_path = Path(output_dir) / 'esg_dax.json'
    csv_path = Path(output_dir) / 'esg_dax.scv'

    with open(json_path, 'w') as f:
        json.dump(records, f, indent=4)
    
    df = pl.json_normalize(records)
    df.to_csv(csv_path, index=False) # TODO Polars DataFrame object has no attribute 'to_csv'

    print(f'File saved to json {json_path}')
    print(f'File saved to csv {csv_path}')

if __name__ == '__main__':
    data = fetch_esg_data(DAX_TICKERS)
    save_data(data)