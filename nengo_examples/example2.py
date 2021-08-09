# a simple network consisting of two layers (Ensembles) which demonstrates
# input response and the synapse parameter

import nengo

model = nengo.Network()
with model:
    
    a = nengo.Ensemble(n_neurons=200, dimensions=1)
    b = nengo.Ensemble(n_neurons=200, dimensions=1,
                       radius=1)
    
    stim = nengo.Node(0)

    nengo.Connection(stim, a)
    nengo.Connection(a, b, synapse=0.050)
    
    def recurrent_func(x):
        return x**2
    
    # we introduce recurrent feedback and find that
    # this system has memory!
    nengo.Connection(b, b, function=recurrent_func)