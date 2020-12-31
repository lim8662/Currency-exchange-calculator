import os
from babel.numbers import format_currency
from country import extract_country_list
from currency import extract_convert_amount


os.system("clear")

print("Welcome to CurrencyConvert PRO 2000\n")

country_list = extract_country_list()

for i, country in enumerate(country_list):
    print(f"# {i} {str(country[0]).lower().capitalize()}")

print("\nWhere are you from? Choose a country by number.")
from_code = ""
to_code = ""

while True:
    try:
        idx = int(input("\n#: "))
        if 0 <= idx and idx < len(country_list):     
            print(f"{str(country_list[idx][0]).lower().capitalize()}")
            from_code = country_list[idx][2]
            break;
        else:
            print("Choose a number from the list.")
    except:
        print("That wasn't a number.")

print("\nNow choose another country.")

while True:
    try:
        idx = int(input("\n#: "))
        if 0 <= idx and idx < len(country_list):     
            print(f"{str(country_list[idx][0]).lower().capitalize()}")
            to_code = country_list[idx][2]
            break;
        else:
            print("Choose a number from the list.")
    except:
        print("That wasn't a number.")

while True:
    try:
        amount = float(input(f"\nHow many {from_code} do you want to convert to {to_code}?\n"))
        convert = extract_convert_amount(from_code, to_code, amount)
        print(f"{from_code}{format(amount, ',')} is", format_currency(convert, to_code))       
        break;
        
    except:
        print("That wasn't a number.")


"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""

