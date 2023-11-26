import numpy
import numpy as np
from sklearn import linear_model
from matplotlib import pyplot as plt

# X represents the size of a tumor in centimeters.
X = numpy.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88])
# Note: X has to be reshaped into a column from a row for the LogisticRegression() function to work.
X = X.reshape(-1, 1)
# y represents whether the tumor is cancerous (0 for "No", 1 for "Yes").
y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

logr = linear_model.LogisticRegression()
logr.fit(X, y)

# predict if tumor is cancerous where the size is 3.46mm:
predicted = logr.predict(numpy.array([3.46]).reshape(-1, 1))
print(predicted)

log_odds = logr.coef_
odds = numpy.exp(log_odds)

print(odds)


def fun(x):
    w = logr.coef_
    b = logr.intercept_
    z = w * x + b
    return 1 / (1 + np.exp(-z))


def logit2prob(logr, x):
    log_odds = logr.coef_ * x + logr.intercept_
    odds = numpy.exp(log_odds)
    probability = odds / (1 + odds)
    return probability


def rr(x):
    return fun(x) / 1 - fun(x)


print(logit2prob(logr, X))

X = X.reshape(1, -1)
arr = np.linspace(X.min(), X.max(), 50)

model = logit2prob(logr, arr)
f_mod = fun(arr)
rr=rr(arr)
print(model)
print(f_mod)

plt.scatter(X, y)
plt.plot(arr, model[0])
plt.plot(arr, f_mod[0])
plt.plot(arr, rr[0])
plt.xlabel("Size of tumor")
plt.ylabel("Probability of being malignant")
plt.title('Probability')
plt.show()
