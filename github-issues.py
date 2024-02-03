import os
import argparse
import logging
import requests 

from requests.exceptions import HTTPError

FORMAT = '%(asctime)s - %(message)s'
logging.basicConfig(format=FORMAT, level=os.environ.get("LOGLEVEL", "DEBUG"))
logger = logging.getLogger(__name__)

# Setup the command line options
parser = argparse.ArgumentParser()
parser.add_argument('--pat', type=str, help='Personal Access Token')

# Parse the commands
try:
    args = parser.parse_args()
except argparse.ArgumentError as e:
    logger.warning('%s', e) 
  
token = args.pat

url = 'https://api.github.com/repos/pcs-devsecops/devOps/issues/210'
headers = {'Accept': 'application/vnd.github+json', 
           'Authorization': f'Bearer {token}',
           'X-GitHub-Api-Version': '2022-11-28'
           }

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()

    title = jsonResponse["title"]
    body = jsonResponse["body"]
    logger.debug("Title:[%s]", title)
    logger.debug("body:[%s]", body)
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
    
#https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-api-to-manage-projects?tool=curl