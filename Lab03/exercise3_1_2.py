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
TTL = int(IPPacketBin[64:70],2)

Protocol = int(IPPacketBin[70:80],2)
HeaderChecksum = int(IPPacketBin[80:96],2)
SRC = int(IPPacketBin[96:128],2)
DST = int(IPPacketBin[128:160],2)
Option = int(IPPacketBin[160:],2)

IPPacketDict = {'Version' : Version , 'Hlen' : Hlen, 'TOS':TOS,'TotalLength':TotalLength,
				'Identification':Identification, 'Flags':Flags, 'FragOffset':FragOffset,
				'TTL':TTL, 'Protocol':Protocol, 'HeaderChecksum':HeaderChecksum, 'SRC':SRC ,
				'DST':DST,'Option':Option}
print(IPPacketDict)

















