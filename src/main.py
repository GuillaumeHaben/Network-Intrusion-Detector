from extract import extractCsv, attackTypes, fields
from sklearn import tree
import pydotplus

''' --- Sample extraction from the training dataset --- '''

print("Extracting connection records from training data")
trainingSamples = extractCsv("../data/kddcup.data_10_percent_corrected")
print(str(len(trainingSamples)) + " connection records extracted")
print("Extracting connection records from target data")
targetSamples = extractCsv("../data/kddcup.data_10_percent_corrected")
print(str(len(targetSamples)) + " connection records extracted")

X = [] # Contains the training samples
Y = [] # Contains their classes

protocols = [] # Contains the different protocols
services = [] # Contain the different services
flags = [] # Contains the different flags

print("Formatting training samples for the decision tree")
for j in trainingSamples:
    line = []
    for i in j.items():
        if i[0] != "attack_type":
        	if i[0]=="protocol_type":
        		if i[1] not in protocols:
        			protocols.append(i[1])
        		line.append(protocols.index(i[1]))
        	elif i[0]=="service":
        		if i[1] not in services:
        			services.append(i[1])
        		line.append(services.index(i[1]))
        	elif i[0]=="flag":
        		if i[1] not in flags:
        			flags.append(i[1])
        		line.append(flags.index(i[1]))
        	else :
        		line.append(i[1])
        else:
            Y.append(attackTypes.index(i[1]))
    X.append(line)
print("Done")

data = [] # Contains the target samples
answers = [] # Contains the class to predict

print("Formatting target samples for the decision tree")
for j in targetSamples:
    line = []
    for i in j.items():
        if i[0] != "attack_type":
        	if i[0]=="protocol_type":
        		line.append(protocols.index(i[1]))
        	elif i[0]=="service":
        		line.append(services.index(i[1]))
        	elif i[0]=="flag":
        		line.append(flags.index(i[1]))
        	else :
        		line.append(i[1])
        else:
            answers.append(attackTypes.index(i[1]))
    data.append(line)
print("Done")

''' --- Main test loop --- '''

for i in range(1,6):

    ''' --- Training of the decision tree --- '''

    minImpurity = i/50
    print("Minimal impurity setting: " + str(minImpurity))
    classifier = tree.DecisionTreeClassifier(min_impurity_split = minImpurity)
    classifier = classifier.fit(X, Y)

    ''' --- Visualisation --- '''

    dotData = tree.export_graphviz(classifier, out_file=None, class_names=attackTypes, feature_names=fields)
    graph = pydotplus.graph_from_dot_data(dotData)
    graph.write_pdf("attacks_" + str(minImpurity) + ".pdf")
    print("PDF file generated")

    ''' --- Prediction --- '''

    predictions = classifier.predict(data)
    good = 0
    bad = 0
    for i in range(len(predictions)):
        if predictions[i] == answers[i]:
            good += 1
        else:
            bad +=1
    errorRate = bad / (good + bad)
    print("Error rate: " + str(errorRate))
