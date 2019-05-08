# -*- coding: utf-8 -*-

import time, socket, thread


def ping(ip):
    alive = False
    port = False
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s.settimeout(4)

    def checkPort(ip, port):
        try:
            exit = s.connect_ex((ip, port))
            return (exit != 113)
        except:
            return False
        finally:
            s.close()

    for port in [80, 443]:
        port = checkPort(ip, port)
        if port:
            alive = True
            break
    return (alive, port)

def ipToList(ip, ips):
    alive, port = ping(ip)
    if alive:
        ips.append(ip)

def getIps():
    ips = []
    nw = ['192.168.10.', '192.168.7.']
    #nw = ['192.168.224.']
    for ip in nw:
        for i in xrange(1, 255):
            IP = ip + str(i)
            thread.start_new_thread(ipToList, (IP, ips))
    time.sleep(2)
    return ips

if __name__ == '__main__':
    from pprint import pprint
    IP = getIps()
    pprint(IP)
    print len(IP)
