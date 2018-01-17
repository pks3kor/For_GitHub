html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
#~ print soup.prettify()
#~ print soup.html # access anything using tag
#~ print soup.head # access anything using tag
#~ print soup.title
#~ print soup.body
#~ print soup.p
#~ print soup.p['class'] # accessing any attributes of tag similar to accessign value of dictioanry key
#~ print soup.p.b
#~ print soup.p.b.text # accessing available text in the tag <b>
#~ print soup.find_all('a') # Find all tage that starts with <a>, will return a list
                        # we can again apply all basics in the list to access specific details
                        
tmp = soup.find_all('a')
#~ print tmp[0].attrs
#~ print tmp[0]['class']
#~ print tmp[0].text
#~ print tmp[0].string

print soup.find_all(['a','b']) # pass tag name as a list that needs to be searched
print soup.find_all(class_="sister") # since class name is already reserved so bs4 provides "class_" instead of "class" to search class with specific name

##############################
#~ for str in soup.strings: # will return all the availabble string including whitespaces
    #~ print str

for str in soup.stripped_strings: # will return all teh availabble string after stripping whitespaces
    print str