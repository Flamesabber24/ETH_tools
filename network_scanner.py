import scapy.all as scapy


def scan(ip):
    answered_list = scapy.srp(scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst=ip), timeout=2)[0]

    for element in answered_list:
        print(element[1].psrc)
        print(element[1].hwsrc)
        print("------------------------------------------------------------------------------------------")


scan('10.0.2.1/24')
