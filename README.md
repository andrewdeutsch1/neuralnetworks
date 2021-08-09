# Optimizing Neural Networks for Next-Gen AI

## Background
All of the code provided, with the exception of the 'resources' folder, was developed during my time in the SULI program at Brookhaven National Laboratory. I would like to give special thanks to Yihui "Ray" Ren and Sandeep Mittal for their assistance. At the time of writing this, I am a senior physics student at Stevens Institute of Technology. 

Andrew Deutsch

## Abstract
Most scientific data challenges involve real-time decision making on high-volume data flows. Deep Neural Networks (DNNs) and Convolutional Neural Networks (CNNs) have been promising solutions for many challenging problems, but are limited to training and evaluation in an offline manner on a Graphics Processing Unit (GPU). In this work, we aim to transform pre-trained DNNs and CNNs into Spiking Neural Networks (SNNs), a better, biologically inspired form that can be implemented and deployed on novel hardware. Unlike discrete matrix multiplication based DNNs, an SNN acts on continuous trains of signals. First, we investigate the sparsity nature of DNNs, pruning techniques, and their connections to SNNs. We then investigate DNN to SNN conversion using NengoDL, an existing framework based on TensorFlow. Specifically, we optimize the accuracy of converted models by properly scaling the firing rates of neurons and applying a lowpass filter over the spike trains. We systematically run these experiments using the popular benchmark image datasets MNIST and CIFAR-10. For further optimization, we limit scaling of firing rates to only one layer and we find evidence that scaling late layers in a converted DNN and early layers in a converted CNN leads to higher accuracy. Further, we investigate the cause of this discrepancy by extracting firing rate data from both networks. Our findings provide insight into the co-design of novel energy-efficient neuromorphic chips for SNNs.

## Outline
### nengo_examples
The project began with an exploration of the Nengo framework, including the NengoGUI. Files concerning these initial steps can be found in the 'nengo_examples' folder.

### network_pruning and preprocessing_techniques
We then explore network pruning and preprocessing techniques to reduce size and tackle overfitting problems. Files concerning these experiments can be found in the 'network_pruning' and 'preprocessing_techniques' folders. We find that a simple CNN can be reduced by up to 80% before the training accuracy on MNIST begins to fall after 20 epochs.

### synapse_and_scaling
The NengoDL framework comes equipped with two important paraments involved in the conversion of non-spiking to spiking networks. These are 'synapse' and 'scale_firing_rates'. In the 'synapse_and_scaling' folder, we explore the 2-dimensional optimization problem posed by these parameters for three simple networks. We find that there exists an optimal value for 'synapse' for each network architecture and that 'scale_firing_rates' increases accuracy of the SNN directly, but consequently requires more computations.

### scaling_early_and_late
For further optimization, we explore the effects of scaling only certain layers (individually and in pairs) so as to reduce the total amount of computations required while maintaining a good level of accuracy. Files concerning this analysis can be found in the 'scaling_early_and_late' folder.

### spiking_rates
To explain the results found in 'scaling_early_and_late', we directly probe the firing rates of neurons in the models using Nengo's Probe class. We observe the follwing correspondence: scaling of firing rates is more beneficial in layers which are statistically firing at lower rates.

## Future Work
The networks experimented on are generally quite small. Deeper architectures with residual connections have demonstrated superior results. In future work, these same tests may be ran on more advanced networks and the results may be compared.
