from scipy.optimize import fsolve 

def find_nb(m):
    for i in range(0, 100):
        solution = fsolve(lambda x: i*x**3 - 3*((1/2)*i(i+1))*x**2 + 3*((1/6)*i*(i+1)*(2*i+1))*x -(1/4)*i**2*(i+1)**2)[0]
        if type(solution) == int:
            return solution
        else:
            return -1