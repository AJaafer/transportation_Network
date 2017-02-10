fileName = input("Please type the HTML file name: ")
fragNumber = input("Please type the number of fragmentation: ")
fd = open(fileName,'r')
fileContent = fd.read()
tableStart = fileContent.find('<table')
tableContent = []
while (tableStart > 0 ):
	tableopeningQuote = tableStart
	tableclosingQuote = fileContent.find('</table>', tableopeningQuote+6)
	tableContent.append(fileContent[tableopeningQuote:tableclosingQuote+1])
	tableStart = fileContent.find('<table', tableclosingQuote)
tableCount = len(tableContent)

fragList = []
frag_offset_list =[]
IDENTIFICATION_list =[]
DATA_START_list =[]
DATA_END_list =[]
FLAG_list = []
TOTAL_LENGTH_list =[]
for eachTable in tableContent:
	frag_offset_open = eachTable.find('<th>FRAGMENTATION OFFEST</th>\n<td>')+34
	frag_offset_close = eachTable.find('</td>',frag_offset_open)
	frag_offset = eachTable[frag_offset_open:frag_offset_close]
	frag_offset_list.append(frag_offset)
	IDENTIFICATION_open = eachTable.find('<th>IDENTIFICATION</th>\n<td>')+28
	IDENTIFICATION_close = eachTable.find('</td>',IDENTIFICATION_open)
	IDENTIFICATION = eachTable[IDENTIFICATION_open:IDENTIFICATION_close]
	IDENTIFICATION_list.append(IDENTIFICATION)
	DATA_open = eachTable.find('<th>DATA</th>\n<td>')+18
	DATA_close = eachTable.find('</td>',DATA_open)
	DATA = eachTable[DATA_open:DATA_close]
	DATA_START, DATA_END =DATA.split(' ')[1].split('-')
	DATA_START_list.append(DATA_START)
	DATA_END_list.append(DATA_END)
	FLAG_open = eachTable.find('<th>FLAG</th>\n<td>')+18
	FLAG_close = eachTable.find('</td>',FLAG_open)
	FLAG = eachTable[FLAG_open:FLAG_close]
	FLAG_list.append(FLAG)
	TOTAL_LENGTH_open = eachTable.find('<th>TOTAL LENGTH (IN BYTES)</th>\n<td>')+37
	TOTAL_LENGTH_close = eachTable.find('</td>',TOTAL_LENGTH_open)
	TOTAL_LENGTH = eachTable[TOTAL_LENGTH_open:TOTAL_LENGTH_close]
	TOTAL_LENGTH_list.append(int(TOTAL_LENGTH))
	fragDict = {'IDENTIFICATION': IDENTIFICATION, 'TOTAL LENGTH (IN BYTES)' : TOTAL_LENGTH ,
			'FLAG':FLAG, 'FRAGMENTATION OFFEST': frag_offset,'DATA_START' : DATA_START, 'DATA_END':DATA_END}
			
	fragList.append(fragDict)
FLAG_list.sort()
frag_offset_list.sort()
DATA_START_list.sort()
DATA_END_list.sort()
DATA_END_list.reverse()
length = sum(TOTAL_LENGTH_list)-(20*(len(fragList)-1))
orginalDict = {'IDENTIFICATION': IDENTIFICATION_list[0],'TOTAL LENGTH (IN BYTES)':length ,'FLAG': FLAG_list[0],
			'FRAGMENTATION OFFEST': frag_offset_list[0],'DATA ' : str(DATA_START_list[0]) + '-' + str(DATA_END_list[0])}
			


fd = open('OrignalPacket.html','w')
html_content = []
html_content.append("<!DOCTYPE html>\n<html>\n<head>\n<style>\ntable, th, td \n{ \n border: 1px solid black; \n border-collapse: collapse; \n}\n ")
html_content.append("th, td \n{\npadding: 5px;\ntext-align: center;\n}\n</style>\n</head>\n<body>\n")

html_content.append("<table " + 'style="width:100%"'+ ">\n")
for keys in orginalDict:
	html_content.append("<tr>\n")
	html_content.append("<th>")
	html_content.append(str(keys))
	html_content.append("</th>\n")
	html_content.append("<td>")
	html_content.append(str(orginalDict[str(keys)]))
	html_content.append("</td>\n")
	html_content.append("</tr>\n")
		
html_content.append("</table>\n\n")
html_content.append("</body>\n</html>")
s = "".join(html_content)
fd.write(s)
fd.close()
