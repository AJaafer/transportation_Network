import urllib.request

data =  urllib.request.urlopen('http://engineering.usask.ca/ece/')
html_content = data.read().decode('utf-8')
fd = open('Exercise2_1_output.html','w')
fd.write(html_content)
jpgIndex = html_content.find('.jpg')
jpgSrc = []

while (jpgIndex > 0):
	# opening quote
    openingQuote = html_content.rfind('\"', 0, jpgIndex) + 1
    # closing quote
    closingQuote = jpgIndex + 4
    # add the string in between to list
    jpgSrc.append(html_content[openingQuote:closingQuote])
    jpgIndex = html_content.find('.jpg', closingQuote)
	
# remove duplicated items
uniquejpgSourcelinks = list(set(jpgSrc))
for eachlink in uniquejpgSourcelinks:
    print(eachlink)
fd.close()


