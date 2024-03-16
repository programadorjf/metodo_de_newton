from typing import Sequence
import numpy as np

#função do exmplo 1: dinamica populacional
#def f(x): return 10*np.exp(x)+(1/x)*(np.exp(x)-1)-15
#def f_linha(x): return 10*np.exp(x)-(1/x**2)*(np.exp(x)-1)+(np.exp(x)/x)

#função do exemplo 3
#def f(x): return -x**2+((2*x)/5)-(1/25)+np.cos(x-1/5)
#def f_linha(x): return -2*x+2/5-np.sin(x-1/5)

#função do exercicio 8a
#def f(x): return x**3-2*x**2-5
#def f_linha(x): return 3*x**2-4*x

#função do exercicio 8b
#def f(x): return x-np.cos(x)
#def f_linha(x): return 1+np.sin(x)

def newton(f,f_linha,x0,tol,maxIter):
  n = 1
  while (n <= maxIter): 
    #verifica se a derivada e nula
    fx_linha = f_linha(x0)
    fx = f(x0)
    if (fx_linha == 0):
      raise NameError('Derivada nula!');
    
    x = x0 - fx/fx_linha #iteracao de newton
    print([n,x0,'fx:',fx,'fx°:',fx_linha,'fx/fx°:',np.abs(x-x0)])

    if (np.abs(x-x0) < tol): #condicao de parada
      return x
    x0 = x
    n = n + 1
  raise NameError ('Número máximo de iterações excedido!');
  
#exmplo 1: dinamica populacional
#newton(f,f_linha,0.3,10**(-4),100) #não bate o resultado da fx com x2

#exemplo 3
#newton(f,f_linha,0.5,10**(-4),100)

#exercicio 8a
#newton(f,f_linha,1,10**(-5),100)

#exercicio 8b
#newton(f,f_linha,np.pi/8,10**(-5),100)