## Algorithms implemented in python

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

### TODO

- Djikstra
- Trie
- Prims
- Kruskal

## Commonly used snippets

### Print statements

Formatted print
```
print("My name is {} {}".format(first, last))
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

### Mutable string
TODO

### Min/Max heaps in python
In case tuples are given ordering is taken based of first then second element etc.
comparisons are done between comparable types of objects only

Sets don’t keep elements in sorted order or in any defined order

### Substrings
```
>>> a = ‘rahul’
>>> a[1:3] 
‘ah’
>>> a[1:-1]
ahu
```
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







