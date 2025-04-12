
#%%
import time

p1={'Aa':9,'Ba':'-','Ca':'-','Ab':4,'Bb':'-','Cb':'-','Ac':'-','Bc':'-','Cc':'-'}
p=p1.copy()
s={'Aa':9,'Ba':2,'Ca':7,'Ab':4,'Bb':6,'Cb':8,'Ac':5,'Bc':10,'Cc':3}

instructions= ["Hi! I have a fun MAGIC SQUARE for you. It's very easy, just all rows, columns and diagonals must add up to 18.", 'To play, enter a  number between 2-10 and then enter its cell in the format COLUMNrow','ex- Ab is correct while aB,AB,ab are wrong', "Numbers cannot be repeated. You can update already filled cells in case you make a mistake.","Game ends when you have filled the magic square correctly. Press q to quit anytime. Good luck!"]
for line in instructions:
    print(line, flush=True)  
    time.sleep(1.2)               
print()
t='y'
def printtable():
    print('\n----------\n   A  B  C')
    for i in p:
        if i[0]=='A':
            print('\n',i[1],p[i],end='')
        else:
            print(' ',p[i],end='')
    print("\n----------\n")


while t=='y':
    printtable()
    c=0
    c2=0
    while c<7:
        x=input('enter no. ')
        if x=='q':
            print("Bye Bye!")
            t='n'
            break
        elif x>='0' and x<='9':
            x=int(x)
        else:
            print("invalid input")

            continue
        y=input('enter cell ')

        if y=='q':
            print("Bye Bye!")
            t='n'
            break
        if x<2 or x>10 :
            print('invalid number try again\n')
        elif x in p.values():
            print(x,'already exists!\n')
        elif y not in p.keys():
            print('invalid input try again\n')

        elif p1[y]!='-':
            print('non updatable cell, try again\n')
        elif x not in p.values():
            if p[y]!='-':
                print('Updating',y)
                p[y]=x
                printtable()
                c2+=1
            else:
                p[y]=x
                printtable()
                c+=1

    if t=='n':
        break
    if p==s:
        print('You got it right in',c+c2,'moves. Thank You for Playing')
        break
    else:
        print('You got it wrong')
        t=input('wanna try again? y or n ')
        if t=='n':
            print('Well played! goodbye')
            break
        else:
            print('Ok try again-')

            p=p1.copy()
            print()
#%%
