import requests
from bs4 import BeautifulSoup
from use_case_utils import get_data, calculate_stats

women_url = 'https://shopping.louboutin2024.com/index.php?main_page=index&cPath=2&page='
all_women_prices = []
all_women_brands = []

for page in range(1, 17):
    url = women_url + str(page)
    brands, prices = get_data(url)
    all_women_prices.extend(prices)
    all_women_brands.extend(brands)

num_women, avg_women_price = calculate_stats(all_women_prices)
print(f"Femmes : {num_women} articles, Prix moyen : €{avg_women_price:.2f}")
