# 상속: 부모 메서드 안의 self.메서드() 는 "지금 이 물건"의 것을 부른다. 실행 전에 각 줄 출력을 예상해 보기.

class Store:                      # 부모 (JSON판 역할)
    def get(self):                # 자식이 다시 안 적는 메서드
        return "get → " + self._load()
    def _load(self):              # 창고 문 (JSON판)
        return "JSON 파일 읽음"

class PgStore(Store):             # 자식 — 괄호 안이 부모. _load 만 다시 적는다
    def _load(self):
        return "DB 읽음"

a = Store()
b = PgStore()
print(a.get())        # 1) JSON판 물건
print(b.get())        # 2) Pg판 물건 — get 은 부모 것인데, 안의 self._load() 는 누구 것?
print(type(b).__name__)                 # 3) b 의 클래스 이름
print(isinstance(b, Store))             # 4) b 는 Store 이기도 할까?
