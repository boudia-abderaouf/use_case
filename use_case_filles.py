import requests
from bs4 import BeautifulSoup
from use_case_utils import get_data, calculate_stats


filles_url = 'https://shopping.louboutin2024.com/index.php?main_page=index&cPath=236'
all_filles_prices = []
all_filles_brands = []

for page in range(1, 3):
    url = filles_url + str(page)
    brands, prices = get_data(url)
    all_filles_prices.extend(prices)
    all_filles_brands.extend(brands)
    print(all_filles_brands)






num_filles, avg_filles_price = calculate_stats(all_filles_prices)
print(f"Filles : {num_filles} articles, Prix moyen : €{all_filles_prices:.2f}")

