import requests
from datetime import datetime

# https://jsonviewer.stack.hu
# https://newsapi.org/docs/get-started#search
# https://www.alphavantage.co/documentation/

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# Stock API
# API key: BQCGHABP9UOUW3TI

# News API
NEWS_API_KEY = "4c3bb1cc8212411e8b3d846360c9e919"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

# day = datetime.now().day
# yesterday = str(day - 1)
# month = str(datetime.now().month)
# year = str(datetime.now().year)
# hour = "20:00:00"
# yesterday_date = year + "-" + month + "-" + yesterday
# print(yesterday_date)

params = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK_NAME,
    "interval": "60min",
    "apikey": NEWS_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params)
response.raise_for_status()
data = response.json()
yesterday_closing_price = data["Time Series (60min)"]["2023-05-09 20:00:00"]["4. close"]
print(yesterday_closing_price)

#TODO 2. - Get the day before yesterday's closing stock price

day_before_yesterday_closing_price = int(data["Time Series (60min)"]["2023-05-08 20:00:00"]["4. close"])
print(day_before_yesterday_closing_price)
print(type(day_before_yesterday_closing_price))

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

# price_different = abs(day_before_yesterday_closing_price - yesterday_closing_price)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

# percentage_difference = price_different / day_before_yesterday_closing_price
# print(percentage_difference)
# print(type(percentage_difference))

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").



    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio.



#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

