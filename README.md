# categorize
 
This script helps with bulk URL categorization against the Netskope SWG-NG. The file to be ingested should be a flat text file with one URL per line. 

This script was developed using threads to add performance but I tried to maintain it within the APIv1 boundaries so with 2 threads, which is the default configuration, it can do about 2-3 URL lookups per second. 

The output includes the url and its associated categories on an array. There is also an option to output any custom categories in the tenant that might contain a URL List that matches the URL. This option is turned off by default. 

## requirements
It just requires the request library so installing it using pip. 

'''
# pip install -r requirements.txt
'''

## usage
To run the script, first configure the settings inside categorize.py: 

'''
tenantName = "tenant.goskope.com" # this should be full tenant name like mytenant.goskope.com
apiv1Token = "xxxxx" # this should be your api v1 key from tenant settings.
file_name = 'list-of-websites.csv' # this is the file containing the urls. no headers and one url per line.
include_customURLL = False #set this to 'True' if you want custom URLs that match on the tenant to be included in the results on a separate column
'''

Afer configuring it, just run the script

'''
# python3 categorize.py
'''

And if you want to output the results to a file: 

'''
# python3 categorize.py > results.txt
'''

The results look like this: 

'''
# python3 categorize_threaded.py

0.docs.google.com,['Cloud Storage'],['custom_regex']
00002e388f7d8e3d4a8a9917c3d98355.safeframe.usercontent.goog,['Search Engines'],[]
0000adc4642c66b0aa1fdfe7dd9e7e68.safeframe.usercontent.goog,['Search Engines'],[]
00056df632ab861d370ee0a9ddb39fce.safeframe.usercontent.goog,['Search Engines'],[]
000731975aec7a42d0b0bfda70faab14.safeframe.usercontent.goog,['Search Engines'],[]
'''


