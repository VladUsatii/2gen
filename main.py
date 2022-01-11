#!/usr/bin/env python3
from bit import PrivateKeyTestnet
import dbm
from pathlib import Path

"""
Arguments:

[ blank spot ] -- program will infer whether you have created a WIF or not
DELETE         -- delete WIF cache, delete key

"""

def printall(key):
	args = {'version': key.version, 'WIF': key.to_wif(), 'pubadd': key.address}
	print("""
Version             : {version}/production
WIF (PrivateAddress): {WIF}
Public address      : {pubadd}
""".format(**args))

keypath = Path('WIF.db')
if keypath.is_file():
	with dbm.open('WIF', 'r') as db:
		WIF = db['wif_address'].decode('utf-8')
		key = PrivateKeyTestnet(WIF)
	printall(key)
else:
	key = PrivateKeyTestnet()
	with dbm.open('WIF', 'c') as db:
		WIF = key.to_wif()
		db['wif_address'] = WIF
	printall(key)


