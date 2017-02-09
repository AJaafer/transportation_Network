import json
IPPacket = input("Please type the IP Packet String: ")
IPPacketLength = 4*len(IPPacket)
IPPacketBin = bin(int(IPPacket,16))[2:].zfill(IPPacketLength)

Version = int(IPPacketBin[0:4],2)
Hlen = int(IPPacketBin[4:8],2)
TOS = int(IPPacketBin[8:16],2)
TotalLength = int(IPPacketBin[16:32],2)

Identification = int(IPPacketBin[32:48],2)
Flags = int(IPPacketBin[48:51],2)
FragOffset = int(IPPacketBin[51:64],2)
TTL = int(IPPacketBin[64:72],2)

Protocol = int(IPPacketBin[72:80],2)
HeaderChecksum = int(IPPacketBin[80:96],2)
SRC = int(IPPacketBin[96:128],2)
DST = int(IPPacketBin[128:160],2)
Option = int(IPPacketBin[160:],2)

IPPacketDict = {'Version' : Version , 'Hlen' : Hlen, 'TOS':TOS,'TotalLength':TotalLength,
				'Identification':Identification, 'Flags':Flags, 'FragOffset':FragOffset,
				'TTL':TTL, 'Protocol':Protocol, 'HeaderChecksum':HeaderChecksum, 'SRC':SRC ,
				'DST':DST,'Option':Option}


fd = open('IPPacketDict.html','w')
html_content = []
html_content.append("<!DOCTYPE html>\n<html>\n<head>\n<style>\ntable, th, td \n{ \n border: 1px solid black; \n border-collapse: collapse; \n}\n ")
html_content.append("th, td \n{\npadding: 5px;\ntext-align: center;\n}\n</style>\n</head>\n<body>\n<table " + 'style="width:100%"'+ ">\n")

for keys in IPPacketDict:
	html_content.append("<tr>\n")
	html_content.append("<th>")
	html_content.append(str(keys))
	html_content.append("</th>\n")
	html_content.append("<td>")
	html_content.append(str(IPPacketDict[str(keys)]))
	html_content.append("</td>\n")
	html_content.append("</tr>\n")
	
html_content.append("</table>\n</body>\n</html>")
s = "".join(html_content)
fd.write(s)
fd.close()













