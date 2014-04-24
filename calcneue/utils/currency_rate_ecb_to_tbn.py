import sys
import pprint
import json

name, rate = tuple(open(sys.argv[1]).readlines())
name = [n.strip() for n in name.split(',')]
rate = [[r.strip(), 0, 'EURO'] for r in rate.split(',')]
d = dict(zip(name, rate))
del d['Date']
del d['']
for c in d:
    d[c][0] = 1 / float(d[c][0])
    d[c] = tuple(d[c])

print(json.dumps(d, indent=2))
