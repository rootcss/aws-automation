class AWS(object):
  auth = {'aws_access_key_id': '<key_id>',
          'aws_secret_access_key': '<secret_key>'}
  region = 'ap-southeast-1'

  def __init__(self, auth=None, region=None):
    self.auth.update(auth)
    if region != None:
      self.region = region

  def print_aws_creds(self):
    print self.auth
    print self.region