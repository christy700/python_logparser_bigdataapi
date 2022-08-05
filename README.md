# python_logparser_bigdataapi

#Description

#### This is a python script for identifying which IP's are hitting our server's mostly based on the frequency count you give as input. It will also show the risk/threat level, and country of each IP using BigDataCloud API.

##### For security Hardening we used AWS SeceretManager for storing our BigDataCloud API and used the boto3 python module to fetch the API details from  SeceretManager. You can edit the secretmanager.py details as yours for fetching the API key from your AWS SeceretManager.
