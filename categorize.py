'''
Netskope - Nov/22

This script helps categorize URLs in bulk against a Netskope Tenant. 
the input file should just contain the URLs, one by line. 
results will be in the prompt. If you want to record on a file run it sending the output to a txt file
example:

# python3 categorize_threaded.py >> results.txt

'''

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import json

##### Configuration starts here

tenantName = "tenant.goskope.com" # this should be full tenant name like mytenant.goskope.com
apiv1Token = "xxxxx" # this should be your api v1 key from tenant settings.
file_name = 'list-of-websites.csv' # this is the file containing the urls. no headers and one url per line.
include_customURLL = False #turn this on if you want custom URLs that match on the tenant to be included in the results on a separate column

#### Configuratoin ends here - no tweaking below this point 

apiurl = 'https://{}/api/v1/urlcategory?token={}&url={}'

def parseResponse(response):
    result = []
    result_custom = []
    data = response.get("data")
    categories = data.get("categories")
    parsedurl = data['url']
    for i in categories:
        if i.get("name") == "All Categories":
            continue
        if i.get("desc") == "":
            result_custom.append(i.get("name"))
        else:
            result.append(i.get("name"))
    return parsedurl, result, result_custom
 
def lookup(url, tenantName, apiv1Token):
    try:
        response = requests.get(apiurl.format(tenantName, apiv1Token, url))
        return response.text
    except requests.exceptions.RequestException as e:
       return e
 
def runner():
    threads= []
    with ThreadPoolExecutor(max_workers=2) as executor:
        
        with open(file_name) as text_file: 
            for url in text_file:
                threads.append(executor.submit(lookup, url.strip(), tenantName, apiv1Token))
            
        for task in as_completed(threads):
            #parsed = parseResponse(task.result())
            result = json.loads(task.result())
            parsed_result = parseResponse(result)
            if include_customURLL == False: 
                print(str(parsed_result[0]) + "," + str(parsed_result[1]))
            else:
                print(str(parsed_result[0]) + "," + str(parsed_result[1]) + "," + str(parsed_result[2]))
       
runner()