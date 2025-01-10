n = int(input())
haab = ['pop', 'no', 'zip', 'zotz', 'tzec', 'xul', 'yoxkin', 'mol', 'chen', 'yax', 'zac', 'ceh', 'mac', 'kankin',
        'muan', 'pax', 'koyab', 'cumhu', 'uayet']
tzo = ['imix', 'ik', 'akbal', 'kan', 'chicchan', 'cimi', 'manik', 'lamat', 'muluk', 'ok', 'chuen', 'eb', 'ben', 'ix',
       'mem', 'cib', 'caban', 'eznab', 'canac', 'ahau']

results = []

for i in range(n):
    date = input().split()
    d1 = int(date[0].replace('.', '')) + 1
    m1 = haab.index(date[1]) + 1
    y1 = int(date[2])

    d2 = m1 * 20 - 20
    d3 = y1 * 365
    d = d1 + d2 + d3

    y2 = d // 260
    m2 = (d - y2 * 260) % 20
    d2_ = (d - y2 * 260) % 13
    if d2_ == 0:
        d2_ = 13
        if m2==0:
            y2 -= 1
    results.append(f"{d2_} {tzo[m2-1]} {y2}")

# 输出所有结果
print(n)
for result in results:
    print(result)


