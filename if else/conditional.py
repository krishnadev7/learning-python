good_credit = False
price_of_house = 1000000

if good_credit: 
    down_payment = (price_of_house * 10) / 100
    print("Your down payment is " + str(down_payment))
else: 
    down_payment = (price_of_house * 20) / 100
    print("Your down payment is " + str(down_payment))
