import requests
from bs4 import BeautifulSoup

# GET REQUEST
url = "https://en.wikipedia.org/wiki/Science"
data = requests.get(url)
# print(data.text)

soup = BeautifulSoup(data.text, 'html.parser')
# print(soup.prettify())

# Web scrapping
heading = soup.find_all('p') # Returns a list of paragraphs
for i in heading:
    print(i.text)



# POST REQUEST
import requests
url = "https://jsonplaceholder.typicode.com/posts"
body = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1,
}
headers = {
    'Content-type': 'application/json',
    'charset': 'UTF-8'
}
response = requests.post(url, json=body, headers=headers)
print(response.text)

# PUT Request
import requests
url = 'https://jsonplaceholder.typicode.com/posts/1'
headers = {
    'Content-type': 'application/json',
    'charset': 'UTF-8'
}
body = {
    'title': 'Dexter',
    'body': 'soldier',
    'userId': 1,
}
response = requests.put(url, headers=headers, json=body)
print(response.text)

# DELETE Request
import requests
response = requests.delete(url := 'https://jsonplaceholder.typicode.com/posts/1')
print(response.text)