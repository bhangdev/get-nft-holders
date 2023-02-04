import os
import argparse
import csv
import pandas as pd

from helpers.endpoints import *

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--address", help="Collection contract address", required=True)
parser.add_argument("-c", "--chain", help="EVM chain name")
parser.add_argument("-m", "--manifold", help="Add mint amount for manifold")
args = parser.parse_args()

if args.address:
    print("Contract address: % s" % args.address)

if args.manifold:
    print("Manifold value: % s" % args.manifold)

chain = args.chain if args.chain else "eth"

api_key = os.environ['APIKEY']

try:
    contract_info = get_contract_info(api_key, args.address, chain)
    print("Contract info: %s" % contract_info)
except:
    print("Contract not found")
    exit(1)

filename = "data/holders_%s.csv" % contract_info["symbol"]

if os.path.exists(filename):
    os.remove(filename)

cursor = ""
has_header = False

while True:
    result = get_nft_holders(api_key, args.address, chain, 100, cursor)

    cursor = result["cursor"]

    if args.manifold:
        header = ["address", "value"]
    else:
        header = ["address"]
        
    with open(filename, "a", encoding="UTF8", newline="") as f:
        writer = csv.writer(f)

        if not has_header:
            writer.writerow(header)
            has_header = True

        for i in result["result"]:
            print(i['owner_of'])

            if args.manifold:
                writer.writerow([i["owner_of"], args.manifold])
            else:
                writer.writerow([i["owner_of"]])

    if cursor is None:
        data = pd.read_csv(filename)
        data.drop_duplicates(subset="address", keep="first", inplace=True)
        data.to_csv(filename, index=False)

        break
