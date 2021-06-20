def goodput(packet):
    from time import time
    try:
        if packet["TCP"]["dstport"] == 6667 or packet["TCP"]["srcport"] == 6667:
            payload_len = packet["IP"]["len"] - 52
            tiempo = time() - packet.TIEMPO_INICIAL
            print(payload_len, ',', tiempo)
        else:
            pass
    except:
        try:
            packet.TIEMPO_INICIAL
        except:
            packet.global_var("TIEMPO_INICIAL", time())
    
    return packet


