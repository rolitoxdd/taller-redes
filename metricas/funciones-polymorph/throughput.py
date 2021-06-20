def throughput(packet):
    from time import time
    try:
        if packet["TCP"]["dstport"] == 6667 or packet["TCP"]["srcport"] == 6667:
            packet_len = packet["IP"]["len"] + 14 
            tiempo = time() - packet.TIEMPO_INICIAL
            print(packet_len, ',', tiempo)
        else:
            pass
    except:
        try:
            packet.TIEMPO_INICIAL
        except:
            packet.global_var("TIEMPO_INICIAL", time())
            try:
                if packet["TCP"]["dstport"] == 6667 or packet["TCP"]["srcport"] == 6667:
                    packet_len = packet["IP"]["len"] + 14
                    print(packet_len,',',tiempo)
            except:
                pass
    
    return packet


