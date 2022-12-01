import math as mt
import numpy as np

class Complex_Number:
    def __init__(self, r, i):
        self.real = r
        self.image = i
    def show(self):
        print(str(self.real)+ ' ' + str(self.image) + 'j')
    def magnitude(self):
        return mt.sqrt((self.real)**2+(self.image)**2)
    def angle(self):
        return mt.atan(self.image/self.real)
    def summation(self, ComplexB):
        self.real += ComplexB.real
        self.image += ComplexB.image
    def multiplication(self, ComplexB):
        self.real, self.image = self.real * ComplexB.real - self.image * ComplexB.image, self.real * ComplexB.image + self.image * ComplexB.real

A = Complex_Number(2, -2)
B = Complex_Number(4, 4)
A.show()
A.summation(B)
A.show()
A.multiplication(B)
A.show()

print(A.magnitude())
print(A.angle())

class Complex_Vector():
    def __init__(self, cols):
        self.dimension = cols
        self.vect = []
        for n in range(self.dimension):
            real_part = np.random.randint(-10,10)
            image_part = np.random.randint(-10,10)
            self.vect.append(Complex_Number(real_part, image_part))
    def show(self):
        for n in range(self.dimension):
        	self.vect[n].show()
    def magnitude(self):
        self.magnitude_vector = []
        for n in range(self.dimension):
            self.magnitude_vector.append(Complex_Number.magnitude(self.vect[n]))
        return self.magnitude_vector
    def summation(self, VectorB):
        if self.dimension == VectorB.dimension:
            for n in range(self.dimension):
                self.vect[n].summation(VectorB.vect[n])
        else:
            print("Vectors are not at the same size")
    def multiplication(self, VectorB):
        if self.dimension == VectorB.dimension:
            for n in range(self.dimension):
                self.vect[n].multiplication(VectorB.vect[n])
        else:
            print("Vectors are not at the same size")
    def search_higher_magnitude(self):
        module = self.magnitude_vector[0]
        ind = 0
        for n in range(1, self.dimension):
            if self.magnitude_vector[n] >= module:
                module = self.magnitude_vector[n]
                ind = n
        return ind


M = Complex_Vector(3)
print(M.magnitude())
N = Complex_Vector(3)
print(N.magnitude())
M.show()
N.show()
M.summation(N)
M.show()
M.multiplication(N)
M.show()
print(M.search_higher_magnitude())


class Complex_Matrix(Complex_Vector):
    def __init__(self, cols, line):
        Complex_Vector.__init__(self, cols)
        self.nbr_lines = line
        self.lines = []
        for n in range(self.nbr_lines):
            real_part = np.random.randint(-10,10)
            image_part = np.random.randint(-10,10)
            self.lines.append(Complex_Vector(cols))
    def show(self):
        for n in range(self.nbr_lines):
            self.lines[n].show()
    def magnitude(self):
        self.magnitude_matrix = []
        for n in range(self.nbr_lines):
            self.magnitude_matrix.append(Complex_Vector.magnitude(self.lines[n]))
        return self.magnitude_matrix
    def summation(self, MatrixB):
        if(self.nbr_lines == MatrixB.nbr_lines):
            for n in range(self.nbr_lines):
                self.lines[n].summation(MatrixB.lines[n])
        else:
            print("Matrixs are not at the same size")
    def search_higher_magnitude(self):
        module = self.magnitude_matrix[0][0]
        indice_line = 0
        indice_col = 0
        for n in range(self.nbr_lines):
            for m in range(self.dimension):
                if self.magnitude_matrix[n][m] >= module:
                    indice_col = m
                    indice_line = n
                    module = self.magnitude_matrix[n][m]
        return indice_line, indice_col

M = Complex_Matrix(3, 3)
print("M magnitude:")
print(M.magnitude())
N = Complex_Matrix(3, 3)
print("N magnitude:")
print(N.magnitude())
print("M matrix:")
M.show()
print("N matrix:")
N.show()
M.summation(N)
print("M + N:")
M.show()
M.multiplication(N)
print("M * N:")
M.show()
print("Position of the higher magnitude for M and N:")
print(M.search_higher_magnitude())
print(N.search_higher_magnitude())


























