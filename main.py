import requests
import json
from decimal import Decimal, ROUND_DOWN
from config import loadConfig



# Reads "input.json" file from the root of the project
def loadAssetsInput():
    with open('input.json') as f:
        data = json.load(f)  

    return data

# Validates the total amout of assets in the input file
# Sum of the assets should exactly 1 (100% of the portfolio)
def validateTotalAmountOfAssets(data):
    total = Decimal(0)
    for asset in data['assets']:
        total += Decimal(asset['allocation'])

    if not (Decimal('0.9999') <= total <= Decimal('1.0001')):
        raise ValueError('Total amount of allocations should be 1')

# Enriches the list of assets with the current price of each asset
# using coinmarketcap API
def enrichAssetsWithPrice(cfg, data):
    url = cfg['coin_market_cap_base_url'] + cfg['coin_market_cap_price_url']
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': cfg['coin_market_cap_api_key']
    }

    slugs = []
    for asset in data['assets']:
        slugs.append(asset['id'])

    response = requests.get(url, headers=headers, params={'slug': ','.join(slugs)})
    if response.status_code != 200:
        raise ValueError('Failed to get prices from CoinMarketCap API')

    response = response.json()

    processCoinMarketCapResponse(data, response)

    return data


def processCoinMarketCapResponse(data, response):
    for asset in data['assets']:
        for k, v in response['data'].items():
            if v['slug'] == asset['id']:
                asset['price'] = v['quote']['USD']['price']


def calculatePortfolioValue(data):
    total_value = Decimal(0)
    for asset in data["assets"]:
        asset["current_value"] = Decimal(asset["amount"]) * Decimal(asset["price"])
        total_value += asset["current_value"]
    
    return total_value

# Determines buy/sell actions to rebalance the portfolio
def calculateRebalancing(data, total_value):
    adjustments = []

    for asset in data["assets"]:
        target_value = Decimal(asset["allocation"]) * total_value
        current_value = asset["current_value"]
        price = Decimal(asset["price"])

        # Calculate current allocation percentage
        current_percent = (current_value / total_value * 100).quantize(
            Decimal("0.01"), rounding=ROUND_DOWN
        )

        # Calculate the difference
        delta_value = target_value - current_value
        delta_amount = (delta_value / price).quantize(
            Decimal("0.00000001"), rounding=ROUND_DOWN
        )

        action = "buy" if delta_value > 0 else "sell" if delta_value < 0 else "hold"

        adjustments.append(
            {
                "ticker": asset["ticker"],
                "current_amount": str(asset["amount"]),
                "current_value": str(current_value),
                "current_percent": str(current_percent) + " %",
                "target_value": str(target_value),
                "delta_value": str(delta_value),
                "delta_amount": str(delta_amount),
                "action": action,
            }
        )

    return adjustments

if __name__ == '__main__':
    cfg = loadConfig()
    data = loadAssetsInput()

    validateTotalAmountOfAssets(data)
    data = enrichAssetsWithPrice(cfg, data)

    total_value = calculatePortfolioValue(data)
    adjustments = calculateRebalancing(data, total_value)

    print(json.dumps(adjustments, indent=4))