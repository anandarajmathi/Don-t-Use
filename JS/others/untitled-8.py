
# simple exception usage
try:                          # wrap "dangerous" code in a try block
  f = open("/manandaraj/books/BasicDTML.dtml")
  print "file is open"
except IOError:               # catch IOError and deriving exceptions
  print "Could not open"
else:                         # optional, run block if no exception thrown
  f.close()

