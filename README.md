### Algorithms implemented in python

- Merge sort (0(nlogn) sorting)
- Min heap (Native implementation)
- HeapSort (using python's heapq)
- Breadth First Search
- Depth First Search (with cycle detection)
- String pattern matching - rabin karp
- Union find
- min_heap - wrapper around heapq for min heaps
- max_heap - wrapper around heapq for min heaps (using negation of initial values)
- Trie
- Djikstra
### TODO
- Prims
- Kruskal

## Commonly used snippets

### Print statements

Formatted print
```
print("My name is {} {}".format(first, last))
```
### Multi - line code
```
if a or b and c \
or d:
  print("blah")
```
### Sort based on a key
```
def sortKey(v):
  return v[1]
ls = [(2,7), (5,6)]
ls.sort(key=sortKey) # [(5, 6), (2, 7)]

```

### ASCII to chr 

`ord('a') # 97`

## Chr to ASCII

`chr(97) # a` 


### Not operators
`not`, `!=` are valid operators in python. `!` is invalid.

Also, not None = True and not 0 = True

### List comprehensions

Multiply each element in a list by a number

```
numbers = [1, 2, 3, 4, 5]
numbers5 = [i* 5 for i in numbers]
```
### filter and map
```
strings = ["rahul", "gurnani"]
string_lengths = list(map(len, strings))
```
```
numbers = [1, 2, 3, -1, -3]
positive = list(filter(lambda x: x>0, numbers))
```
### Enumerate and items

enumerate(alist) to get i, v

dictionarys.items() to get k, v

### String search

```
s.find(pattern, start)
```
find method uses Boyer-Moore algorithm.

### Mutable string
TODO

### Min/Max heaps in python
In case tuples are given ordering is taken based of first then second element etc.
comparisons are done between comparable types of objects only

Sets don’t keep elements in sorted order or in any defined order

### Substring of a string
```
>>> a = ‘rahul’
>>> a[1:3] 
```
### Writing multi-threaded programs in python
TODO
‘ah’
>>> a[1:-1]
ahu
```
Time Complexity: O(n), a new copy is created when a substring is created

## Reversing a string
Using the extended slice syntax: `s[::-1]` reverses the string

### Iterating backwards
```
for i in reversed(ls):
```

### Infinity
```
float("inf")
```

### Stack
```
stack = list()
stack.append(10)
n = stack.pop()
```

### Queue
Use python queue module
```
import queue
q = queue.Queue()
# insert
q.put(1)
# remove first element
e = q.get()
# peek first element
e = q.queue[0]
# peek last element
q.queue[-1]
# NOTE: q.get() takes infinite time if the queue is empty
len(q.queue) == 0 to check if the queue is empty
```

### OrderedDict, dict and SortedSets?

OrderedDict is a special type of dictionary which maintains keeps the keys in the order they were inserted into the dictionary. 
```
from collections import OrderedDict 
d = OrderedDict()
d['a'] = 'x'
```
Python doesn't have an implementation of sorted set.
### Graph
defaultdict is often handy,

```
from collections import defaultdict
edges = [(1, 2), (2, 3)]
graph = defaultdict(list)
for edge in edges:
  graph[edge[0]].append(edge[1])
  graph[edge[1]].append(edge[0])
```

NOTE: defaultdict(int) will initialize dictionary with default value of any key = 0

### Dictionary

key deletion

`del mapping['key']`

### Counter class
Useful if we want count of occurrences of numbers in a list
```
>>> from collections import Counter
>>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
>>> counter = Counter(myList)
>>> counter
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
>>> counter.items()
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
>>> counter.keys()
[1, 2, 3, 4, 5]
>>> counter.values()
[3, 4, 4, 2, 1]
```

### Copy objects
Suppose you have a 2D array. You want to make copy of this array in order to mutate the array. To make such a copy, you can use deep copy

```
from copy import copy, deepcopy
x = [[1, 2], [3, 4]]
y = deepcopy(x)
```

### Binary Search
```
from bisect import bisect_left, bisect_right
a = [1,2,3]
bisect_left(a, 2) # gives 1
```

### String in set in python
```
strings = set()
strings.add('rahul')
strings.add('something')
'rahul' in strings # O(1) operation
```

### List vs Tuples
Tuples are hashable, lists are not. So, we may need to convert list to tuples.

```
ls = [1,2,3]
t = tuple(ls)
```

### zip and unzip

Useful if we have 2 lists which we want to combine and do some operations
```
listpairs = list(zip(list1, list2))
list1, list2 = zip(*listpairs)
```
