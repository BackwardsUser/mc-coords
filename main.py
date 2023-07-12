import argparse

def convert(nether, x, y, z):
    coords = []
    if (nether):
        coords.append(x*8)
        coords.append(y)
        coords.append(z*8)
    else:
        coords.append(x/8)
        coords.append(y)
        coords.append(z/8)
    return coords

parser = argparse.ArgumentParser(description="A Tool used to convert minecraft coordinates.")
parser.add_argument('-n', '--nether', action='store_true', help='Whether to convert from nether coords or overworld coords.')
parser.add_argument('x', type=int, default=0, help='The X Coordinate.')
parser.add_argument('y', type=int, default=0, help='The Y Coordinate.')
parser.add_argument('z', type=int, default=0, help='The Z Coordinate.')

args = parser.parse_args();

conversion = convert(args.nether, args.x, args.y, args.z)

print(f'Given Coordinates X:{args.x}, Y:{args.y}, Z:{args.z}\nConverted Coordinates: X:{conversion[0]}, Y:{conversion[1]}, Z:{conversion[2]}.')