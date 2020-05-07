import requests
import json

from decouple import config

# CURL EXAMPLE
# curl https://api.search.esteem.app/search -d '{"q":"esteem", "sort": "newest"}' -H "Content-Type: application/json" -H "Authorization: YOUR_ACCESS_TOKEN" -X POST

base_url = "https://api.search.esteem.app/"
status_url = base_url + "state"
query_url = base_url + "search"

query_headers = {
    'Content-Type': 'application/json',
    'Authorization': config('API_KEY'),
}

# query_body = '"esteem surfer" -"monthly digest" -giveaway author:good-karma tag:esteem,wallet type:post'
# query_body = "esteem"

def search(query_body):
    query_data = {"q": query_body, "sort": "newest"}
    query_response = requests.post(url=query_url, headers=query_headers, data=json.dumps(query_data))
    return query_response.json()

def get_status():
    status_response = requests.get(url=status_url, headers={'Authorization': config('API_KEY'),})
    return status_response.json()

# headers = {
#     'Content-Type': 'application/json',
#     'Authorization': api_key,
# }

# data = '{"q":"esteem", "sort": "newest"}'

# query_response = requests.post('https://api.search.esteem.app/search', headers=headers, data=data)

# print(query_data)

# if __name__ == "__main__":
#     print(query_response.text)
#     print('\n-----------------------------------------------------------\n')
    # print(status_response.text)