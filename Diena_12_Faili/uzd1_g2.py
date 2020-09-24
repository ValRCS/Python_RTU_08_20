# Nauris
import requests

melnraksts = requests.get(
    "https://raw.githubusercontent.com/ValRCS/Python_RTU_08_20/master/data/veidenbaums.txt").text.split('\n')
veidenbaums = []
titles = []
for line in melnraksts:
    if len(line) > 1:
        veidenbaums.append(line)
        if line[-3:] == '***':
            titles.append(veidenbaums.index(line))

with open('Veidenbauma Dzeja.txt', 'w', encoding='utf-8') as f:
    for line in veidenbaums:
        f.write(line + '\r')

with open('veidenbaums.txt', 'w', encoding='utf-8') as f:
    for line in melnraksts:
        f.write(line + '\r')

print('Iekļautie Vedenbauma dzejoļi:')
for i in titles:
    print(' * ' + veidenbaums[i][:-3])

melnraksts = []
veidenbaums = []
titles = []
