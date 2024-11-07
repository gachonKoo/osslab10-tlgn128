import sys

# 커맨드 라인 인수로 전달된 숫자 받기
number = int(sys.argv[1])

# 주어진 숫자의 약수 찾기
for i in range(1, number + 1):
    if number % i == 0:
        print(i, end=" ")

print()
