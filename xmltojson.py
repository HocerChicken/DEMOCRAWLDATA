import xmltodict
import json

with open("result_a.xml", "r", encoding="utf-8") as fr:
  xml_string = fr.read()
python_dict = xmltodict.parse(xml_string)
with open('dictionary_a.json', 'w', encoding='utf-8') as fp:
  json.dump(python_dict, fp, ensure_ascii=False, indent=2)