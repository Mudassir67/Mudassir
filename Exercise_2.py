# Step 1: Starting with two toys
toy_collection = {
    "Teddy Bear": {
        "age_suitability": 3,
        "is_electronic": False
    },
    "Remote Control Car": {
        "age_suitability": 6,
        "is_electronic": True
    }
}

# Step 2: Functions

# Function to find a toy by name
def find_toy(name):
    if name in toy_collection:
        toy = toy_collection[name]
        print(f"Toy: {name}")
        print(f"Age Suitability: {toy['age_suitability']}")
        print(f"Electronic: {toy['is_electronic']}")
    else:
        print(f"{name} is not in the toy collection.")

# Function to add a new toy
def add_toy(name, age_suitability, is_electronic):
    if name not in toy_collection:
        toy_collection[name] = {
            "age_suitability": age_suitability,
            "is_electronic": is_electronic
        }
        print(f"{name} has been added to the collection.")
    else:
        print(f"{name} already exists in the collection.")

# Function to remove a toy by name
def remove_toy(name):
    if name in toy_collection:
        del toy_collection[name]
        print(f"{name} has been removed from the collection.")
    else:
        print(f"{name} is not in the collection.")

# Function to list all toys in the collection
def list_toys():
    if toy_collection:
        print("Toys in the collection:")
        for name in toy_collection.keys():
            print(f"- {name}")
    else:
        print("The toy collection is empty.")

# Step 2: Adding more toys
add_toy("Lego Set", 5, False)  # Example of adding a new toy
add_toy("RC Helicopter", 10, True)  # Another toy

# Step 3: Testing the functions

# Listing all toys
list_toys()

# Finding a toy
find_toy("Teddy Bear")
find_toy("Lego Set")

# Removing a toy
remove_toy("Remote Control Car")

# Listing again after removal
list_toys()
