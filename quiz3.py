# 다음 이중 리스트의 평균값을 아래 출력 결과와 같이 각각 구하여라.

m = [[100, 200], [400, 800], [1000, 1400]]

for i in m:
    data = 0
    for a in i:
        data = data + a
    print(data/2)

# for i in m:
#     for a in i:
#         print(a)