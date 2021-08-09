# the significance of this is to show that with
# relative simplicity a recurrent SNN can simulate
# differential equations

import nengo

# seed changes initial randomly generated neurons
model = nengo.Network(seed=5)
with model:
    
    x = nengo.Ensemble(n_neurons=100, dimensions=3,
                        radius=30)
    
    synapse = 0.1
    
    def lorenz(x):
        sigma = 10
        beta = 8.0/3
        rho = 28
        
        dx0 = -sigma * x[0] + sigma * x[1]
        dx1 = -x[0] * x[2] - x[1]
        dx2 = x[0] * x[1] - beta * (x[2] + rho) - rho
        
        return [dx0 * synapse + x[0],
                dx1 * synapse + x[1],
                dx2 * synapse + x[2]]
        
    nengo.Connection(x, x, synapse=synapse,
                    function=lorenz)