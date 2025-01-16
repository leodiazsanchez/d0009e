def bounce(n):
    print(n) #Skriver ut alla tal i den övre delen av bounce ner till 0

    if(n>0): #När vi kommer 0 kommer print funktionen att skriva ut den undre delen av bouncen t.o.m n
        bounce(n-1)
        print(n)

def bounce2(n):
    #Skriver ut -n till n där de negativa talen blir positva pga abs(x)
    for x in range(-n, n+1):
      print(abs(x))
