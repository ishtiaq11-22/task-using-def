print('''We have 
      eggs
      biscuit
      book
      iphone
      macbook
      Please enter the correct spelling of items
      ''')


def item():
    name=input("Enter item name: ")
    return name

def qty():
    quantity=int(input("Enter quantity: "))
    return quantity

def price(name,quantity):
    if name == "eggs":
        return quantity * 20
    elif name == "biscuit":
        return quantity * 50
    elif name == "book":
        return quantity * 200
    elif name == "iphone":
        return quantity * 50000
    elif name == "macbook":
        return quantity * 100000
        


def discount(a):
    if a <= 50 :
        c=print("No discount")
    elif   a <= 100:
        c= 5
    elif  a <= 200 :
        c= 10
    elif a <= 500:
        c= 15
    elif a > 500 :
        c=20
    return c

def discounted_amount(a,c):
    d= (a * c) / 100
    return d

def after_discount(a,d):
    e = a - d
    return e

def tax (e):
    f=e * 0.085
    return f

def total_amount_to_pay(e,f):
    g=e + f
    return g
    
def main():
    name_=item()
    quantity_=qty()
    price_=price(name_,quantity_)
    discount_=discount(price_)
    discounted_amount_=discounted_amount(price_,discount_)
    after_discount_=after_discount(price_,discounted_amount_)
    Tax=tax(after_discount_)
    total_amount=total_amount_to_pay(after_discount_,Tax)

    print("Item Price: ",price_)
    print("Percent Discount ",discount_,"%")
    print("Discount : ",discounted_amount_)
    print("Discounted Amount: ",after_discount_)
    print("Sales Tax: ",Tax)
    print("Total Amount : ",total_amount)

main()