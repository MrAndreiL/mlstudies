def stepTransfer(activation: float) -> int:
    """
    Applies linear step function transfer.

    Input:
        activation: float value representing activation
    of a linear equation.

    Returns:
        Step function boolean result.
    """
    return 1 if activation >= 0.0 else 0


def predict(inputs, weights, bias):
    """
    Computes linear equation and returns prediction result.

    Input:
        inputs:  perceptron input values.
        weights: corresponding weights for each input value.
        bias:    linear equation free term.

    Returns:
        Perceptron boolean prediction value.
    """
    linEq = 0.0
    for i in range(len(inputs)):
        linEq += (weights[i] * inputs[i])
    linEq += bias

    return stepTransfer(linEq)


# test predictions from the sonar dataset.
dataset = [[2.7810836, 2.550537003, 0],
           [1.465489372, 2.362125076, 0],
           [3.396561688, 4.400293529, 0],
           [1.38807019, 1.850220317, 0],
           [3.06407232, 3.005305973, 0],
           [7.627531214, 2.759262235, 1],
           [5.332441248, 2.088626775, 1],
           [6.922596716, 1.77106367, 1],
           [8.675418651, -0.242068655, 1],
           [7.673756466, 3.508563011, 1]]


# Set up ideal weights and bias values.
bias = -0.1
weights = [0.20653640140000007, -0.23418117710000003]

for inputRow in dataset:
    y = inputRow[-1]
    x = inputRow[:2]
    prediction = predict(x, weights, bias)
    print(f"Expected={y}, Predicted={prediction}")
