import requests

API_URL = "https://api.coingecko.com/api/v3/simple/price"

def get_crypto_price(crypto, currency="usd"):
    try:
        response = requests.get(
            API_URL,
            params={
                "ids": crypto,
                "vs_currencies": currency
            },
            timeout=5
        )

        if response.status_code != 200:
            print("Failed to fetch data from API.")
            return

        data = response.json()

        if crypto not in data:
            print("Invalid cryptocurrency name.")
            return

        price = data[crypto][currency]
        print(f" {crypto.upper()} price: {price} {currency.upper()}")

    except requests.exceptions.RequestException as e:
        print("Network error:", e)
    except ValueError:
        print("Error parsing API response.")

def main():
    print("Cryptocurrency Price Checker")
    crypto = input("Enter cryptocurrency (e.g., bitcoin, ethereum): ").lower()
    get_crypto_price(crypto)

if __name__ == "__main__":
    main()
