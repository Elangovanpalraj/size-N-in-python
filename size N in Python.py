# Break a list into chunks of size N in Python
# -------------------------------------------\n
# Using yield
# Using for loop in Python
# Using List comprehension
# Using Numpy
# Using itertool
# ----------------------------------------------------------\n
# Method 1: Break a list into chunks of size N in Python using yield keyword
# ============================================================\n
my_list = ['geeks', 'for', 'geeks', 'like', 
           'geeky','nerdy', 'geek', 'love', 
               'questions','words', 'life'] 
  
# Yield successive n-sized 
# chunks from l. 
def divide_chunks(l, n): 
      
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 
  
# How many elements each 
# list should have 
n = 5
  
x = list(divide_chunks(my_list, n)) 
print (x)
print(' ')
# Method 2: Break a list into chunks of size N in Python using a loop
# ============================================================\n
my_list = [1, 2, 3, 4, 5, 
           6, 7, 8, 9] 
start = 0
end = len(my_list) 
step = 3
for i in range(start, end, step): 
    x = i 
    print(my_list[x:x+step])

print(' ')
# using List comprehension
# =========================\n
my_list = [1, 2, 3, 4, 5, 
              6, 7, 8, 9] 
  
# How many elements each 
# list should have 
n = 4 
  
# using list comprehension 
final = [my_list[i * n:(i + 1) * n] for i in range((len(my_list) + n - 1) // n )]  
print (final)
print(' ')
# Alternate Implementation :
# =======================\n
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]  
   
# How many elements each  
# list should have  
n = 4
   
# using list comprehension  
x = [l[i:i + n] for i in range(0, len(l), n)]  
print(x)
print(' ')
#  using a Numpy.array_split
# =========================\n
import numpy as np 
  
arr = range(30) 
np.array_split(arr, 6)
print(' ')

# use itertool
# =============\n
from itertools import islice 
  
  
def chunk(arr_range, arr_size): 
    arr_range = iter(arr_range) 
    return iter(lambda: tuple(islice(arr_range, arr_size)), ()) 
  
  
list(chunk(range(30), 5))
print(' ')
# Method 6: Collections
# ====================\n
from collections import deque 
  
def split_list(input_list, chunk_size): 
  # Create a deque object from the input list 
  deque_obj = deque(input_list) 
  # While the deque object is not empty 
  while deque_obj: 
      # Pop chunk_size elements from the left side of the deque object 
      # and append them to the chunk list 
      chunk = [] 
      for _ in range(chunk_size): 
        if deque_obj: 
          chunk.append(deque_obj.popleft()) 
          
      # Yield the chunk 
      yield chunk 
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
chunk_size = 3
chunks = list(split_list(input_list, chunk_size)) 
print(chunks) # [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
print(' ')
# Method 7: Partial assignment
# ============================\n
my_list = list(range(10)) 
chunk_size = 3
while my_list: 
    chunk, my_list = my_list[:chunk_size], my_list[chunk_size:] 
    print(chunk)
print(' ')

# ----------------------------------------------------------\n



















































































































