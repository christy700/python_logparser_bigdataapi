# python_logparser_bigdataapi
python_logparser_bigdataapi

## This is a python script log parser for identifying the total number of IP HIT based on the frequency count you give as input. It will also show the risk/threat level, and country of each IP using BigDataCloud API.

### For security Hardening we used AWS SeceretManager for storing our BigDataCloud API and used the boto3 python module to fetch the API details from  SeceretManager. You can edit the secretmanager.py details as yours for fetching the API key from your AWS SeceretManager.
