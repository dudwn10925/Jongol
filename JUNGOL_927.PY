import numpy as np
scores = [list(map(int, input().split())) for _ in range(5)]
cnt = 0
for i in range(len(scores)):
    # mean_score = sum(scores[i]) / len(scores[i])
    mean_score = np.mean(scores[i])
    if mean_score >= 80:
        print('pass')
        cnt += 1
    else:
        print('fail')
print(f'Successful : {cnt}')