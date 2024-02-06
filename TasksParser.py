import logging
import os
import csv
# List
#   title
#   body
#   assignees
#   label

from TaskDetail import TaskDetail

 
class TasksParser:
  logger = logging.getLogger(__name__)

  # =================================================
  def __init__(self):
    self.taskList = list()

  # =================================================
  def parse(self, tasksCsvFile):
    with open(tasksCsvFile, mode='r') as tasks_file:
        tasks_reader = csv.reader(tasks_file, delimiter=',', quotechar='"')
        for row in tasks_reader:
          self.taskList.append(TaskDetail(row[0], row[1], row[2], row[3], row[4], row[5]))
          # for item in row:
              
  
