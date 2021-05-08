def change_nick(packet):
    try:
        req = packet["IRC"]["request"].split()
        if req[0]=="NICK":
            packet["IRC"]["request"] = "NICK pwnd"
        return packet
    except:
        print("except")
        return packet
    