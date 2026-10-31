# A or B 를 값으로 쓰기 — A가 비어 있지 않으면 A, 비어 있으면 B   (mqtt_client.py:77 · app.py:108)
print(3 or 10)             # 1번
print(0 or 10)             # 2번
print(None or "기본값")     # 3번
print("가짜" or "진짜")     # 4번
print(True or False)       # 5번: if 안에서 쓰던 그 or도 사실 같은 규칙

client = None
client = client or "make_mqtt_client()가 만든 진짜"
print(client)              # 6번: 77줄과 같은 꼴
