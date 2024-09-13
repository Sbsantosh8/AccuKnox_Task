
class Rectangle:
    def __init__(self, length: int, width: int):
        if not isinstance(length, int) or not isinstance(width, int):
            raise TypeError("Length and width must be integers.")
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive integers.")
        self.length = length
        self.width = width

    def __iter__(self):
        # Returns an iterator for the Rectangle class
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage:
rectangle = Rectangle(25, 10)

# Iterating over the rectangle instance
for attribute in rectangle:
    print(attribute)


