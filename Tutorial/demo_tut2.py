import os
import urllib.request

# open url
data = urllib.request.urlopen('http://www.usask.ca/')
# read content, utf-8 encode
html_content = data.read().decode('utf-8')

# find '.png'
pngIndex = html_content.find('.png')
pngHyperlinks = []
while (pngIndex > 0):
    # opening quote
    openingQuote = html_content.rfind('\"', 0, pngIndex) + 1
    # closing quote
    closingQuote = pngIndex + 4
    # add the string in between to list
    pngHyperlinks.append(html_content[openingQuote:closingQuote])
    pngIndex = html_content.find('.png', closingQuote)

# remove duplicated items
uniquepngHyperlinks = list(set(pngHyperlinks))

for eachlink in uniquepngHyperlinks:
    print(eachlink)

for j in uniquepngHyperlinks:
    # extract file name
    filename = j[j.find('/')+1 : ]
    # save file
    urllib.request.urlretrieve('http://www.usask.ca/img/'+filename.replace(" ", "%20"), filename.replace("/", "_"))