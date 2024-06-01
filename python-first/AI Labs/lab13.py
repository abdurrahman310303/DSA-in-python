import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target.reshape(-1, 1)

# One-hot encode the target variable
encoder = OneHotEncoder(sparse_output=False)
y = encoder.fit_transform(y)

# Normalize the feature data
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Neural Network architecture parameters
input_size = X.shape[1]
hidden_size = 10
output_size = y.shape[1]

# Initialize weights and biases
np.random.seed(42)
W1 = np.random.randn(input_size, hidden_size) * 0.01
b1 = np.zeros((1, hidden_size))
W2 = np.random.randn(hidden_size, output_size) * 0.01
b2 = np.zeros((1, output_size))

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def sigmoid_derivative(z):
    return z * (1 - z)

def forward_propagation(X, W1, b1, W2, b2):
    Z1 = np.dot(X, W1) + b1
    A1 = sigmoid(Z1)
    Z2 = np.dot(A1, W2) + b2
    A2 = sigmoid(Z2)
    return Z1, A1, Z2, A2

def backpropagation(X, y, Z1, A1, Z2, A2, W1, W2, b1, b2, learning_rate=0.01):
    m = X.shape[0]

    dZ2 = A2 - y
    dW2 = np.dot(A1.T, dZ2) / m
    db2 = np.sum(dZ2, axis=0, keepdims=True) / m

    dZ1 = np.dot(dZ2, W2.T) * sigmoid_derivative(A1)
    dW1 = np.dot(X.T, dZ1) / m
    db1 = np.sum(dZ1, axis=0, keepdims=True) / m

    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1
    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2

    return W1, b1, W2, b2

def train_neural_network(X_train, y_train, W1, b1, W2, b2, epochs=1000, learning_rate=0.01):
    for i in range(epochs):
        Z1, A1, Z2, A2 = forward_propagation(X_train, W1, b1, W2, b2)
        W1, b1, W2, b2 = backpropagation(X_train, y_train, Z1, A1, Z2, A2, W1, W2, b1, b2, learning_rate)
        if i % 100 == 0:
            loss = np.mean(np.square(y_train - A2))
            print(f'Epoch {i}, Loss: {loss:.4f}')
    return W1, b1, W2, b2

# Train the neural network
W1, b1, W2, b2 = train_neural_network(X_train, y_train, W1, b1, W2, b2, epochs=1000, learning_rate=0.01)



def predict(X, W1, b1, W2, b2):
    _, _, _, A2 = forward_propagation(X, W1, b1, W2, b2)
    return np.argmax(A2, axis=1)

# Predict on test data
y_pred = predict(X_test, W1, b1, W2, b2)
y_test_labels = np.argmax(y_test, axis=1)

# Calculate accuracy
accuracy = np.mean(y_pred == y_test_labels)
print(f'Accuracy: {accuracy:.4f}')
