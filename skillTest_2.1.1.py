def solution(record):
    answer = []
    answer_clone = []
    users = []

    user = ""
    command = ""
    nick = ""
    
    #for i in record_length:
    for i in record:
        passing = i.split(" ")
        #command = record[i].split(" ")[0]
        command = passing[0]
        user = passing[1]
        #user = record[i].split(" ")[1]
        user_len = range(len(users))
        clone_length = range(len(answer_clone))
        if command == "Leave":
            for p in user_len:
                if user == users[p][0]:
                    answer += [users[p][1]+ "님이 나갔습니다."]
                    answer_clone += [[user, users[p][1], command]]
        elif command == "Enter":
            #nick = record[i].split(" ")[2]
            nick = passing[2]
            
            for j in clone_length:
                if user == answer_clone[j][0]:
                    if answer_clone[j][2] == "Enter":
                        answer[j] = nick+"님이 들어왔습니다."
                    elif answer_clone[j][2] == "Leave":
                        answer[j] = nick+"님이 나갔습니다."
            answer += [nick+ "님이 들어왔습니다."]
            answer_clone += [[user, nick, command]]
            for m in user_len:
                if user != users[m][0]:
                    users += [[user, nick]]
                    break;
#            if users == []:
#                users += [[user, nick]]
#                answer += [nick+ "님이 들어왔습니다."]
#                answer_clone += [[nick, user, command]]
#            elif user not in user_df["user"]:
##                print("hello")
  #              print([user], "@@")
  #              print(users,"##")
  #              users += [[user, nick]]
  #              answer += [nick+ "님이 들어왔습니다."]
  #              answer_clone += [[nick, user, command]]
  #          else:
  #              for o in clone_length:
  #                  if user == answer_clone[o][1]:
  #                      if nick == answer_clone[o][0]:
  ####                          break;
   #                     if answer_clone[o][2] == "Enter":
   #                         answer[o] = nick+"님이 들어왔습니다."
   #                     elif answer_clone[o][2] == "Leave":
   #                         answer[o] = nick+"님이 나갔습니다."
   #                     answer_clone[o][0] = nick
   #             answer += [nick+ "님이 들어왔습니다."]
   #             answer_clone += [[nick, user, command]]
   #             
        else:
            #nick = record[i].split(" ")[2]
            nick = passing[2]
            for k in clone_length:
                if user == answer_clone[k][0]:
                    if answer_clone[k][2] == "Enter":
                        answer[k] = nick+"님이 들어왔습니다."
                    elif answer_clone[k][2] == "Leave":
                        answer[k] = nick+"님이 나갔습니다."
                answer_clone[k][1] = nick
    return answer


a = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
b = ["Enter uid1234 Muzi", "Enter uid4567 Prodo"]
c = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234"]
d = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo"]
e = ["Enter uid1234 Muzi"]
f = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan","Enter uid1111 Ryan","Change uid1111 Prodo"]
print(solution(a))

"""

    dict1 = {}
    
    for i in record:
        a = i.split(" ")
        a = ["Enter", "uid1234", "Muzi"]
        b, c = a[0], a[1]    
        
        if b in ("Enter","Change"):
            nick = a[2]
            dict1 = {a:c}
    
    """

# 프로도 들어옴
# 라이언 들어옴
# 프로도 나감
# 프로도 들어옴

# 프로도 들어옴
# 라이언 들어옴
# 프로도 나감
# 프로도 들어옴
