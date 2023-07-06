
# <a href="https://intranet.alxswe.com/projects/250"> Python - More Classes and Object </a>
Python programming provides the flexibility of object-oriented programming (OOP) with features like objects, classes, attributes, and methods. Special methods like __init__, __str__, and __repr__ were explored during the project to create and manipulate objects. This exploration significantly improved understanding and proficiency in OOP with Python.
## Project Objectives
- Python Programming: Discovering its Power and Versatility.
- Object-Oriented Programming (OOP): Understanding the Basics and Principles.
- Classes, Objects, and Attributes: Building and Manipulating Data Structures.
- Special Methods and Functionality: Exploring Initialization, Representation, and Property Access.
- Advanced Concepts in OOP: Encapsulation, Abstraction, and Dynamic Attribute Manipulation.

## Resources
 <ul>
<li><a href="[/rltoken/M-MFweENpRdEfRto_Gzlvg](https://python.swaroopch.com/oop.html)" title="Object Oriented Programming" target="_blank">Object Oriented Programming</a> (<em>Read everything until the paragraph “Inheritance” (excluded)</em>)</li>
<li><a href="https://python-course.eu/oop/object-oriented-programming.php" title="Object-Oriented Programming" target="_blank">Object-Oriented Programming</a> (<em>Please be careful: in most of the following paragraphs, the author shows the way you should not use or write a class, in order to help you better understand some concepts and how everything works in Python 3. Make sure you read only the following paragraphs: “General Introduction,” “First-class Everything,” “A Minimal Class in Python,” “Attributes,” “Methods,” “The <code>__init__</code> Method,”  “Data Abstraction, Data Encapsulation, and Information Hiding,” “<code>__str__</code>- and <code>__repr__</code>-Methods,” “Public- Protected- and Private Attributes,” &amp; “Destructor”</em>)</li>
<li><a href="https://python-course.eu/oop/class-instance-attributes.php" title="Class and Instance Attributes" target="_blank">Class and Instance Attributes</a> </li>
<li><a href="https://www.youtube.com/watch?v=rq8cL2XMM5M" title="classmethods and staticmethods" target="_blank">classmethods and staticmethods</a> </li>
<li><a href="https://python-course.eu/oop/properties-vs-getters-and-setters.php" title="Properties vs. Getters and Setters" target="_blank">Properties vs. Getters and Setters</a> (<em>Mainly the last part “Public instead of Private Attributes”</em>)</li>
<li><a href="https://shipit.dev/posts/python-str-vs-repr.html" title="str vs repr" target="_blank">str vs repr</a> </li>
</ul>

## Mandatory tasks
> **0. Simple rectangle:** 
 :point_right: [0-rectangle.py](./0-rectangle.py)
* Write an empty class Rectangle that defines a rectangle
```
#!/usr/bin/python3
""" Rectangle class."""
class Rectangle:
    """Represent a rectangle."""
    pass
```
> **1. Real definition of a rectangle**   
:point_right: [1-rectangle.py](./1-rectangle.py)
 * Write a class `Rectangle` that defines a rectangle by: (based on `0-rectangle.py`) with:
    * Private instance attribute `width`.
      * Property getter `def width(self):` to get `width`.
      * Property setter `def width(self, value):` to set `width`.
    * Private instance attribute `height`:
      * Property getter `def height(self):` to get `height`.
      * Property setter `def height(self, value):` to set `height`.
    * Instantiation with optional `width` and `height`: `def __init(self,   width=0, height=0):`
  *  If either `width` or `height` is not an integer, a  `TypeError` exception is raised with the message `width must be an integer` or `height must be an integer`.
  * If either `width` or `height` is less than 0, a `ValueError` is raised with the message `width must be >= 0` or `height must be >= 0`.

  ```
#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    @property
    def width(self):
            return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    @property
    def height(self):
	    return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
  ```

> **2. Area and Perimeter**
:point_right: [2-rectangle.py](./2-rectangle.py)
  * Python class that defines a rectangle. Builds on [1-rectangle.py](./1-rectangle.py) with:

	* Public instance method `def area(self):` that returns the area of the rectangle.

	* Public instance attribute `def perimeter(self):` that returns the permiter of the rectangle (if either of `width` or `height` equals `0`, the perimeter is `0`).
  ```
 def area(self):
        return (self.__width * self.__height)
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
  ```
> **3. String representation**
:point_right: [3-rectangle.py](./3-rectangle.py)
  * Python class that defines a rectangle. Builds on [2-rectangle.py](./2-rectangle.py) with:
	  * Special method `__str__` to print the rectangle with the `#` character (if either of `width` or `height` equals `0`, the method returns an empty

  ```
 def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
  ```
> **4. Eval is magic**
:point_right: [4-rectangle.py](./4-rectangle.py)
  * Python class that defines a rectangle. Builds on [3-rectangle.py](./3-rectangle.py) with:
	* Special method `__repr__` to return a string representation of the rectangle.
  ```
def __repr__(self):
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
  ```
> **5. Detect instance deletion**
:point_right: [5-rectangle.py](./5-rectangle.py)
  * Python class that defines a rectangle. Builds on [4-rectangle.py](./4-rectangle.py) with:
	* Special method `__del__` that prints the message `Bye rectangle...` when a `Rectangle` is deleted.
  ```
 def __del__(self):
        print("Bye rectangle...")
  ```
> **6. How many instances**
:point_right: [6-rectangle.py](./6-rectangle.py)
  * Python class that defines a rectangle. Builds on [5-rectangle.py](./5-rectangle.py) with:
	* Public class attribute `number_of_instances` that is initialized to `0`, incremented for each new instantiation, and decremened for each instance deletion.
```
class Rectangle:
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
        self.width = width
        self.height = height
```
  ```
 def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
  ```
> **7. Change representation**
:point_right: [7-rectangle.py](./7-rectangle.py)
  * Python class that defines a rectangle. Builds on [6-rectangle.py](./6-rectangle.py) with:
	* Public class attribute `class_symbol` that is initialized to `#` but can be any type - used as the symbol for string representation.
```
class Rectangle:
    number_of_instances = 0
    print_symbol = "#"
```
  ```
 def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
  ```
> **8. Compare rectangles**
:point_right: [8-rectangle.py](./8-rectangle.py)
  * Python class that defines a rectangle. Builds on [7-rectangle.py](./7-rectangle.py) with:
	* Static method `def bigger_or_equal(rect_1, rect_2):` that returns the rectangle with the greater area (returns `rect_1` if both areas are equal).
	* If either of `rect_1` or `rect_2` is not a `Rectangle` instance, a `TypeError` is raised with the message `rect_1 must be an instance of Rectangle` or `rect_2 must be an instance of Rectangle`.
  ```
 @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)
  ```
  > **9. A square is a rectangle**
:point_right: [9-rectangle.py](./9-rectangle.py)
  * Python class that defines a rectangle. Builds on [8-rectangle.py](./8-rectangle.py) with:
	* Class method `def square(cls, size=0):` that returns a new `Rectangle` instance with `width == height == size`.
  ```
@classmethod
    def square(cls, size=0):
        return (cls(size, size))
  ```
  
  ## Advanced tasks
  
  > **10. N queens**
   :point_right: [101-nqueens.py](./101-nqueens.py)

 
* Python program that solves the [N queens puzzle](https://en.wikipedia.org/wiki/Eight_queens_puzzle).
* Determines all possible solutions for placing N non-attacking queens on an NxN chessboard.
* Exactly two arguments must be provided. Otherwise, the program prints `Usage: nqueens N` and exits with the status `1`.
* If the provided `N` is not an integer, the program prints `N must be a number` and exits with the status `1`.
* If the provided `N` is less than `4`, the program prints `N must be at least 4` and exits with the status `1`.
* Solutions are printed one per line in the format `[[r, c], [r, c], [r, c], [r, c]]` where `r` and `c` represent the row and column, respectively, where a queen must be placed.
```
code
``` 

