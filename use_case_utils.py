import requests
from bs4 import BeautifulSoup
import re


def get_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    
    # Trouver les éléments contenant le nom des produits et les prix
    product_names = soup.find_all('li', class_='musheji_name')
    product_prices = soup.find_all('span', class_='productSpecialPrice')
    
    product_details = []
    
    # Parcourir chaque produit
    for name, price in zip(product_names, product_prices):
        product_text = name.text.strip()
        # Extraire le prix
        product_price = float(price.text.replace('€', '').strip())
        
        match = re.match(r"(.+)\s*-\s*(.+)\s*-\s*(.+)\s*-\s*(.+)", product_text)
        if match:
            model = match.group(1).strip()
            leather_type = match.group(2).strip()
            color = match.group(3).strip()

            product_details.append({
                'Model': model,
                'Type_cuir': leather_type,
                'Couleur': color,
                'Price': product_price
            })
    
    return product_details

def calculate_stats(prices):
    num_items = len(prices)
    avg_price = sum(prices) / num_items if num_items > 0 else 0
    return num_items, avg_price




