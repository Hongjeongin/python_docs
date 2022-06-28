# programmers skill test Level.1 

def solution(arr1, arr2):
    answer_col = len(arr1[0])
    answer = []
    for x in range(len(arr1)):
        answer += [[0]* answer_col]
        for y in range(len(arr1[x])):
            answer[x][y] =  arr1[x][y] + arr2[x][y]
    return answer

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]

answer = solution(arr1, arr2)

print(answer)
