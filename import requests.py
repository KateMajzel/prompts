import os
import requests
from bs4 import BeautifulSoup
import openai

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

# Ustaw klucz API OpenAI
openai.api_key  = os.environ['OPENAI_API_KEY']

# Pobierz zawartość strony
url = "https://porady.pracuj.pl/rozmowa-kwalifikacyjna/najczestsze-pytania-rekrutacyjne-sprawdz-liste-i-przygotuj-sie-do-rozmowy/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Znajdź nagłówki artykułów (może wymagać dostosowania selektora w zależności od struktury strony)
headers = soup.select('h1, h2, h3')  # Przykładowe selektory dla nagłówków

for header in headers:
    text = header.get_text()
    print(f"Nagłówek: {text}")
    
    # Użyj OpenAI do podsumowania nagłówka
    response = openai.Completion.create(
      engine="davinci",
      prompt=f"Wciel się w rolę rekrutera, wypisz 10 pytań przygotowujących do rozmowy rekrutacyjnej, które znajdują się na stronie pracuj.pl: {text}",
      max_tokens=50
    )
    summary = response.choices[0].text.strip()
    print(f"Podsumowanie: {summary}\n")

