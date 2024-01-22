import requests
from bs4 import BeautifulSoup

def post_request(url, payload):
    try:
        r = requests.post(url, data=payload)
        if(r.status_code == 200):
            return r.content
        else:
            print(r.status_code)
    except Exception as e: print(e)

class DictionaryEntry:
    def __init__(self, title, definitions):
        self.title = title
        self.definitions = definitions

class Definition:
    def __init__(self, meaning, source):
        self.meaning = meaning
        self.source = source

def crawl_data(word):
    payload = {'inputText': word}
    data = post_request('https://chunom.net/Tu-Dien.html', payload)
    soup = BeautifulSoup(data, 'html.parser')

    table_responsive = soup.find("div", {'class': 'table-responsive'})
    result = []

    current_title = None
    current_definitions = []

    for row in table_responsive.find_all('tr'):
        cells = [cell.get_text(strip=True) for cell in row.find_all(['td'])]

        if len(cells) == 2:
            # New entry
            if current_title:
                entry = DictionaryEntry(current_title, current_definitions)
                result.append(entry)

            current_title = cells[0]
            current_definitions = []

            definition_parts = cells[1].split('//')
            if len(definition_parts) == 2:
                meaning = definition_parts[0].strip()
                source = definition_parts[1].strip()
                current_definitions.append(Definition(meaning, source))

        elif len(cells) == 1:
            # Additional definition for the current entry
            definition_parts = cells[0].split('//')
            if len(definition_parts) == 2:
                meaning = definition_parts[0].strip()
                source = definition_parts[1].strip()
                current_definitions.append(Definition(meaning, source))

    # Add the last entry
    if current_title:
        entry = DictionaryEntry(current_title, current_definitions)
        result.append(entry)

    return result
def display_data(entries):
    for entry in entries:
        print(f"Word: {entry.title}")
        for i, definition in enumerate(entry.definitions, 1):
            print(f"  Definition {i}:")
            print(f"    Meaning: {definition.meaning}")
            print(f"    Source: {definition.source}")
        print()

# Example usage:
entries = crawl_data('a')
display_data(entries)