vehicle = []

def create(vehicle):
    n = int(input("Enter the number of vehicles: "))
    for _ in range(n):
        a = input("Enter the vehicle name: ")
        
        # Check for duplicate vehicle names
        if any(a == v[0] for v in vehicle):
            print("!! Already exists !!")
        else:
            b = input("Enter the price: ")
            vehicle.append([a, b])  # Directly append name and price as a list

def display(vehicle):
    if not vehicle:
        print("No vehicles to display.")
    else:
        print("\nVehicle Records:")
        for v in vehicle:
            print(f"Name: {v[0]}, Price: {v[1]}")

while True:
    print("\nVehicle Records Menu")
    print("1. Create")
    print("2. Display")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        create(vehicle)
    elif choice == "2":
        display(vehicle)
    elif choice == "3":
        break
    else:
        print("!! Invalid choice !!")
