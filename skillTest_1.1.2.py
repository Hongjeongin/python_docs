def solution(numbers):
    answer = []
    length = len(numbers)

    for j in range(length):
        for i in range(j + 1,length):
            number = numbers[j] + numbers[i]
            if number in answer:
                continue
            else:
                answer +=[number]
            print(answer)
    answer.sort()
    return answer

print(solution([5, 0, 2, 7]))
