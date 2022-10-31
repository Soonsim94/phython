score = [10,5,5]

total = 0
for s in score:
    total += s
print('합계', total)


#최소,최대값구할때는 배열의 첫번째값을 첫번째 값으로 넣어준다.
maxScore = score[0]
minScore = score[0]

for s in score:
    if s > maxScore:
        maxScore = s
    if s < minScore:
        minScore = s
print('최대', maxScore)
print('최소', minScore)


