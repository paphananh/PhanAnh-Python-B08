shop = {
"HP" : 20,
"DELL" : 50,
"MACBOOK" : 12,
"ASUS" : 30,
"ACER" : 350,
}

print (shop["MACBOOK"])

numbrand=input("brand?")
print (shop[numbrand])

shop["TOSHIBA"]=10
print (shop)

addmoreb = input("Newbrand?")
addmoren = int(input("How many?"))
shop[addmoreb]=addmoren
print(shop)

shop["DELL"]=60
shop["MACBOOK"]=2
print(shop)

print (shop["MACBOOK"])

s = 0
for v in shop.values():
    s = s + v
    print(v)
print ("Sum", s)

shop["FUJITSU"]=15
shop["ALIENWARE"]=5


######################################################PRICE


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


#######################################################BILLs


bill=shopprice["ASUS"]*5
shop["ASUS"]=shop["ASUS"]-5
print(bill)

brandbill=input("Choose brand: ")
numbill=int(input("How many?"))
shop[brandbill]=shop[brandbill]-numbill
bills=shopprice[brandbill]*numbill
print(bills)


# SUMALL
gia = 0
sum = 0
for v in shop.key() :
    gia = shop[v] * shopprice[v]
    sum += gia
    print (gia)
print (sum)


#XUAT KHO
