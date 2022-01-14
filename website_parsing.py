import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html' 
    page = requests.get(url)
    if page.status_code != 200:
        raise Exception("Status code is not equal 200 - problem in loading site")
    soup = BeautifulSoup(page.text, 'html.parser')
    all_cards = soup.find_all(class_='search-registry-entry-block box-shadow-search-input')
    print(all_cards)
    all_cards_saved = []
    for data in all_cards:
        number_card = None
        amount_card = None
    e1 = data.find(class_='registry-entry__header-mid__number')
    e2 = data.find(class_='price-block__value')
    if e1 is not None:
        number_card = e1.text
    if e2 is not None:
        amount_card = e2.text
    all_cards_saved.append({number_card, amount_card})
    print(all_cards_saved)

if __name__ == '__main__':
    main()
