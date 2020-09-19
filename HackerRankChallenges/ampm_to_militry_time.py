def timeConversion(time):
    meridiem = time[-2:]
    hours = int(time[:2])
    if meridiem == 'PM' and hours != 12:
        return f'{hours + 12}:{time[3:-2]}'
    elif meridiem == 'AM' and hours == 12:
        return f'00:{time[3:-2]}'
    return time[0:-2]

def main():
    time = '12:00:32PM'
    print(timeConversion(time))

if __name__ == '__main__':
    main()
