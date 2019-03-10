inventory = {'gold':500, 'pouch':['flint', 'twine', 'gemstore'], 'backpack':['xylophone', 'danger', 'bedroll','bread loaf']}
print(inventory)

inventory['pocket'] = ['seashell', 'strange berry', 'lint']
print(inventory)
inventory['backpack'].remove('danger')
print(inventory)
inventory['gold'] += 50
print(inventory)