#allows cursor movement in input
import readline

#sympy
from sympy import Symbol, diff, sympify
from sympy.core.mul import Mul
from sympy.printing.latex import latex
from sympy.core.add import Add
from sympy.simplify.simplify import simplify

varList = []
isTesting = False
symList = {}
partialsList = []
isDebug = False

if not isTesting:
    numVar = int(input("Enter number of variables: "))

    for i in range(numVar):
        varList.append(input("Enter next var: "))
    if isDebug:
        print(varList)

    #numConst = int(input("Enter number of constants: "))

    #for i in range(numConst):
    #    constList.append(input("Enter next constant: "))
    
    #creates symbols for each var and stores them to symList
    for i in range(numVar):
        symList.update({varList[i]: Symbol(varList[i], real=True)}) 
#x, y, z = symbols('x y z', real=True)
eq = input("Enter full equation: ")


#***** something not working here?????
#replace all ^ with **
eq = eq.replace("^", "**")


#print("Your equivalent equation is:")
#print(parse_expr(eq, transformations=transformations))
if isDebug:
    print(symList)
#print(type(symList["x"]))
# Convert the string to a SymPy expression

symEq = sympify(eq, evaluate=False)

varSet = symEq.free_symbols

for var in varSet:
    if symList.get(str(var)) != None:
        symList.update({str(var): var})

#do partial diff
for i in range(numVar):
    if isDebug: 
        print(diff(symEq, symList[varList[i]]), "\n")
    partialsList.append(diff(symEq, symList[varList[i]]))

finalEq = 0
for i, x in enumerate(partialsList):
    tmp = (Mul(x, Symbol("\\delta " + varList[i])))**2
    finalEq = Add(finalEq, tmp)

finalEq = simplify(finalEq)
print("final uncertainty equation: \\sqrt{", latex(finalEq), "}")


