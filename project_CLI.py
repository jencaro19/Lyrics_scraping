import argparse



parser = argparse.ArgumentParser(description='my first program')
parser.add_argument('message', help = 'displays the string you use here')
args = parser.parse_args()



print(args.message)
