print ("#######################################################")
print ("SELECT INPUT CURRENCY")
print (" * EUR")
print (" * USD")
print (" * MDL")
print ("#######################################################")
currency_in = input ("choose: ")
money_in    = float (input ("money: "))


print ("#######################################################")
print ("SELECT OUTPUT CURRENCY")

if currency_in != "EUR": 
    print (" * EUR")

if currency_in != "USD":
    print (" * USD")

if currency_in != "MDL":    
    print (" * MDL")

print ("#######################################################")
currency_out = input ("choose: ")
eur_2_usd    =  1.10
eur_2_mdl    = 20.00
usd_2_mdl    = 15.00


if currency_in == "EUR" and currency_out == "USD":
    money_out   = round (money_in * eur_2_usd)

if currency_in == "USD" and currency_out == "EUR":
    money_out   = round (money_in / eur_2_usd)    



if currency_in == "EUR" and currency_out == "MDL":
    money_out   = round (money_in * eur_2_mdl)    

if currency_in == "MDL" and currency_out == "EUR":
    money_out   = round (money_in / eur_2_mdl)     



if currency_in == "USD" and currency_out == "MDL":
    money_out   = round (money_in * usd_2_mdl)    

if currency_in == "MDL" and currency_out == "USD":
    money_out   = round (money_in / usd_2_mdl)     

print (money_out)