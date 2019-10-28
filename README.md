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
disp_latex(a)
```




$$\displaystyle5$$






    '9'




```python
globals()['LatexPrinter']
```




    sympy.printing.latex.LatexPrinter




```python
get_ipython().profile_dir.startup_dir
```




    '/Users/phuocdo/.ipython/profile_default/startup'




```python

```
