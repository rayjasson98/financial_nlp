import requests
import csv


def fetch_financial_news():
    url = 'https://api.marketaux.com/v1/news/all'

    params = {
        'api_token': 'knyI5AAk1Pf1RXTSbulPp3LGX7rzPb9oO5WnyRTS',
        'countries': 'my',
        'filter_entities': 'true',
        'limit': 3,
    }

    for page in range(1, 10000):
        params['page'] = page
        res = requests.get(url, params=params)

        write_json(res)
        print(f"Page {page}")


def write_json(res):
    try:
        data = res.json()['data']
    except:
        print("No more news available. Script terminated.")
        quit()

    data_rows = []

    for news in data:
        entity = news['entities'][0]

        data_rows.append([news['description'], entity['sentiment_score'],
                         news['published_at'], news['source'], news['url']])

    with open("financial_news.csv", "a", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        for data_row in data_rows:
            writer.writerow(data_row)


fetch_financial_news()
