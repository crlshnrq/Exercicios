import re

numGrupos = int(input())

for i in range(numGrupos):
    luzes = int(input())
    luzes = bin(luzes)
    luzesRegex = re.compile(r'(?:1)+')
    luzSeq = luzesRegex.findall(luzes)
    if not luzSeq:
        print(0)
    else:
        print(len(max(luzSeq)))
