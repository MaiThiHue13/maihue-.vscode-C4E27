from matplotlib import pyplot

# 1. prepare data
machine_counts = [18, 4, 2]

# 2. prepare labels
machine_name = ["PC", "MAC", "Linux"]

# 3. draw pie
pyplot.pie(machine_counts, labels = machine_name, autopct="%1.f%%", shadow=True, explode=[0, 0.1,0])

# 4. show
pyplot.show()