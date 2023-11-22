class House:
    """A simple house class"""

    total_house = 0  # Keep track of the total number of houses

    def __init__(self, floors, doors, windows, color="White", has_garage=False, address=""):
        self.floors = floors
        self.doors = doors
        self.windows = windows
        self.color = color
        self.has_garage = has_garage
        self.address = address

        # Increment
        House.total_house += 1

    def display_info(self):
        """Displays attribute information of a house object."""
        print("House Information: ")
        print(f"    - Address: {self.address}")
        print(f"    - Doors: {self.doors}")
        print(f"    - Floors: {self.floors}")
        print(f"    - Windows: {self.windows}")
        print(f"    - Color: {self.color}")
        print(f"    - Has Garage: {'Yes' if self.has_garage else 'No'}")

    @classmethod
    def display_total_houses(cls):
        print(f"Total number of houses = {cls.total_house}")

    @staticmethod
    def validate_house(house):
        if not isinstance(house, House):
            return False    # Not a valid house object
        if not all(isinstance(attr, int) and attr > 0 for attr in (house.floors, house.doors, house.windows)):
            return False    # Floors, Doors, Windows should all be positive integers

        return True

    def paint_house(self, new_color):
        """Change the color of the house."""
        self.color = new_color
        print(f"The house at {self.address} has been painted {new_color}.")

    def add_garage(self):
        """Add a garage to the house if it doesn't already have one."""
        if not self.has_garage:
            self.has_garage = True
            print(f"A garage has been added to the house at {self.address}.")
        else:
            print(f"The house at {self.address} already has a garage.")

    def set_address(self, new_address):
        """Change the address of the house."""
        self.address = new_address
        print(f"The address of the house has been updated to {new_address}.")

# Creating instances (objects) of the House class
house1 = House(floors=2, doors=3, windows=6, color="Blue", has_garage=True, address="123 Main St")
house2 = House(floors=1, doors=2, windows=4, address="123 Main St")
house3 = House(floors=12, doors=23, windows=42,has_garage=True, address="123 Main St")

house1.display_info()
print()
house2.display_info()
print()
house3.display_info()
print()
House.display_total_houses()
print()

validation_result = House.validate_house(house2)
print(f"House Validation Result: {'Valid' if validation_result else 'Invalid'}")

# Testing the new methods
house3.paint_house("Red")
house3.add_garage()
house1.add_garage()  # Attempting to add a garage to a house that already has one
house2.set_address("456 Oak St")
house2.display_info()
