import logging
import os
import csv
# List
#   title
#   body
#   assignees
#   label

 
class TasksParser:
  logger = logging.getLogger(__name__)

  # =================================================
  def __init__(self):
    pass

  # =================================================
  def parse(self, tasksCsvFile):
    with open('employee_file.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        employee_writer.writerow(['John Smith', 'Accounting', 'November'])
        employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
  
  
