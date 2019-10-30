# from sympy.printing.latex import LatexPrinter
def funcA():
    print("A")

funcC = funcA

def funcB():
    funcC()
    print("B")

funcA = funcB

funcB()
