units = {
    'kilometer': (1000, 'meter'),
    'kilometers': (1000, 'meter'),
    'kilometre': (1000, 'meter'),
    'kilometres': (1000, 'meter'),
}
def convert(quantity, unit):
    if quantity[1] == None:
        return (quantity[0], unit)
    else:
        factor = units[quantity[1]]
        return quantity[0] * factor[0], factor[1]

def lookup_base_unit(unit):
    return None
