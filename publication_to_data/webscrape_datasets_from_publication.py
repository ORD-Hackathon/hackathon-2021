from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def get_datasets_from_publication(doi):

	URL = 'https://dx.doi.org/' + doi

	html = urlopen(URL)
	soup = BeautifulSoup(html, "html.parser")


	dataset = [{}]
	data_id = []

	#for nature
	table = soup.findAll('div',attrs={"id":"data-availability-content"})
	for x in table:
		myString = (x.find('p').text)
		data_id += re.findall(r'(https?://\S+)', myString)


	table = soup.findAll('div',attrs={"id":"code-availability-content"})
	for x in table:
		myString = (x.find('p').text)
		data_id += re.findall(r'(https?://\S+)', myString)

	#for science
	table = soup.findAll('div',attrs={"class":"ack"})
	myString = str(table)
	data_id += re.findall(r'(https?://\S+)', myString)


	#for PeerJ
	table = soup.findAll('div',attrs={"id":"addinfo-1"})
	for x in table:
		myString = str((x.find('a')['href']))
		data_id += re.findall(r'(https?://\S+)', myString)

	table = soup.findAll('div',attrs={"class":"object-id article-component-doi"})

	for x in table:
		myString = str((x.find('a')['href']))
		data_id += re.findall(r'(https?://\S+)', myString)

	
	for item in data_id:
		dataset.append({'identifier':item, 'access_open': True, 'license_cc_by': True})

	return (dataset)


#dataset = get_datasets_from_publication('10.1038/s41467-020-18551-0')
#print (dataset)

