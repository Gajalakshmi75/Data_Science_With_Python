>>> #tuple
>>> t=(1,2,3)
>>> type(t)
<class 'tuple'>
>>> help(t)
Help on tuple object:

class tuple(object)
 |  tuple(iterable=(), /)
 |  
 |  Built-in immutable sequence.
 |  
 |  If no argument is given, the constructor returns an empty tuple.
 |  If iterable is specified the tuple is initialized from iterable's items.
 |  
 |  If the argument is a tuple, the return value is the same object.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(self, /)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  index(self, value, start=0, stop=2147483647, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

>>> print(t)
(1, 2, 3)
>>> t[0]=10
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    t[0]=10
TypeError: 'tuple' object does not support item assignment
>>> x=list(t)
>>> type(t)
<class 'tuple'>
>>> type(x)
<class 'list'>
>>> x[1]=20
>>> print(x)
[1, 20, 3]
>>> print(t)
(1, 2, 3)
>>> t=tuple(x)
>>> print(t)
(1, 20, 3)
>>> t=(1,1,2,3,2,2,4,2,2)
>>> count(t)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    count(t)
NameError: name 'count' is not defined
>>> t.count(2)
5
>>> t.insert(0,10)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    t.insert(0,10)
AttributeError: 'tuple' object has no attribute 'insert'
>>> t.index(20)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    t.index(20)
ValueError: tuple.index(x): x not in tuple
>>> 
