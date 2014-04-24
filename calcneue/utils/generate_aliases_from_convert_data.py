import sys
import json
import os
from pluralize import pluralize

relations = json.loads(open(sys.argv[1]).read())
result = {}
for unit, base in relations.items():
    bare = unit.lower()
    if bare not in result:
        result[bare] = unit
        result[pluralize(bare)] = unit
    bare = base[2].lower()
    if bare not in result:
        result[bare] = base[2]
        result[pluralize(bare)] = base[2]

print(json.dumps(result, indent=2))
