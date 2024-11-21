import requests
from bs4 import BeautifulSoup
from use_case_utils import get_data, calculate_stats


baby_url = 'https://shopping.louboutin2024.com/index.php?main_page=index&cPath=232&page='
all_baby_details = []
all_baby_prices = []

for page in range(1, 2):
    url = baby_url + str(page)
    details = get_data(url)
    all_baby_details.extend(details)
    all_baby_prices.extend([product['Price'] for product in details])

num_baby, avg_baby_price = calculate_stats(all_baby_prices)
print(f"Baby : {num_baby} articles, Prix moyen : €{avg_baby_price:.2f}")

# Correct