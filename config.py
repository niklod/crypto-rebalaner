from dotenv import load_dotenv
import os

# Loads the configuration from .env file
def loadConfig():
    load_dotenv()

    return {
        'coin_market_cap_base_url': os.getenv('COIN_MARKET_CAP_BASE_URL'),
        'coin_market_cap_price_url': os.getenv('COIN_MARKET_CAP_PRICE_URL'),
        'coin_market_cap_api_key': os.getenv('COIN_MARKET_CAP_API_KEY')
    }