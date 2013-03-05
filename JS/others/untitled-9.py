a = [1,2,3]                   # init some simple list
try:
  a[7] = 0                    # will throw an IndexError exception
except (IndexError,TypeError):# handle several types with (,) syntax
  print "IndexError caught"   # handle the exception
except Exception, e:          # catch all deriving from Exception (instance e)
  print "Exception: ", e      # address the instance, print e.__str__()
except:                       # catch everything
  print "Unexpected:"         # handle unexpected exceptions
  print sys.exc_info()[0]     # info about curr exception (type,value,traceback)
  raise                       # re-throw caught exception
try:
  a[7] = 0                    # will throw an IndexError exception
finally:                      # cleanup code that should always run (no except)
  print "Will run regardless" # will run if thrown, not thrown, caught, uncaught

