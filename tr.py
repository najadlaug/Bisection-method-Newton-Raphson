from os import system
import numpy as np
import time

def f(x, lista): 
	#convert list with the x
	lista = lista.copy()
	for num in range(len(lista)):
		if lista[num] == "x":
			lista[num] = x  

	timesAppend = (len(lista)-1)/4 #Normalmente sera el grado de la funcion pero no tiene porque
	cont = 0

	#Get value of the x at the power * the coefficent
	res1 = []
	for i in range(len(lista)):
		if cont == 0 and timesAppend > 0:
			res1.append(lista[i]*(lista[i+1]**lista[i+2]))
			timesAppend -= 1
			cont = -4

		elif cont == -1:
			res1.append(lista[i])

		cont += 1
	res1.append(lista[len(lista)-1])
	
	#Sum or Rest the last values
	while len(res1) > 1:
		if res1[1] == "+":
			suma = res1[0] + res1[2]
			res1.pop(0)
			res1.pop(0)
			res1.pop(0)
			res1.insert(0, suma)

		elif res1[1] == "-":
			suma = res1[0] - res1[2]
			res1.pop(0)
			res1.pop(0)
			res1.pop(0)
			res1.insert(0, suma)

	return res1[0]

def f2(x, lista):
	return 2*x**4-6*x**3+10 #2x⁴ - 6x³ + 10


def inputPolynomial():
	power = int(input("Digues el grau del polinomi: "))
	_ = system('cls')
	coefficent = 0
	polynomial = []

	while power != 0:
		coefficent = int(input("Digues el coeficient:"))
		_ = system('cls')
		printPolynomial(polynomial)
		print()
		polynomial.append(coefficent)
		polynomial.append("x")
		polynomial.append(power)
		sign = input("Digues el signe:")
		_ = system('cls')
		polynomial.append(sign)
		power -= 1
	coefficent = int(input("Digues el terme independent: "))
	polynomial.append(coefficent)

	return polynomial


def printPolynomial(PolynomialList):
	t = False
	exponents = ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]

	for x in PolynomialList:
		if t == True:
			try:
				print(exponents[x], end = " ")
				t = False
			except:
				print("^", end = "")
				print(x, end = " ")
				t = False

		elif x == "x":
			print(x, end = "")
			t = True

		elif x == "+" or x == "-" or x == "/" or x == "*":
			print(x, end = " ")

		else:
			print(x, end= "")


def rangCalculator(PolynomialList):
	maxval = 0 #Valor maximo
	xmax = PolynomialList[0] #Coeficiente del de maximo exponente

	for number in PolynomialList:
		try:
			if maxval < number:
				maxval = number
		except:
			pass

	M = (maxval/xmax) + 1 #Formula M (rango)

	print()
	print(" Range: [", -M, ",", M, "]" )
	return M


def bisection(a, b, tol, listaFunction):
	while np.abs(a-b) >= tol: #Mentres que la longitud(absoluta) sigui mes petita o igual a la tolerancia:
		c = (a + b)/ 2
		product = f(a, listaFunction) * f(c, listaFunction)

		if product > tol:
			a = c

		elif product < tol:
			b = c

	return c


def findBisectionPoints(M, listaFunction):
	BisectionPoints = [-M]
	ActualPoint = -M
	ansFuncStart = f(-M, listaFunction)

	if ansFuncStart > 0:
		ActualState = "pos" #bool que dice que empieza por positivo

	elif ansFuncStart < 0:
		ActualState = "neg" #bool que dice que empieza por negativo

	while ActualPoint < M:
		ansFuncActualPoint = f(ActualPoint, listaFunction)

		if ansFuncActualPoint < 0 and ActualState == "pos":
			BisectionPoints.append(ActualPoint)
			ActualState = "neg"

		if ansFuncActualPoint > 0 and ActualState == "neg":
			BisectionPoints.append(ActualPoint)
			ActualState = "pos"

		sumaIteracio = 0.1
		ActualPoint += sumaIteracio

	print(" The Bisection points are: ", BisectionPoints)
	return BisectionPoints


def ApplyBisection(BisectionPointsList, listaFunction):
	roots = []
	for x in range(len(BisectionPointsList)-1):
		ans = bisection(BisectionPointsList[x], BisectionPointsList[x+1], 1e-10, listaFunction)
		roots.append(ans)

	return roots

def convertPoli(function):
	mat = []
	listinmat = []
	cont = 0
	for x in range(len(function)):
		if function[x] == "-":
			function[x+1] = -function[x+1]

	for x in function:
		try:
			if x == int(x):
				listinmat.append(x)
				cont += 1
				if cont == 2:
					mat.append(listinmat)
					listinmat = []
					cont = 0

		except:
			pass

	listinmat = []
	independent = function[len(function)-1]
	print(independent)
	listinmat.append(independent)
	listinmat.append(0)
	mat.append(listinmat)

	return mat


def derivate(fMat):
	fMat = fMat.copy()
	fMat.pop()
	derivate = []
	glist = []
	for x in range(len(fMat)):
		glist.append(fMat[x][0]*fMat[x][1])
		glist.append(fMat[x][1]-1)
		derivate.append(glist)
		glist = []

	return derivate


def evaluate_function(function, x0):
	totalValue = 0
	for x in range(len(function)):
		Valor = (x0 ** function[x][1]) * function[x][0]
		totalValue += Valor

	return totalValue


def newton_raphson(f, g, xn, tol):
	firstEntry = True
	x1 = 0
	cont = 0
	infinit = False
	if evaluate_function(g, xn) != 0:
		while np.abs(x1-xn) > tol and infinit == False or firstEntry == True:
			if cont < 25:
				cont += 1
				firstEntry = False
				x1 = xn
				if evaluate_function(g, xn) != 0: #en cas de que g sigui 0 vol dir que el denominador endira a infinit per aixo es fara un bucle infinit
					xn = xn - (evaluate_function(f, xn) / evaluate_function(g, xn))

				else:
					infinit = True
					xn = False
				#print("iteraction: ", cont, ", xn: ", xn)
			else:
				xn = False
				infinit = True
	return xn


def apply_raphson(fMat, gMat, M, tol) :
	x0 = -M
	roots_NR = []
	root = newton_raphson(fMat, gMat, x0, tol)
	try:
		roots_NR.append(float(root))

	except Exception as e:
		print(e)

	while x0 == M or x0 < M:
		root = newton_raphson(gMat, fMat, x0, tol)
		if np.abs(root - roots_NR[len(roots_NR)-1]) > 0.1:
			if root != False:
				roots_NR.append(root)

		x0 += 0.5

	return roots_NR



def cleanList(Listroots):
	cont = 0
	for x in range(len(Listroots)-1):
		if len(Listroots) - 1 >= x:
			cont = 0
			for i in range(len(Listroots)-1):
				if len(Listroots) - cont >= i:
					if x != i:
						#print(x, i)
						if np.abs(Listroots[x]-Listroots[i]) < 0.5:
							Listroots.pop(i)
							cont += 1

			#print(Listroots)

	return Listroots


if __name__ == "__main__":
	Polynomial = [9, "x", 7, "-", 8, "x", 1, "+", 6, "x", 1, "-", 92]

	M = rangCalculator(Polynomial) #Calcula el rang i l'assigna a M

	start_time = time.time()
	print(bisection(-M, M, 1e-10, Polynomial))
	time.sleep(2)
	end_time = time.time()
	print(f" Tiempo total: {end_time - start_time}")

	start_time = time.time()
	fMat = convertPoli(Polynomial)
	print("funcion:", fMat)
	gMat = derivate(fMat)
	print("derivate:", gMat)
	newton_raphson(fMat, gMat, -11.5, 0.000001)
	time.sleep(2)
	end_time = time.time()
	print(f" Tiempo total: {end_time - start_time}")
