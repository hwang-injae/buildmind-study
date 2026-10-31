# 딕셔너리를 훑는 중에 칸을 추가하면? (snapshot 123줄이 읽는 동안 _on_blob 270줄이 쓰면 이렇게 된다)
state = {'state': 1, 'progress': 2}
for k in state:               # 훑기 시작 (snapshot 역할)
    print(k)
    state['wrist_image'] = 3  # 훑는 중에 새 칸 추가 (_on_blob 역할)
