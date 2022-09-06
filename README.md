# python_logparser_bigdataapi

# Description

#### This is a python script for identifying which IP's are hitting our server's mostly based on the frequency count you give as input. It will also show the risk/threat level, and country of each IP using BigDataCloud API.

##### For security Hardening I used AWS SeceretManager for storing our BigDataCloud API Key and used the boto3 python module to fetch the API details from  SeceretManager. You can edit the secretmanager.py details as yours for fetching the API key from your AWS SeceretManager.



# USAGE:
```
git clone https://github.com/christy700/python_logparser_bigdataapi.git
python3 main.py
```

# WORKING:

#### Here the python interpretor will take a log file path and also a frquency count for IP hit as input and prints the output with IP address along with other details which are greater than the given frequnecy hit.

# SAMPLE OUTPUT:

```

python3 main.py 
Enter The Log file Path: ./access.log
Enter The Number Of Hit(Hit Per IP Count): 200
Successfully Retrived API from SecretManager

IPAddress          HitCount   Theatlevel      Country        
45.144.0.179          521      Moderate      United States of America
176.222.58.254        518      Moderate      United States of America
45.138.145.131        506      Moderate      Germany
45.132.51.62          506      Moderate      United States of America
45.153.227.31         500      Moderate      United States of America
176.222.58.90         494      Moderate      United States of America
45.138.4.22           484      Moderate      United States of America
45.132.51.36          482      Moderate      United States of America
45.132.207.154        478      Moderate      Germany
45.153.227.55         478      Moderate      United States of America
45.132.207.221        478      Moderate      Germany
45.138.4.35           460      Moderate      United States of America
45.138.145.106        456      Moderate      Germany
45.144.0.98           454      Moderate      United States of America
87.247.143.24         429      Moderate      Germany
45.145.161.6          389      Moderate      Germany
87.247.143.30         369      Moderate      Germany
194.156.95.52         365      Moderate      United States of America
45.145.161.12         356      Moderate      Germany
194.156.95.20         337      Moderate      United States of America
```


###### Here in the above sample output it prints ip address that have hit count greater than 200 
