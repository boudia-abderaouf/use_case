import sqlite3
from collections import Counter
from itertools import islice
from use_case_utils import get_data, calculate_stats


# Définir une fonction pour extraire les bigrammes
def get_bigrams(words):
    return [(words[i], words[i + 1]) for i in range(len(words) - 1)]


# Créer et configurer la base de données SQLite
def setup_database():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Model TEXT,
            Model_exact TEXT,
            Couleur TEXT,
            Sexe TEXT,
            Price REAL
        )
    """)
    conn.commit()
    return conn


# Insérer les données dans la base de données
def insert_into_database(conn, products):
    cursor = conn.cursor()
    for product in products:
        cursor.execute("""
            INSERT INTO products (Model, Model_exact, Couleur, Sexe, Price)
            VALUES (?, ?, ?, ?, ?)
        """, (
            product['Model'],
            product['Model_exact'],
            product['Couleur'],
            product['Sexe'],
            product['Price']
        ))
    conn.commit()


# Extraire et traiter les données des pages
def process_page_data(base_url, page_range, top_words, top_bigrams, sexe):
    all_details = []
    all_prices = []

    for page in page_range:
        print(f"Processing page {page}...")
        url = f"{base_url}{page}"
        details = get_data(url)

        for product in details:
            if 'Model' in product and 'Price' in product:
                for word in product['Model'].split():
                    if word in top_words:
                        product_details = {
                            'Model': product['Model'],
                            'Model_exact': next(
                                (bigram for bigram in top_bigrams if bigram in product['Model']),
                                None
                            ),
                            'Couleur': product.get('Couleur', 'Non spécifié'),
                            'Sexe': sexe,
                            'Price': product['Price']
                        }
                        all_details.append(product_details)
                        all_prices.append(product['Price'])
                        break  # Évite les doublons pour un même produit
    return all_details, all_prices


# URL pour les hommes et cadeauH
men_url = 'https://shopping.louboutin2024.com/index.php?main_page=index&cPath=155&page='
cadeauH_url = 'https://shopping.louboutin2024.com/index.php?main_page=index&cPath=175&page='

# 1. Extraction des données pour les hommes
all_man_details = []
all_men_prices = []
all_men_model = []

for page in range(1, 8):
    url = f"{men_url}{page}"
    details = get_data(url)
    all_man_details.extend(details)
    all_men_prices.extend([product['Price'] for product in details])
    all_men_model.extend([product['Model'] for product in details])

num_men, avg_men_price = calculate_stats(all_men_prices)
print(f"Hommes : {num_men} articles, Prix moyen : €{avg_men_price:.2f}")

# Analyse des mots et bigrammes
all_words = []
for model in all_men_model:
    all_words.extend(model.split())

word_counts = Counter(all_words)
top_words = [word for word, _ in word_counts.most_common(8)]  # Mots les plus fréquents

bigrams = get_bigrams(all_words)
bigram_counts = Counter(bigrams)
top_bigrams1 = [' '.join(bigram) for bigram, _ in bigram_counts.most_common(8)]  # Bigrammes les plus fréquents

print("Mots les plus fréquents :", top_words)
print("Bigrammes les plus fréquents :", top_bigrams1)

# 2. Extraction des données pour cadeauH
all_cadeauH_details, all_cadeauH_prices = process_page_data(
    cadeauH_url, range(1, 5), top_words, top_bigrams1, "Homme"
)

num_cadeauH, avg_cadeauH_price = calculate_stats(all_cadeauH_prices)
print(f"CadeauH : {num_cadeauH} articles, Prix moyen : €{avg_cadeauH_price:.2f}")

# 3. Fusionner les données et insérer dans la base de données
conn = setup_database()

# Insertion des produits hommes
insert_into_database(conn, all_man_details)

# Insertion des produits cadeauH
insert_into_database(conn, all_cadeauH_details)

# Affichage des produits insérés
cursor = conn.cursor()
cursor.execute("SELECT * FROM products")
for row in cursor.fetchall():
    print(row)

conn.close()
