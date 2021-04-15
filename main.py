import time
import colorama
from os import system
import numpy as np
from colorama import Fore, Back, Style
from tr import bisection, rangCalculator, printPolynomial, findBisectionPoints, ApplyBisection, inputPolynomial, derivate, convertPoli, newton_raphson, apply_raphson, cleanList


def main():
	#INPUTS
	Polynomial = inputPolynomial()

	#PRINTS COMIENZO
	_ = system('cls')
	colorama.init(autoreset = False)
	print()
	print(" Welcome to roots finder!")
	print(" I will find the roots of this Polynomial: ", end = " ")
	print(Fore.CYAN, end= "")
	printPolynomial(Polynomial) #Print del polinomi
	print(Fore.RESET)

	#GENERAL INFO:
	M = rangCalculator(Polynomial) #Calcula el rang i l'assigna a M

	#BISECTION METHOD:
	print(" Bisection:")
	start_time = time.time()
	BisectionPoints = findBisectionPoints(M, Polynomial)
	rootsBisection = ApplyBisection(BisectionPoints, Polynomial)
	print(" The roots of this Polynomial are:", end = " ")
	print(Fore.CYAN, end= "")
	print(rootsBisection) #Print del roots
	print(Fore.RESET)
	end_time = time.time()
	print(f" Tiempo total: {end_time - start_time}")

	#NEWTON RAPHSON METHOD:
	print()
	print(" Newton Raphson:")
	start_time = time.time()
	fMat = convertPoli(Polynomial)
	gMat = derivate(fMat)
	#newton_raphson(fMat, gMat, -11.5, 0.000001)
	print(" The roots of this Polynomial are:", end = " ")
	rootsNewton = apply_raphson(fMat, gMat, M, 0.0001)
	rootsNewtonClean = cleanList(rootsNewton)
	print(rootsNewtonClean)

	end_time = time.time()
	print(f" Tiempo total: {end_time - start_time}")


if __name__ == "__main__":
	main()