# JSON 글자 <-> 파이썬 딕셔너리. 실행 전에 각 줄의 출력을 먼저 예상해 보기.
import json

d = {'alive': True, 'stamp': 12.5, 'name': None}   # 파이썬 딕셔너리 (따옴표는 ' " 둘 다 됨)
s = json.dumps(d)                                   # 딕셔너리 -> JSON 글자
print(s)                   # 1) 따옴표 · True · None 이 어떻게 바뀔까?
print(type(s))             # 2) str 일까 dict 일까?

back = json.loads('{"success": false, "reason": "TIMEOUT", "n": 3}')   # JSON 글자 -> 딕셔너리
print(back['reason'])      # 3)
print(back['success'])     # 4) false 가 파이썬에서 무엇으로 바뀌었을까?
print(type(back))          # 5)

print(json.loads("{'a': 1}"))   # 6) 작은따옴표 JSON — 될까?
