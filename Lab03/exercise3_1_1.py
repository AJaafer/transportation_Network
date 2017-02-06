IPPacket = "450000283b1a400080066ac40ae30108cdc47b42c76a0050498a3cdaadbd4f1f5010fd5c128a0000"
IPPacketLength = 4*len(IPPacket)
IPPacketBin = bin(int(IPPacket,16))[2:].zfill(IPPacketLength)
length = int(IPPacketBin[16:32],2)
print("The totoal length of the IP packet is: %d"  %(length))

