'''
xingeng wang
11144515
xiw031
'''
EthernetPacket = input("Please type the Ethernet String: ")
EthernetPacketLength = 4*len(EthernetPacket)
EthernetPacketBin = bin(int(EthernetPacket,16))[2:].zfill(EthernetPacketLength)
Frame =[]
i=0
while 1:
	dic = { 'DST. MAC ADDR' : int(EthernetPacketBin[0:48],2),'SRC. MAC ADDR' : int(EthernetPacketBin[48:96],2),'TYPE' : hex(int(EthernetPacketBin[96:112],2))}
	Frame.append(dic)
	EthernetPacketBin = EthernetPacketBin[112:]
	if (len(EthernetPacketBin)==0):
		break
	elif (Frame[i]['TYPE'] == '0x800'):
		IPLength = int(EthernetPacketBin[16:32],2)
		Frame[i]['PAYLOAD'] = EthernetPacketBin[0:IPLength*8]
		EthernetPacketBin = EthernetPacketBin[IPLength*8:]
	if (len(EthernetPacketBin)==0):
		break
	i=i+1

print("There are " + str(len(Frame)) + " frame")
print(Frame)

fd = open('Ethernet.html','w')
html_content = []
html_content.append("<!DOCTYPE html>\n<html>\n<head>\n<style>\ntable, th, td \n{ \n border: 1px solid black; \n border-collapse: collapse; \n}\n ")
html_content.append("th, td \n{\npadding: 5px;\ntext-align: center;\n}\n</style>\n</head>\n<body>\n")

for element in Frame:
	html_content.append("<table " + 'style="width:100%"'+ ">\n")
	for keys in element:
		if (str(keys) == 'PAYLOAD'):
			IPPacket = element[str(keys)]
			Version = int(IPPacket[0:4],2)
			Hlen = int(IPPacket[4:8],2)
			TOS = int(IPPacket[8:16],2)
			TotalLength = int(IPPacket[16:32],2)

			Identification = int(IPPacket[32:48],2)
			Flags = int(IPPacket[48:51],2)
			FragOffset = int(IPPacket[51:64],2)
			TTL = int(IPPacket[64:72],2)

			Protocol = int(IPPacket[72:80],2)
			HeaderChecksum = int(IPPacket[80:96],2)
			SRCList = []
			SRCList.append(str(int(IPPacket[96:104],2)))
			SRCList.append(str(int(IPPacket[104:112],2)))
			SRCList.append(str(int(IPPacket[112:120],2)))
			SRCList.append(str(int(IPPacket[120:128],2)))
			SRC =".".join(SRCList) 
			DSTList = []
			DSTList.append(str(int(IPPacket[128:136],2)))
			DSTList.append(str(int(IPPacket[136:144],2)))
			DSTList.append(str(int(IPPacket[144:152],2)))
			DSTList.append(str(int(IPPacket[152:160],2)))
			DST =".".join(DSTList) 
			Option = int(IPPacket[160:],2)
			IPPacketDict = {'Version' : Version , 'Hlen' : Hlen, 'TOS':TOS,'TotalLength':TotalLength,
				'Identification':Identification, 'Flags':Flags, 'FragOffset':FragOffset,
				'TTL':TTL, 'Protocol':Protocol, 'HeaderChecksum':HeaderChecksum, 'SRC':SRC ,
				'DST':DST,'Option':Option}
			
			for keys in IPPacketDict:
				html_content.append("<tr>\n")
				html_content.append("<th>")
				html_content.append(str(keys))
				html_content.append("</th>\n")
				html_content.append("<td>")
				html_content.append(str(IPPacketDict[str(keys)]))
				html_content.append("</td>\n")
				html_content.append("</tr>\n")
		else:
			html_content.append("<tr>\n")
			html_content.append("<th>")
			html_content.append(str(keys))
			html_content.append("</th>\n")
			html_content.append("<td>")
			html_content.append(str(element[str(keys)]))
			html_content.append("</td>\n")
			html_content.append("</tr>\n")
		
	html_content.append("</table>\n")
html_content.append("</body>\n</html>")
s = "".join(html_content)
fd.write(s)
fd.close()

