import boto3
import json

def api_fetch():

  try:
  
    session = boto3.session.Session()
    client = session.client(service_name = 'secretsmanager', region_name = 'ap-south-1')
    response = client.get_secret_value(SecretId = 'prod/myapikey')
    api_dict = json.loads(response["SecretString"])
    api_key = api_dict["bigdatakey"]
    return api_key

  except:
    
    return "noapi"
