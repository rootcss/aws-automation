# /usr/bin/python

import boto.ec2
import time
from aws import AWS
from exception_handler import ExceptionHandler

class EC2(AWS, ExceptionHandler):
  instance_id = 'i-1234567'
  ip_address = None

  def __init__(self, auth=None, region=None):
    AWS.__init__(self, auth, region)

  def connect(self):
    print "[AWS] Connect"
    try:
      self.ec2 = boto.ec2.connect_to_region(self.region, **self.auth)
    except Exception, e:
      self.onException(e)

  def set_instance(self, instance_id=None):
    self.instance_id = instance_id

  def start(self, wait_for_state=False):
    print "[%s] Start" % self.instance_id
    try:
      self.ec2.start_instances(instance_ids=self.instance_id)
    except Exception, e:
      self.onException(e)

  def stop(self, wait_for_state=False):
    print "[%s] Stop" % self.instance_id
    try:
      self.ec2.stop_instances(instance_ids=self.instance_id)
    except Exception, e:
      self.onException(e)

  def state(self):
    try:
      state = self.ec2.get_only_instances(instance_ids=self.instance_id)[0].state
      print "[%s] State %s" % (self.instance_id, state)
      return state
    except Exception, e:
      self.onException(e)

  def ip(self):
    try:
      self.ip_address = self.ec2.get_only_instances(instance_ids=self.instance_id)[0].ip_address
      print "[%s] IP %s" % (self.instance_id, self.ip_address)
      return self.ip_address
    except Exception, e:
      self.onException(e)

  def private_ip(self):
    try:
      self.ip_address = self.ec2.get_only_instances(instance_ids=self.instance_id)[0].private_ip_address
      print "[%s] IP %s" % (self.instance_id, self.ip_address)
      return self.ip_address
    except Exception, e:
      self.onException(e)

  def wait_for_state(self, desired_state="running"):
    print "[%s] Wait for: %s" % (self.instance_id, desired_state)
    while self.state() != desired_state:
      print "Waiting.."
      time.sleep(3)
    print "Instance state is now: %s" % self.state()