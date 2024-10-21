import numpy as np
from numpy.linalg import norm
from typing import List


def check_feasibility(const_coeff: List[List[float]], rhs_coeff: List[float],
                      x: List[float]) -> bool:
    for i in range(len(const_coeff)):
        temp = 0
        for j in range(len(const_coeff[i])):
            temp += const_coeff[i][j] * x[j]
        if temp >= rhs_coeff[i]:
            return False

    return True


def interior_point_method(obj_coeff: List[float],
                          const_coeff: List[List[float]],
                          rhs_coeff: List[float], x0: List[float]):
    if check_feasibility(const_coeff, rhs_coeff, x0):
        print("Feasible")
    else:
        print("Infeasible")


# Input section
n, m = map(int, input("Enter number of variables and constraints:\n").split())
obj_coeff = list(
    map(int, input("Enter objective function coefficients:\n").split()))
const_coeff = [list(map(int, input("Enter constraint coefficients:\n").split()))
               for _ in range(m)]
rhs_coeff = list(
    map(int, input("Enter right hand side coefficients:\n").split()))
initial_point = list(map(int, input("Enter initial point:\n").split()))
eps = float(input("Enter epsilon:\n"))

# Calling the function
interior_point_method(obj_coeff, const_coeff, rhs_coeff, initial_point)
