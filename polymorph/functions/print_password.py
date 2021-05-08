def print_password(packet):
    try:
        req = packet["IRC"]["request"].split()
        if req[0]=="OPER":
            print(req[2])
        return packet
    except:
        print("except")
        return packet
