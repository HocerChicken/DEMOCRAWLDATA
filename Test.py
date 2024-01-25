import json 
import requests
from bs4 import BeautifulSoup

def post_request(url, payload):
    try:
        with requests.Session() as session:
            r = session.post(url, data=payload)
            r.raise_for_status()
            return r.content
    except requests.RequestException as e:
        print(f"An error occurred during the request: {e}")

def crawl_data(word, base_url='https://chunom.net/Tu-Dien.html'):
    try:
        payload = {'inputText': word}
        data = post_request(base_url, payload)
        soup = BeautifulSoup(data, 'html.parser')

        rows = soup.select('.table-responsive tr')
        result = [ [cell.get_text(strip=True) for cell in row.select('td')] for row in rows ]
        
        return result
    except Exception as e:
        print(f"An error occurred during crawling: {e}")

def normalize(word, data, dictionary):
    if not data:
        return  

    word_entry = dictionary.setdefault(word, {"definitions": [], "sources": []})

    word_entry["definitions"].extend(line[1] for line in data if len(line) == 2)
    word_entry["sources"].extend(line[0] for line in data if len(line) != 2)


def process_words(words, dictionary):
    for word in words:
        crawl_result = crawl_data(word)
        normalize(word, crawl_result, dictionary)

from collections import defaultdict

def main():
    my_dictionary = dict()

    with open('text_a.txt', 'r', encoding='utf-8') as file:
        data_list = [line.strip() for line in file.readlines()]

    process_words(data_list, my_dictionary)

    with open('result_a.json', 'w', encoding='utf-8') as fp:
      json.dump(my_dictionary, fp, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()