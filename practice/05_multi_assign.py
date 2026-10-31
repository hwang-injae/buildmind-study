# 여러 개 한꺼번에 넣기  a, b = x, y   (mqtt_client.py:62 · 70 · 264)
host, port = "localhost", "1883"
print(host)            # 1번: 뭐가 나올까?
print(port)            # 2번: 뭐가 나올까?
print(int(port) + 1)   # 3번: 글자 "1883"을 숫자로 바꾸고 1 더하면?
a, b = 1, 2
a, b = b, a            # 4번: 서로 바꾸기 — a는? b는?
print(a, b)
