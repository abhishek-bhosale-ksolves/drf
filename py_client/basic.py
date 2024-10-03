import requests

endpoint = "https://httpbin.org/"
endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.get(endpoint,json={"product":123})
# print(get_response.text)
# print(get_response)
# print(get_response.status_code)
print(get_response.json())
# print(get_response.json()['message'])

# JSON
# {
#   "args": {}, 
#   "data": "", 
#   "files": {}, 
#   "form": {}, 
#   "headers": {
#     "Accept": "*/*", 
#     "Accept-Encoding": "gzip, deflate", 
#     "Host": "httpbin.org", 
#     "User-Agent": "python-requests/2.32.3", 
#     "X-Amzn-Trace-Id": "Root=1-66fe3891-2f965b467640ed8903f379ff"
#   }, 
#   "json": null, 
#   "method": "GET", 
#   "origin": "115.160.212.98", 
#   "url": "https://httpbin.org/anything"
# }

# DICT
{'args': {}, 'data': '', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.32.3', 'X-Amzn-Trace-Id': 'Root=1-66fe3999-1ccb72986906f1e60112c7c5'}, 'json': None, 'method': 'GET', 'origin': '115.160.212.98', 'url': 'https://httpbin.org/anything'}