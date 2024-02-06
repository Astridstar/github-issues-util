import configparser

class WorkspaceConfig:
    def __init__(self, configFile):
        self.configFile= configFile
        self.config= configparser.ConfigParser()
        
    def readWorkspaceConfig(self):
        # Reading the config file
        self.config.read(self.configFile)
    
    def getWorkspaceConfig(self):
        # Returning all the sections defined in the config file
        return self.config.sections()
    
    def getWorkspaceConfig(self, name, key):
        # Getting the values from the particular section (name) 
        # by using the key       
        return self.config[name][key]
    
    def getGithubConfigDetails(self):
        # Getting all the values defined under the given section (name).
        # Assuming the keys are known and fixed.
        chartdata= self.config['github_repository']
        return chartdata['project_url']
    
    def getLocalConfigDetails(self):
        # Getting all the values defined under the given section (name).
        # Assuming the keys are known and fixed.
        chartdata= self.config['local_config']
        return chartdata['local_tasks_filename']
