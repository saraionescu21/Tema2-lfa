dictionar={
      "S":["aA","dE"],
      "A":["aB","aS"],
      "B":["bC"],
      "C":["bD","bB"],
      "D":["cD","$"],
      "E":["$"]
      }

cuvant=[]

for caracter in dictionar["S"]:
    cuvant.append(caracter)
print(cuvant)

n=int(input("n="))

for i in range(n-1):
    cuvant2=[]
    for caracter in cuvant:
        if caracter[-1] != "$":
            for caracter2 in dictionar[caracter[-1]]:
                 cuvant2.append(caracter[:-1]+caracter2)
    cuvant=cuvant2
final=[]
for chei in dictionar:
    if "$" in dictionar[chei]:
        final.append(chei)

for caracter in cuvant:
    if caracter[-1] in final:
        print(caracter[:-1])