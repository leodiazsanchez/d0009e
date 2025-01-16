def tvarsumman(n):
  if n == 0:
    return 0
  else:
    return (n%10) + tvarsumman(n//10)
 
def tvarsumman2(n): 
    summa = 0
    while n:
      summa += n % 10 # Resten av n delat på 10 adderas till summan
      n //= 10 # n = n delat på 10 (heltalsdivision), processen fortsätter tills n = 0 och summan returneras
    return summa
