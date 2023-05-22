import argparse

parser = argparse.ArgumentParser(description="Test terminal args")

parser.add_argument("-test", help="Input a number", type=int)

args = parser.parse_args()

print(f"The input args is {args.test}")
