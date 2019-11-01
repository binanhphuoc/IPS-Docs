# Introduction

> $$\displaystyle5$$  
> $$\displaystyle9$$

**Out:**  
TEST  
Something else



## In this tutorial, we will learn how to set up a Python Dev Process.

{% code-tabs %}
{% code-tabs-item title="In:" %}
```python
x = symbols("x")
expr = (x**4 + x**2*exp(x) - x**2 - 2*x*exp(x) - 2*x - exp(x))*exp(x)/((x - 1)**2*(x + 1)**2*(exp(x) + 1))
expr
```
{% endcode-tabs-item %}
{% endcode-tabs %}

$$\displaystyle\frac{\left(x^{4} + x^{2} e^{x} - x^{2} - 2 x e^{x} - 2 x - e^{x}\right) e^{x}}{\left(x - 1\right)^{2} \left(x + 1\right)^{2} \left(e^{x} + 1\right)}$$

{% code-tabs %}
{% code-tabs-item title="In:" %}
```python
integ = Integral(expr, x)
integ.doit()
```
{% endcode-tabs-item %}
{% endcode-tabs %}

$$\displaystyle\log{\left(e^{x} + 1 \right)} + \frac{e^{x}}{x^{2} - 1}$$

{% code-tabs %}
{% code-tabs-item title="In:" %}
```python
x = 5
a = x+4
x
a
```
{% endcode-tabs-item %}
{% endcode-tabs %}

$$\displaystyle5$$  
$$\displaystyle9$$

{% code-tabs %}
{% code-tabs-item title="In:" %}
```python
get_ipython().profile_dir.startup_dir
print("okay")
```
{% endcode-tabs-item %}
{% endcode-tabs %}

> '/Users/phuocdo/.ipython/profile\_default/startup'  
> okay

{% code-tabs %}
{% code-tabs-item title="In:" %}
```python
LatexPrinter
print("yes")
```
{% endcode-tabs-item %}
{% endcode-tabs %}

> ### Out:
>
> sympy.printing.latex.LatexPrinter  
>  yes  
>
>
> Yeahhhh  
> oka

