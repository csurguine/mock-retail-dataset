import pycountry
import random

def get_random_states(country_name, k=5):
    country = pycountry.countries.get(name=country_name)
    if not country:
        raise ValueError(f"Country not found: {country_name}")
    
    subdivisions = pycountry.subdivisions.get(country_code=country.alpha_2)
    states = [s.name for s in subdivisions]
    
    if not states:
        raise ValueError(f"No subdivisions found for: {country_name}")
    
    return random.sample(states, min(k, len(states)))