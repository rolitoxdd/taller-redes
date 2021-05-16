def malform_packet(packet):
    try:
        req = packet["IRC"]["request"]
        print(req)
        packet["IRC"]["request"] = "x"*len(req)
        print(packet["IRC"]["request"])
        return packet
    except:
        print("except")
        return None
