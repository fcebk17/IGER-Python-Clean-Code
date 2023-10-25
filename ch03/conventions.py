#Bad
if attr == True:
    print('True!')

if attr == None:
    print('attr is None!')

#Good
if attr:
    print('attr is truthy!')

if not attr:
    print('attr is falsy!')

if attr is None:
    print('attr is None!')