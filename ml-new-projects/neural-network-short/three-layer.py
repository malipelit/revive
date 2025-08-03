import numpy as np

# sigmoid function
def sigmoid(x, slope=False):
    if(slope==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))

# input : 3 input variables
X = np.array([  [0,0,1],
                [0,1,1],
                [1,0,1],
                [1,1,1]     ])

# output (target) :1 output variable
y = np.array([  [0],
                [1],
                [1],
                [0] ])

# use a fix seed
np.random.seed(1)

# synapsis weights:  3 input, 1 output, zero mean
#                    learning is stored in synapsis matrix
syn0 = 2*np.random.random((3,4)) - 1
syn1 = 2*np.random.random((4,1)) - 1

for iter in range(60000):
    # forward propagation
    l0 = X
    l1 = sigmoid(np.dot(l0,syn0))
    l2 = sigmoid(np.dot(l1,syn1))

    # error calculation
    l2_error = y - l2

    # update calculations
    l2_delta = l2_error * sigmoid(l2,True)

    l1_error = l2_delta.dot(syn1.T)

    l1_delta = l1_error * sigmoid(l1,True)

    # update weights
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)
    
    if iter%10000 == 0:
        # print("iter", iter, ":")
        print("Error:" + str(np.mean(np.abs(l2_error))))
        # print(l1)
        # print(l2_error)
        # print(syn0)

print("Output After Training:")
print(l2)
