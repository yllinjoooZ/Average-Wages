salary = [340, 210, 450, 600, 230, 500, 550, 300]
shumaEpagave = 0
for paga in salary:
    shumaEpagave = shumaEpagave + paga 
print(f"Shuma e pagave eshte: {shumaEpagave}")
    
pagaMesatare = shumaEpagave / len(salary)
print(pagaMesatare)

pagaMax = salary[0]
for pagaAktuale in salary:
    if(pagaAktuale > pagaMax):
        pagaMax = pagaAktuale
        print(f"Paga maksimale eshte (pagaMax)")