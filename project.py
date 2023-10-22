class Container:
    def __init__(self, capacity_cubic_units, weight_limit_kg):
        self.capacity_cubic_units = capacity_cubic_units
        self.weight_limit_kg = weight_limit_kg
        self.items = []
        self.weight_kg = 0
        # Initialize container weight to 0

class Type:
    def __init__(self, container_type):
        self.container_type = container_type

class Item:
    def __init__(self, name, size_cubic_units, height_units, weight_kg):
        self.name = name
        self.size_cubic_units = size_cubic_units
        self.height_units = height_units
        self.weight_kg = weight_kg
        # Include weight as an attribute

def pack_containers(items, container_capacity_cubic_units, unit_name, weight_limit_kg):
    containers = []
    # List to store container instances
    packed_items = []
    # List to store items that have been successfully packed

    for item in items:
        packed = False
        for container in containers:
            if (container.capacity_cubic_units - sum(i.size_cubic_units for i in container.items) >= item.size_cubic_units and
                    container.weight_kg + item.weight_kg <= container.weight_limit_kg):
                container.items.append(item)
                container.weight_kg += item.weight_kg
                # Update container weight
                packed_items.append(item)
                packed = True
                break

        # If the item couldn't be packed into any existing container, create a new container
        if not packed:
            new_container = Container(container_capacity_cubic_units, weight_limit_kg)
            new_container.items.append(item)
            new_container.weight_kg += item.weight_kg
            # Update container weight
            containers.append(new_container)
            packed_items.append(item)

    return containers, packed_items

def main():
    unit_name = input("Enter the name of the cubic units (e.g., 'cubic meters', 'cubic feet'): ")
    container_type = input("Enter the container type (20-foot or 40-foot): ")
    if container_type not in ["20-foot", "40-foot"]:
        print("Invalid container type. Please specify '20-foot' or '40-foot'.")
        return

    container_capacity_cubic_units = float(input(f"Enter the container capacity in {unit_name}: "))
    weight_limit_kg = 24000 if container_type == "20-foot" else 40000
    num_items = int(input("Enter the number of items: "))

    items = []
    for i in range(num_items):
        item_name = input(f"Enter the name of item {i + 1}: ")
        item_size_cubic_units = float(input(f"Enter the size of item {i + 1} (in {unit_name}): "))
        item_height_units = float(input(f"Enter the height of item {i + 1} (in units): "))
        item_weight_kg = float(input(f"Enter the weight of item {i + 1} (in kg): "))
        # Added weight input
        items.append(Item(item_name, item_size_cubic_units, item_height_units, item_weight_kg))
        # Pass weight

    containers, packed_items = pack_containers(items, container_capacity_cubic_units, unit_name, weight_limit_kg)

    print("\nPacking result:")
    print(f"Number of containers used: {len(containers)}")

    for i, container in enumerate(containers):
        print(f"Container {i + 1}:")
        for item in container.items:
            print(f"  - {item.name} ({item.size_cubic_units} {unit_name}, {item.height_units} units tall)")

        if container.weight_kg > container.weight_limit_kg:
            print(f"  - Container is overweight (Total weight: {container.weight_kg} kg)")

    unpacked_items = [item for item in items if item not in packed_items]
    if unpacked_items:
        print("\nUnpacked items:")
        for item in unpacked_items:
            print(f"  - {item.name} ({item.size_cubic_units} {unit_name}, {item.height_units} units tall)")

if __name__ == "__main__":
    main()
