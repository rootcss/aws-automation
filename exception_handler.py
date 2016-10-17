import sys

class ExceptionHandler:
  def __init__(self, e):
    self.onException(e)

  def onException(self, e):
    error = "Error: %s" % str(e)
    print(error)
    sys.exit(0)