import xml.etree.ElementTree as ET
from xml.dom import minidom

class Word:
    def __init__(self, meanings, source):
        self._meanings = meanings
        self._source = source

    @property
    def meanings(self):
        return self._meanings

    @meanings.setter
    def meanings(self, new_meanings):
        self._meanings = new_meanings

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, new_source):
        self._source = new_source

    def __str__(self):
        return f"Word(meanings={self.meanings}, source={self.source})"

class Dictionary:
    def __init__(self, words):
        self._words = words

    @property
    def words(self):
        return self._words

    @words.setter
    def words(self, new_words):
        self._words = new_words

    def add_word(self, word):
        self._words.append(word)

    def __str__(self):
        words_str = ', '.join(str(word) for word in self.words)
        return f"Dictionary(words=[{words_str}])"
    

data_list = [
    ['word', 'meaning1'],
    ['word', 'meaning2'],
    ['word', 'meaning3'],
    ['word', 'meaning4'],
    ['source1'],
    ['word', 'meaning5'],
    ['word', 'meaning6'],
    ['word', 'meaning7'],
    ['word', 'meaning8'],
    ['source2']
]


root = ET.Element("root")
def export_xml(data_list):
    global root
    
    d = Dictionary()
    word = Word()
    
    d.


    for meaning_text in meanings:
        meaning = ET.SubElement(source, "meaning")
        meaning.text = meaning_text

# Create an ElementTree from the root element
tree = ET.ElementTree(root)

# Create a string with the XML content
xml_string = ET.tostring(root, encoding="utf-8", method="xml").decode("utf-8")

# Use minidom to format the XML string with indentation
xml_dom = minidom.parseString(xml_string)
pretty_xml = xml_dom.toprettyxml(indent="  ")