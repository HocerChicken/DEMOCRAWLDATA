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

def crawl_data(word, base_url='https://chunom.net/Tra-cuu-Han-Nom'):
    try:
        payload = {'inputText': word}
        data = post_request(base_url, payload)
        #soup object
        soup = BeautifulSoup(data, 'html.parser')

        rows = soup.select('.table-responsive tbody tr')
        result = [ [cell.get_text(strip=True) for cell in row.select('td')] for row in rows ]
        
        return result
    except Exception as e:
        print(f"An error occurred during crawling: {e}")

def normalize(word, data, dictionary):
    if not data:
        return  
    word_entry = dictionary.setdefault(word, {"Nom": [], "boThu": [], "contexts": [], "sources": [], "spellings": []})
    for line in data:    
        if len(line) >= 6:
            word_entry["Nom"].append(line[1])
            word_entry["boThu"].append(line[2])
            word_entry["contexts"].append(line[3])
            word_entry["sources"].append(line[4])
            word_entry["spellings"].append(line[5])

def process_words(words, dictionary):
    for word in words:
        crawl_result = crawl_data(word)
        normalize(word, crawl_result, dictionary)

def main():
    my_dictionary = dict()
    with open('text_a_filtered.txt', 'r', encoding='utf-8') as file:
        data_list = [line.strip() for line in file.readlines()]

    process_words(data_list, my_dictionary)

    with open('result_a_Nom.json', 'w', encoding='utf-8') as fp:
      json.dump(my_dictionary, fp, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()