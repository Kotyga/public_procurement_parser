import requests
from bs4 import BeautifulSoup
import unittest

class Test(unittest.TestCase):
    def test_site(self):
        url = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html'
        page = requests.get(url)
        self.assertEqual(page.status_code, 200)
        soup = BeautifulSoup(page.text, 'html.parser')
        all_cards = soup.find_all(class_='search-registry-entry-block box-shadow-search-input')
        #print(all_cards)
        self.assertGreater(len(all_cards), 0)
        for data in all_cards:
            self.assertIsNotNone(data.find(class_='registry-entry__header-mid__number'))
            self.assertIsNotNone(data.find(class_='price-block__value'))

if __name__ == '__main__':
    unittest.main()
