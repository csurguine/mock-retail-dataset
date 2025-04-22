Sales Mock Dataset Generator

This repository generates a high-quality synthetic sales transactions dataset for use in dashboards, ETL pipelines, data modeling, analytics engineering, and portfolio projects.

The dataset includes:
- 1 million sales transactions
- 30+ countries across 6 global regions
- 100 stores
- 500 customers
- Realistic customer loyalty and marketing campaign effects
- Local currency for each country
- 11 years of historical data (2015–2025)

Repository Structure:
- /data/customers.csv
- /data/stores.csv
- /data/sales_transactions.csv
- /data/sample_10000.csv
- generate_dataset.py
- requirements.txt
- .gitignore
- LICENSE
- README.md

How to Use:
1. Clone this repository
2. Create and activate a virtual environment
3. Install requirements
4. Run the dataset generator

Commands:
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python generate_dataset.py

Data Files:
- customers.csv: Customer dimension table
- stores.csv: Store dimension table
- sales_transactions.csv: Full transaction fact table (large)
- sample_10000.csv: Smaller transaction sample (for demos)

Each dataset is regenerated cleanly on script run.

License:
MIT License - free for personal, educational, or commercial use.

Author:
[Your Name]

