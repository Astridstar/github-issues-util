import logging
import os
import csv

class task_detail:
  logger = logging.getLogger(__name__)

  # =================================================
  def __init__(self, sno, tile, body, labels, assignees, parents):
    self.issue_sno=sno
    self.issue_id=-1
    self.title=tile.strip()
    self.body=body.strip()
    self.labels=self.parse_labels(labels)
    self.assignees=self.parse_assignees(assignees)
    self.parents=self.parse_parents(parents)
  
  # =================================================
  def parse_labels(self, labels):
    return labels.strip()

  # =================================================
  def parse_assignees(self, assignees):
    return assignees.strip()
    

  # =================================================
  def parse_parents(self, parents):
    return parents.strip()
  
  # =================================================
  def __str__(self):
    return "[" + str(self.issue_sno) + "]: " + self.title