import requests
from bs4 import BeautifulSoup

def get_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    product_names = soup.find_all('li', class_='musheji_name')
    product_prices = soup.find_all('span', class_='productSpecialPrice')
    
    # print(product_names)
    brands = [name.text.split(' ')[0] for name in product_names]
    # breakpoint()
    prices = [float(price.text.replace('€', '').strip()) for price in product_prices]
    
    return brands, prices

def calculate_stats(prices):
    num_items = len(prices)
    avg_price = sum(prices) / num_items if num_items > 0 else 0
    return num_items, avg_price




