#!/bin/python3

# Complete the repeatedString function below.
def repeatedString(s, n):
    occurence_of_a_in_s = 0
    for char in s:
        if char == 'a':
            occurence_of_a_in_s += 1

    # Find how many times 's' can be completely repeated then multiple that by the occurence of a character
    # in 's' string
    occurence_of_a_in_s *= int(n / len(s))

    # Now the calculate the occurence of renmaing part that does not completely fit in string
    end_part = s[:n % len(s)]
    for char in end_part:
        if char == 'a':
            occurence_of_a_in_s += 1
    return occurence_of_a_in_s

def main():
    s = 'abcacaccccac'
    n = 100000
    print(repeatedString(s, n))

if __name__ == '__main__':
    main()
