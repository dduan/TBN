# each unit is consist of (factor, offset, base unit)
relations = {
    'kilometer': (1000, 0, 'meter'),
    'celsius': (9/5, 32, 'farenheit'),
}

# quantity is a tuple of (number, old_unit)
def convert(quantity, unit):
    # 1 in meter, unit should be meter
    if quantity[1] == None:
        if unit == None:
            return (quantity[0], ([], []))
        else:
            return (quantity[0], ([unit, 1], []))
    else: 
        try:
            # found relation
            relation = relations[quantity[1]]
            return quantity[0] * relation[0] + relation[1], ([(relation[2],1)],[])
        except KeyError:
            try:
                    # found inverse relation
                    relation = relations[unit]
                    return (quantity[0] - relation[1]) / relation[0], ([(unit, 1)],[])
            except KeyError:
                # can't find relation, keep old unit
                return quantity[0], ([(quantity[1], 1)], [])

def lookup_base_unit(unit):
    '''also takes care of aliases 'm' => "meter"'''
    return unit

if __name__ == '__main__':
    while True:
        try:
            s = input('convert > ')
        except EOFError:
            break
        s.split()
        print(convert(s[0], s[1]));
