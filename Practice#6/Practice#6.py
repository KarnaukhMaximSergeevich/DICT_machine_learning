import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression


class gradient_descent:
    def __init__(self):
        self.X, self.y = make_regression(n_samples=300, n_features=1, n_informative=1, noise=10, random_state=5)
        self.gradient_descent_manual()
        self.gradient_descent_encapsulated()

    def gradient_descent_manual(self):
        """Gradient descent manual"""

        N = len(self.X)

        W1 = 0
        W0 = 0

        n_iteration = 100
        learning_rate = 0.1
        min_weight_change = 0.0001

        def MSE_func():
            MSE = np.sum((self.y - y_pred) ** 2) / (N)
            return MSE

        def W1_grad():
            """Gradient W1"""

            W1_gradient = np.sum((self.y - y_pred) * (-self.X[:, 0])) * (2 / N)
            return W1_gradient

        def W0_grad():
            """Gradient W0"""

            W0_gradient = np.sum((self.y - y_pred) * (-1)) * (2 / N)
            return W0_gradient

        next_W1 = W1
        next_W0 = W0

        for iteration in range(n_iteration):
            cur_W1 = next_W1
            cur_W0 = next_W0

            y_pred = cur_W1 * self.X[:, 0] + cur_W0

            next_W1 = cur_W1 - learning_rate * W1_grad()
            next_W0 = cur_W0 - learning_rate * W0_grad()

            if abs(cur_W1 - next_W1) <= min_weight_change and (abs(cur_W0 - next_W0) <= min_weight_change):
                break

        print(f"Manual\nW1(coef) = {cur_W1}\nW0(intercept) = {cur_W0}")

    def gradient_descent_encapsulated(self):
        """Gradient descent encapsulated"""

        model_n = LinearRegression()

        model_n.fit(self.X, self.y)

        print(f"\nEncapsulated\nW1(coef) = {model_n.coef_}\nW0(intercept) = {model_n.intercept_}")


if __name__ == "__main__":
    gd_class = gradient_descent()
