import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
import numpy as np


class linear_regression:
    def __init__(self):
        self.X, self.Y = make_regression(n_samples=300, n_features=1, n_informative=1, noise=5, random_state=10)
        self.linear_regression_manual()
        self.liner_regression_encapsulated()

    def linear_regression_manual(self):
        """Linear regression detail"""

        N = len(self.X)

        alpha1 = np.sum(self.X * self.Y) / N
        alpha2 = np.sum(self.X ** 2) / N

        m_x = np.mean(self.X)
        m_y = np.mean(self.Y)

        w1 = (alpha1 - m_x * m_y) / (alpha2 - m_x ** 2)
        w0 = m_y - w1 * m_x

        print(f"Linear regression (manual):\nw0 = {w0};\nw1 = {w1}\n")

        y_pred_manual = w0 + w1 * self.X

        plt.scatter(self.X, self.Y)
        plt.plot(self.X, y_pred_manual, color="r")
        plt.xlabel("features")
        plt.ylabel("target")
        plt.show()

    def liner_regression_encapsulated(self):
        """Liner regression encapsulated"""

        model_lr = LinearRegression()

        model_lr.fit(self.X, self.Y)

        w0 = model_lr.intercept_
        w1 = model_lr.coef_

        print(f"Linear regression (encapsulated):\nw0 = {w0};\nw1 = {w1}")

        y_pred = model_lr.predict(self.X)

        plt.scatter(self.X, self.Y)
        plt.plot(self.X, y_pred, color="r")
        plt.xlabel("features")
        plt.ylabel("target")
        plt.show()


if __name__ == "__main__":
    start = linear_regression()
