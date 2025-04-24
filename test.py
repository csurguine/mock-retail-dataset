import pycountry

country = pycountry.countries.get(name="United States")
subdivisions = pycountry.subdivisions.get(country_code=country.alpha_2)

for state in subdivisions:
    print(state.name)