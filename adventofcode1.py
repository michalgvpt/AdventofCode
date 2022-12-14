fr=open('texts/adventofcode1.txt','r', encoding='UTF-8')

max_elf=0
elf=0
total=[ ]
for row in fr:
    temp=row.strip()
    if temp.isdigit():
        elf+=int(temp)
    else:
        if elf>max_elf:
            max_elf=elf
        total.append(elf)
        elf=0

sort=sorted(total, reverse=True)
print(sum(sort[:3:]))

