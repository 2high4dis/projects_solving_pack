# Find Cost of Tile to Cover W x H Floor
# Calculate the total cost of tile it would take to cover a floor plan of width and height,
# using a cost entered by the user.

cost = int(input('Enter a cost of 1 square meter of tile ($): '))

width = int(input('Enter a width of floor (m): '))
height = int(input('Enter a height of floor (m): '))

total_cost = round((width * height) * cost, 2)

print(f'Cost of tile to cover {width} x {height} floor: {total_cost}$')
