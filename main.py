import os
import sys
import logparser
import secretmanager
import bigdata_api

def sort_ip_count(t):
  return t[-1]

File_Name = input("Enter The Log file Absalute Path: ")
freq = input("Enter The Number Of Hit(Hit Per IP Count): ")

if os.path.isfile(File_Name):
  access_lf = open(File_Name,"r")
  
  if freq.isdigit():
    freq = int(freq)

  else:
    print("\nPlease Enter A Valid Hit Count(Value Must Be An Integer)")
    sys.exit(0)
    
  api_key = secretmanager.api_fetch()

  if api_key == "noapi":
    print ("Error! - There is some error fetching the API details. Please make sure the provided Secret Manager details are correct.")

  else:
    print("Successfully Retrived API from SecretManager")
    ipdict = {}
    
    for logline in access_lf:
      logdict = logparser.parser(logline)
      if logdict["host"] not in ipdict:     
        ipdict[logdict["host"]] = 1
      
      else:            
        ipdict[logdict["host"]] = ipdict[logdict["host"]] + 1

  print("\n{:18} {:10} {:15} {:15}".format("IPAddress","HitCount","Theatlevel","Country"))
  
  ip_sorted = sorted(ipdict.items(),key=sort_ip_count,reverse=True)
  for item in ip_sorted:
    ip,count = item
    if count >= freq:
      api_result = bigdata_api.bigdata_api(ip=ip,big_api_key=api_key)
      
      if type(api_result) == list:
        print("{:15}{:10}      {:10}    {:5}".format(ip,count,api_result[1],api_result[0]))
      else:
        print("Couldn't Retrive Details Of Country And Threat level As API Call Failed\n")
        print("{:15}{:10}".format(ip,count))
        
  
else:
    
  print("\nPlease enter a valid path(absolute path of access log). The given path is not valid!")

