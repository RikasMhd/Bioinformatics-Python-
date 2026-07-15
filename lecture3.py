 ls=[8,5,0,4,2,1,7]
>>> ls.sort()
>>> ls
[0, 1, 2, 4, 5, 7, 8]
>>>
>>> ls.sort(reverse=True)
>>> ls
[8, 7, 5, 4, 2, 1, 0]


>>> ls1=[8,8,1,5,0,2,4,2,1,7]
>>> ls1.count(2)
2

>>> ls1=[8,8,1,5,0,2,4,2,1,7]
>>> ls1.count(2)
2
>>>
>>> ls1.index(5)
3
>>>
>>> ls1.index(8)
0
>>>

t=("John",24,"Jaffna")
>>> name,age,city=t[0],t[1],t[2]
>>> name,age,city
('John', 24, 'Jaffna')
>>>
>>> name
'John'
>>> city
'Jaffna'
>>> age
24
>>>

>>> hash("john")
-3134102245315481563
>>>
>>> hash("John")
-6675318360349301779
>>>
>>> hash(10)
10
>>>
>>> hash(12.356)
820880111280074764
>>>
>>> hash(123456)
123456
>>>

>>> hash((1,2,3))   #Bcz, Tuple is immutable(Can't change).list is mutable,int , string are immutable
529344067295497451

>>> hash([1,2,3,4])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>>

>>> {('A','B'):'Name'}  #Immutable and immutable
{('A', 'B'): 'Name'}
>>>


>>> s1={"ATG","ACG","AGG"}
>>> s2={"ATG","ACC","AGG"}
>>> s1+s2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>>
>>> s1 - s2
{'ACG'}
>>> s2 - s1
{'ACC'}

>>> s1.union(s2)
{'AGG', 'ACG', 'ATG', 'ACC'}
>>>
>>> s1.intersection(s2)
{'AGG', 'ATG'}
>>>
>>> s1 & s2
{'AGG', 'ATG'}
>>>
>>> s1 | s2
{'AGG', 'ACG', 'ATG', 'ACC'}
>>>
>>> list(range(0,10,2))
[0, 2, 4, 6, 8]
>>>
>>> evens=[x for x in range(0,10,2) if x%2==0]
>>>
>>> evens
[0, 2, 4, 6, 8]
>>>
>>> r=range(0,10,2)
>>> r[0]
0
>>>
>>> r[1]
2
>>>

