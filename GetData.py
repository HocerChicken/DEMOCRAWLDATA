import requests
from bs4 import BeautifulSoup

url = 'https://chunom.net/Tu-Dien.html'
response = requests.post(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Identify the HTML elements containing the dictionary data and extract them
    # For example, if the dictionary entries are in <div> elements with a class 'dictionary-entry':
    dictionary_entries = soup.find_all('div', class_='dictionary-entry')

    # Process and print the extracted data
    for entry in dictionary_entries:
        print(entry.text)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
