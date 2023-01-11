#!/usr/bin/python3
import requests
import json
#author skoll101
url = "https://api.writesonic.com/v2/business/content/chatsonic?engine=premium"

payload = {
    "enable_google_results": True,
    "enable_memory": True,
    "input_text": "Who is the President of the United States?"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "X-API-KEY": "your api key here"
}
x=1
while x==1:
	question= input("how can i help you sir? ")
	payload = {
    "enable_google_results": True,
    "enable_memory": True,
    "input_text": question
    }
	jsonString = json.dumps(payload, indent=4)
	response = requests.post(url, json=payload, headers=headers)
	k=response.text
	sd = json.loads(k)
	answer = sd['message']
	print("======================================================================\n=======================================================\n================================")
	print("                          ")
	print(answer)
	print("                          ")
	print("======================================================================\n=======================================================\n================================")

	another_q= input("do you have another question?   ").lower()
	if another_q=="yes":
		x=1
	else:
		x -=1
