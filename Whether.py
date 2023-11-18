import requests

city = input("Enter City Name : ")

url = "https://wttr.in/{}".format(city)
whether = requests.get(url)             

print(whether.text)