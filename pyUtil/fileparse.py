import pickle, json

clean = list()
f = open("RpackageNames")
lines = f.readlines()
for line in lines:
  line = line.split()[1]
  line = line.replace('"','')
  clean.append(line)

with open("RpackNames.pkl", "wb") as f:  #Pickling
    pickle.dump(clean, f)

with open("RpackNames.pkl", "rb") as f: # Unpickling
    b = pickle.load(f)
    j = json.dumps(b)
    text_file = open("RpackNames.txt", "w")
    text_file.write("var packList = %s" % j)
    text_file.close()
