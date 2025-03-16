# 📈 Crypto Portfolio Rebalancer

A Python script to **rebalance your cryptocurrency portfolio** based on real-time prices from CoinMarketCap. It calculates the necessary buy/sell adjustments to match the desired asset allocation, ensuring your investments remain aligned with your strategy.

---

## 🚀 Features

- Fetches **real-time cryptocurrency prices** from CoinMarketCap.
- Computes **current vs. target portfolio allocation**.
- Suggests **buy/sell actions** to rebalance the portfolio.
- Uses **precise decimal calculations** to avoid rounding errors.
- Outputs a **detailed JSON report** with adjustments.

---

## 🛠 Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/niklod/crypto-rebalancer.git
   cd crypto-rebalancer
   ```

2. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

3. Create an `.env` file and fill in your **CoinMarketCap API credentials**:

   ```sh
   COIN_MARKET_CAP_BASE_URL=https://pro-api.coinmarketcap.com
   COIN_MARKET_CAP_PRICE_URL=/v1/cryptocurrency/quotes/latest
   COIN_MARKET_CAP_API_KEY=your_api_key_here
   ```

---

## 📊 Usage

1. Prepare an **input file** (`input.json`) defining your portfolio structure:

   ```json
   {
       "assets": [
           {
               "id": "bitcoin",
               "ticker": "BTC",
               "amount": 1.0,
               "allocation": 0.7
           },
           {
               "id": "ethereum",
               "ticker": "ETH",
               "amount": 1.0,
               "allocation": 0.2
           },
           {
               "id": "usd-coin",
               "ticker": "USDC",
               "amount": 1.0,
               "allocation": 0.1
           }
       ]
   }
   ```

2. Run the script:

   ```sh
   python main.py
   ```

---

## 📜 Output Format

The script returns a **structured JSON report** with **current allocations**, **target allocations**, and **suggested actions** to rebalance your portfolio:

```json
[
    {
        "ticker": "BTC",
        "current_amount": "1.0",
        "current_value": "63000.00",
        "current_percent": "63.00 %",
        "target_value": "70000.00",
        "delta_value": "7000.00",
        "delta_amount": "0.11111111",
        "action": "buy"
    },
    {
        "ticker": "ETH",
        "current_amount": "1.0",
        "current_value": "3500.00",
        "current_percent": "3.50 %",
        "target_value": "20000.00",
        "delta_value": "16500.00",
        "delta_amount": "4.71428571",
        "action": "buy"
    }
]
```

### **Fields Explained:**

- `ticker` – Asset symbol (e.g., BTC, ETH, USDC).
- `current_amount` – Number of units currently held.
- `current_value` – Current value in USD.
- `current_percent` – Percentage of total portfolio held.
- `target_value` – Desired portfolio value based on allocation.
- `delta_value` – USD difference between current and target value.
- `delta_amount` – Number of units to buy or sell.
- `action` – Suggested action (`"buy"`, `"sell"`, or `"hold"`).

---

## ⚡ License

This project is licensed under the **MIT License**. Contributions are welcome!
