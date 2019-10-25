```python
from sympy import *
from sympy.printing.latex import LatexPrinter

#get_ipython().profile_dir.startup_dir

def disp_latex(expr, **settings):
    return LatexPrinter(settings).doprint(expr).replace('$$', '$$\displaystyle', 1)

from sympy.interactive import init_printing
init_printing(latex_mode="equation",itex=True,latex_printer=disp_latex)
    
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
```

# Introduction

## In this tutorial, we will learn how to set up a Python Dev Process.


```python
x = symbols("x")
expr = (x**4 + x**2*exp(x) - x**2 - 2*x*exp(x) - 2*x - exp(x))*exp(x)/((x - 1)**2*(x + 1)**2*(exp(x) + 1))
expr
```




$$\displaystyle\frac{\left(x^{4} + x^{2} e^{x} - x^{2} - 2 x e^{x} - 2 x - e^{x}\right) e^{x}}{\left(x - 1\right)^{2} \left(x + 1\right)^{2} \left(e^{x} + 1\right)}$$




```python
integ = Integral(expr, x)
integ.doit()
```




$$\displaystyle\log{\left(e^{x} + 1 \right)} + \frac{e^{x}}{x^{2} - 1}$$




```python
x = 5
a = x+4
x
a
```




$$\displaystyle5$$






$$\displaystyle9$$




```python

```
