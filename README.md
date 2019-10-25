# Introduction

## In this tutorial, we will learn how to set up a Python Dev Process.


```python
from sympy import *
from IPython.display import *
def disp_latex(expr):
    display_latex(latex(expr,mode='equation',itex=True),raw=True)

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
```


```python
x = symbols("x")
expr = (x**4 + x**2*exp(x) - x**2 - 2*x*exp(x) - 2*x - exp(x))*exp(x)/((x - 1)**2*(x + 1)**2*(exp(x) + 1))
disp_latex(expr)
```


$$\frac{\left(x^{4} + x^{2} e^{x} - x^{2} - 2 x e^{x} - 2 x - e^{x}\right) e^{x}}{\left(x - 1\right)^{2} \left(x + 1\right)^{2} \left(e^{x} + 1\right)}$$



```python
integ = Integral(expr, x)
disp_latex(integ.doit())
```


$$\log{\left(e^{x} + 1 \right)} + \frac{e^{x}}{x^{2} - 1}$$



```python
x = 5
a = x+4
disp_latex(x)
a
```


$$5$$





$\displaystyle 9$




```python

```
