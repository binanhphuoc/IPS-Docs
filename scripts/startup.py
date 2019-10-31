from sympy import *
from sympy.printing.latex import LatexPrinter

def disp_latex(expr, **settings):
    return LatexPrinter(settings).doprint(expr).replace('$$', '$$\displaystyle', 1)

from sympy.interactive import init_printing
init_printing(use_latex="mathjax",latex_mode="equation",itex=True,latex_printer=disp_latex)
    
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# try:
#     def exit_register(fun, *args, **kwargs):
#         """ Decorator that registers at post_execute. After its execution it
#         unregisters itself for subsequent runs. """
#         def callback():
#             fun()
#             ip.events.unregister('post_execute', callback)
#         ip.events.register('post_execute', callback)


#     ip = get_ipython()
# except NameError:
#     from atexit import register as exit_register


# @exit_register
# def callback():
#     print('I\'m done!')


# print('Running')

# import os

# from IPython.core.error import TryNext
# import IPython.core.hooks

# def calljed(self):
#     print("Something?")
#     os.system('echo something > ~/helloFromPython.txt')
#     if os.system('echo something > ~/helloFromPython.txt') != 0:
#         raise TryNext()

# # ip.set_hook('shutdown_hook', calljed)
# IPython.core.hooks.shutdown_hook = calljed