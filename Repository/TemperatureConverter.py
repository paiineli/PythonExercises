# Temperature converter exercise, C to F, F to C, C to K, K to C, F to K, K to F

print(30 * "-")
def c_to_f(celsius):
    return celsius * 9/5 + 32
def f_to_c(farenheit):
    return(farenheit - 32) * 5/9
def c_to_k(celsius):
    return celsius + 273.15
def k_to_c(kelvin):
    return kelvin - 273.15
def f_to_k(fahrenheit):
    return(fahrenheit + 459.67) * 5/9
def k_to_f(kelvin):
    return kelvin * 9/5 - 459.67

def main():
    while True:
        print("Choose the conversion:")
        print("1 - Celsius to Farenheit")
        print("2 - Farenheit to Celsius")
        print("3 - Celsius to Kelvin")
        print("4 - Kevin to Celsius")
        print("5 - Farenheit to Kelvin")
        print("6 - Kevin to Farenheit")
        print("0 - Exit program")

        choice = input("Enter your choice (0/1/2/3/4/5/6): ")

        if choice == '0':
            print("Exiting program. Goodbye!")
            break

        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid choice. Please enter a valid option.")
            continue

        if choice == '1':
            temp_celsius = float(input("Enter your temperature in Celsius: "))
            print(temp_celsius,"°C =", c_to_f(temp_celsius),"°F")
        elif choice == '2':
            temp_farenheit = float(input("Enter your temperature in Fahrenheit: "))
            print(temp_farenheit,"°F =", f_to_c(temp_farenheit),"°C")
        elif choice == '3':
            temp_celsius = float(input("Enter your temperature in Celsius: "))
            print(temp_celsius,"°C =", c_to_k(temp_celsius),"K")
        elif choice == '4':
            temp_kelvin = float(input("Enter your temperature in Kelvin: "))
            print(temp_kelvin,"K =", k_to_c(temp_kelvin),"°C")
        elif choice == '5':
            temp_farenheit = float(input("Enter your temperature in Fahrenheit: "))
            print(temp_farenheit,"°F =", f_to_k(temp_farenheit),"K")
        elif choice == '6':
            temp_kelvin = float(input("Enter your temperature in Kelvin: "))
            print(temp_kelvin,"K =", k_to_f(temp_kelvin),"°F")
        
        answer = input("Do you want to select another option? (y/n): ").lower()
        if answer != 'y':
            print("Exiting program. See You!")
            break

if __name__ == "__main__":
    main()

print(30 * "-")
