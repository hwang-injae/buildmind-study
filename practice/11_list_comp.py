# 목록을 돌며 하나씩 바꿔 새 목록 만들기   (mqtt_client.py:134)
names = ['command', 'stop', 'resume']

# 1번: 지금까지 알던 방식 — 빈 목록에 하나씩 붙이기
out1 = []
for n in names:
    out1.append('d2/' + n + '/res')
print(out1)

# 2번: 같은 일을 한 줄로 — [만들 것 for 이름 in 목록]
out2 = ['d2/' + n + '/res' for n in names]
print(out2)

print(out1 == out2)   # 3번: 둘이 같은가?
