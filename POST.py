'''
This file is used to send a POST request to the Google Translate API to detect the language of a given text.
The text to be analyzed is specified in the payload under the 'q' parameter.
The response will be a JSON object containing the detected language and other metadata.
'''
import requests  # Importing the requests module for HTTP operations

# Request URL
url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"

# Payload
'''
The payload contains the data to be sent in the body of the request.
'''
payload = {"q": "English is hard, but detectably so"}

# Headers
'''
Headers in an HTTP request provide metadata about the request.
Here, headers include the API key for authentication, the host information, 
the content type, and the encoding preferences.
'''
headers = {
    "x-rapidapi-key": "be66b9a47emsh51482eb6cc9732ap18309cjsn51d8aa14fbef",
    "x-rapidapi-host": "google-translate1.p.rapidapi.com",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept-Encoding": "application/gzip"
}

# Sending POST request
'''
The post() method sends a POST request to the specified URL.
The payload is passed as the data parameter, and headers are included in the request.
More info: https://www.w3schools.com/python/module_requests.asp
'''
response = requests.post(url, data=payload, headers=headers)

# Printing response
'''
The response is expected to be in JSON format, which provides details about the detected language.
JSON: JavaScript Object Notation is a lightweight data-interchange format that is easy to parse and generate.
'''
print(response.json())
