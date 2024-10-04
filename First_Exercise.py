for user in users:
    name, age = user
    if age >= 18:
        print(f"{name} is allowed to vote.")
    else:
        print(f"{name} is not allowed to vote.")


# Dictionary to store the toy collection
toy_collection = {}

# Function to add a toy to the collection
def add_toy(name, age_suitability, is_electronic):
    toy_collection[name] = {
        "age_suitability": age_suitability,
        "is_electronic": is_electronic
    }

# Function to find a toy by name
def find_toy(name):
    return toy_collection.get(name, f"Toy '{name}' not found in the collection.")

# Function to remove a toy from the collection
def remove_toy(name):
    if name in toy_collection:
        del toy_collection[name]
        return f"Toy '{name}' removed from the collection."
    else:
        return f"Toy '{name}' not found in the collection."

# Function to list all toys in the collection
def list_toys():
    if toy_collection:
        for name, details in toy_collection.items():
            print(f"Name: {name}, Age Suitability: {details['age_suitability']}, Electronic: {details['is_electronic']}")
    else:
        print("No toys in the collection.")

# Example Usage
add_toy("Action Figure", 7, False)
add_toy("Remote Car", 8, True)
print(find_toy("Action Figure"))
print(remove_toy("Remote Car"))
list_toys()