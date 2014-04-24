# each unit is consist of (factor, offset, base unit)
import json
import os

datapath = os.path.join(os.path.dirname(__file__), 'convert.json')
relations = json.loads(open(datapath).read())
aliaspath = os.path.join(os.path.dirname(__file__), 'aliases.json')
aliases = json.loads(open(aliaspath).read())

def convert(quantity, unit):

    if quantity[1] == None:
        if unit == None:
            return (quantity[0], (set(), set()))
        else:
            return (quantity[0], ({(unit, 1)}, set()))
    else: 
        unit = lookup_alias(unit)
        old_unit = lookup_alias(quantity[1])
        if unit == old_unit:
            return quantity[0], ({(unit, 1)}, set())
        try:
            # found relation
            relation = relations[old_unit]
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

def convert_to_base(number, unit):
    if not unit:
        return number, (set(), set())
    try:
        # found relation
        relation = relations[unit]
        if isinstance(relation[0], str):
            relation[0] = eval(relation[0])
        return number * relation[0] + relation[1], ({(relation[2], 1)}, set())
    except KeyError:
        return number, ({(unit, 1)}, set())


def lookup_alias(unit):
    global aliases
    if unit:
        alias = aliases.get(unit.lower(), None)
        if alias:
            return alias
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
