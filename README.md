Universal Transaction Generator

This project generates realistic synthetic transaction datasets across multiple industries, including retail, healthcare, insurance, manufacturing, and logistics.

It is designed for use in:
- Dashboard demos
- ETL pipeline testing
- Data modeling exercises
- Analytics engineering projects
- Personal branding portfolios

Key Features:
- Domain-driven profiles (Retail, Healthcare, Insurance, etc.)
- Modular actor, receiver, item, and transaction generators
- Scalable output (generate thousands to millions of transactions)
- Flexible schema per industry
- Standard output: clean CSV files

Repository Structure:
- /data_profiles/ : Domain profiles (rules for each industry)
- /generators/ : Logic for generating actors, receivers, items, transactions
- /config/ : Centralized global settings
- /utils/ : Helpers for I/O and randomization
- /data/ : Output datasets (generated)
- generate_dataset.py : CLI to generate synthetic datasets

Setup:
1. Clone this repository
2. Create and activate a virtual environment
3. Install requirements
4. Run the generator

Commands:
git clone https://github.com/your-username/universal-transaction-generator.git
cd universal-transaction-generator
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python generate_dataset.py

Data Files (per domain):
- <domain>_actors.csv
- <domain>_receivers.csv
- <domain>_items.csv
- <domain>_transactions.csv

Each file is regenerated cleanly based on the selected domain profile.

How to Extend:
- To add a new industry, create a new profile in /data_profiles/
- No changes needed to core generators
- Supports easy future scaling to additional domains

License:
MIT License - free for personal, educational, or commercial use.

Author:
[Your Name]