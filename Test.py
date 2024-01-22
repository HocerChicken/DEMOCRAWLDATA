import requests
from bs4 import BeautifulSoup

class DictionaryEntry(dict):
    def __init__(self, dict, source):
        self.dict = dict
        self.source = source

def post_request(url, payload):
    try:
        r = requests.post(url, data=payload)
        if(r.status_code == 200):
            return r.content
        else:
            print(r.status_code)
    except Exception as e: print(e)
def crawl_data(word):
    payload = {'inputText': word}
    data = post_request('https://chunom.net/Tu-Dien.html', payload)
    soup = BeautifulSoup(data, 'html.parser')

    table_responsive = soup.find("div", {'class': 'table-responsive'})
    result = {}
    for row in table_responsive.find_all('tr'):
        cells = [cell.get_text(strip=True) for cell in row.find_all(['td'])]
        for cell in cells:
            if(len(cell) == 2):
                result[cell[0]].add(cell[1])
            elif(len(cell) == 1):
                continue
    return result
print(crawl_data("học"))
# with open('vietanh.txt', 'r', encoding='utf-8') as file:
#     data_list = [line.strip() for line in file.readlines()]
# import xml.etree.ElementTree as ET
# import xml.dom.minidom

# data = crawl_data("anh")

# def list_to_xml(data):
#     root = ET.Element("word") #<word></word> 
#     for item in data:
#         if (len(item) == 2):
#             title = ET.Element("title") #<word></word>
#             title.text = str(item[0])
#             definition = ET.Element("definition") #<definition></definition>
#             definition.text = str(item[1])
#             root.append(title)
#             root.append(definition)
#         if (len(item) == 1):
#             source = ET.Element("source") #<source></source>
#             source.text = item[0]
#             root.append(source)
#     return ET.tostring(root, encoding="utf-8", method="xml", xml_declaration=True)

# xml_data = list_to_xml(data)
# dom = xml.dom.minidom.parseString(xml_data)
# pretty_xml_data = dom.toprettyxml()

# with open("output.xml", "wb") as file:
#     file.write(pretty_xml_data.encode("utf-8"))