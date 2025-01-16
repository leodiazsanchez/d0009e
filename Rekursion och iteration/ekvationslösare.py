def derivative(f,x,h):
    return (1/(2 * h)) * (f(x+h) - f(x-h))    

def f(x):
      return x**2-1


def solve(f,x0,h):

    while True:
        x1 = x0 - (f(x0)/derivative(f,x0,h))
        if abs(x0-x1) < h: # Här måste vi ha absolutbeloppet för att kunna hitta negativa rötter
            return x1
        else:
            x0 = x1
