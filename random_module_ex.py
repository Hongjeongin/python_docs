# random module exercise

import random as r

rainbow = ['빨강', '주황', '노랑', '초록', '파랑', '남색', '보라']

choice = r.choice(rainbow)

print("셔플 전 >>", rainbow)

print("랜덤 뽑기 >>", choice)

r.shuffle(rainbow)
print("셔플 후 >>", rainbow)

print("0~6 랜덤 뽑기 >> ", r.randint(0, 6))
