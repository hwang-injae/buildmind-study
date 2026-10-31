# 같은 자물쇠를 잠근 채 또 잠그면? — 1초만 기다려 보고 포기(True면 잠금 성공, False면 못 잠금)
import threading
lock = threading.Lock()
print(lock.acquire(timeout=1))   # 1번: 처음 잠그기
print(lock.acquire(timeout=1))   # 2번: 잠긴 채로 또 잠그기 → 1초 기다리다…  (실제 코드라면 여기서 영원히 멈춤)
lock.release()
