import pandas as pd
import requests




med_path = 'https://api.endlessmedical.com/v1/dx/GetFeatures'        # Path for Ars Technica data

def get_url(path):
    raw = requests.get(path)  # This 'get' method is the one that has been imported from the requests library above
    soup = raw.json() #BeautifulSoup(raw.text,
            #             'html.parser')  # This 'BeautifulSoup' method is imported through from the bs4 library above

    return soup

print(get_url(med_path))