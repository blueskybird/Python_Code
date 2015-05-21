from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import TanhLayer
from pybrain.structure import SoftmaxLayer
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets import SupervisedDataSet

net = buildNetwork(2, 3, 1)
net1 = buildNetwork(2, 3, 1, hiddenclass=TanhLayer)
net2 = buildNetwork(2, 3, 2, hiddenclass=TanhLayer, outclass=SoftmaxLayer)
net4 = buildNetwork(2, 3, 1, bias=True, hiddenclass=TanhLayer)

ds = SupervisedDataSet(2, 1)

ds.addSample((0, 0), (0,))
ds.addSample((0, 1), (1,))
ds.addSample((1, 0), (1,))
ds.addSample((1, 1), (0,))

print ds['input']

trainer = BackpropTrainer(net4,ds)

print trainer.train()
print trainer.trainUntilConvergence()