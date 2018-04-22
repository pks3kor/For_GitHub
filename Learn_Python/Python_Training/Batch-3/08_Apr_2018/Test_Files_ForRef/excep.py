#~ def div(x,y):
    #~ try:
        #~ assert(y!=0),"divide by zero will come"
    #~ except AssertionError as tmp:
        #~ print tmp
    #~ finally:
        #~ print "I am in finally clause"
#~ div(1,0)

def functionName( level ):
   if level < 1:
      raise Exception("Invalid level!")
      # The code below to this would not be executed
      # if we raise the exception
try:
   functionName(-3)
except Exception as tmp:
   print tmp
else:
   print "OK"