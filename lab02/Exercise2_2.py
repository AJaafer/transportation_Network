import urllib.request
import os

data =  urllib.request.urlopen('http://engineering.usask.ca/ece/syllabi-CME.php')
html_content = data.read().decode('utf-8')
fd = open('Exercise2_2_output.html','w')
fd.write(html_content)
href = html_content.find('href=')
hrefCount = 0
while (href > 0):
	hrefCount = hrefCount+1
	href = html_content.find('href=',href+5)
print('there are ' +str(hrefCount)+ ' hyperlinks in this website')

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
    urllib.request.urlretrieve('http://engineering.usask.ca/ece/syllabi-CME.php/'+filename.replace(" ", "%20"), filename.replace("/", "_"))
