# categorize
 Script to perform bulk URL categorization on Netskope 

 This script helps with bulk categorization against the Netskope platform. It uses threads (2 by default) so the peformance is about 2-3 URLs/sec. 

 After configured, the script will output results to prompt. In case you want to save them to a file, just direct the results to a file like below: 

 # python3 categorize.py > results.txt

 All the required settings are at the top of the script.

 The script requires the requests library so don't forget to install it before running 

 # pip install -r requirements.txt


