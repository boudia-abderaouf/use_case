import requests
from bs4 import BeautifulSoup
from use_case_utils import get_data, calculate_stats


men_url = 'https://shopping.louboutin2024.com/index.php?main_page=index&cPath=155&page='
all_men_prices = []
all_men_brands = []

for page in range(1, 8):
    url = men_url + str(page)
    brands, prices = get_data(url)
    all_men_prices.extend(prices)
    all_men_brands.extend(brands)
    print(all_men_brands)

num_men, avg_men_price = calculate_stats(all_men_prices)
print(f"Hommes : {num_men} articles, Prix moyen : €{avg_men_price:.2f}")
