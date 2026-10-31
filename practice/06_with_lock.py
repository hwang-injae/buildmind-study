# 잠금(Lock)이 없으면 어떤 사고가 나나 — 일꾼 둘이 같은 칠판 숫자에 1씩 더한다
import threading, time

count = 0                   # 칠판. 일꾼 둘이 같이 쓴다
lock = threading.Lock()

def add_without_lock():
    global count
    v = count               # ① 칠판을 읽고
    time.sleep(0.1)         # ② 잠깐 딴짓 (이 틈에 다른 일꾼이 끼어든다)
    count = v + 1           # ③ 1 더한 값을 칠판에 쓴다

def add_with_lock():
    global count
    with lock:              # 문을 잠근다. 다른 일꾼은 여기서 멈춰 기다린다
        v = count
        time.sleep(0.1)
        count = v + 1
                            # 여기서 자동으로 문이 풀린다. 기다리던 일꾼이 들어간다

for fn in (add_without_lock, add_with_lock):
    count = 0
    t1 = threading.Thread(target=fn)
    t2 = threading.Thread(target=fn)
    t1.start(); t2.start()          # 일꾼 둘 출발
    t1.join(); t2.join()            # 둘 다 끝날 때까지 기다림
    print(fn.__name__, "→ 칠판 =", count)   # 둘이 1씩 더했으니 2가 나와야 맞다
