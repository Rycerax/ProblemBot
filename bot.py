import random
import requests
rating = int(input('Digite seu rating: '))
rating += (200 - (rating%100))
response = requests.get('https://codeforces.com/api/problemset.problems?')

response = response.json()
response = response['result']['problems']
problems = []
for p in response:
  if "rating" in p:
    if(p["rating"] == rating):
      problems.append(p)

r = random.randint(0, len(problems) - 1)
print(f"Ta aí um bom problema para treinar com rating {rating}: https://codeforces.com/problemset/problem/{problems[r]['contestId']}/{problems[r]['index']}")