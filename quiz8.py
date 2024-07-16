# while문을 사용하여 1부터 45 사이에 중복이 없는 랜덤한 수 6개 생성
# 이를 result 리스트 변수에 추가하는 코드를 작성

import random
result = []
i = 0
while i <= 6 :
    i = i + 1
    n_num = random.randint(1, 45)
    if n_num in result:
        print("값이 기존에 있습니다.")
    else:
        result.append(n_num)
print(result)
