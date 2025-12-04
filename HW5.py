from abc import ABC, abstractmethod
import math

# ===== PROBLEM 1: Shape Calculator with Polymorphism =====

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        return f"This is a {self.__class__.__name__}"

    @staticmethod
    def validate_positive(value, name):
        if value > 0:
            return True
        else:
            print(f"{name} must be positive!")
            return False


class Circle(Shape):
    def __init__(self, radius):
        if Shape.validate_positive(radius, "radius"):
            self.radius = radius
        else:
            raise ValueError("Invalid radius")

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        if (Shape.validate_positive(width, "width") and 
            Shape.validate_positive(height, "height")):
            self.width = width
            self.height = height
        else:
            raise ValueError("Invalid dimensions")

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        if (Shape.validate_positive(side1, "side1") and 
            Shape.validate_positive(side2, "side2") and 
            Shape.validate_positive(side3, "side3")):
            self.side1 = side1
            self.side2 = side2
            self.side3 = side3
        else:
            raise ValueError("Invalid side lengths")

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


class ShapeCollection:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def total_area(self):
        return sum(shape.area() for shape in self.shapes)

    def total_perimeter(self):
        return sum(shape.perimeter() for shape in self.shapes)


# ===== PROBLEM 2: Pizza Order System with Factory Pattern =====

class Pizza:
    price_list = {'small': 10, 'medium': 15, 'large': 20}
    topping_price = 2

    def __init__(self, size, toppings):
        if not self.validate_size(size):
            raise ValueError(f"Invalid size: {size}")
        self.size = size
        self.toppings = toppings

    def calculate_price(self):
        base_price = self.price_list[self.size]
        return base_price + (len(self.toppings) * self.topping_price)

    def __str__(self):
        return f"{self.size} pizza with {len(self.toppings)} toppings - ${self.calculate_price()}"

    @classmethod
    def create_margherita(cls, size):
        return cls(size, ['cheese', 'tomato', 'basil'])

    @classmethod
    def create_pepperoni(cls, size):
        return cls(size, ['cheese', 'pepperoni'])

    @classmethod
    def create_veggie(cls, size):
        return cls(size, ['cheese', 'mushrooms', 'peppers', 'onions'])

    @staticmethod
    def validate_size(size):
        return size in ['small', 'medium', 'large']


class PizzaOrder:
    total_orders = 0

    def __init__(self):
        PizzaOrder.total_orders += 1
        self.order_id = f"ORDER_{PizzaOrder.total_orders:03d}"
        self.pizzas = []

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def get_total(self):
        return sum(pizza.calculate_price() for pizza in self.pizzas)

    @classmethod
    def get_total_orders(cls):
        return cls.total_orders

    def __str__(self):
        return f"Order {self.order_id} - Total: ${self.get_total()}"


class OrderManager:
    @staticmethod
    def create_order_from_string(order_string):
        order = PizzaOrder()
        items = order_string.split(', ')
        
        for item in items:
            size, pizza_type = item.split(' ')
            
            if pizza_type == 'pepperoni':
                pizza = Pizza.create_pepperoni(size)
            elif pizza_type == 'margherita':
                pizza = Pizza.create_margherita(size)
            elif pizza_type == 'veggie':
                pizza = Pizza.create_veggie(size)
            else:
                raise ValueError(f"Unknown pizza type: {pizza_type}")
            
            order.add_pizza(pizza)
        
        return order

    @staticmethod
    def format_receipt(order):
        receipt = "=== RECEIPT ===\n"
        receipt += f"Order: {order.order_id}\n"
        receipt += "Items:\n"
        
        for pizza in order.pizzas:
            receipt += f"  {pizza}\n"
        
        receipt += f"Total: ${order.get_total()}\n"
        receipt += "==========="
        return receipt


# ===== PROBLEM 3: Time Duration with Operator Overloading =====

class Duration:
    def __init__(self, hours=0, minutes=0, seconds=0):
        # Handle overflow from seconds
        total_seconds = hours * 3600 + minutes * 60 + seconds
        self.hours = total_seconds // 3600
        remaining_seconds = total_seconds % 3600
        self.minutes = remaining_seconds // 60
        self.seconds = remaining_seconds % 60

    @property
    def total_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __str__(self):
        parts = []
        if self.hours > 0:
            parts.append(f"{self.hours}h")
        if self.minutes > 0:
            parts.append(f"{self.minutes}m")
        if self.seconds > 0:
            parts.append(f"{self.seconds}s")
        return " ".join(parts) if parts else "0s"

    def __repr__(self):
        return f"Duration({self.hours}, {self.minutes}, {self.seconds})"

    def __add__(self, other):
        total_secs = self.total_seconds + other.total_seconds
        return Duration(0, 0, total_secs)

    def __sub__(self, other):
        total_secs = self.total_seconds - other.total_seconds
        if total_secs < 0:
            return Duration(0, 0, 0)
        return Duration(0, 0, total_secs)

    def __mul__(self, multiplier):
        if not isinstance(multiplier, int):
            raise TypeError("Multiplier must be an integer")
        total_secs = self.total_seconds * multiplier
        return Duration(0, 0, total_secs)

    def __eq__(self, other):
        return self.total_seconds == other.total_seconds

    def __lt__(self, other):
        return self.total_seconds < other.total_seconds

    def __le__(self, other):
        return self.total_seconds <= other.total_seconds


# ===== TEST CODE =====

if __name__ == "__main__":
    print("=== PROBLEM 1: Shape Calculator ===")
    # Create shapes
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 4, 5)

    # Test individual shapes
    print("Individual Shapes:")
    for shape in [circle, rectangle, triangle]:
        print(f"  {shape.describe()}")
        print(f"    Area: {shape.area():.2f}")
        print(f"    Perimeter: {shape.perimeter():.2f}")

    # Test collection (polymorphism)
    collection = ShapeCollection()
    collection.add_shape(circle)
    collection.add_shape(rectangle)
    collection.add_shape(triangle)

    print(f"\nCollection Totals:")
    print(f"  Total Area: {collection.total_area():.2f}")
    print(f"  Total Perimeter: {collection.total_perimeter():.2f}")

    # Test validation
    print("\nTesting validation:")
    try:
        bad_circle = Circle(-5)
    except:
        print("  Correctly rejected negative radius")

    print("\n" + "="*50 + "\n")
    
    print("=== PROBLEM 2: Pizza Order System ===")
    # Test factory methods
    pizza1 = Pizza.create_margherita("large")
    pizza2 = Pizza.create_pepperoni("medium")
    pizza3 = Pizza.create_veggie("small")

    print("Individual Pizzas:")
    for pizza in [pizza1, pizza2, pizza3]:
        print(f"  {pizza}")

    # Test order
    order1 = PizzaOrder()
    order1.add_pizza(pizza1)
    order1.add_pizza(pizza2)
    print(f"\n{order1}")

    # Test order from string
    print("\nOrder from string:")
    order2 = OrderManager.create_order_from_string(
        "large pepperoni, small margherita, medium veggie"
    )
    print(OrderManager.format_receipt(order2))

    print(f"\nTotal orders created: {PizzaOrder.get_total_orders()}")

    print("\n" + "="*50 + "\n")
    
    print("=== PROBLEM 3: Time Duration ===")
    # Create durations
    d1 = Duration(1, 30, 45)
    d2 = Duration(0, 45, 30)
    d3 = Duration(2, 15, 0)

    print("Durations:")
    print(f"  d1 = {d1}")
    print(f"  d2 = {d2}")
    print(f"  d3 = {d3}")

    # Test arithmetic
    print("\nArithmetic:")
    print(f"  d1 + d2 = {d1 + d2}")
    print(f"  d3 - d1 = {d3 - d1}")
    print(f"  d2 * 3 = {d2 * 3}")

    # Test comparisons
    print("\nComparisons:")
    print(f"  d1 == d2? {d1 == d2}")
    print(f"  d1 < d3? {d1 < d3}")
    print(f"  d2 <= d1? {d2 <= d1}")

    # Test sorting
    durations = [d3, d1, d2]
    durations.sort()
    print("\nSorted durations:")
    for d in durations:
        print(f"  {d}")

    # Test overflow
    print("\nOverflow test:")
    d4 = Duration(0, 90, 90)  # Should become 1h 31m 30s
    print(f"  Duration(0, 90, 90) = {d4}")

    # Test repr
    print(f"\nRepr: {repr(d1)}")