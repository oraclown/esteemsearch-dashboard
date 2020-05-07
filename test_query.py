import requests
import json
from decouple import config

url = "https://api.search.esteem.app/search"

query_headers = {
    'Content-Type': 'application/json',
    'Authorization': config('API_KEY'),
}

query_data = {
    "query": {
        "more_like_this" : {
            "fields" : ["ingredients"],
            "like" : "2 whole Medium Onions, Halved And Sliced\n1-1/4 stick Butter\n2 pounds Cube Steak, Cut Into 1/2-inch Strips\n1 teaspoon Kosher Salt\n1 teaspoon Black Pepper\n1/4 cup Worcestershire Sauce\n5 dashes Tabasco Sauce\n4 whole Deli Rolls (crusty), Split\n8 slices (thick) Fresh Mozzarella\n8 slices (thick) Ripe Tomato\n1-1/2 cup Arugula",
            "min_term_freq" : 1,
            "max_query_terms" : 12
        }
    },
    "sort": "newest"
}


query_response = requests.post(url=url, headers=query_headers, data=json.dumps(query_data))
print(query_response.json())