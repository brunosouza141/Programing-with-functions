import math
i = int(input('The number of manufactured items'))
t = int(input('The number of items that the user will pack per box'))

print(f'For {i} items, packing {t} items in each box, you will need {math.ceil(i/t)} boxes.')