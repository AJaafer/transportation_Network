'''
xingeng wang
11144515
xiw031
'''

import urllib.request
import os

data =  urllib.request.urlopen('http://engineering.usask.ca/ece/syllabi-CME.php')
html_content = data.read().decode('utf-8')
fd = open('Exercise2_2_output.html','w')
fd.write(html_content)
href = 1
hreflist =[]
while (href > 0):
	hrefopeningQuote = html_content.find('href=', href)
	hrefclosingQuote = html_content.find('"', hrefopeningQuote+6)
	hreflist.append(html_content[hrefopeningQuote:hrefclosingQuote+1])
	href = html_content.find('href=', hrefclosingQuote)
    
uniquehyperlinks = list(set(hreflist))
hrefCount = len(uniquehyperlinks)
print('there are ' +str(hrefCount)+ ' unique hyperlinks in this website')


pdf = html_content.find('.pdf')
pdflist = []

while (pdf > 0):
	# opening quote
    openingQuote = html_content.rfind('\"', 0, pdf) + 1
    # closing quote
    closingQuote = pdf + 4
    # add the string in between to list
    pdflist.append(html_content[openingQuote:closingQuote])
    pdf = html_content.find('.pdf', closingQuote)

# remove duplicated items
uniquepdfSourcelinks = list(set(pdflist))
for eachlink in uniquepdfSourcelinks:
    print(eachlink)
fd.close()

os.makedirs('PDF_files')
os.chdir('PDF_files')
for j in uniquepdfSourcelinks:
    # extract file name
    filename = j[j.find('/')+1 : ]
    # save file
    urllib.request.urlretrieve('http://engineering.usask.ca/ece/documents/'+filename.replace(" ", "%20"), filename.replace("/", "_"))
