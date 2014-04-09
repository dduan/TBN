# each unit is consist of (factor, offset, base unit)
relations = {
    'kilometer': (1000, 0, 'meter'),
}

# quantity is a tuple of (number, old_unit)
def convert(quantity, unit):
    if quantity[1] == None:
        return (quantity[0], unit)
    else:
        relation = relations[quantity[1]]
        return quantity[0] * relation[0] + relation[1], relation[2]

def lookup_base_unit(unit):
    return None
