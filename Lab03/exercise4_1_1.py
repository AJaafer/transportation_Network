import json
EthernetPacket = input("Please type the IP Packet String: ")
EthernetPacketLength = 4*len(EthernetPacket)
EthernetPacketBin = bin(int(EthernetPacket,16))[2:].zfill(EthernetPacketLength)

Version = int(EthernetPacketBin[0:4],2)
Hlen = int(EthernetPacketBin[4:8],2)
TOS = int(EthernetPacketBin[8:16],2)
TotalLength = int(EthernetPacketBin[16:32],2)

Identification = int(EthernetPacketBin[32:48],2)
Flags = int(EthernetPacketBin[48:51],2)
FragOffset = int(EthernetPacketBin[51:64],2)
TTL = int(EthernetPacketBin[64:72],2)

Protocol = int(EthernetPacketBin[72:80],2)
HeaderChecksum = int(EthernetPacketBin[80:96],2)
SRC = int(EthernetPacketBin[96:128],2)
DST = int(EthernetPacketBin[128:160],2)
Option = int(EthernetPacketBin[160:],2)

EthernetPacketDict = {'Version' : Version , 'Hlen' : Hlen, 'TOS':TOS,'TotalLength':TotalLength,
				'Identification':Identification, 'Flags':Flags, 'FragOffset':FragOffset,
				'TTL':TTL, 'Protocol':Protocol, 'HeaderChecksum':HeaderChecksum, 'SRC':SRC ,
				'DST':DST,'Option':Option}


fd = open('EthernetPacketDict.html','w')
html_content = []
html_content.append("<!DOCTYPE html>\n<html>\n<head>\n<style>\ntable, th, td \n{ \n border: 1px solid black; \n border-collapse: collapse; \n}\n ")
html_content.append("th, td \n{\npadding: 5px;\ntext-align: center;\n}\n</style>\n</head>\n<body>\n<table>\n")

for keys in EthernetPacketDict:
	html_content.append("<tr>\n")
	html_content.append("<th>")
	html_content.append(str(keys))
	html_content.append("</th>\n")
	html_content.append("<th>")
	html_content.append(str(EthernetPacketDict[str(keys)]))
	html_content.append("</th>\n")
	html_content.append("</tr>\n")
	
html_content.append("</table>\n</body>\n</html>")
s = "".join(html_content)
fd.write(s)
fd.close()

class Ethernet:
	frameCount = 0
	frameList = []
	
	def _init_(self,inputEthernetPacket):
		
		
	def 











