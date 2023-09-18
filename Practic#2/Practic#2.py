import numpy as np


class matrix_processing:
    """Matrix processing"""

    def __init__(self):

        self.easy_matrix = np.array([[1, 2, 3],
                                     [4, 5, 6],
                                     [7, 8, 9]])
        self.matrix_A = np.array([[1, 2, 3],
                                  [4, 5, 6]])
        self.matrix_B = np.array([[-1, -2, -3],
                                  [-4, -5, -6]])

    def vector(self):
        """Create ready vector"""

        vector_a = np.array([1, 2, 3])
        print(f"v = {vector_a}")
        print(type(vector_a))

        input("push Enter to continue")

    def matrix(self):
        """Create ready matrix"""

        print(*self.easy_matrix, sep="\n")

        input("push Enter to continue")

    def zero_matrix(self):
        """Create zero matrix(size = 4,5)"""

        zero_matrix = np.zeros((4, 5))
        print(*zero_matrix, sep='\n')

        input("push Enter to continue")

    def identity_matrix(self):
        """Create single matrix (size = 3,3)"""

        identity_matrix = np.identity(3)
        print(*identity_matrix, sep="\n")

        input("push Enter to continue")

    def size_matrix(self):
        """Show size of matrix"""

        print(f"Size of matrix = {self.easy_matrix.shape}")

        input("push Enter to continue")

    def two_matrix(self):
        """Create matrix A and B. Execute operation"""

        adding_matrix = self.matrix_A + self.matrix_B
        matrix_subtraction = self.matrix_A - self.matrix_B
        print(*adding_matrix, sep="\n")
        print("-------")
        print(*matrix_subtraction, sep="\n")

        input("push Enter to continue")

    def multiplication(self):
        """Matrix(A, B) multiplication."""

        multiplication_matrix = np.multiply(self.matrix_A, self.matrix_B)
        print(*multiplication_matrix, sep="\n")

        input("push Enter to continue")

    def const_and_matrix(self):
        """Const b for matrix A."""

        b = 2
        adding_const = self.matrix_A + b
        print(*adding_const, sep="\n")

        input("push Enter to continue")

    def multiplication_no_name(self):
        """Matrix(no name) multiplication"""

        matrix_A = np.array([[1, 2, 3],
                             [4, 5, 6]])
        matrix_B = np.array([[1, 1],
                             [1, 1],
                             [1, 1]])
        multiply_matrix = np.dot(matrix_A, matrix_B)

        print(*multiply_matrix, sep="\n")

        input("push Enter to continue")

    def euclidean_norm(self):
        """Euclidean norm"""

        v = np.array([1, 2, 3])
        u = np.array([1, 1, 1])

        e_norm_1 = np.linalg.norm(v)
        e_norm_2 = np.linalg.norm(u)

        print(f"{e_norm_1}\n{e_norm_2}")

        input("push Enter to continue")

    def vector_slice(self):
        """Vector slice"""

        vector = np.array([11, 22, 33, 33, 44, 55])
        vector_slice = vector[4:]

        print(vector_slice)

        input("push Enter to continue")

    def start_menu(self):
        """Start menu"""
        while True:
            print(f"""Please, choise operation:
1. Create ready vector.
2. Create ready matrix.
3. Create zero matrix(size = 4,5)
4. Create single matrix (size = 3,3)
5. Show size of matrix on 2-nd step.
6. Create matrix A and B. Execute operation.
7. Matrix(A, B) multiplication.
8. Const b for matrix A.
9. Matrix(no name) multiplication.
10. Euclidean norm.
11. Vector slice.
0. Exit""")
            while True:
                try:
                    operation = int(input(f"User: "))
                    break
                except ValueError:
                    print("Please, input the number.")

            match operation:
                case 1:
                    self.vector()
                case 2:
                    self.matrix()
                case 3:
                    self.zero_matrix()
                case 4:
                    self.identity_matrix()
                case 5:
                    self.size_matrix()
                case 6:
                    self.two_matrix()
                case 7:
                    self.multiplication()
                case 8:
                    self.const_and_matrix()
                case 9:
                    self.multiplication_no_name()
                case 10:
                    self.euclidean_norm()
                case 11:
                    self.vector_slice()
                case 0:
                    exit()


start = matrix_processing()
start.start_menu()
