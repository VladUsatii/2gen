#!/usr/bin/env python3
from bit import PrivateKeyTestnet
import dbm
from pathlib import Path
import sys, os

"""
Arguments:

GET            -- program will infer whether you have created a WIF or not
DELETE         -- delete WIF cache, delete key

"""

def printall(key):
	args = {'version': key.version, 'WIF': key.to_wif(), 'pubadd': key.address}
	print("""
Version             : {version}/production
WIF (PrivateAddress): {WIF}
Public address      : {pubadd}
""".format(**args))




def main(kwargs):
	keypath = Path('WIF.db')

	if kwargs == 'GET':
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
	elif kwargs == 'DELETE':
		if keypath.is_file():
			prompter = input("Are you sure you want to delete your key? You will lose access to your coins, unless your WIF is documented. [Y/N]")
			if prompter == 'Y' or prompter == 'y':
				os.remove('WIF.db')
			elif prompter == 'N' or prompter == 'n':
				print('Operation canceled.')
	else:
		print('Not a valid argument.')


if __name__ == '__main__':
	try:
		main(sys.argv[1]) # sys.argv[1] is an argument
	except Exception:
		print('Not a valid argument.')


