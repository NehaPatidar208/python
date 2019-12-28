import ctypes
n=10
print("id of %d is :"%n,id(n))
print(ctypes.cast(id(n),ctypes.py_object).value)
address=int(input("Enter the id "))
print(ctypes.cast(address,ctypes.py_object).value);
