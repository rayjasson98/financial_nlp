from transformers import pipeline
import csv

p = pipeline('sentiment-analysis')

def write_csv(input_path, output_path):
    with open(input_path, "r", newline='', encoding='utf-8') as original_file:
        csv_reader = csv.reader(original_file, delimiter=',')
        with open(output_path, mode='w') as output_file:
            writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            skip_row = True
            for row in csv_reader:
                # skip first row (csv headers)
                if skip_row:
                    writer.writerow(row)
                    skip_row = False
                    continue
                row[1] = get_sentiment(row[0])
                writer.writerow(row)

def get_sentiment(text):
    sentiment = p(text)[0]
    sentiment_score = sentiment['score']
    if sentiment['label'] == 'NEGATIVE':
        sentiment_score *= -1
    return sentiment_score

write_csv('stopwords_removed.csv', 'sentiment_updated.csv')