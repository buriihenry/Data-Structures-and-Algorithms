    An array is a data structure that stores a collection of items, usually of the same data type, in a contiguous block of memory. Arrays allow you to organize multiple values under a single name and access them using an index or position.
Key Characteristics of Arrays:
1.	Fixed Size: Arrays are typically of a fixed size, meaning the number of elements in an array is determined when it is created.
2.	Same Data Type: All elements in an array must be of the same data type (e.g., all integers, all floats, etc.).
3.	Indexing: Each element in an array is associated with an index. The first element has an index of 0, the second element has an index of 1, and so on.
4.	Contiguous Memory: Arrays store elements in contiguous memory locations, which makes them efficient for accessing elements by index.
Array in Python:
In Python, arrays can be created using the array module (for arrays with type constraints) or simply using lists (which are more flexible but don't enforce a fixed type).
Example of an array using the array module:
python
Copy code
import array

# Creating an array of integers
arr = array.array('i', [1, 2, 3, 4, 5])

# Accessing elements in an array
print(arr[0])  # Output: 1
print(arr[2])  # Output: 3
Example of a list (Python's built-in array-like structure):
python
Copy code
# Creating a list (which behaves like an array)
lst = [10, 20, 30, 40]

# Accessing elements in the list
print(lst[1])  # Output: 20
Advantages of Arrays:
•	Efficient Indexing: Arrays allow fast access to elements using their index.
•	Memory Efficient: Arrays are more memory efficient than other collections like linked lists.
Disadvantages:
•	Fixed Size: The size of an array is fixed, meaning once created, you cannot change its size.
•	Homogeneous: Arrays must store elements of the same data type, whereas other data structures like Python lists allow mixed types.
When to Use Arrays:
Arrays are useful when you need to:
•	Store a collection of data where you need efficient access by index.
•	Work with a fixed number of elements.
•	Perform mathematical computations that benefit from a contiguous memory layout (e.g., in scientific computing).
