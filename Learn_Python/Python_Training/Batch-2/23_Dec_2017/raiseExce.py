def levelChk( level ):
    if level != "":
        try:           
            raise TypeError("Invalid level")
            # The code below to this would not be executed
            # if we raise the exception
        except Exception as error:
           print error

levelChk(4)