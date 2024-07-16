# 1부터 100까지 수를 2의 배수, 3의 배수, 5의 배수로 분류하려고 한다.
# 2의 배수는 numbers_1 리스트에,
# 3의 배수는 numbers_2 리스트에,
# 5의 배수는 numbers_3 리스트에 저장하는 코드를 작성하시오.
n = []
n_2 = []
n_3 = []
for i in range(1, 101):
    if i % 2 == 0:
        n.append(i)
    if i % 3 == 0:
        n_2.append(i)
    if i % 5 == 0:
        n_3.append(i)
print(n)
print(n_2)
print(n_3)


