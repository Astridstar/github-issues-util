import os
import argparse
import logging
# import requests 

# from requests.exceptions import HTTPError
from WorkspaceConfig import workspace_config
from TasksParser import tasks_parser
from Project import project

FORMAT = '%(asctime)s - %(message)s'
logging.basicConfig(format=FORMAT, level=os.environ.get("LOGLEVEL", "DEBUG"))
logger = logging.getLogger(__name__)

# Setup the command line options
parser = argparse.ArgumentParser()
parser.add_argument('--pat', type=str, help='Personal Access Token')
parser.add_argument('--config_file', type=str, help='Local project configurations')

# Parse the commands
try:
    args = parser.parse_args()
except argparse.ArgumentError as e:
    logger.warning('%s', e) 
  
token = args.pat
config_file=args.config_file

if (config_file is None) or (not config_file):
    exit
    
# Grab the configuration from config file
workspace_cfg = workspace_config(config_file)            # creating object of HostConfig
workspace_cfg.read_workspace_config()                    # Reading config file 
githubConfig = workspace_cfg.get_github_config_details() # Getting the list of sections (servers)
localConfig = workspace_cfg.get_local_config_details()   # Getting the list of sections (servers)
print("githubConfig: ", githubConfig)
print("localConfig: ", localConfig)

tasksPareser = tasks_parser()
tasksPareser.parse(localConfig)
for task in tasksPareser.task_list:
    logger.debug("Issue => %s", task)
    

gh_project = project(githubConfig) 
gh_project.update_github_project()
    
# url = 'https://api.github.com/repos/pcs-devsecops/devOps/issues/210'
# headers = {'Accept': 'application/vnd.github+json', 
#            'Authorization': f'Bearer {token}',
#            'X-GitHub-Api-Version': '2022-11-28'
#            }

# try:
#     response = requests.get(url, headers=headers)
#     response.raise_for_status()
#     # access JSOn content
#     jsonResponse = response.json()

#     title = jsonResponse["title"]
#     body = jsonResponse["body"]
#     logger.debug("Title:[%s]", title)
#     logger.debug("body:[%s]", body)
# except HTTPError as http_err:
#     print(f'HTTP error occurred: {http_err}')
# except Exception as err:
#     print(f'Other error occurred: {err}')
    

#https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-api-to-manage-projects?tool=curl