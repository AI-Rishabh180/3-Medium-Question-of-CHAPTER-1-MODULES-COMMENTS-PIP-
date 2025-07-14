 #  Install the external package requests using pip. Then write a Python program to fetch and print the HTML content of https://example.com using the requests.get() function


print("https://example.com")

import requests
response = requests.get("https://example.com")
print(response.text)



