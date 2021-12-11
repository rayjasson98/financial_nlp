import spacy
import re
import csv

en = spacy.load('en_core_web_sm')
spacy_stopwords = en.Defaults.stop_words
my_stopwords = {
    "KUALA LUMPUR: ",
    " [a-z]*\.\.\."
}

def write_csv(input_path, output_path):
    with open(input_path, "r", newline='', encoding='utf-8') as original_file:
        csv_reader = csv.reader(original_file, delimiter=',')
        with open(output_path, mode='w') as output_file:
            writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in csv_reader:
                row[0] = remove_stop_words(row[0])
                writer.writerow(row)    


def remove_stop_words(text):
    words = [word for word in text.split() if word.lower() not in spacy_stopwords]
    text = " ".join(words)
    for sw in my_stopwords:
        text = re.sub(sw, '', text)
    return text


write_csv("financial_news.csv", "stopwords_removed.csv")