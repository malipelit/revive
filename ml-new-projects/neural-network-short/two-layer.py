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
y = np.array([  [1,0,0,0]   ]).T

# use a fix seed
np.random.seed(1)

# synapsis weights:  3 input, 1 output, zero mean
#                    learning is stored in synapsis matrix
syn0 = 2*np.random.random((3,1)) - 1

l1_list = []
l1_error_list = []
syn0_list = []
for iter in range(10000):
    # forward propagation
    l0 = X
    l1 = sigmoid(np.dot(l0,syn0))

    # error calculation
    l1_error = y - l1

    # update calculation
    l1_delta = l1_error * sigmoid(l1,True)

    # update weights
    syn0 += np.dot(l0.T,l1_delta)

    if iter%2000 == 0:
        # print("iter", iter, ":")
        print("Error:" + str(np.mean(np.abs(l1_error))))
        # print(l1)
        # print(l2_error)
        # print(syn0)

print("Output After Training:")
print(l1)