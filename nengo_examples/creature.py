# in this example we use several ensembles of neurons
# to model the position of a creature, position of food,
# along with a motor to control motion

import nengo

model = nengo.Network()
with model:
    stim_food = nengo.Node([0,0])
    food = nengo.Ensemble(n_neurons=100, dimensions=2)
    nengo.Connection(stim_food, food)
    
    motor = nengo.Ensemble(n_neurons=200, dimensions=2)
    
    stim_scared = nengo.Node(-1)
    scared = nengo.Ensemble(n_neurons=50, dimensions=1)
    nengo.Connection(stim_scared, scared)
    
    pos = nengo.Ensemble(n_neurons=500, dimensions=2, 
                         radius=5)
    nengo.Connection(pos, pos, synapse=0.1)
    
    nengo.Connection(motor, pos, transform=0.1, synapse=0.1)
    
    # Setting neuron_type to nengo.Direct() is mostly for
    # debugging purposes (it computes directly instead of using
    # the neural network at all)
    do_food = nengo.Ensemble(n_neurons=300, dimensions=3, radius=1.4)
                             
    nengo.Connection(scared, do_food[0])
    nengo.Connection(food, do_food[1:])
    def do_food_function(x):
        scared, food_x, food_y = x
        if scared > 0:
            return 0, 0
        else:
            return food_x, food_y
    
    nengo.Connection(do_food, motor, function=do_food_function)

    do_home = nengo.Ensemble(n_neurons=300, dimensions=3, radius=1.4)
    
    
    nengo.Connection(scared, do_home[0])
    nengo.Connection(pos, do_home[1:])
    def do_home_function(x):
        scared, pos_x, pos_y = x
        if scared > 0:
            return -pos_x, -pos_y
        else:
            return 0, 0
    nengo.Connection(do_home, motor, function=do_home_function)