TCPPacket = input("Please type the TCP Packet String: ")
TCPPacketLength = 4*len(TCPPacket)

TCPPacketBin = bin(int(TCPPacket,16))[2:].zfill(TCPPacketLength)
TCPPacketDict ={}
TCPPacketDict['SRC. PORT ADDR. (16 BITS)'] = int(TCPPacketBin[0:16],2)
TCPPacketDict['DST. PORT ADDR. (16 BITS)'] = int(TCPPacketBin[16:32],2)
TCPPacketDict['SEQUENCE NO. (32 BITS)'] = int(TCPPacketBin[32:64],2)
TCPPacketDict['ACKNOWLEDGMENT NO. (32 BITS)'] = int(TCPPacketBin[64:96],2)
TCPPacketDict['HLEN (4 BITS)'] = int(TCPPacketBin[96:100],2)
TCPPacketDict['RESERVED (6 BITS)'] = int(TCPPacketBin[100:106],2)
TCPPacketDict['URG'] = int(TCPPacketBin[106],2)
TCPPacketDict['ACK'] = int(TCPPacketBin[107],2)
TCPPacketDict['PSH'] = int(TCPPacketBin[108],2)
TCPPacketDict['RST'] = int(TCPPacketBin[109],2)
TCPPacketDict['SYN'] = int(TCPPacketBin[110],2)
TCPPacketDict['FIN'] = int(TCPPacketBin[111],2)
TCPPacketDict['WINDOW SIZE (16 BITS)'] = int(TCPPacketBin[112:128],2)
TCPPacketDict['CHECKSUM (16 BITS)'] = int(TCPPacketBin[128:144],2)
TCPPacketDict['URGENT POINTER (16 BITS)'] = int(TCPPacketBin[144:160],2)
if (TCPPacketLength>480):
	TCPPacketDict['DATA (16 BITS)'] = int(TCPPacketBin[480:],2)
	if (TCPPacketLength>160):
		TCPPacketDict['OPTION AND PADDING (UP TO 40 BYTES)'] = int(TCPPacketBin[160:480],2)
if ((TCPPacketLength>160) and (TCPPacketLength<=480)):
	TCPPacketDict['OPTION AND PADDING (UP TO 40 BYTES)'] = int(TCPPacketBin[160:],2)



fd = open('TCPPacket.html','w')
html_content = []
html_content.append("<!DOCTYPE html>\n<html>\n<head>\n<style>\ntable, th, td \n{ \n border: 1px solid black; \n border-collapse: collapse; \n}\n ")
html_content.append("th, td \n{\npadding: 5px;\ntext-align: center;\n}\n</style>\n</head>\n<body>\n")

html_content.append("<table " + 'style="width:100%"'+ ">\n")
for keys in TCPPacketDict:
	html_content.append("<tr>\n")
	html_content.append("<th>")
	html_content.append(str(keys))
	html_content.append("</th>\n")
	html_content.append("<td>")
	html_content.append(str(TCPPacketDict[str(keys)]))
	html_content.append("</td>\n")
	html_content.append("</tr>\n")
		
html_content.append("</table>\n\n")
html_content.append("</body>\n</html>")
s = "".join(html_content)
fd.write(s)
fd.close()


















