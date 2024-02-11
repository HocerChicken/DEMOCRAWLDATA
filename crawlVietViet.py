import json 
import requests
from bs4 import BeautifulSoup
from pprint import pprint

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
    # if not data:
    #     return  
    # current_meanings = []

    # for line in data:
    #     if(len(line)) == 2:
    #     # [word, meaning] here
    #         meaning = line[1]
    #         current_meanings.append(meaning)
    #     else:
    #     # [source] here
    #         source = line[0]
    #         word_entry = dictionary.setdefault(word, {})
    #         if source not in word_entry:
    #             word_entry[source] = []
    #         word_entry[source].extend(current_meanings)
    #         current_meanings = []
    if not data:
        return

    current_entry = {"tu": word, "nguonThamKhao": []}

    for line in data:
        if len(line) >= 2:
            # [word, meaning] here
            if current_entry["nguonThamKhao"]:
                current_entry["nguonThamKhao"][-1]["dinhNghia"].append(line[1])
        elif line:
            # [source] here
            source = line[0]
            current_entry["nguonThamKhao"].append({"tacGia": source, "dinhNghia": []})

    dictionary[word] = current_entry

def process_words(words, dictionary):
    for word in words:
        crawl_result = crawl_data(word)
        normalize(word, crawl_result, dictionary)

def main():
    my_dictionary = dict()
    
    with open('text_a_filtered.txt', 'r', encoding='utf-8') as file:
        data_list = [line.strip() for line in file.readlines()]

    process_words(data_list, my_dictionary)

    with open('result_a.json', 'w', encoding='utf-8') as fp:
      json.dump(my_dictionary, fp, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
# data_list = [
#     ['word', 'meaning1'],
#     ['word', 'meaning2'],
#     ['word', 'meaning3'],
#     ['word', 'meaning4'],
#     ['source1'],
#     ['word', 'meaning5'],
#     ['word', 'meaning6'],
#     ['word', 'meaning7'],
#     ['word', 'meaning8'],
#     ['source2']
# ]