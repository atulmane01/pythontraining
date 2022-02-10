'''
1.Python Arithmetic Operators:
    Arithmetic operators are used with numeric values to perform common mathematical operations:

Operator	                Name
+	                Addition	x + y
-	                Subtraction	x - y
*	                Multiplication	x * y
/	                Division	x / y
%	                Modulus	x % y
**	                Exponentiation	x ** y
//	                Floor division	x // y


2. Python Assignment Operators:
    Assignment operators are used to assign values to variables:

Operator	                        Example	                    Same As
=	                                x = 5	                x = 5
+=	                                x += 3              	x = x + 3
-=	                                x -= 3              	x = x - 3
*=	                                x *= 3          	    x = x * 3
/=	                                x /= 3	                x = x / 3
%=	                                x %= 3	                x = x % 3
//=         	                    x //= 3	                x = x // 3
**=	                                x **= 3	                x = x ** 3
&=	                                x &= 3	                x = x & 3
|=	                                x |= 3	                x = x | 3
^=	                                x ^= 3	                x = x ^ 3
>>=	                                x >>= 3	                x = x >> 3
<<=	                                x <<= 3	                x = x << 3

3.Python Comparison Operators:
    Comparison operators are used to compare two values:

Operator	    Name	                Example
==	             Equal	                       x == y
!=	            Not equal	                 x != y
>	             Greater than	                   x > y
<	            Less than	                    x < y
>=	             Greater than or equal to   	x >= y
<=	            Less than or equal to   	x <= y

4.Python Logical Operators
    Logical operators are used to combine conditional statements:

Operator	                            Description	Example
and 	                        Returns True if both statements are true	        x < 5 and  x < 10
or	                            Returns True if one of the statements is true   	x < 5 or x < 4
not	                            Reverse the result, returns False if the result is true	not (x < 5 and x < 10)


5.Python Identity Operators
    Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

Operator	                            Description	                                                Example
is 	                        Returns True if both variables are the same object                  	x is y
is not	                    Returns True if both variables are not the same object	                x is not y

6.Python Membership Operators
    Membership operators are used to test if a sequence is presented in an object:

Operator	                Description	                                                                Example
in 	                Returns True if a sequence with the specified value is present in the object	    x in y
not in	            Returns True if a sequence with the specified value is not present in the object	x not in y



7.Python Bitwise Operators:
    Bitwise operators are used to compare (binary) numbers:

Operator	                        Name	                                    Description
&                               	AND             	Sets each bit to 1 if both bits are 1
|	                                OR	                Sets each bit to 1 if one of two bits is 1
 ^	                                XOR	                Sets each bit to 1 if only one of two bits is 1
~ 	                                NOT	                Inverts all the bits
<<	                                Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>	                                Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off


In Python, bitwise operators are used to performing bitwise calculations on integers.
 The integers are first converted into binary and then operations are performed on bit by bit,
hence the name bitwise operators. Then the result is returned in decimal format.



1.Bitwise left shift:
    Shifts the bits of the number to the left and fills 0 on voids right as a result.
    Similar effect as of multiplying the number with some power of two.


2.Bitwise right shift:
    Shifts the bits of the number to the right and fills 0 on voids left( fills 1 in the case of a negative number) as a result.
    Similar effect as of dividing the number with some power of two.


# Python program to show
# shift operators

a = 10
b = -10

# print bitwise right shift operator
print("a >> 1 =", a >> 1)
print("b >> 1 =", b >> 1)

a = 5
b = -10

# print bitwise left shift operator
print("a << 1 =", a << 1)
print("b << 1 =", b << 1)




'''