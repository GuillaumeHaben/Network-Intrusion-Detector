from extract import extractCsv

samples = extractCsv("data.csv")
print(str(len(samples)) + " connection records extracted")
print("First sample:")
X = []
for j in samples:
	line = []
	for i in j.items():
		if i[0] != "attack_type":
			line.append(i[1])
	X.append(line)

print X[1]