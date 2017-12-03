# A program to check the data type and based on type print the number of items present
#~ in the data and get the last element of the data. [Use only String and list]

#~ import sys
#~ print("The name of the Script : ",sys.argv[0])
#~ tmp = type(sys.argv[1:])
#~ print tmp
#~ tmp = str(tmp)
#~ if tmp.split("'")[-2] == "list":
    #~ print "This is list and its last element is ::",sys.argv[1:][-1]
#~ if tmp.split("'")[-2] == "str":
    #~ print "This is string and its last element is ::",sys.argv[1:][-1]

#~ print("The type of String is : ",(type(sys.argv[1])))
#~ print("The type of List is : ",(type(sys.argv[2])))
#~ print("The type last element of String is : ",(type(sys.argv[1])))
#~ print("The type last element of List is : ",(type(sys.argv[2])))
#~ print("The number of items present in the String are : ",(len(sys.argv[1])))
#~ print("The number of items present in the List are : ",(len(sys.argv[2])))
#~ print("The last element of String is : ",((sys.argv[1])[-1]))
#~ print("The last element of String is : ",((sys.argv[2])[-1]))

#~ print("\n")
#~ import os
#~ os.system('pause')

a = input()
tmp = type(a)
#~ print tmp
tmp2 = str(tmp).split("'")
tmp2 = tmp2
if "list" in tmp2:
    print "This is list and last element is ::",a[-1]
if "str" in tmp2:
    print "This is string and last element is ::",a[-1]
if "tuple" in tmp2:
    print "This is tuple and last element is ::",a[-1]
    