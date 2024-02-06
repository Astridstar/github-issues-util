import logging
import os
import csv
# List
#   title
#   body
#   assignees
#   label

from TaskDetail import task_detail

 
class tasks_parser:
  logger = logging.getLogger(__name__)

  # =================================================
  def __init__(self):
    self.task_list = list()

  # =================================================
  def parse(self, tasks_csv_file):
    with open(tasks_csv_file, mode='r') as tasks_file:
        tasks_reader = csv.reader(tasks_file, delimiter=',', quotechar='"')
        for row in tasks_reader:
          self.task_list.append(task_detail(row[0], row[1], row[2], row[3], row[4], row[5]))
          # for item in row:
              
  
