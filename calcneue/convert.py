# each unit is consist of (factor, offset, base unit)
import json
import os

datapath = os.path.join(os.path.dirname(__file__), 'convert.json')
relations = json.loads(open(datapath).read())
mappath = os.path.join(os.path.dirname(__file__), 'aliases.json')
aliases = json.loads(open(mappath).read())

# quantity is a tuple of (number, old_unit)
def convert(quantity, unit):
    unit = lookup_alias(unit)
    if quantity[1] == None:
        if unit == None:
            return (quantity[0], (set(), set()))
        else:
            return (quantity[0], ({(unit, 1)}, set()))
    else: 
        try:
            # found relation
            relation = relations[quantity[1]]
            if isinstance(relation[0], str):
                relation[0] = eval(relation[0])
            return quantity[0] * relation[0] + relation[1], ({(relation[2],1)},set())
        except KeyError:
            try:
                    # found inverse relation
                    relation = relations[unit]
                    if isinstance(relation[0], str):
                        relation[0] = eval(relation[0])
                    return (quantity[0] - relation[1]) / relation[0], ({(unit, 1)},set())
            except KeyError:
                # can't find relation, keep old unit
                return quantity[0], ({(quantity[1], 1)}, set())

def lookup_alias(unit):
    '''also takes care of aliases 'm' => "meter"'''
    global aliases
    base = aliases.get(unit, None)
    if base:
        return base
    else: 
        return unit

if __name__ == '__main__':
    while True:
        try:
            s = input('convert > ')
        except EOFError:
            break
        s.split()
        print(convert(s[0], s[1]));
