C:\Users\dcsuser>mkdir csc209s3      //Make Directionary

C:\Users\dcsuser>cd ./csc209s3

C:\Users\dcsuser\csc209s3>python --version
Python 3.12.5

C:\Users\dcsuser\csc209s3>python -m venv my_env

C:\Users\dcsuser\csc209s3>my_env\Scripts\activate

(my_env) C:\Users\dcsuser\csc209s3>python
Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("hello")
hello
>>> 5+3
8
>>> 10/3
3.3333333333333335
>>> 10//3
3
>>> sqrt(2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sqrt' is not defined]

>>> pow(2,3)
8
>>> sqrt(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sqrt' is not defined

>>> pow(4,0.5)
2.0
>>> 4**0.5
2.0
>>> (2+5)*2/3%2+10
10.666666666666668
>>> (2+5)*2/2%2+10
11.0
>>> (2+5)**2/2%2*5+10
12.5
>>>
>>> 0.1+1.5
1.6
>>>
>>> 0.1+0.2
0.30000000000000004
>>> format(0.1+.2,".2f")
'0.30'
>>> format(0.1,".20f")
'0.10000000000000000555'
>>> 2**0.5
1.4142135623730951
>>> import math
>>> math.sqrt(2)
1.4142135623730951
>>> math.factorial(5)
120
>>> math.max(1,2,3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'max'
>>> max(1,2,3)
3
>>> min(1,2,3)
1
>>> math.gcd(48,18)
6
>>> math.pi
3.141592653589793
>>> math.e
2.718281828459045
>>> math.inf
inf
>>> math.sin(math.pi/2)
1.0
>>> math.cos(math.pi/4)
0.7071067811865476
>>> math.cos(math.pi)
-1.0
>>> math.radians(180)
3.141592653589793
>>> math.degrees(math.pi/4)
45.0

>>> 28%4==0
True
>>> 37%2==1
True
>>>
>>> if(28%4==0):
...     print("Divisible")
... else:
...     print("Not Divisible")
...
Divisible

>>> if(37%2==0):
...     print("Even Number")
... else:
...     print("Odd Number")
...
Odd Number
>>> 999%10
9
>>> a=6
>>> import math
>>> math.sqrt(6)
2.449489742783178
>>> math.pow(6,2)
36.0
>>> 11*4
44

>>>
>>> a=6
>>> area=a**2
>>> print(f"area is {area}")
area is 36


>>> a=11
>>> perimeter=a*4
>>> print(f"perimeter is {perimeter}")
perimeter is 44


>>> a=8
>>> area=a**2
>>> perimeter=perimeter=a*4
>>> print(f"area is {area} \nperimeter is {perimeter}")
area is 64
perimeter is 32

>>> a=3
>>> b=5
>>> c=6
>>> area=0.5*b*a
>>> print(f"area is {area}")
area is 7.5

>>> base=12
>>> height=9
>>> area=0.5*base*height
>>> print(f"area is {area}")
area is 54.0

>>>
>>> radius=7
>>> area=math.pi*(radius**2)
>>> print(f"area is {area}")
area is 153.93804002589985


>>> radius=3
>>> area=math.pi*(radius**2)
>>> circum=2*math.pi*radius
>>> print(f"area is {area} \nCircumference is {circum}")
area is 28.274333882308138
Circumference is 18.84955592153876


>>> radius=7
>>> area=math.pi*(radius**2)
>>> print(f"area is {area:.2f}")
area is 153.94
>>>
>>>

>>> math.log(100,10)
2.0
>>> math.log(16,4)
2.0
>>> math.log10(100)
2.0
>>> math.log2(100)
6.643856189774724
>>> math.log2(16)
4.0
>>>
>>>
>>> z=3i+4j
  File "<stdin>", line 1
    z=3i+4j
      ^
SyntaxError: invalid decimal literal
>>>
>>>
>>> z=3+4j
>>> y=1-2j
>>> z+y
(4+2j)
>>>

>>> z.real
3.0
>>> abs(-52)
52
>>> abs(z)
5.0
>>> z.imag
4.0
>>> cmath.sqrt(-1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'cmath' is not defined. Did you mean: 'math'? Or did you forget to import 'cmath'?
>>>
>>> import cmath
>>> cmath.sqrt(-1)
1j
>>>
>>> abs(z)
5.0

>>> math.exp(1)    //exponent
2.718281828459045
>>> type(1j)
<class 'complex'>
>>>
>>>
>>>
>>>
>>> 1j*cmath.pi
3.141592653589793j
>>> cmath.exp(1j*cmath.pi)
(-1+1.2246467991473532e-16j)
>>>
>>>

>>> Decimal('0.1')+Decimal('0.2')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Decimal' is not defined
>>>
>>>
>>>
>>> import decimal
>>> Decimal('0.1')+Decimal('0.2')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Decimal' is not defined. Did you mean: 'decimal'?
>>> ddecimal('0.1')+decimal('0.2')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ddecimal' is not defined. Did you mean: 'decimal'?
>>> decimal('0.1')+decimal('0.2')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'module' object is not callable
>>>
>>>
>>>
>>> from decimal import Decimal
>>> Decimal('0.1')+Decimal('0.2')
Decimal('0.3')
>>>
>>>
>>> Decimal(1)/Decimal(7)
Decimal('0.1428571428571428571428571429')

>>> from fractions import Fraction
>>> f0=1/3
>>> f0
0.3333333333333333
>>>
>>> f1=Fraction(1,3)
>>> f2=Fraction(1,6)
>>> f1+f2
Fraction(1, 2)
>>>
>>> fraction
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'fraction' is not defined. Did you mean: 'Fraction'?
>>> fraction('0.125')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'fraction' is not defined. Did you mean: 'Fraction'?
>>>
>>>
>>> Fraction('0.125')
Fraction(1, 8)
>>>
>>>

