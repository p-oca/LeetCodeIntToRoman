class Solution:
    def intToRoman(self, num: int) -> str:
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

        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]: # Iterate n through array
            while n <= num: # while iterator n is less that input number
                result += romanNumerals[n] # add mapped numeral through to result string
                num -= n # subtract iterator from input number
        return result # return once finished