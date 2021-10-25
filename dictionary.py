alien01 = {'color': 'green', 'point': 5, 'ccok': 'rice'}
print(alien01['color'])
print(alien01['point'])
print(alien01['ccok'])

new_cook = alien01['ccok']
print(f"You just cooked {new_cook}.")

# Adding New Key-Value Pairs

alien02 = {'color': 'green', 'point': 5, 'ccok': 'rice'}
print(alien02)

alien02['x_position'] = 0
alien02['y_position'] = 25
alien02['name'] = 'Santosh'
print(alien02)

print("\nDone\n")

# Starting with an empty Dictionary
san_0 = {}
san_0['color'] = 'green'
san_0['points'] = 5
print(san_0)
print("Done\n")

# Modify values in a dictinary

san_0 = {'color': 'green'}
print(f"this is {san_0['color']}")

san_0['color'] = 'yellow'
print(f"now this is {san_0['color']}")
print('Done Modyfy value\n')
san_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original Possion: {san_0['x_position']} ")
# Move the san to the right
if san_0['speed'] == 'slow':
    x_increment = 1
elif san_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
san_0['x_position'] = san_0['x_position'] + x_increment

print(f"New position: {san_0['x_position']}")
print("Done Move Value\n")

# Reviving key value
san_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
del san_0['speed']
print(san_0)
print("Done Delete\n")
