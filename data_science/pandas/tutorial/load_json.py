import pandas as pd
import json
from pandas import DataFrame

json_data = """
{
    "Country": "Brazil",
    "Products": ["Cars", "Boats", "Motorcycles"],
    "Location": ["Sao Paulo"],
    "Contact": ["alexandre_geraldo@hotmail.com"],
    "Payment": [{
        "Online": "Credit Card",
        "Offline": "Cash"
    }]
}
"""
company_data = json.loads(json_data)
#print (company_data)
#print (company_data['Country'])

df = DataFrame(company_data['Products'])   # columns to DataFrame

person = {
    'name': 'Alex',
    'age': 40,
    'isEmployeed': True
}

j_person = json.dumps(person)  # obj to json
print (j_person)