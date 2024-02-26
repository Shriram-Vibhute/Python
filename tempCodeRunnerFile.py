import requests
response = requests.delete(url := 'https://jsonplaceholder.typicode.com/posts/1')
print(response.text)