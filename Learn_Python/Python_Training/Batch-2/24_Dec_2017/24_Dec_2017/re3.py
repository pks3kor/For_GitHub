import re

line = "This is Learnbay Learnbay Learnbay Class C:\\";

#~ sub(<pattern>)
tmp = re.sub(r'Learnbay', "LB", line);
print tmp