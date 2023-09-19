>>> l=[1,2,3,4,5,6]
>>> print(l)
[1, 2, 3, 4, 5, 6]
>>> #access
>>> l[0]
1
>>> l[2]
3
>>> l[-1]
6
>>> l[-2]
5
>>> l[-3]
4
>>> l[3]
4
>>> l[1:3]
[2, 3]
>>> l[:5]
[1, 2, 3, 4, 5]
>>> l[2:]
[3, 4, 5, 6]
>>> #concatentation
>>> l1=[11,12,13]
>>> l2=l+l1
>>> print(l2)
[1, 2, 3, 4, 5, 6, 11, 12, 13]
>>> l2=l+[14,15,16]
>>> print(l2)
[1, 2, 3, 4, 5, 6, 14, 15, 16]
>>> #insert
>>> print(l)
[1, 2, 3, 4, 5, 6]
>>> l.insert(0,10)
>>> print(l)
[10, 1, 2, 3, 4, 5, 6]
>>> print(l1)
[11, 12, 14, 13]
>>> print(l2)
[1, 2, 3, 4, 5, 6, 14, 15, 16]
>>> l2.insert(5,20)
>>> print(l2)
[1, 2, 3, 4, 5, 20, 6, 14, 15, 16]
>>> len(l)
7
>>> len(l1)
4
>>> len(l2)
10
>>> #extend
>>> print(l)
[10, 1, 2, 3, 4, 5, 6]
>>> print(l1)
[11, 12, 14, 13]
>>> print(l2)
[1, 2, 3, 4, 5, 20, 6, 14, 15, 16]
>>> l.extend([7,8,9])
>>> print(l)
[10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> l1.extend([15,16,17])
>>> print(l1)
[11, 12, 14, 13, 15, 16, 17]
>> len(l)
10
>>> len(l1)
7
>>> l2.extend([21,22])
>>> print(l2)
[1, 2, 3, 4, 5, 20, 6, 14, 15, 16, 21, 22]
>>> len(l2)
12
>>> #append
>>> print(l)
[10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> print(l1)
[11, 12, 14, 13, 15, 16, 17]
>>> print(l2)
[1, 2, 3, 4, 5, 20, 6, 14, 15, 16, 21, 22]
>>> l.append([11,12,13])
>>> print(l)
[10, 1, 2, 3, 4, 5, 6, 7, 8, 9, [11, 12, 13]]
>>> len(l)
11
>>> l1.append([18,19,20])
>>> print(l1)
[11, 12, 14, 13, 15, 16, 17, [18, 19, 20]]
>>> len(l1)
8
>>> #remove
>>> l.remove(10)
>>> print(l)
[1, 2, 3, 4, 5, 6, 7, 8, 9, [11, 12, 13]]
>>> del(l[9])
>>> print(l)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> l.pop()
9
>>> print(l)
[1, 2, 3, 4, 5, 6, 7, 8]
>>> l1.remove(14)
>>> print(l1)
[11, 12, 13, 15, 16, 17, [18, 19, 20]]
>>> del(l[6])
>>> print(l)
[1, 2, 3, 4, 5, 6, 8]
>>> del(l1[6])
>>> print(l1)
[11, 12, 13, 15, 16, 17]
>>> #modify
>>> l[0]=100
>>> l[-1]=200
>>> print(l)
[100, 2, 3, 4, 5, 6, 200]
>>> l[1:3]=[60,70]
>>> print(l)
[100, 60, 70, 4, 5, 6, 200]
>>> l[1:3]=[80,90,110,120]
>>> print(l)
[100, 80, 90, 110, 120, 4, 5, 6, 200]
>>> l[1:5]=[115]
>>> print(l)
[100, 115, 4, 5, 6, 200]
>>> #s0rting
>>> l.sort()
>>> print(l)
[4, 5, 6, 100, 115, 200]
>>> l.sort[reverse=true]
SyntaxError: invalid syntax
>>> l.sort[reverse]
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    l.sort[reverse]
NameError: name 'reverse' is not defined
>>> l.sort(reverse=true)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    l.sort(reverse=true)
NameError: name 'true' is not defined
>>> #reverse
>>> print(l)
[4, 5, 6, 100, 115, 200]
>>> l.reverse()
>>> print(l)
[200, 115, 100, 6, 5, 4]
>>> l.reverse(display)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    l.reverse(display)
NameError: name 'display' is not defined
>>> l.reverse[display]
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    l.reverse[display]
NameError: name 'display' is not defined
>>> #copy
>>> l1=l.copy()
>>> print(l1)
[200, 115, 100, 6, 5, 4]
>>> print(l)
[200, 115, 100, 6, 5, 4]
>>> l2=l
>>> print(l)
[200, 115, 100, 6, 5, 4]
>>> #count
>>> l.count(6)
1
>>> l.count()
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    l.count()
TypeError: count() takes exactly one argument (0 given)
>>> l=[1,1,2,2,2,2,23,4,5]
>>> print(l)
[1, 1, 2, 2, 2, 2, 23, 4, 5]
>>> l.count(2)
4
>>> 
