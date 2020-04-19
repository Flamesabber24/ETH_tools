import scapy.all as scapy
import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP / IP range.")
    options = parser.parse_args()
    return options


def scan(ip):
    answered_list = scapy.srp(scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst=ip), verbose=False, timeout=1)[0]

    clients_list = []
    for element in answered_list:
        client_dict = {'ip': element[1].psrc, 'mac': element[1].hwsrc}
        clients_list.append(client_dict)

    return clients_list


def print_result(results_list):
    print("IP\t\tMAC ADDRESS\n----------------------------------------")
    for client in results_list:
        print(client['ip'] + '\t' + client['mac'])


# options = get_arguments()
print_result(scan(get_arguments().target))