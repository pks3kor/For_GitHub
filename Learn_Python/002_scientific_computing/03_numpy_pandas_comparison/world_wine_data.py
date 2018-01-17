import numpy as np

world_alcohol = np.genfromtxt("world_wine_data.csv",delimiter=",",dtype="U75",skip_header =1)
#~ print world_alcohol

list_of_co = ["Texas","India","Autralia"]
list_of_year = range(1970,2000)
for con in list_of_co:
        is_texas_1989 = (world_alcohol[:,2] == con) & (world_alcohol[:,0] == '1989')
        print is_texas_1989
        texas_1989 = world_alcohol[is_texas_1989]
        #~ print texas_1989
        texas_alcohol = texas_1989[:,4]
        #~ print texas_alcohol
        empty_strings = texas_alcohol == ''
        texas_alcohol[empty_strings] = "0"
        texas_alcohol = texas_alcohol.astype(float)
        #~ print texas_alcohol
        total_texas_drinking = texas_alcohol.sum()
        print "for Country::",con,total_texas_drinking