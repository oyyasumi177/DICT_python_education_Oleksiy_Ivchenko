import requests

base_currency = input().lower()

url = "http://www.floatrates.com/daily/" + base_currency + ".json"
response = requests.get(url)

cache = {}

if response.status_code == 200:
    rates_data = response.json()

    if base_currency != "usd":
        cache["usd"] = rates_data["usd"]["rate"]
    if base_currency != "eur":
        cache["eur"] = rates_data["eur"]["rate"]

    while True:
        target_currency = input().strip().lower()
        if not target_currency:
            break

        amount = float(input())

        print("Checking the cache...")

        if target_currency in cache:
            print("It is in the cache!")
            rate = cache[target_currency]
        else:
            print("Sorry, but it is not in the cache!")
            rate = rates_data[target_currency]["rate"]
            cache[target_currency] = rate

        received = round(amount * rate, 2)
        print("You received " + str(received) + " " + target_currency.upper() + ".")