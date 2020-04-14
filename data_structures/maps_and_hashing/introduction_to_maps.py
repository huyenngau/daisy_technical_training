# Code

locations = {"North America": {"USA": ["Mountain View"]},
             "Asia": {"India": ["Bangalore"], "China": ["Shanghai"]},
             "Africa": {"Egypt": ["Cairo"]},
             }

# Print a list of all cities in the USA in alphabetic order.
print(1)
all_cities_in_the_USA = sorted(locations["North America"]["USA"])
for item in all_cities_in_the_USA:
    print(item)


# Print all cities in Asia, in alphabetic order, next to the name of the country
print(2)
all_countries_in_Asia = locations["Asia"]
all_cities_in_the_Asia = []
for country, city in all_countries_in_Asia.items():
    city_in_country = city[0] + " - " + country
    all_cities_in_the_Asia.append(city_in_country)

for item in sorted(all_cities_in_the_Asia):
    print(item)
