def autokick(packet):
    try:
        req = packet["IRC"]["request"].split()
        if req[0]=="KICK":
            packet["IRC"]["request"] = "KICK #canal_secreto pwnd"
    except:
        pass
    return packet
