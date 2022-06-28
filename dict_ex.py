# this file is dictionary exercise
dict_rsp = {
    '가위':'보',
    '바위':'가위',
    '보':'바위',
    }

dict_result = {
    'win':'이겼다~~',
    'draw':'비겼다..!',
    'lose':'졌다...',
    'err':'이상한 값을 입력했어요!'
    }

def rsp(mine, yours):
    if mine == yours:
        return 'draw'
    elif dict_rsp[mine] == yours:
        return 'win'
    elif dict_rsp[yours] == mine:
        return 'lose'

print(dict_result[rsp('보', '가위')])
