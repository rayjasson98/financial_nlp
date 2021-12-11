import spacy
import re
import csv

en = spacy.load('en_core_web_sm')
spacy_stopwords = en.Defaults.stop_words
my_stopwords = {
    "KUALA LUMPUR: ",                     # KUALA LUMPUR: 
    " [0-9,\,,A-Z,a-z]*\.\.\.",                      # The be...
    "KUALA LUMPUR, (.*) [0-9]*: ",        # KUALA LUMPUR (April 8): 
    "KUALA LUMPUR \((.*) [0-9]*\):[-]* ", # KUALA LUMPUR (Sept 11):-
    "KUALA LUMPUR ",
    # KUALA LUMPUR, Jan 9
    "KUALA LUMPUR \((Jan(uary)?|Feb(bruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?) [0-9]*\)"
    "/KUALA LUMPUR, [0-9]*",              # KUALA LUMPUR, 17 
    "KUALA LUMPUR, [0-9]* \(Bernama\) -- ",
    "KUALA LUMPUR, [0-9]*  -- ",
    # (July 29) / (Aug 29)
    "\((Jan(uary)?|Feb(bruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sept(ember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?) [0-9]*\)",
    "[ ]\([A-Z, ]*\)[.]*",                # (FBM KLCI)
    ":-[ ]",
    "\(.*\)",
    "PETALING JAYA: "
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