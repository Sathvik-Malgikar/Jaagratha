import http.client

conn = http.client.HTTPSConnection("connect.routee.net")

payload = "{ \"body\": \"A new game has been posted to the MindPuzzle. Check it out\",\"to\" : \"+917019486115\",\"from\": \"amdTelecom\"}"

headers = {
    'authorization': "Bearer 12dc9fe4-7df4-4786-8d7a-a46d307687f4",
    'content-type': "application/json"
    }

conn.request("POST", "/sms", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))