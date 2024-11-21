import requests
from bs4 import BeautifulSoup
from use_case_utils import get_data, calculate_stats


baby_url = 'https://shopping.louboutin2024.com/index.php?main_page=index&cPath=232'
all_baby_prices = []
all_baby_brands = []

for page in range(1, 3):
    url = baby_url + str(page)
    brands, prices = get_data(url)
    all_baby_prices.extend(prices)
    all_baby_brands.extend(brands)
    print(all_baby_brands)

num_baby, avg_baby_price = calculate_stats(all_baby_prices)
print(f"Baby : {num_baby} articles, Prix moyen : €{avg_baby_price:.2f}")
