def main():
    while True:
        try:
            integer = int(input('Enter an integer: '))
            break
        except ValueError:
            print('Invaid number')
    is_negative = integer < 0
    if is_negative:
        integer = integer * -1
    reversed_integer = integer
    if integer <= 9:
        pass
    else:
        pass


