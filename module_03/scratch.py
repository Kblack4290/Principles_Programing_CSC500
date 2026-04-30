
# Containers received
shipping_containers = ['A101','A102','A103','B201','B202','B203','C301','C302','C303']

# Initializing transportation arrays
train_array= []
truck_array = []
boat_array = []

# Sorting containers into transportation arrays
for container in shipping_containers:
    if container.startswith('A'):
        train_array.append(container)
    elif container.startswith('B'):
        truck_array.append(container)
    elif container.startswith('C'):
        boat_array.append(container)       
        
    # print updated transportation arrays     
    print('Train Array:', train_array)
    print('Truck Array:', truck_array)
    print('Boat Array:', boat_array)