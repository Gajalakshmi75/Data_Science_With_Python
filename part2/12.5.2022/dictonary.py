>>> #dictonaries
>>> d={}
>>> type(d)
<class 'dict'>
>>> help(d)
Help on dict object:

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |  
 |  Methods defined here:
 |  
 |  __contains__(self, key, /)
 |      True if the dictionary has the specified key, else False.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
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
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
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
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      D.__sizeof__() -> size of D in memory, in bytes
 |  
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |  
 |  copy(...)
 |      D.copy() -> a shallow copy of D
 |  
 |  get(self, key, default=None, /)
 |      Return the value for key if key is in the dictionary, else default.
 |  
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
 |  
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
 |  
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      If key is not found, d is returned if given, otherwise KeyError is raised
 |  
 |  popitem(...)
 |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
 |      2-tuple; but raise KeyError if D is empty.
 |  
 |  setdefault(self, key, default=None, /)
 |      Insert key with a value of default if key is not in the dictionary.
 |      
 |      Return the value for key if key is in the dictionary, else default.
 |  
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]
 |  
 |  values(...)
 |      D.values() -> an object providing a view on D's values
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  fromkeys(iterable, value=None, /) from builtins.type
 |      Create a new dictionary with keys from iterable and values set to value.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> d["name"]="gowri"
>>> print(d)
{'name': 'gowri'}
>>> d["rn0"]=21
>>> print(d)
{'name': 'gowri', 'rn0': 21}
>>> len(d)
2
>>> d["id"]="s180311"
>>> print(d)
{'name': 'gowri', 'rn0': 21, 'id': 's180311'}
>>> del(d["name"])
>>> print(d)
{'rn0': 21, 'id': 's180311'}
>>> d['rn0']=45
>>> print(d)
{'rn0': 45, 'id': 's180311'}
>>> d.popitem()
('id', 's180311')
>>> print(d)
{'rn0': 45}
>>> d.pop("rn0")
45
>>> print(d)
{}
>>> d=dict([('one',1),('two',2)])
>>> print(d)
{'one': 1, 'two': 2}
>>> d.keys()
dict_keys(['one', 'two'])
>>> d.values()
dict_values([1, 2])
>>> d.items()
dict_items([('one', 1), ('two', 2)])
>>> d2=([(1,2),(2,3),(2,4)])
>>> d.copy(d2)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    d.copy(d2)
TypeError: copy() takes no arguments (1 given)
>>> d.copy()
{'one': 1, 'two': 2}
>>> d2.copy
<built-in method copy of list object at 0x03CE8D78>
>>> print(d2)
[(1, 2), (2, 3), (2, 4)]
>>> d2=dict[(1, 2), (2, 3), (2, 4)]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    d2=dict[(1, 2), (2, 3), (2, 4)]
TypeError: 'type' object is not subscriptable
>>> 
>>> d2=dict([(1,2),(2,3),(2,4)])
>>> print(d2)
{1: 2, 2: 4}
>>> d.copy(d2)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    d.copy(d2)
TypeError: copy() takes no arguments (1 given)
>>> d2.clear()
>>> print(d2)
{}
>>> d.get()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    d.get()
TypeError: get expected at least 1 arguments, got 0
>>> d.get(name)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    d.get(name)
NameError: name 'name' is not defined
>>> d.get('name')
>>> print(d)
{'one': 1, 'two': 2}
>>> d.get('one)
      
SyntaxError: EOL while scanning string literal
>>> d.get('one')
1
>>> 
