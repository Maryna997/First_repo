# lesson 7 @15:00

import argparse

parser = argparse.ArgumentParser(description="User data generator")
parser.add_argument("--filename", help="JSON file", required=True)
parser.add_argument("--amount", required=True)

arguments = parser.parse_args()
print(arguments)
my_arg = vars(arguments)    # vars - dictionary creation

dict()
arguments.__dict__
vars(arguments)

print(my_arg)

filename = my_arg.get("filename")
amount = int(my_arg.get("amount"))