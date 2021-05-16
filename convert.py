import rates

def usd():
    data = rates.store()
    inv = float(data[0][2])
    unit = float(data[0][3])

    print("Choose the Operation Number:")
    while True:
        ch = input("1. USD to INR\n2. INR to USD\n")
        if ch == '1':
            while True:
                try:
                    usd = float(input("USD: "))
                except:
                    print("Enter Numerical Value Only")
                    continue
                break
            inr = usd * unit
            print("INR: ", inr)
        
        if ch == '2':
            while True:
                try:
                    inr = float(input("INR: "))
                except:
                    print("Enter Numerical Value Only")
                    continue
                break
            usd = inv * inr
            print("USD: ")
        
        else:
            print("Please Enter an Operation Number among them,")
            continue
        
        break

def eur():
    data = rates.store()
    inv = float(data[1][2])
    unit = float(data[1][3])

    print("Choose the Operation Number:")
    while True:
        ch = input("1. EUR to INR\n2. INR to USD\n")
        if ch == '1':
            while True:
                try:
                    eur = float(input("EUR: "))
                except:
                    print("Enter Numerical Value Only")
                    continue
                break
            inr = eur * unit
            print("INR: ", inr)
        
        if ch == '2':
            while True:
                try:
                    inr = float(input("INR: "))
                except:
                    print("Enter Numerical Value Only")
                    continue
                break
            eur = inv * inr
            print("EUR: ", eur)
        
        else:
            print("Please Enter an Operation Number among them,")
            continue
        
        break

def gbp():
    data = rates.store()
    inv = float(data[2][2])
    unit = float(data[2][3])

    print("Choose the Operation Number:")
    while True:
        ch = input("1. GBP to INR\n2. GBP to USD\n")
        if ch == '1':
            while True:
                try:
                    gbp = float(input("GBP: "))
                except:
                    print("Enter Numerical Value Only")
                    continue
                break
            inr = gbp * unit
            print("INR: ", inr)
        
        if ch == '2':
            while True:
                try:
                    inr = float(input("INR: "))
                except:
                    print("Enter Numerical Value Only")
                    continue
                break
            gbp = inv * inr
            print("GBP: ", gbp)
        
        else:
            print("Please Enter an Operation Number among them,")
            continue
        
        break    		

def aud():
    data = rates.store()
    inv = float(data[3][2])
    unit = float(data[3][3])

    print("Choose the Operation Number:")
    while True:
        ch = input("1. AUD to INR\n2. AUD to USD\n")
        if ch == '1':
            while True:
                try:
                    aud = float(input("AUD: "))
                except:
                    print("Enter Numerical Value Only")
                    continue
                break
            inr = aud * unit
            print("INR: ", inr)
        
        if ch == '2':
            while True:
                try:
                    inr = float(input("INR: "))
                except:
                    print("Enter Numerical Value Only")
                    continue
                break
            aud = inv * inr
            print("AUD: ", aud)
        
        else:
            print("Please Enter an Operation Number among them,")
            continue
        
        break

def cad():
    data = rates.store()
    inv = float(data[4][2])
    unit = float(data[4][3])

    print("Choose the Operation Number:")
    while True:
        ch = input("1. CAD to INR\n2. INR to CAD\n")
        if ch == '1':
            while True:
                try:
                    cad = float(input("CAD: "))
                except:
                    print("Enter Numerical Value Only")
                    continue
                break
            inr = cad * unit
            print("INR: ", inr)
        
        if ch == '2':
            while True:
                try:
                    inr = float(input("INR: "))
                except:
                    print("Enter Numerical Value Only")
                    continue
                break
            cad = inv * inr
            print("CAD: ", cad)
        
        else:
            print("Please Enter an Operation Number among them,")
            continue
        
        break

def sgd():
    data = rates.store()
    inv = float(data[5][2])
    unit = float(data[5][3])

    print("Choose the Operation Number:")
    while True:
        ch = input("1. SGD to INR\n2. INR to SGD\n")
        if ch == '1':
            while True:
                try:
                    sgd = float(input("SGD: "))
                except:
                    print("Enter Numerical Value Only")
                    continue
                break
            inr = sgd * unit
            print("INR: ", inr)
        
        if ch == '2':
            while True:
                try:
                    inr = float(input("INR: "))
                except:
                    print("Enter Numerical Value Only")
                    continue
                break
            sgd = inv * inr
            print("SGD: ", sgd)
        
        else:
            print("Please Enter an Operation Number among them,")
            continue
        
        break

def chf():
    data = rates.store()
    inv = float(data[6][2])
    unit = float(data[6][3])

    print("Choose the Operation Number:")
    while True:
        ch = input("1. CHF to INR\n2. INR to CHF\n")
        if ch == '1':
            while True:
                try:
                    chf = float(input("CHF: "))
                except:
                    print("Enter Numerical Value Only")
                    continue
                break
            inr = chf * unit
            print("INR: ", inr)
        
        if ch == '2':
            while True:
                try:
                    inr = float(input("INR: "))
                except:
                    print("Enter Numerical Value Only")
                    continue
                break
            chf = inv * inr
            print("EUR: ", chf)
        
        else:
            print("Please Enter an Operation Number among them,")
            continue
        
        break

#test
#usd()