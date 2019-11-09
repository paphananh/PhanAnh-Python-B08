shopprice = {
    "HP": 600,
    "DELL": 650,
    "MACBOOK": 12000,
    "ASUS": 400,
    "ACER": 350,
    "TOSHIBA": 600,
    "FUJITSU": 900,
    "ALIENWARE": 1000,
}

print (shopprice["ASUS"])

printprice=input("ENTER A BRAND: ")
print(shopprice[printprice])

bill=shopprice["ASUS"]*5
print(bill)

brandbill=input("Choose brand: ")
numbill=int(input("How many?"))
bills=shopprice[brandbill]*numbill
print(bills)
