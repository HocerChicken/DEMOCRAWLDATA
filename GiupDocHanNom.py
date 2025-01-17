import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement
from xml.dom import minidom

def get_request(url, payload):
    try:
        with requests.Session() as session:
            r = session.get(url + payload)  
            r.raise_for_status()
            return r.content
    except requests.RequestException as e:
        print(f"An error occurred during the request: {e}")

def crawl_data(word, base_url='https://hvdic.thivien.net/hv/'):
    try:
        page = get_request(base_url, word)
        soup = BeautifulSoup(page, 'html.parser')
        
        word_field = soup.find_all(class_="hvres")
        for word in word_field:
          header = word.find(class_='hvres-header') # array of header
          details = word.find(class_='hvres-details') # array of detail
          if header is not None:
            inside_header_word = header.find(class_='hvres-word')
            inside_header_definition = header.find(class_='hvres-definition')
            insider_header_definition_spell = inside_header_definition.find(class_='hvres-spell').find('a')
            insider_header_definition_info = inside_header_definition.find(class_='hvres-info')

            word = {
              "word": inside_header_word.text.strip(),
              "title": insider_header_definition_spell.text.strip(),
              "info": insider_header_definition_info.text.strip()
            }
        if details is not None:
            word_fields = soup.find_all(class_="hvres-details")

            for word in word_fields:
                inside_details_source = word.find(class_="hvres-source")
                inside_details_meaning = word.find(class_="hvres-meaning")

                if inside_details_source and inside_details_meaning:
                    source = inside_details_source.text.strip()
                    meaning = inside_details_meaning.text.strip()
                    print("Source:", source)
                    print("Meaning:", meaning)
                 
        return None
    except Exception as e:
        print(f"An error occurred during crawling: {e}")

def normalize(word, data, xml_root):
    if not data:
        return

    word_elem = Element("word")
    quocngu_elem = Element("quocngu")
    quocngu_elem.text = word

    word_elem.append(quocngu_elem)
    dinhnghia_elem = SubElement(word_elem, "dinhnghia")

    for line in data:
        if len(line) == 6:
            #[nom, bothu, ngucanh, nguon, phienam, class] here
            phanloai_elem = SubElement(dinhnghia_elem, "phanloai")

            nom_elem = SubElement(phanloai_elem, "nom")
            nom_elem.text = line[1]  # Assuming the first element is 'nom'

            bothu_elem = SubElement(phanloai_elem, "bothu")
            bothu_elem.text = line[2]

            ngucanh_elem = SubElement(phanloai_elem, "ngucanh")
            ngucanh_elem.text = line[3]

            nguon_elem = SubElement(phanloai_elem, "nguon")
            nguon_elem.text = line[4]
            
            phienam_elem = SubElement(phanloai_elem, "phienam")
            phienam_elem.text = line[5 ]

    xml_root.append(word_elem)

def process_words(words, xml_root):
    for word in words:
        crawl_result = crawl_data(word)
        normalize(word, crawl_result, xml_root)

def prettify(elem):
    rough_string = ET.tostring(elem, encoding='utf-8').decode('utf-8')
    try:
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")
    except Exception as e:
        print(e)
        print(rough_string)

def main():
    print(crawl_data("a"))
    # xml_root = Element('dictionary')

    # with open('text_d_filtered.txt', 'r', encoding='utf-8') as file:
    #     data_list = [line.strip() for line in file.readlines()]
    # process_words(data_list, xml_root) 
    # pretty_xml = prettify(xml_root)
    # if pretty_xml is not None:
    #     with open('text_d.xml', 'w', encoding='utf-8') as xml_file:
    #         xml_file.write(pretty_xml)
    # else:
    #     print("Error")

if __name__ == "__main__":
    main()