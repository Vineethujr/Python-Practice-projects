# Temperature Converter: Convert Celsius ↔ Fahrenhit using functions
def c_to_f(c):
    f=(c * 9/5) + 32
    return f

def f_to_c(f):
    c=(f - 32) * 5/9
    return c

choice = input("Enter 'C' to convert Celsius to Fahrenhit or 'F' to conert Fahrenhit to Celsius: ")

if choice.upper() == 'C':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenhit = c_to_f(celsius)
    print(f"{celsius}°C is coverted to {fahrenhit}°F")

elif choice.upper() == 'F':
    fahrenhit = float(input("Enter temperature in Fahrenhit: "))
    celsius = f_to_c(fahrenhit)
    print(f"{fahrenhit}°F is converted to {celsius}°C")
    
else:
    print("Invalid choice")