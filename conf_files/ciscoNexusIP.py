#!/usr/bin/etc python
#coding:utf-8

import json

ciscoNexusIP = {
"ZZTC30SW0A-S6" : "10.102.254.3",
"ZZTC30SW0B-S6" : "10.102.254.4",
"ZZTC30SW01-A6" : "10.102.250.1",
"ZZTC30SW02-A6" : "10.102.250.2",
"ZZTC30SW03-S6" : "10.102.250.3",
"ZZTC30SW04-S6" : "10.102.250.4",
"ZZTC30SW0A-D6" : "10.102.254.19",
"ZZTC30SW0B-D6" : "10.102.254.20",
"SHZB30SW01-C1" : "10.48.254.37",
"SHZB30SW02-C1" : "10.48.254.38",
"SHZB30SW0A-C1" : "10.48.255.3",
"SHZB30SW0B-C1" : "10.48.255.4",
"SHZB30SW0A-D3" : "10.53.254.3",
"SHZB30SW0B-D3" : "10.53.254.4",
"ZZTC70SW0A-A1" : "172.30.0.1",
"ZZTC30SW0B-D4" : "172.30.0.100",
"ZZTC30SW0A-S1S2" : "172.30.0.129",
"ZZTC30SW0B-S1S2" : "172.30.0.130",
"ZZTC30SW01-S1" : "172.30.0.135",
"ZZTC30SW02-S1" : "172.30.0.136",
"ZZTC30SW0A-M1" : "172.30.0.161",
"ZZTC30SW0B-M1" : "172.30.0.162",
"ZZTC30SW01-M1" : "172.30.0.163",
"ZZTC30SW02-M1" : "172.30.0.164",
"ZZTC56SW0A-C1" : "172.30.0.17",
"ZZTC30SW01-NAS" : "172.30.0.179",
"ZZTC56SW0B-C1" : "172.30.0.18",
"ZZTC30SW02-NAS" : "172.30.0.180",
"ZZTC30SW03-NAS" : "172.30.0.181",
"ZZTC30SW04-NAS" : "172.30.0.182",
"ZZTC30SW01-RAC" : "172.30.0.193",
"ZZTC30SW02-RAC" : "172.30.0.194",
"ZZTC30SW03-RAC" : "172.30.0.195",
"ZZTC30SW04-RAC" : "172.30.0.196",
"ZZTC30SW05-RAC" : "172.30.0.197",
"ZZTC30SW06-RAC" : "172.30.0.198",
"ZZTC70SW0B-A1" : "172.30.0.2",
"ZZTC70SW0A-HL" : "172.30.0.3",
"ZZTC56SW0A-C2" : "172.30.0.33",
"ZZTC56SW0B-C2" : "172.30.0.34",
"ZZTC70SW0B-HL" : "172.30.0.4",
"ZZTCZX30SW0A-C2" : "172.30.0.43",
"ZZTCZX30SW0B-C2" : "172.30.0.44",
"ZZTC56SW0A-C3" : "172.30.0.49",
"ZZTC56SW0B-C3" : "172.30.0.50",
"ZZTC30SW0A-C3" : "172.30.0.55",
"ZZTC30SW0B-C3" : "172.30.0.56",
"ZZTC30SW0A-A2" : "172.30.0.67",
"ZZTC30SW0B-A2" : "172.30.0.68",
"ZZTC30SW0A-D3" : "172.30.0.83",
"ZZTC30SW0B-D3" : "172.30.0.84",
"ZZTC30SW0A-D4" : "172.30.0.99",
"ZZDC70SW0A-A1" : "172.31.0.1",
"ZZDC30SW0B-D4" : "172.31.0.100",
"ZZDC30SW01-D4" : "172.31.0.107",
"ZZDC30SW02-D4" : "172.31.0.108",
"ZZDC30SW0A-D5" : "172.31.0.147",
"ZZDC30SW0B-D5" : "172.31.0.148",
"ZZDC30SW0A-S1" : "172.31.0.163",
"ZZDC30SW0B-S1" : "172.31.0.164",
"ZZDC30SW0A-S2" : "172.31.0.179",
"ZZDC30SW0B-S2" : "172.31.0.180",
"ZZDC4F30SW0A-S3" : "172.31.0.195",
"ZZDC4F30SW0B-S3" : "172.31.0.196",
"ZZDC70SW0B-A1" : "172.31.0.2",
"ZZDC30SW0A-M1" : "172.31.0.211",
"ZZDC30SW0B-M1" : "172.31.0.212",
"ZZDC30SW01-NAS" : "172.31.0.225",
"ZZDC30SW02-NAS" : "172.31.0.226",
"ZZDC30SW03-NAS" : "172.31.0.227",
"ZZDC30SW04-NAS" : "172.31.0.228",
"ZZDC30SW05-NAS" : "172.31.0.229",
"ZZDC30SW06-NAS" : "172.31.0.230",
"ZZDC30SW01-RAC" : "172.31.0.241",
"ZZDC30SW02-RAC" : "172.31.0.242",
"ZZDC56SW0A-C1" : "172.31.0.33",
"ZZDC56SW0B-C1" : "172.31.0.34",
"ZZDC56SW0A-C3" : "172.31.0.35",
"ZZDC56SW0B-C3" : "172.31.0.36",
"ZZDC70SW0A-HL" : "172.31.0.5",
"ZZDC70SW0B-HL" : "172.31.0.6",
"ZZDC30SW0A-A2" : "172.31.0.67",
"ZZDC30SW0B-A2" : "172.31.0.68",
"ZZDC30SW0A-D3" : "172.31.0.83",
"ZZDC30SW0B-D3" : "172.31.0.84",
"ZZDC30SW0A-D4" : "172.31.0.99",
"ZZDC30SW03-RAC" : "172.31.254.43",
"ZZDC30SW04-RAC" : "172.31.254.44",
"ZZDC30SW05-RAC" : "172.31.254.27",
"ZZDC30SW06-RAC" : "172.31.254.28",
"ZZDC4F56SW0C-C1" : "172.31.32.1",
"ZZDC4F30SWM301-S1" : "172.31.32.100",
"ZZDC4F30SWN201-S1" : "172.31.32.101",
"ZZDC4F30SWN301-S1" : "172.31.32.102",
"ZZDC4F30SW0C-S2" : "172.31.32.129",
"ZZDC4F30SW0D-S2" : "172.31.32.130",
"ZZDC4F30SWM201-S2" : "172.31.32.131",
"ZZDC4F30SWM301-S2" : "172.31.32.132",
"ZZDC4F30SWN201-S2" : "172.31.32.133",
"ZZDC4F30SWN301-S2" : "172.31.32.134",
"ZZDC4F30SW0C-D5" : "172.31.32.161",
"ZZDC4F30SW0D-D5" : "172.31.32.162",
"ZZDC4F30SWM201-D5" : "172.31.32.163",
"ZZDC4F30SWM301-D5" : "172.31.32.164",
"ZZDC4F30SWN201-D5" : "172.31.32.165",
"ZZDC4F30SWN301-D5" : "172.31.32.166",
"ZZDC4F30SW0C-M1" : "172.31.32.193",
"ZZDC4F30SW0D-M1" : "172.31.32.194",
"ZZDC4F30SWM201-M1" : "172.31.32.195",
"ZZDC4F30SWM301-M1" : "172.31.32.196",
"ZZDC4F30SWN201-M1" : "172.31.32.197",
"ZZDC4F30SWN301-M1" : "172.31.32.198",
"ZZDC4F56SW0D-C1" : "172.31.32.2",
"ZZDC4F30SWM201-NAS" : "172.31.32.225",
"ZZDC4F30SWM301-NAS" : "172.31.32.226",
"ZZDC4F30SWN201-NAS" : "172.31.32.227",
"ZZDC4F30SWN301-NAS" : "172.31.32.228",
"ZZDC4F30SW01-RAC" : "172.31.32.241",
"ZZDC4F30SW02-RAC" : "172.31.32.242",
"ZZDC4F30SW03-RAC" : "172.31.32.243",
"ZZDC4F30SW04-RAC" : "172.31.32.244",
"ZZDC4F56SW0C-C2" : "172.31.32.3",
"ZZDC4F30SW0C-D3" : "172.31.32.33",
"ZZDC4F30SW0D-D3" : "172.31.32.34",
"ZZDC4F30SWM201-D3" : "172.31.32.35",
"ZZDC4F30SWM301-D3" : "172.31.32.36",
"ZZDC4F30SWN201-D3" : "172.31.32.37",
"ZZDC4F30SWN301-D3" : "172.31.32.38",
"ZZDC4F30SWJ101-D3" : "172.31.32.39",
"ZZDC4F56SW0D-C2" : "172.31.32.4",
"ZZDC4F30SWK101-D3" : "172.31.32.40",
"ZZDC4F56SW0C-C3" : "172.31.32.5",
"ZZDC4F56SW0D-C3" : "172.31.32.6",
"ZZDC4F30SW0C-D4" : "172.31.32.65",
"ZZDC4F30SW0D-D4" : "172.31.32.66",
"ZZDC4F30SWM201-D4" : "172.31.32.67",
"ZZDC4F30SWM301-D4" : "172.31.32.68",
"ZZDC4F30SWN201-D4" : "172.31.32.69",
"ZZDC4F30SWN301-D4" : "172.31.32.70",
"ZZDC4F30SW0C-S1" : "172.31.32.97",
"ZZDC4F30SW0D-S1" : "172.31.32.98",
"ZZDC4F30SWM201-S1" : "172.31.32.99",
}
NexusIP = {
 "ZZTC70SW0A-A1" : "172.30.0.1",
 "ZZTC56SW0A-C1" : "172.30.0.17",
}

with open('ciscoNexusIP.txt', 'w') as f:
    json.dump(ciscoNexusIP, f)
    #json.dump(NexusIP, f)

print(len(ciscoNexusIP))
