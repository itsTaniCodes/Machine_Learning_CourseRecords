import numpy as np

def gradient_descent(x, y):
    m_curr = 0
    b_curr = 0
    iterations = 10000
    n = len(x)
    learning_rate = 0.01

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1 / n) * sum((y - y_predicted) ** 2)
        md = -(2 / n) * sum(x * (y - y_predicted))
        bd = -(2 / n) * sum(y - y_predicted)

        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd

        
        print("Iteration " + str(i) + ": m=" + str(m_curr) + ", b=" + str(b_curr) + ", cost=" + str(cost))

    return m_curr, b_curr


x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])

m, b = gradient_descent(x, y)
print(m)
print(b)
