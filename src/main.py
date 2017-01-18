from extract import extractCsv, attackTypes, fields
from sklearn import tree
import pydotplus

''' --- Sample extraction from the training dataset --- '''

print("Extracting connection records from data.csv")
samples = extractCsv("data.csv")
print(str(len(samples)) + " connection records extracted")

X = [] # Contains the training samples
Y = [] # Contains their classes

protocole=[] #contain all the protocole type
service=[]   #contain all the services
flag=[]		#contain all the flags

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
        	if i[0]=="protocol_type":
        		if i[1] not in protocole:
        			protocole.append(i[1])
        		line.append(protocole.index(i[1]))
        	elif i[0]=="service":
        		if i[1] not in service:
        			service.append(i[1])
        		line.append(service.index(i[1]))
        	elif i[0]=="flag":
        		if i[1] not in flag:
        			flag.append(i[1])
        		line.append(flag.index(i[1]))
        	else :
        		line.append(i[1])
        else:
            Y.append(attackTypes.index(i[1]))
    X.append(line)

''' --- Training of the decision tree --- '''

classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(X, Y)

''' --- Visualisation --- '''

dotData = tree.export_graphviz(classifier, out_file=None, class_names=attackTypes, feature_names=fields)
graph = pydotplus.graph_from_dot_data(dotData)
graph.write_pdf("attacks.pdf")
