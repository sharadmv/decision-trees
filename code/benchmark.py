from classifier import * 
from scipy.io import loadmat

d = DecisionTree({
    'depth' : 7,
})

r = RandomForest(parameters={
    'trees' : 200,
    'samples' : 400,
    'depth' : 30,
    'features' : 5 
})

a = AdaBoost(parameters={
    'iterations' : 20,
    'depth' : 2,
})

print("Loading data")
data = loadmat('spamData.mat')
x = data['Xtrain']
y = data['ytrain']
c = Collection(x, y)

xtest = data['Xtest']
ytest = data['ytest']

t = Collection(xtest, ytest)

def benchmark(classifier):
    classifier.train(c)
    print("Training Error rate: %f" % classifier.test(c))
    print("Testing Error rate: %f" % classifier.test(t))

print("Training Decision Tree")
benchmark(d)
print("Training Random Forest")
benchmark(r)
print("Training AdaBoost")
benchmark(r)
