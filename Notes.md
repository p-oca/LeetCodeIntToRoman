# Notes
## Operators in Python
+-------------------+------------------------------------------+-------------------------------------------------------+
|   Operator        |             Example                        |                     Description                       |
+-------------------+------------------------------------------+-------------------------------------------------------+
|    =              |   x = 5                                  |   Assigns the value on the right to the variable on   |
|                   |                                          |   the left.                                          |
|    +=             |   x += 3                                 |   Adds the value on the right to the variable on the  |
|                   |                                          |   left and assigns the result to the variable.        |
|    -=             |   x -= 3                                 |   Subtracts the value on the right from the variable  |
|                   |                                          |   on the left and assigns the result to the variable. |
|    *=             |   x *= 3                                 |   Multiplies the variable on the left by the value    |
|                   |                                          |   on the right and assigns the result to the variable.|
|    /=             |   x /= 3                                 |   Divides the variable on the left by the value on    |
|                   |                                          |   the right and assigns the result to the variable.   |
|    //=            |   x //= 3                                |   Performs floor division on the variable on the left |
|                   |                                          |   by the value on the right and assigns the result.   |
|    %=             |   x %= 3                                 |   Computes the modulus of the variable on the left    |
|                   |                                          |   with the value on the right and assigns the result. |
|    **=            |   x **= 3                                |   Raises the variable on the left to the power of the |
|                   |                                          |   value on the right and assigns the result.          |
|    &=             |   x &= 3                                 |   Performs a bitwise AND operation on the variable    |
|                   |                                          |   on the left with the value on the right and assigns |
|                   |                                          |   the result.                                        |
|    |=             |   x |= 3                                 |   Performs a bitwise OR operation on the variable on  |
|                   |                                          |   the left with the value on the right and assigns    |
|                   |                                          |   the result.                                        |
|    ^=             |   x ^= 3                                 |   Performs a bitwise XOR operation on the variable on |
|                   |                                          |   the left with the value on the right and assigns    |
|                   |                                          |   the result.                                        |
|    >>=            |   x >>= 3                                |   Performs a right shift operation on the variable on |
|                   |                                          |   the left by the value on the right and assigns the  |
|                   |                                          |   result.                                            |
|    <<=            |   x <<= 3                                |   Performs a left shift operation on the variable on  |
|                   |                                          |   the left by the value on the right and assigns the  |
|                   |                                          |   result.                                            |
+-------------------+------------------------------------------+-------------------------------------------------------+
## Pseudocode
```
FUNCTION intToRoman(num):
    romanNumerals = {
        1: "I",
        5: "V", 4: "IV",
        10: "X", 9: "IX",
        50: "L", 40: "XL",
        100: "C", 90: "XC",
        500: "D", 400: "CD",
        1000: "M", 900: "CM"
    }
    result = ''

    FOR iterator "n" IN [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
        WHILE "n" is less than or equal to the input number "num":
            add resulting numeral to "result" string
            subtract iterator "n" from input number "num"

    RETURN result
```
### Explanation
The key learning from this code was the use of the mapped numerals from their key-values, as well as a deeper understanding of Python operators such as "-=" and "+=".