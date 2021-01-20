## So far format only for Nature journals.

def get_datasets_from_publication(doi):
    """Returns list of datasets (in Whatever format IVAN wants, from a paper's doi."""
    ## TO DO !
    
    pass

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#DOI = 'https://www.nature.com/articles/s41467-020-18551-0'
#DOI = 'https://www.nature.com/articles/s41467-020-20688-x'
DOI = 'https://science.sciencemag.org/content/366/6462/255'

html = urlopen(DOI)

soup = BeautifulSoup(html, "html.parser")

url = []
#for nature
table = soup.findAll('div',attrs={"id":"data-availability-content"})
for x in table:
        myString = (x.find('p').text)
        url += re.findall(r'(https?://\S+)', myString)


table = soup.findAll('div',attrs={"id":"code-availability-content"})
for x in table:
        myString = (x.find('p').text)
        #print (myString)
        url += re.findall(r'(https?://\S+)', myString)

#for science
table = soup.findAll('div',attrs={"class":"ack"})
myString = str(table)
url += re.findall(r'(https?://\S+)', myString)


print (url)
#Collapse

