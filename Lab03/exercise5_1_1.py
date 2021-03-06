IDENTIFICATION = 45678
TotalLengthOrginal = 5020
data_length = TotalLengthOrginal
mtu = 1500
mtu_d = mtu - 20
frag_num = 0
fragList = []
while (data_length > 0):
	frag_offset = mtu_d * frag_num / 8
	data_length = data_length - mtu_d
	if (data_length > 0):
		flag = '001'
		frag_data_start = frag_offset * 8
		frag_data_length = mtu_d
	else:
		flag = '000'
		frag_data_start = frag_offset * 8
		frag_data_length = mtu_d + data_length -20
	frag_num = frag_num + 1
	fragDict = {'IDENTIFICATION': IDENTIFICATION, 'TOTAL LENGTH (IN BYTES)' : frag_data_length+20 ,
				'FLAG':flag, 'FRAGMENTATION OFFEST': frag_offset,'DATA' : 'Bytes ' + str(frag_data_start) + '-' + str(frag_data_start+frag_data_length-1)}
	fragList.append(fragDict)
	
fd = open('Fragmentation.html','w')
html_content = []
html_content.append("<!DOCTYPE html>\n<html>\n<head>\n<style>\ntable, th, td \n{ \n border: 1px solid black; \n border-collapse: collapse; \n}\n ")
html_content.append("th, td \n{\npadding: 5px;\ntext-align: center;\n}\n</style>\n</head>\n<body>\n")

for element in fragList:
	html_content.append("<table " + 'style="width:100%"'+ ">\n")
	for keys in element:
		html_content.append("<tr>\n")
		html_content.append("<th>")
		html_content.append(str(keys))
		html_content.append("</th>\n")
		html_content.append("<td>")
		html_content.append(str(element[str(keys)]))
		html_content.append("</td>\n")
		html_content.append("</tr>\n")
		
	html_content.append("</table>\n\n")
html_content.append("</body>\n</html>")
s = "".join(html_content)
fd.write(s)
fd.close()

