# 경우의 수 = n!
# 모든 경우의 수 다 포함한 배열 만들기
# quick 정렬로 오름차순 정렬
# 가장 마지막 값 뽑기

from itertools import *

def solution(numbers):
    
    answer = ''

    length = 1
    columns = len(numbers)
    rows = len(numbers)
    for i in range(1, rows + 1):
        length *= i

    num_list = list(permutations(numbers, rows))

    print(num_list)
    print(columns)

    hi = 0
    for i in range(columns):
        hi += num_list[0][i]

    num = "{}".format(num_list[0])

    print(num)
    a = ' '.join(num_list[0])
    print(a)

    
    return answer

print(solution([6, 10, 2]))
