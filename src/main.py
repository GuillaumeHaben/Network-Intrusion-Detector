from extract import extractCsv, attackTypes
from sklearn import tree
import pydotplus

''' --- Sample extraction from the training dataset --- '''

print("Extracting connection records from data.csv")
samples = extractCsv("data.csv")
print(str(len(samples)) + " connection records extracted")

X = [] # Contains the training samples
Y = [] # Contains their classes

''' TODO

Index of the following parameters:
  - protocol_type
  - service
  - flag

Could be done dynamically while building X
'''

for j in samples:
    line = []
    for i in j.items():
        if i[0] != "attack_type":
            line.append(i[1])
        else:
            Y.append(attackTypes.index(i[1]))
    X.append(line)

''' --- Training of the decision tree --- '''

classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(X, Y)

''' --- Visualisation --- '''

dotData = tree.export_graphviz(classifier, out_file=None)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf("attacks.pdf")

