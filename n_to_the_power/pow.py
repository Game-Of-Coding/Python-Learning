from datetime import datetime as dt

def custom_pow(number, exponent):
    power = 1
    while exponent > 0:
        print(f"Exponent: {exponent}")
        power *= number
        exponent -= 1
    return power

def main():
    # Get user input
    number = int(input("Enter a number: "))
    exponent = int(input("Enter an exponent: "))

    # Calculate number ^ exponent
    power = custom_pow(number, exponent)

    # Print power
    print(f"{number} raised to {exponent}: {power}")

# Start program
print("------------")
begin_time = dt.now()
main()
end_time = dt.now()

# Print time taken
time_taken = end_time - begin_time
print(f"\nTime: {time_taken}")
print("------------")
