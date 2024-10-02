# Array
    An array is a data structure that stores a collection of items, usually of the same data type, in a contiguous block of memory. Arrays allow you to organize multiple values under a single name and access them using an index or position.
     
## Key Characteristics of Arrays:
1.	Fixed Size: Arrays are typically of a fixed size, meaning the number of elements in an array is determined when it is created.
2.	Same Data Type: All elements in an array must be of the same data type (e.g., all integers, all floats, etc.).
3.	Indexing: Each element in an array is associated with an index. The first element has an index of 0, the second element has an index of 1, and so on.
4.	Contiguous Memory: Arrays store elements in contiguous memory locations, which makes them efficient for accessing elements by index.


# Creating an array of integers
arr = array.array('i', [1, 2, 3, 4, 5])


# Advantages of Arrays:
1. Efficient Indexing: Arrays allow fast access to elements using their index.
2. Memory Efficient: Arrays are more memory efficient than other collections like linked lists.

# Disadvantages:
1. Fixed Size: The size of an array is fixed, meaning once created, you cannot change its size.
2. Homogeneous: Arrays must store elements of the same data type, whereas other data structures like Python lists allow mixed types.

# When to Use Arrays:
Arrays are useful when you need to:
1. Store a collection of data where you need efficient access by index.
2. Work with a fixed number of elements.
3. Perform mathematical computations that benefit from a contiguous memory layout (e.g., in scientific computing).
