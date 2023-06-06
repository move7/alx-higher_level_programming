# 0x00. Python - Hello, World
By the end of this project, we will have a solid understanding of the fundamentals of Python programming and how to interact with the shell.
## Project Objectives
- Execute Python scripts and code using Bash scripts.
- Explore different ways to print strings, integers, floats with precision.
- Print "the Zen of Python" a collection of guiding principles for Python developers, in less than 98 characters.
- Compile Python script into bytecode.
- Write python script from bytecode.

## Resources
<ul>
<li><a href="https://docs.python.org/3/tutorial/index.html" title="The Python tutorial" target="_blank">The Python tutorial</a> (<em>only the first three chapters below</em>)</li>
<li><a href="https://docs.python.org/3/tutorial/appetite.html" title="Whetting Your Appetite" target="_blank">Whetting Your Appetite</a> </li>
<li><a href="https://docs.python.org/3/tutorial/interpreter.html" title="Using the Python Interpreter" target="_blank">Using the Python Interpreter</a> </li>
<li><a href="https://docs.python.org/3/tutorial/introduction.html" title="An Informal Introduction to Python" target="_blank">An Informal Introduction to Python</a> (<em>Read up until “3.1.2. Strings” included</em>)</li>
<li><a href="https://realpython.com/python-f-strings/" title="How To Use String Formatters in Python 3" target="_blank">How To Use String Formatters in Python 3</a> </li>
<li><a href="https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt" title="Learn to Program" target="_blank">Learn to Program</a> </li>
<li><a href="https://pypi.org/project/pycodestyle/" title="Pycodestyle -- Style Guide for Python Code" target="_blank">Pycodestyle – Style Guide for Python Code</a> </li>
</ul>

## Mandatory tasks
> **0. Run Python File:**
* Execute a Python script using the environment variable $PYFILE, which stores the name of the Python file
```
#!/bin/bash
python3 $PYFILE
```
> **1. Run inline**
  * Execute Python code stored in the environment variable $PYCODE.
  ```
  #!/bin/bash
python3 <<< $PYCODE
  ```

> **2. Hello, print**
  * Print the phrase ""Programming is like building a multilingual puzzle" followed by a new line.
```
#!/usr/bin/python3
print("\"Programming is like building a multilingual puzzle")
  ```
> **3. Print integer**
  * Print the integer stored in the variable number, followed by Battery street, followed by a new line.
```
#!/usr/bin/python3
number = 98
print(f"{number:d} Battery street")
  ```
  
> **4. Print float**
  * Print the float stored in the variable number with a precision of 2 digits
```
#!/usr/bin/python3
number = 3.14159
print(f"Float: {number:.2f}")
  ```
  
> **5. Print string**
  * Print 3 times a string stored in the variable str, followed by its first 9 characters..
```
#!/usr/bin/python3
str = "Holberton School"
print(3*str)
print(str[:9])
  ```
  
> **6. Play with strings**
  * Print `Welcome to Holberton School!` using the variables `str1 = "Holberton"` and `str2 = "School"`.
```
#!/usr/bin/python3
str1 = "Holberton"
str2 = "School"
str1 += " "+str2
print(f"Welcome to {str1}!")
  ```
  
> **7. Copy - Cut - Paste**
  * Print the variables
  * `word_first_3`: Contains the first three letters of the variable `word`.
  * `word_last_2`: Contains the last two letters of the variable `word`.
  * `middle_word`: Contains the value of the variable `word` without the first and last letters.
  ```
#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[0:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
  ```

> **8. Create a new sentence**
  * Print `object-oriented
  programming with Python`, followed by a new line without creating new variables..
```
#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[39:66] + str[106:112] + str[:6]
print(str)
  ```
  
> **9. Easter Egg**
  * Print "The Zen of Python" by Tim Peters, followed by a new line.
```
#!/usr/bin/python3
import this
  ```
  
> **10. Linked list cycle** (**Technical interview preparation:**)
  * Write a function in C that checks if a singly linked list has a cycle in it
```
#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;
	if (!list)
		return (0);

	slow = list;
	fast = list->next;

	while (fast && fast->next)
	{
		if (fast == slow)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
  ```
  
## Advanced tasks

> **11. Hello, write**
  * Using the write function from the sys module, print "and that piece of art is useful - Dora Korpar, 2015-10-19," followed by a new line, and exit with a status code of 
  ```
#!/usr/bin/python3
import sys
message = "and that piece of art is useful - Dora Korpar, 2015-10-19\n"
sys.stderr.write(message)
sys.exit(1)
  ```
  
> **12. Compile**
  * Write a script that compiles a Python script file stored in the environment variable $PYFILE.
  ```
#!/bin/bash
python3 -m compileall -b $PYFILE
echo "Compiling $PYFILE ..."
  ```
> **13. ByteCode -> Python #1**
  * Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:.
  * Tip: <a href="https://docs.python.org/3.4/library/dis.html" title="The Python tutorial" target="_blank">Python bytecode</a>
  ```
  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
```
```
def magic_calculation(a, b):
    result = 98
    result += a ** b
    return result
  ```
