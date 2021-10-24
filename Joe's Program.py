import JoesAutomotiveShop as js

def main():

    # Get the customer info
    cust_name = input('Enter your name: ')
    cust_address = input('Enter your address: ')
    cust_phone = input('Enter your phone number: ')

    customer = js.Customer(cust_name, cust_address, cust_phone)

    # Input car info
    car_make = input('Enter car make: ')
    car_model = input('Enter car model: ')
    car_year = input('Enter car year: ')

    car = js.Car(car_make, car_model, car_year)

    # Input charges
    parts_charge = input('Enter the parts charges: ')
    labor_charge = input('Enter the labor charge: ')

    servicequote = js.ServiceQuote(parts_charge, labor_charge)

    # return Service Quote

    print()
    print('Here is your service quote.')
    print('Name:', customer.get_name())
    print('Address:', customer.get_address())
    print('Phone Number:', customer.get_phone())
    print()
    print('Make:', car.get_make())
    print('Model:', car.get_model())
    print('Year:', car.get_year())
    print()
    print('Parts charge: $' + str(servicequote.get_parts_charges()))
    print('Labor charge: $' + str(servicequote.get_labor_charges()))
    print('Sales Tax: $' + str(servicequote.get_sales_tax()))
    print('Total Charges: $' + str(servicequote.get_total_charges()))

main()

