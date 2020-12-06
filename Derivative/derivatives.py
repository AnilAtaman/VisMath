import matplotlib.pyplot as mplt
import  sympy as sym
import numpy
import matplotlib.patches as mpatches
import string
from colorama import Fore, Back, Style
"""
This piece of code was written to calculate derivative of the any function,
it also plot the derivates 

"""


theFunctionPlt = []
theIncresement = []
theFunctionPlt_1 = []
theIncresement_1 = []
theFunctionPlt_2 = []
theIncresement_2 = []
theFunctionPlt_3 = []
theIncresement_3 = []
theFunctionPlt_4 = []
theIncresement_4 = []
theFunctionPlt_5 = []
theIncresement_5 = []
innerLimit = -4
upperLimit = 2
incresementRate = 0.0001

print('\033[33m'+ "Avaiable Operator : x**y , + , - , / ")
print('\033[33m'+ "Example of Function : x**3 (x^3, y = 3) + 5 ")
theKeyFunction = input('\033[31m'+ "Enter your Function : ")
theKeyFunction = theKeyFunction.replace(" ","")
print(theKeyFunction)
x = sym.Symbol('x')
theKeyFunction = str(theKeyFunction)
theKeyFunction_memo = str(theKeyFunction)





#The function
for x in numpy.arange(innerLimit,upperLimit,incresementRate):
    theFunction = eval(theKeyFunction)
    theFunctionPlt.append(theFunction)
    theIncresement.append(x)
"""
fig_1 = mplt.figure()
fx_1 = fig_1.add_subplot(411)
mplt.grid()
fx_1.plot(theIncresement,theFunctionPlt)
mplt.title('The Function')
mplt.xlabel('The Points')
mplt.ylabel('Values')
"""
#First Derivative
theKeyFunction_otherDeri = ""
x_1 = sym.Symbol('x_1')
for i in range(len(theKeyFunction_memo)):
    if(theKeyFunction_memo[i] == "x"):
      theKeyFunction_otherDeri+=('x_1')
    else:
      theKeyFunction_otherDeri+=(theKeyFunction_memo[i])


theFunctionFirstDerivative = theKeyFunction_otherDeri
derivatedFunction_1 = str(sym.diff(theFunctionFirstDerivative))
print('\033[31m'+"First Derivative : "+'\033[35m'+ derivatedFunction_1)



for x_1 in numpy.arange(innerLimit,upperLimit,incresementRate):
    derivatedFunction_1_1 = eval(derivatedFunction_1)
    theFunctionPlt_1.append(derivatedFunction_1_1)
    theIncresement_1.append(x_1)
"""
fx_1 = fig_1.add_subplot(412)
fx_1.plot(theIncresement_1,theFunctionPlt_1)
mplt.grid()
mplt.title('First Derivative')
mplt.xlabel('The Points')
mplt.ylabel('Values')
"""
"""
fx_1 = fig_1.add_subplot(413)
fx_1.plot(theIncresement_1,theFunctionPlt_1,theIncresement,theFunctionPlt)
mplt.grid()
mplt.title('The Function & First Derivative')
mplt.xlabel('The Points')
mplt.ylabel('Values')
mplt.tight_layout()

"""

#Second Derivative
derivatedFunction_2 = str(sym.diff(derivatedFunction_1))
print('\033[31m'+"Second Derivative : "+'\033[35m'+ derivatedFunction_2)
for x_1 in numpy.arange(innerLimit,upperLimit,incresementRate):
    derivatedFunction_2_2 = eval(derivatedFunction_2)
    theFunctionPlt_2.append(derivatedFunction_2_2)
    theIncresement_2.append(x_1)

blue_patch = mpatches.Patch(color='blue',label = 'The Function ')
red_patch = mpatches.Patch(color='red',label = 'The First Derivative (Slope, Increse or Decrease)')
orange_patch = mpatches.Patch(color='orange',label = 'The Second Derivative (Rate of Change)')
fig_5 = mplt.figure()
fx_5 = fig_5.add_subplot(111)
fx_5.plot(theIncresement,theFunctionPlt, color = 'blue')
fx_5.plot(theIncresement_1,theFunctionPlt_1, color = 'red')
fx_5.plot(theIncresement_2,theFunctionPlt_2,color = 'orange')
mplt.title('The Function & First Derivative & Second Derivative')
mplt.xlabel('The Points')
mplt.ylabel('Values')
mplt.grid()
mplt.legend(handles = [blue_patch,red_patch,orange_patch])

#fig_2 = mplt.figure()
#fx_2 = fig_2.add_subplot(211)
#fx_2.plot(theIncresement_2,theFunctionPlt_2)
#mplt.grid()
#mplt.title('Second Derivative')
#mplt.xlabel('The Points')
#mplt.ylabel('Values')


#Third Derivative
derivatedFunction_3 = str(sym.diff(derivatedFunction_2))
print('\033[31m'+"Third Derivative : "+'\033[35m'+ derivatedFunction_3)

for x_1 in numpy.arange(innerLimit,upperLimit,incresementRate):
    derivatedFunction_3_3 = eval(derivatedFunction_3)
    theFunctionPlt_3.append(derivatedFunction_3_3)
    theIncresement_3.append(x_1)
#fx_2 = fig_2.add_subplot(212)
#fx_2.plot(theIncresement_3,theFunctionPlt_3)
#mplt.grid()
#mplt.title('Third Derivative')
#mplt.xlabel('The Points')
#mplt.ylabel('Values')

mplt.tight_layout()

#Fourth Derivative
derivatedFunction_4 = str(sym.diff(derivatedFunction_3))
print('\033[31m'+"Fourth Derivative : "+'\033[35m'+ derivatedFunction_4)

for x_1 in numpy.arange(innerLimit,upperLimit,incresementRate):
    derivatedFunction_4_4 = eval(derivatedFunction_3)
    theFunctionPlt_4.append(derivatedFunction_4_4)
    theIncresement_4.append(x_1)
#fig_3 = mplt.figure()
#fx_3 = fig_3.add_subplot(211)
#fx_3.plot(theIncresement_4,theFunctionPlt_4)
#mplt.grid()
#mplt.title('Fourth Derivative')
#mplt.xlabel('The Points')
#mplt.ylabel('Values')

#Fifth Derivative
derivatedFunction_5 = str(sym.diff(derivatedFunction_4))
print('\033[31m'+"Fifth Derivative : "+'\033[35m'+ derivatedFunction_5)

for x_1 in numpy.arange(innerLimit,upperLimit,incresementRate):
    derivatedFunction_5_5 = eval(derivatedFunction_5)
    theFunctionPlt_5.append(derivatedFunction_5_5)
    theIncresement_5.append(x_1)
#fx_3 = fig_3.add_subplot(212)
#fx_3.plot(theIncresement_5,theFunctionPlt_5)
#mplt.grid()
#mplt.title('Fifth Derivative')
#mplt.xlabel('The Points')
#mplt.ylabel('Values')

mplt.tight_layout()
mplt.show()