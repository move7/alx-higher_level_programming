# Python - Hello, World
By the end of this project, we will have a solid understanding of the fundamentals of Python programming and how to interact with the shell.
## Project Objectives
- Execute Python scripts and code using Bash scripts.
- Explore different ways to print strings, integers, floats with precision.
- Print "the Zen of Python" a collection of guiding principles for Python developers, in less than 98 characters.
- Compile Python script into bytecode.
- Write python script from bytecode.

## Resources
<ul>
<li><a href="/rltoken/JsFCs_NBzMAR7-XPAZ9BoA" title="The Python tutorial" target="_blank">The Python tutorial</a> (<em>only the first three chapters below</em>)</li>
<li><a href="/rltoken/kifRlLG2iMX5AZiW8lrCMg" title="Whetting Your Appetite" target="_blank">Whetting Your Appetite</a> </li>
<li><a href="/rltoken/RVpfAuagCo9SdfYeoHd6jg" title="Using the Python Interpreter" target="_blank">Using the Python Interpreter</a> </li>
<li><a href="/rltoken/bVps0ZPWq7qVZ7vc-eJGTw" title="An Informal Introduction to Python" target="_blank">An Informal Introduction to Python</a> (<em>Read up until “3.1.2. Strings” included</em>)</li>
<li><a href="/rltoken/Ju0J8BxkuPX5yKZctyKfsQ" title="How To Use String Formatters in Python 3" target="_blank">How To Use String Formatters in Python 3</a> </li>
<li><a href="/rltoken/szBsJ-Qyig_RrImN7RGlOg" title="Learn to Program" target="_blank">Learn to Program</a> </li>
<li><a href="/rltoken/tgYt-0zVy1T4sDlE9ohxnA" title="Pycodestyle -- Style Guide for Python Code" target="_blank">Pycodestyle – Style Guide for Python Code</a> </li>
</ul>

## Mandatory tasks
* **0. Run Python File**
  * Execute a Python script using the environment variable $PYFILE, which stores the name of the Python file

* **1. Run inline**
  * Execute Python code stored in the environment variable $PYCODE.

* **2. Hello, print**
  * Print the phrase ""Programming is like building a multilingual puzzle" followed by a new line.

* **3. Print integer**
  * Print the integer stored in the variable number, followed by Battery street, followed by a new line.

* **4. Print float**
  * Print the float stored in the variable number with a precision of 2 digits

* **5. Print string**
  * Print 3 times a string stored in the variable str, followed by its first 9 characters..

* **6. Play with strings**
  * Print `Welcome to Holberton School!` using the variables `str1 = "Holberton"` and `str2 = "School"`.

* **7. Copy - Cut - Paste**
  * Print the variables
  * `word_first_3`: Contains the first three letters of the variable `word`.
  * `word_last_2`: Contains the last two letters of the variable `word`.
  * `middle_word`: Contains the value of the variable `word` without the first and last letters.
  

* **8. Create a new sentence**
  * Print `object-oriented
  programming with Python`, followed by a new line without creating new variables..

* **9. Easter Egg**
  * Print "The Zen of Python" by Tim Peters, followed by a new line.

* **10. Linked list cycle** (**Technical interview preparation:**)
  * Write a function in C that checks if a singly linked list has a cycle in it

## Advanced tasks

* **11. Hello, write**
  * Using the write function from the sys module, print "and that piece of art is useful - Dora Korpar, 2015-10-19," followed by a new line, and exit with a status code of 1.
  
* **12. Compile**
  * Write a script that compiles a Python script file stored in the environment variable $PYFILE.
  
* **13. ByteCode -> Python #1**
  * Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:.
  ```
  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
```

