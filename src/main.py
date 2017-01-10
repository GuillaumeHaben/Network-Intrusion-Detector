from extract import extractCsv

samples = extractCsv("data.csv")
print(str(len(samples)) + " connection records extracted")
print("First sample:")
for i in samples[0].items():
    print(i)
