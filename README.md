  
# Introduction

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

**Out:**<br>
$$\displaystyle\frac{\left(x^{4} + x^{2} e^{x} - x^{2} - 2 x e^{x} - 2 x - e^{x}\right) e^{x}}{\left(x - 1\right)^{2} \left(x + 1\right)^{2} \left(e^{x} + 1\right)}$$<br><br>

{% code-tabs %}
{% code-tabs-item title="In:" %}
```python
integ = Integral(expr, x)
integ.doit()
```
{% endcode-tabs-item %}
{% endcode-tabs %}

**Out:**<br>
$$\displaystyle\log{\left(e^{x} + 1 \right)} + \frac{e^{x}}{x^{2} - 1}$$<br><br>

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

**Out:**<br>
$$\displaystyle5$$<br>
$$\displaystyle9$$<br><br>

{% code-tabs %}
{% code-tabs-item title="In:" %}
```python
get_ipython().profile_dir.startup_dir
print("okay")
```
{% endcode-tabs-item %}
{% endcode-tabs %}

**Out:**<br>
'/Users/phuocdo/.ipython/profile_default/startup'<br>
okay<br><br>

{% code-tabs %}
{% code-tabs-item title="In:" %}
```python
LatexPrinter
print("yes")
```
{% endcode-tabs-item %}
{% endcode-tabs %}

**Out:**<br>
sympy.printing.latex.LatexPrinter<br>
yes<br><br>
