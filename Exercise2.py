from selenium import webdriver
import requests
import json

response = requests.get('https://jsonplaceholder.typicode.com/todos/')
assert response.status_code == 200, "Unexpected status code: " + str(response.status_code)

json_response = json.loads(response.content)
complete_field = [element['completed'] for element in json_response if element['id'] == 5][0]
assert complete_field == False, "the field completed should be false for id 5"
