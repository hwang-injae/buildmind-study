# list(딕셔너리) — 키만 뽑아 목록으로   (mqtt_client.py:133)
topics = {
    'd2/task/state': 'state',
    'd2/safety/state': 'safety',
}

print(list(topics))            # 1번: 키만?  값만?  둘 다?
print(list(topics) + ['d2/bridge/alive'])   # 2번: 목록 + 목록
