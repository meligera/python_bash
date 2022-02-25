import sys, argparse
name = sys.argv[1:]
name_b = name[1]
print(f"Hello, {name_b}!")
parser = argparse.ArgumentParser()
parser.add_argument("-o", '--output', default='')
p = parser.parse_args(sys.argv[1:])
print(p.output)