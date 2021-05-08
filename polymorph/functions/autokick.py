def test(packet):
    try:
        req = packet["IRC"]["request"].split()
        if req[0]=="KICK":
            packet["IRC"]["request"] = "KICK #abcde juanit"
    except:
        pass
    return packet