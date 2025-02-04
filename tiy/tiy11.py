#cities: make a dictionary called cities. use the names of three cities as keys in your dictionary.
#create a dictionary of information about each city, including the country the city is in, approximate population, and one fact
cities = {
    'london' : {
        'country' : 'UK',
        'population' : '8.8 million',
        'fact' : 'Over 300 languages are spoken in London'
    },
      'tokyo' : {
        'country' : 'Japan',
        'population' : '14.18 million',
        'fact' : 'Tokyo was previously called Edo, which means "Eastern Capital"'
    },
      'miami' : {
        'country' : 'USA',
        'population' : '455,000',
        'fact' : 'The Port of Miami is known as the Cruise Capital of the World.'
    },
}

for city, info in cities.items():
    
    print(f"{city.title()}")
    print(f"\tCountry: {info['country']}")
    print(f"\tFun fact: {info['fact']}")