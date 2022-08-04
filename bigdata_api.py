import requests
import json

def bigdata_api(ip=None,big_api_key=None):
  if ip != None and big_api_key != None:
    try:
      url_country = "https://api.bigdatacloud.net/data/country-by-ip?ip={}&localityLanguage=en&key={}".format(ip,big_api_key)
      url_threat = "https://api.bigdatacloud.net/data/user-risk?ip={}&key={}".format(ip,big_api_key)
      response1 = requests.get(url_country)
      response2 = requests.get(url_threat)
      country = response1.json()["country"]["name"]
      threat = response2.json()["risk"]
      return [country,threat]
     
    except:
      return "fflag"
