import os
import csv
import random
import uuid
from datetime import datetime, timedelta, timezone

# --- Configuration ---
NUM_CUSTOMERS = 500
NUM_STORES = 100
NUM_TRANSACTIONS = 1000000
SAMPLE_TRANSACTIONS = 10000
DATA_FOLDER = "data"

random.seed(42)  # For reproducibility

# --- Data Pools ---
REGIONS = {
    'North America': ['USA', 'Canada', 'Mexico'],
    'Europe': ['UK', 'Germany', 'France', 'Spain', 'Italy', 'Netherlands', 'Sweden'],
    'Asia': ['India', 'Japan', 'China', 'South Korea', 'Singapore'],
    'South America': ['Brazil', 'Argentina', 'Chile'],
    'Africa': ['South Africa', 'Nigeria', 'Egypt'],
    'Oceania': ['Australia', 'New Zealand']
}

COUNTRIES = [c for countries in REGIONS.values() for c in countries]
COUNTRY_TO_REGION = {c: r for r, countries in REGIONS.items() for c in countries}
COUNTRY_TO_CURRENCY = {
    'USA': 'USD', 'Canada': 'CAD', 'Mexico': 'MXN',
    'UK': 'GBP', 'Germany': 'EUR', 'France': 'EUR', 'Spain': 'EUR', 'Italy': 'EUR', 'Netherlands': 'EUR', 'Sweden': 'SEK',
    'India': 'INR', 'Japan': 'JPY', 'China': 'CNY', 'South Korea': 'KRW', 'Singapore': 'SGD',
    'Brazil': 'BRL', 'Argentina': 'ARS', 'Chile': 'CLP',
    'South Africa': 'ZAR', 'Nigeria': 'NGN', 'Egypt': 'EGP',
    'Australia': 'AUD', 'New Zealand': 'NZD'
}

PRODUCTS = [
    {'ProductID': f'P{str(i).zfill(3)}', 'ProductName': f'Product_{i}',
     'Department': f'Department_{i % 3}', 'Category': f'Category_{i % 5}', 'SubCategory': f'SubCategory_{i % 10}'}
    for i in range(1, 26)
]

PAYMENT_METHODS = ['Credit Card', 'PayPal', 'Bank Transfer', 'Gift Card']

# --- Helper Functions ---


def random_date(start, end):
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))


def weighted_choice(choices):
    total = sum(weight for choice, weight in choices)
    r = random.uniform(0, total)
    upto = 0
    for choice, weight in choices:
        if upto + weight >= r:
            return choice
        upto += weight
    assert False, "Should not get here"

# --- Generation Functions ---


def generate_customers():
    customers = []
    for i in range(1, NUM_CUSTOMERS + 1):
        customer_id = f'C{str(i).zfill(3)}'
        segment = random.choice(['Premium', 'Standard'])
        signup_date = random_date(datetime(2010, 1, 1), datetime(2022, 12, 31)).strftime('%Y-%m-%d')
        loyalty_program = 'Y' if (segment == 'Premium' and random.random() < 0.85) or (segment == 'Standard' and random.random() < 0.4) else 'N'
        email_opt_in = 'Y' if random.random() < 0.7 else 'N'

        customers.append({
            'CustomerID': customer_id,
            'CustomerName': f'Customer_{i}',
            'CustomerSegment': segment,
            'AgeGroup': random.choice(['20-29', '30-39', '40-49', '50-59']),
            'Gender': random.choice(['Male', 'Female']),
            'SignupDate': signup_date,
            'LoyaltyProgramMember': loyalty_program,
            'EmailOptIn': email_opt_in
        })
    return customers


def generate_stores():
    stores = []
    for i in range(1, NUM_STORES + 1):
        store_id = f'S{str(i).zfill(3)}'
        country = random.choice(COUNTRIES)
        region = COUNTRY_TO_REGION[country]
        currency = COUNTRY_TO_CURRENCY[country]
        store_open_date = random_date(datetime(2000, 1, 1), datetime(2022, 12, 31)).strftime('%Y-%m-%d')
        store_size = weighted_choice([('Small', 0.2), ('Medium', 0.6), ('Large', 0.2)])

        stores.append({
            'StoreID': store_id,
            'StoreName': f'Store_{i}',
            'City': f'City_{i}',
            'State': f'State_{i % 10}',
            'Country': country,
            'Region': region,
            'Currency': currency,
            'StoreOpenDate': store_open_date,
            'StoreSize': store_size
        })
    return stores


def generate_transactions(customers, stores):
    transactions = []
    start_date = datetime(2015, 1, 1)
    end_date = datetime(2025, 12, 31)

    for _ in range(NUM_TRANSACTIONS):
        transaction_id = str(uuid.uuid4())
        store = random.choice(stores)
        customer = random.choice(customers)
        product = random.choice(PRODUCTS)

        transaction_datetime = random_date(start_date, end_date).strftime('%Y-%m-%d %H:%M:%S')
        quantity = random.randint(1, 5)
        base_price = round(random.uniform(50, 1500), 2)
        total_price = round(quantity * base_price, 2)
        payment_method = random.choice(PAYMENT_METHODS)
        campaign_flag = 'Y' if random.random() < 0.1 else 'N'

        transactions.append({
            'TransactionID': transaction_id,
            'StoreID': store['StoreID'],
            'StoreName': store['StoreName'],
            'City': store['City'],
            'State': store['State'],
            'Country': store['Country'],
            'Region': store['Region'],
            'Currency': store['Currency'],
            'CustomerID': customer['CustomerID'],
            'CustomerName': customer['CustomerName'],
            'CustomerSegment': customer['CustomerSegment'],
            'AgeGroup': customer['AgeGroup'],
            'Gender': customer['Gender'],
            'ProductID': product['ProductID'],
            'ProductName': product['ProductName'],
            'Department': product['Department'],
            'Category': product['Category'],
            'SubCategory': product['SubCategory'],
            'Quantity': quantity,
            'Price': total_price,
            'TransactionDate': transaction_datetime,
            'PaymentMethod': payment_method,
            'CampaignFlag': campaign_flag
        })
    return transactions

# --- Main Execution ---


def main():
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    print('Generating customers...')
    customers = generate_customers()
    with open(f'{DATA_FOLDER}/customers.csv', mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=customers[0].keys())
        writer.writeheader()
        writer.writerows(customers)

    print('Generating stores...')
    stores = generate_stores()
    with open(f'{DATA_FOLDER}/stores.csv', mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=stores[0].keys())
        writer.writeheader()
        writer.writerows(stores)

    print('Generating transactions...')
    transactions = generate_transactions(customers, stores)
    with open(f'{DATA_FOLDER}/sales_transactions.csv', mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=transactions[0].keys())
        writer.writeheader()
        writer.writerows(transactions)

    print('Generating sample transactions...')
    with open(f'{DATA_FOLDER}/sample_10000.csv', mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=transactions[0].keys())
        writer.writeheader()
        writer.writerows(transactions[:SAMPLE_TRANSACTIONS])

    print('Data generation complete!')

# --- Entry Point ---

if __name__ == '__main__':
    main()
