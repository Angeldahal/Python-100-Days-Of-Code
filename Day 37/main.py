import requests
from datetime import datetime

USERNAME = "angeldahal"
TOKEN = "andiheidsld10ei"

pixela_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token":TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
# response = requests.post(url = pixela_endpoint, json = user_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config ={
    "id":"graph1",
    "name":"Reading",
    "unit":"Hours",
    "type":"float",
    "color":"shibafu",
}
headers = {
    "X-USER-TOKEN":TOKEN,
}

# response =requests.post(url= graph_endpoint, json = graph_config, headers = headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{graph_config['id']}"
today = datetime.now()

request_body_params ={
    "date":today.strftime("%Y%m%d"),
    "quantity":"2.5",
}
response = requests.post(url = pixel_endpoint, json = request_body_params, headers = headers)
print(response.text)