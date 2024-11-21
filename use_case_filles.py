import requests
from bs4 import BeautifulSoup
from use_case_utils import get_data, calculate_stats

filles_url = 'https://shopping.louboutin2024.com/index.php?main_page=index&cPath=236&page='
all_filles_details = []
all_filles_prices = []

for page in range(1, 3):
    print(page)
    url = filles_url + str(page)
    details = get_data(url)
    all_filles_details.extend(details)
    all_filles_prices.extend([product['Price'] for product in details])

num_men, avg_men_price = calculate_stats(all_filles_prices)
print(f"Filles : {num_men} articles, Prix moyen : €{avg_men_price:.2f}")




# Correct