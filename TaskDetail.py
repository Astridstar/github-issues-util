import logging
import os
import csv

class TaskDetail:
  logger = logging.getLogger(__name__)

  # =================================================
  def __init__(self, sno, tile, body, labels, assignees, parents):
    self.issue_sno=sno.strip()
    self.issue_id=-1
    self.title=tile.strip()
    self.body=body.strip()
    self.labels=self.parseLabels(labels)
    self.assignees=self.parseAssignees(assignees)
    self.parents=self.parseParents(parents)
  
  # =================================================
  def parseLabels(self, labels):
    return labels.strip()

  # =================================================
  def parseAssignees(self, assignees):
    return assignees.strip()
    

  # =================================================
  def parseParents(self, parents):
    return parents.strip()
  
  