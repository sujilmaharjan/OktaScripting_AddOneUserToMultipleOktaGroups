import requests
import csv

user_id = "<<user_id>>" #user id
your_okta_domain = "<<okta_domain>>" #okta domain
api_token = "<<api_token>>" #api token verisk.okta.com

with open("./oktagroups.csv", 'r') as file: #csv name and path can be renamed
  group_list = csv.reader(file)
  i = 1 #counter
  for group_id in group_list:
    #print(group_id)
    group_id = ' '.join(group_id) #convert list to str
    url = "https://" + your_okta_domain + "/api/v1/groups/" + group_id + "/users/" + user_id

    headers = {"Authorization": "SSWS "+api_token}

    response = requests.put(url, headers=headers)

    if (response.status_code == 204):
      print(i,"success adding user in: ", group_id)
    else:
      print("Error in the group list line: ",i)
      data = response.json()
      print(data)
    i=i+1
