import configparser

class workspace_config:
     
    def __init__(self, config_file):
        self.config_file=config_file
        self.config=configparser.ConfigParser()

    def read_workspace_config(self):
        # Reading the config file
        self.config.read(self.config_file)
        
    def get_workspace_config(self):
        # Returning all the sections defined in the config file
        return self.config.sections()
    
    def get_workspace_config(self, name, key):
        # Getting the values from the particular section (name) 
        # by using the key       
        return self.config[name][key]
    
    def get_github_config_details(self):
        # Getting all the values defined under the given section (name).
        # Assuming the keys are known and fixed.
        chartdata= self.config['github_repository']
        return chartdata['project_url']
    
    def get_local_config_details(self):
        # Getting all the values defined under the given section (name).
        # Assuming the keys are known and fixed.
        chartdata= self.config['local_config']
        return chartdata['local_tasks_filename']
