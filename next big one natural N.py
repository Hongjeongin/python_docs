def solution(n):
    answer = 0
    num = n
    number_of_one = 0
    
    binaryNum = []

    i = n + 1

    while True:
        if num % 2 == 1:
            number_of_one = number_of_one + 1
        binaryNum.insert(0, num % 2)
        if num <= 1:
            break
        num = num // 2
    
    while i <= 1000001:
        next_num = i
        next_num_of_one = 0
        binaryN = []
        while True:
            if next_num % 2 == 1:
                next_num_of_one = next_num_of_one + 1
            binaryN.insert(0, next_num % 2)
            if next_num <= 1:
                break
            next_num = next_num // 2
        if number_of_one == next_num_of_one:
            answer = i
            break
        i = i + 1
    
    return answer

print(solution(4096))
