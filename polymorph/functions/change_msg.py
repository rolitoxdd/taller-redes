def change_msg(packet):
    try:
        req = packet["IRC"]["request"].split()
        if req[0]=="PRIVMSG":
            packet["IRC"]["request"] = req[0] + " " + req[1] + " :lol"
        return packet
    except:
        print("except")
        return packet