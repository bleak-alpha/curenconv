import convert as con
import menu
import rates

menu.title()
while True:
    menu.menu()
    ch = input("Enter a Choice: ")

    if ch == '1':
        con.usd()
        p = input("Do you want to return to Menu(M) or Quit(Q)?")
        while True:
            if p == 'M' or p == 'm': continue
            if p == 'Q' or p == 'q': break
            break
    
    if ch == '2':
        con.eur()
        p = input("Do you want to return to Menu(M) or Quit(Q)?")
        while True:
            if p == 'M' or p == 'm': continue
            if p == 'Q' or p == 'q': break
            break
    
    if ch == '3':
        con.gbp()
        p = input("Do you want to return to Menu(M) or Quit(Q)?")
        while True:
            if p == 'M' or p == 'm': continue
            if p == 'Q' or p == 'q': break
            break
    
    if ch == '4':
        con.aud()
        p = input("Do you want to return to Menu(M) or Quit(Q)?")
        while True:
            if p == 'M' or p == 'm': continue
            if p == 'Q' or p == 'q': break
            break

    if ch == '5':
        con.cad()
        p = input("Do you want to return to Menu(M) or Quit(Q)?")
        while True:
            if p == 'M' or p == 'm': continue
            if p == 'Q' or p == 'q': break
            break
    
    if ch == '6':
        con.sgd()
        p = input("Do you want to return to Menu(M) or Quit(Q)?")
        while True:
            if p == 'M' or p == 'm': continue
            if p == 'Q' or p == 'q': break
            break

    if ch == '7':
        con.chf()
        p = input("Do you want to return to Menu(M) or Quit(Q)?")
        while True:
            if p == 'M' or p == 'm': continue
            if p == 'Q' or p == 'q': break
            break
    
    if ch == '8':
        con.myr()
        p = input("Do you want to return to Menu(M) or Quit(Q)?")
        while True:
            if p == 'M' or p == 'm': continue
            if p == 'Q' or p == 'q': break
            break
    
    if ch == '9':
        con.jpy()
        p = input("Do you want to return to Menu(M) or Quit(Q)?")
        while True:
            if p == 'M' or p == 'm': continue
            if p == 'Q' or p == 'q': break
            break
    
    if ch == '10':
        con.cny()
        p = input("Do you want to return to Menu(M) or Quit(Q)?")
        while True:
            if p == 'M' or p == 'm': continue
            if p == 'Q' or p == 'q': break
            break

    if ch == 'Q' or 'q': break
    
    else:
        print("Enter a valid choice")
        continue

    break