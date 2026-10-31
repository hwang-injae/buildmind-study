# _fresh 흉내 — 다리 안부가 "최근"인가?   (mqtt_client.py:112-115)
lost_after_s = 3          # robot.yaml 값. 3초 넘게 안부 없으면 끊김
bridge_alive = True       # 마지막 안부 내용
seen_at = 10              # 마지막 안부를 받은 시각 (초)

def fresh(now):
    return bridge_alive and seen_at is not None and now - seen_at < lost_after_s

print(fresh(10))   # 1번: 받은 바로 그 순간
print(fresh(12))   # 2번: 2초 뒤 (전원 뽑힘 — 웹은 아직 모름)
print(fresh(13))   # 3번: 3초 뒤
print(fresh(14))   # 4번: 4초 뒤

bridge_alive = False      # 다리가 인사하고 꺼지면 alive false 를 보낸다
print(fresh(10.5))        # 5번: 받은 지 0.5초밖에 안 됐지만?
