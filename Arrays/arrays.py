# importing "array" for array operations
import array

# initializing array with array values and signed integers
arr = array.array('i', [1, 2, 3])

# printing original array
print("The new created array is : ", end=" ")
for i in range(0, 3):
    print(arr[i], end=" ")
print("\r")

# using append() to insert new value at end
arr.append(4)

# printing appended array
print("The appended array is : ", end="")
for i in range(len(arr)):
    print(arr[i], end=" ")



#Remove Elements of an array    

print("\r")

# importing "array" for array operations
import array

# initializing array with array values
arr= array.array('i',[1, 2, 3, 1, 5])

# printing original array
print ("The new created array is : ",end="")
for i in range (0,5):
	print (arr[i],end=" ")

print("\r")

# using remove() to remove 1st occurrence of 1
arr.remove(1)

# printing array after removing
print ("The array after removing is : ",end="")
for i in range (len(arr)):
	print (arr[i],end=" ")

