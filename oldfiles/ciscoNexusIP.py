#!/usr/bin/etc python
#coding:utf-8

import json

ciscoNexusIP = {
    "ZZTC30SW01-A6" : "10.102.250.1",
    "ZZTC30SW02-A6" : "10.102.250.2",
    "ZZTC30SW0A-D6" : "10.102.254.19",
    "ZZTC30SW0B-D6" : "10.102.254.20",
    "ZZTC30SW0A-S6" : "10.102.192.251",
    "ZZTC30SW0B-S6" : "10.102.192.252",
    "ZZTC30SW03-S6" : "10.102.250.3",
    "ZZTC30SW04-S6" : "10.102.250.4",
    "ZZDC70SW0A-A1" : "172.31.0.1",
    "ZZDC70SW0B-A1" : "172.31.0.2",
    "ZZDC70SW0A-HL" : "172.31.0.5",
    "ZZDC70SW0B-HL" : "172.31.0.6",
}

with open('ciscoNexusIP.txt', 'w') as f:
    json.dump(ciscoNexusIP, f)

print(len(ciscoNexusIP))
