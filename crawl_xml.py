import json
import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
from xml.dom import minidom

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
        result = [[cell.get_text(strip=True) for cell in row.select('td')] for row in rows]

        return result
    except Exception as e:
        print(f"An error occurred during crawling: {e}")

def normalize(word, data, xml_root):
    # data.reverse()
    if not data:
        return

    word_elem = Element("word")
    title_elem = Element("title")
    title_elem.text = word
    word_elem.append(title_elem)

    definitions_elem = Element("definitions")
    word_elem.append(definitions_elem)

    current_source_elem = Element("source")

    for line in data:
        if len(line) == 2:
            # [word, meaning] here
            meaning = line[1]
            meaning_elem = Element("meaning")
            meaning_elem.text = meaning
            current_source_elem.append(meaning_elem)
        else:
            # [source] here
            source = line[0]
            current_source_elem.set("class", source)
            definitions_elem.append(current_source_elem)
            current_source_elem = Element("source")

    xml_root.append(word_elem)

def process_words(words, xml_root):
    for word in words:
        crawl_result = crawl_data(word)
        normalize(word, crawl_result, xml_root)

def prettify(elem):
    rough_string = ET.tostring(elem, encoding='utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def main():
    xml_root = Element('dictionary')

    with open('text_i_k.txt', 'r', encoding='utf-8') as file:
        data_list = [line.strip() for line in file.readlines()]
        
    process_words(data_list, xml_root) 
    pretty_xml = prettify(xml_root)

    with open('text_i_k.xml', 'wb') as xml_file:
        xml_file.write(pretty_xml.encode('utf-8'))

if __name__ == "__main__":
    main()