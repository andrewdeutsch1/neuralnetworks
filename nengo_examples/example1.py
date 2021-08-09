# demonstrating how we can model some arbitrary
# function with a set of neurons

import nengo

model = nengo.Network()
with model:
    
    # create ensembles of neurons
    a = nengo.Ensemble(n_neurons=4, dimensions=1)
    #b = nengo.Ensemble(n_neurons=1, dimensions=1)
    
    # create input stimulus
    stim = nengo.Node(0)
    
    def square(x):
        return x**2
    
    def Heaviside(x):
        if x<0:
            return 0
        else:
            return 1
    
    # nengo will find the best weight matrix between
    # a and b to approximate this function
    nengo.Connection(stim, a)
    #nengo.Connection(a, b, function=Heaviside)