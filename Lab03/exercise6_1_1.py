'''
xingeng wang
11144515
xiw031
'''
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


print(TCPPacketDict)

















