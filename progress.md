# 진도 기록

## 2026-10-26(월) 첫 시간 — 데스크톱 앱에서 하다가 VS Code로 옮기며 중간 기록

**일정 대비: 일정대로.** 10/26 계획(파이썬 수준 확인 + 1단계 실행) 중 수준 확인은 끝났고, 1단계 실행은 시작 전. 10/28 일정에 '(실행 마무리)'가 잡혀 있어서 아직 밀린 건 아님.

### 오늘 한 것
- git 점검: `study` 브랜치, 작업 트리 깨끗함, origin push = `no_push`. `study`에는 upstream(기본 push 대상)이 걸려 있지 않음.
- `study-notes/` 만듦: `progress.md` · `python-notes.md` · `buildmind.md` · `practice/`
- `.git/info/exclude` 7번째 줄에 `study-notes/` 추가 → `git status`에서 `?? study-notes/`가 사라진 것 확인. `.gitignore`는 안 건드림.
- 파이썬 수준 확인 4문제
- `.get` 연습 예제 `practice/01_dict_get.py` 만듦 (실행은 아직)
- 공부 규칙 원문을 `study-notes/teacher.md`로 저장 (VS Code에서 이어 하려고)

### 파이썬 수준 (10/26 퀴즈)
| 문제 | 내 답 | 결과 |
|---|---|---|
| Q1 `robot["speed"]`, `robot.get("color", "없음")` | 30 / 에러 | 반만 맞음 — `.get`은 키가 없으면 에러 대신 기본값을 돌려준다 |
| Q2 `try: n = int("abc")` … `except ValueError: n = 0` | 0 | 맞음 |
| Q3 `Counter` 클래스에서 `add()` 두 번 부르기 | 2 | 맞음 |
| Q4 본 적 있는 것 | `with`(파일 여는 구문?), f-string, lambda | `@staticmethod`(데코레이터)는 모름. `with`는 파일 쓸 때만 앎 |

설명 수준: 딕셔너리 `[ ]` · try/except · 클래스와 self 기초는 다시 설명하지 않는다. `.get` · `with` · 데코레이터처럼 처음 보는 문법은 나올 때 기초부터. 함수는 몇 줄씩 끊어서 "이 줄은 무엇을 하는지"부터.

### 새로 배운 파이썬 문법
- `딕셔너리.get(키, 기본값)` (`python-notes.md`에 정리. 예: `mqtt_client.py:263`)

### 모르는 것 (나올 때 기초부터)
- `with`가 파일 말고 하는 일: `with self._lock:` (공부할 6개 파일에 18번)
- 데코레이터: `@staticmethod` 21번, `@property` · `@contextmanager` 각 1번
- lambda를 실제로 쓰는 곳 (`design_store.py` · `design_gen.py`)

### 고친 것
- 없음. 코드 수정 없음, `study` 브랜치 그대로.

### 멈춘 곳
1. `.get` 연습: `study-notes/practice/01_dict_get.py`를 **아직 실행 안 함**. 실행 전에 2~5번째 줄의 출력을 먼저 예상해 보기로 함(마지막 줄은 일부러 KeyError).
   `python3 study-notes/practice/01_dict_get.py`
2. 확인 질문(아직 답 안 함): `web/backend/mqtt_client.py:263`의 `seq = self._blob_seq.get(kind, 0) + 1`
   - 어떤 kind가 처음 들어왔다면 `seq`는 몇?
   - `.get(kind, 0)` 대신 `self._blob_seq[kind]`라고 썼다면 처음 들어올 때 어떻게 됐을까?
3. 1단계(웹 + 가짜 로봇 실행): **시작 전.** 읽을 곳:
   - `README.md` '🚀 설치 · 실행'(515줄~) · '실행 순서'(554줄~) · 로봇 없이 돌려 보기(607줄)
   - `web/README.md` '1-B. 실행'(28줄~), 가짜 로봇 실행 예 `python3 web/backend/mock_robot.py --step 1.0`(57줄)
   - `web/backend/README.md` 15줄: `mock_robot.py` = 가짜 로봇 PC(MQTT만, `--step` · `--timeout-at` 옵션)

### 다음에 할 것
1. `.get` 예제 실행 → 예상과 같았는지 확인 + 확인 질문 답하기
2. "다음" 하면 1단계: README로 로봇 없이 웹 + `web/backend/mock_robot.py`를 띄우는 순서를 먼저 보여 주고, 한 단계씩 확인받고 실행
3. 10/28(수): (실행 마무리) + 2단계 파일 6개 클래스 · 함수 목록

---

## 2026-10-26(월) 밤 ~ 10/27(화) 0시 35분 — VS Code에서 이어서

**일정 대비: 앞섬.** 10/26 계획(파이썬 수준 확인 + 1단계 실행)을 다 끝냄. 10/28에 잡아 둔 '(실행 마무리)'는 할 게 없으니 10/28(수)은 바로 2단계. 10/27(화)은 예비군이라 공부 없음.

### 오늘 한 것
- 시작 점검: `study` 브랜치 · 작업 트리 깨끗 · origin push = `no_push`
- `.get` 연습 `practice/01_dict_get.py` 실행: 4줄 중 3줄 맞힘. 2번째 줄 `robot.get("speed", 0)`을 0으로 예상했는데 실제는 30(키가 있으면 기본값은 안 씀)
- 확인 질문 `mqtt_client.py:263`: (가) 1 · (나) 2 맞힘. (다) `self._blob_seq[kind]`였다면 → None이라고 답함, 실제는 KeyError
- 내 말로 한 줄 요약: "키가 없을 때 딕셔너리[키]는 keyerror가 출력되고, 딕셔너리.get(키, 기본값)은 기본값이 출력돼" → '출력'을 '돌려준다(반환)', 'KeyError가 나서 멈춘다'로 다듬음
- **1단계(실행) 끝** — 로봇 없이 웹 + 가짜 로봇(`web/README.md` 1-B '개발 PC 호스트에서 직접')
  1. 화면 만들기(Claude가 실행) `cd web/frontend && npm ci && npm run build` → `web/frontend/out` 생김. 명령은 마지막에 Next.js 16.4.0 보안 경고로 에러(종료 코드 1)로 끝났지만 화면 파일은 다 만들어짐(`index.html`이 부르는 파일 8개 확인)
  2. backend(직접) `cd web/backend && MQTT_HOST=localhost python3 -m uvicorn app:app --host 127.0.0.1 --port 8000` → 저장소 = JSON 폴더 `web/backend/data`, 기본 설계 4개 등록, 화면 있음
  3·4. 브라우저 `http://127.0.0.1:8000`을 먼저 열고(점 2개 초록 · 로봇 PC 빨강) → `python3 web/backend/mock_robot.py --step 1.0` → 점 3개 다 초록
  5. 1차 `004_DESK_PEDESTAL_V000` → DONE 11/11(손목 그림 `seq` 60 = `mqtt_client.py:263`이 센 번호). 2차 `003_DESK_STAND_V000` → [정지] → [다시 시작] → 7/9까지 이어 감
  6. 끄기: 가짜 로봇 끔 → 로봇 PC만 빨강 / backend 끔 → 셋 다 빨강(브로커는 켜져 있는데도)
- 확인 질문 `ConnectionBadge.tsx:21-23`(브로커가 켜져 있는데 왜 '브로커' 점이 빨강?): "화면은 backend한테, backend는 브로커한테 들으니 backend가 꺼지면 다 꺼졌다고 판단" → 거의 맞음. 다듬은 것: 꺼졌다고 판단한 게 아니라 '알 수 없음'이라 빨강(페일 세이프). 화면 기억엔 broker true가 남아 있지만(`ws.ts:80`은 ws만 false로) `robot.ws &&`가 막는다. 끊김 띠에 '급하면 펜던트 비상정지'

### 새로 배운 것 (`python-notes.md`에 정리)
- `.get`: 키가 있으면 기본값은 안 씀 · 기본값 없이 `.get(kind) + 1`이면 `None + 1` → TypeError
- 에러 글(Traceback)은 아래에서 위로 읽는다
- `os.environ.get(이름, 기본값)` · 환경 변수(`이름=값 명령` = 그 명령 하나에만, `export` = 터미널을 닫을 때까지). 연습 `practice/02_env.py` — 예상 다 맞힘
- 명령 · 도구: uvicorn(웹 서버 = 홀 직원, FastAPI `app` = 주방) · `python3 -m` · `app:app` · `--옵션` · 127.0.0.1 = localhost · 포트
- '출력(print)'과 '돌려준다(반환)'의 차이 · MQTT retained(브로커가 토픽마다 마지막 소식 하나를 들고 있음) · 화면 TypeScript의 `&&` = 파이썬 `and`

### 모르는 것 (나올 때 기초부터)
- `with`가 파일 말고 하는 일: `with self._lock:` (`mqtt_client.py:262` 등)
- 데코레이터: `@staticmethod` · `@property` · `@contextmanager` · `@asynccontextmanager`(`app.py` lifespan)
- lambda를 실제로 쓰는 곳(`design_store.py` · `design_gen.py`)
- 새로 본 것: 여러 개 한꺼번에 넣기 `a, b = x, y`(`mqtt_client.py:70` · `264`) · argparse 옵션 받기(`mock_robot.py:560` `ap.add_argument('--host', default='localhost')`)

### 고친 것
- 코드 수정 없음. `study` 브랜치 깨끗.
- 새로 생긴 것(모두 git이 무시): `web/frontend/node_modules` · `web/frontend/out`(화면 빌드) · `web/backend/data`(JSON 저장소, 기본 설계 4개)
- 노트: `python-notes.md`에 줄 추가, `practice/02_env.py` 만듦

### 선생님 메모 (다음 시간에 쓸 것)
- Claude는 VS Code 터미널 화면을 못 읽는다(사용자가 "터미널 봐 봐"라고 두 번 함). 터미널 글은 붙여 넣어 받거나, 로그를 봐야 하면 Claude가 백그라운드로 띄운다. 켜져 있을 때 상태는 `curl -s http://127.0.0.1:8000/api/robot/state`, 브로커 마지막 소식은 `mosquitto_sub -h localhost -v -W 2 --retained-only -t d2/task/state -t d2/safety/state -t d2/bridge/alive`
- 다시 띄우는 순서: 브로커(mosquitto)는 이미 켜져 있음 → 터미널 A backend → 브라우저 → 터미널 B 가짜 로봇. 화면 빌드는 이미 있음(화면 코드가 바뀔 때만 다시)
- Next.js 16.4.0: `npm audit` = next 16.0.0 ~ 16.4.0 critical(이미지 최적화 · Server Actions · `use cache` — 모두 Next.js 서버 기능). BuildMind는 `output: 'export'`라 실행 때 Next.js 서버가 없어 로컬 실행엔 영향 적음. 판 올리기는 팀 저장소 일. `buildmind.md` '고치고 싶은 것'에 적을지 물었는데 답 없음 → 다음에 한 번 더 묻기
- 10/29 `mqtt_client.py` 때 같이 볼 것: `_on_message`(194줄) 설명은 "예외는 삼켜 paho 스레드를 살린다"인데, 그림 길(199줄 `_on_blob`) · 점군 미리보기 길(202줄)은 `try:`(204줄) 밖이다. 설치된 paho 1.6.1은 `suppress_exceptions=False`가 기본이라 콜백 예외를 다시 던지고, 그러면 `loop_start` 스레드가 끝난다(`/usr/lib/python3/dist-packages/paho/mqtt/client.py` 3567 ~ 3575 · 3590). 지금 `_on_blob`은 예외를 낼 곳이 거의 없지만 `_emit`(329줄)이 예외를 낼 수 있는지 먼저 확인하고, '이상한 코드' 순서(왜 이상한지 → 팀이 일부러 그랬을 까닭 · 결정 기록 → 힌트 → 직접 고치기 → pytest)로 다룬다

### 멈춘 곳
- 1단계(실행) 끝. 2단계 시작 전.

### 다음에 할 것
1. 10/27(화): 예비군 — 공부 없음
2. 10/28(수): 2단계 — 파일 6개의 클래스 · 함수 목록으로 큰 그림 보기(`mqtt_client.py` → `bridge_codec.py` → `design_store.py` → `design_gen.py` → `claude_bridge.py` → `bridge_node.py`). 한 번에 다 펼치지 말고 파일 하나씩
3. 10/29(목): `mqtt_client.py` (위 선생님 메모의 '같이 볼 것' 포함)

---

## 2026-10-28(수) ~ 10/29(목) 0시 넘어서 — VS Code

**일정 대비: 반나절 밀림.** 10/28 계획(2단계 파일 6개 뼈대) 중 2개(`mqtt_client.py` · `bridge_codec.py`)만 끝. 첫 두 파일에서 질문이 많아 깊이 들어갔기 때문. 남은 4개 뼈대는 10/29 맨 앞에서 각 5분씩 보고 바로 `mqtt_client.py`로.

### 오늘 한 것
- 시작 점검: `study` 브랜치 · 작업 트리 깨끗 · origin push = `no_push`
- **`mqtt_client.py` 뼈대**(332줄, 함수 1 + 클래스 1 · 메서드 26) → 7묶음 지도는 `buildmind.md` '큰 그림'에. 바깥에서 부르는 건 밑줄 없는 8개만(`routes/robot.py` · `ws.py` · `voice.py` · `app.py`)
- `start()` 5줄 읽음. 확인 질문 "`target=self._alive_loop`에 괄호가 없는 이유" → 처음엔 `async`와 섞었다가 정리: 괄호 있으면 그 자리에서 `_alive_loop`가 돌아 `start()`가 영원히 안 끝남(에러도 안 남). 내 말 요약 잘 됨
- **`bridge_codec.py` 뼈대**(239줄, 모듈 함수 16 + 작은 클래스 2). 처음 설명이 너무 빨라 "이해 못 하겠다" → 그림부터 다시: 로봇 PC(ROS, `/d2/…`) ↔ 다리 ↔ 브로커(우체국) ↔ 웹 PC(MQTT만). 요청 · 응답은 우편함 두 개(`…/req` · `…/res`) + 번호표 `req_id`. [정지] 버튼 한 번이 지나가는 길 6단계로 함수들 자리 잡음
- 확인 질문: `req_topic('/d2/safety/stop')` → 처음엔 `/req` 붙이는 걸 빠뜨림 → `d2/safety/stop/req`. 번호표가 필요한 이유 → "응답이 어느 요청의 답인지 알고, 같은 요청이 두 번 오면 한 번만 실행" 맞음
- 연습 `practice/03_json.py` 만듦. 6줄 출력 예상 다 맞음(1번 `True→true` · `None→null`은 직접 돌려 눈으로 확인하기로). **실행은 아직**
- 정한 것(teacher.md에 적음): 고친 코드는 내 포크 `fork`의 `study`에 올린다(커밋은 Claude, push는 내가 `git push fork study`). 로봇 PC는 수료로 없음 → `bridge_node.py`도 간단한 시험(pytest · 작은 가짜 서비스)만 하고 고치되 "수정은 했고 실기 검증은 못 함"을 커밋 글 · `buildmind.md` · 면접에서 그대로 말한다. Next.js 판 올리기는 11/4(수)

### 새로 배운 것 (`python-notes.md`에 정리)
- `_이름` 밑줄 약속(안에서만 쓰는 것) · `함수` vs `함수()` · `threading.Thread(target=함수).start()` · `while not 이벤트.wait(초)` · paho · `connect_async` vs `connect`
- `json.dumps` / `json.loads`(s = 글자, s 없으면 파일) · JSON은 큰따옴표만, `true`/`false`/`null` · `A if 조건 else B` · `글자[1:]` · `startswith`
- 개념: ROS 이름은 경로가 아니라 이름 규칙 · MQTT는 반드시 브로커를 거침(보내는 쪽은 받는 쪽을 모름) · ROS 2는 로봇 PC 안에서만(E-27) · codec = 양쪽이 같은 번역 규칙을 쓰게 한 파일(ROS · paho import 없음 → `tests/test_bridge_codec.py` 22개가 로봇 없이 돈다)

### 모르는 것 (나올 때 기초부터)
- `**fields`(`bridge_codec.py:84` `typed_response(req_id, **fields)` · `mqtt_client.py:169` `{**fields, 'req_id': req_id}`) — 10/30
- `uuid.uuid4()`(`mqtt_client.py:167`) — 10/29
- 전부터: `with self._lock:` · 데코레이터(`@staticmethod` · `@property` · `@contextmanager` · `@asynccontextmanager`) · lambda · `a, b = x, y` · argparse

### 고친 것
- 코드 수정 없음. `study` 브랜치 깨끗
- 노트: `buildmind.md` '큰 그림'(mqtt_client 7묶음) · '고치고 싶은 것'에 Next.js 메모, `python-notes.md` 9줄 추가, `practice/03_json.py`, `teacher.md` '10/26 이후 정한 것' 3줄

### 선생님 메모
- 파일 뼈대를 표로 한 번에 보여 주면 막힌다(bridge_codec). **그림(누가 누구에게) → 한 버튼이 지나가는 길 → 그 길 위의 함수** 순서가 먹혔다. 남은 4개도 이 순서로
- 날이 넘어가면(0시 뒤) 날짜가 바뀐다. 기록은 시작한 날 기준으로
- 어제 메모 그대로: 10/29 `mqtt_client.py` 때 `_on_message`(194줄) `try:` 밖의 `_on_blob` · 미리보기 길 + paho 1.6.1 콜백 예외 문제를 '이상한 코드' 순서로

### 멈춘 곳
- 2단계 뼈대 2/6. `practice/03_json.py` 실행 전

### 다음에 할 것
1. `python3 study-notes/practice/03_json.py` 돌려서 1번 줄 `true` · `null` 확인, 6번 줄 에러 아래에서 위로 읽기
2. 남은 뼈대 4개를 "그림 → 길 → 함수" 순서로 각 5분: `design_store.py`(724줄) → `design_gen.py`(905줄) → `claude_bridge.py`(408줄) → `bridge_node.py`(408줄)
3. 10/29 본 공부: `mqtt_client.py` 메서드 하나씩(위 선생님 메모 포함)

---

## 2026-10-30(금) ~ 10/31(토) 0시 넘어서 — VS Code (10/29 목은 쉼)

**일정 대비: 이틀 밀림.** 시작할 때 하루 반(10/29 쉼 + 2단계 뼈대 4개 남음). 오늘 2단계를 끝냈지만 3단계(`mqtt_client.py` 10/29 몫 · `bridge_codec.py` 10/30 몫)는 시작 못 해 이틀. 뼈대 단계에서 질문이 깊이 들어갔기 때문(삼킨 예외 · 상속). 새 일정은 아래 '다음에 할 것'(모두 이틀씩 뒤로, Next.js 11/4 → 11/6).

### 오늘 한 것
- 시작 점검: `study` 브랜치 · 작업 트리 깨끗 · origin push = `no_push`
- `practice/03_json.py` 실행: 6줄 다 예상대로. 6번 줄 `JSONDecodeError` = 작은따옴표 때문, 맞힘. 새로 본 것: `File` 줄이 4개인데 내 파일은 맨 위 하나(나머지는 `/usr/lib/python3.12/json/…`), `JSONDecodeError`는 `ValueError`의 자식이라 `mqtt_client.py:218` `except (ValueError, …)`에 잡힌다
- 질문 "예외 삼키면 어떻게 되나": 소식 하나만 버리고 paho 스레드는 산다(안 삼키면 1.6.1이 다시 던져 스레드 죽음). 약점 = 로그가 한 줄도 없어 조용함 → `buildmind.md` '고치고 싶은 것'에 적음. 확인 질문([정지] 답장 `/res`만 깨졌을 때): (가) "주기적으로 상태가 와서 따라잡는다" → 반 맞음(상태는 바뀔 때만 retained, 1초마다는 alive뿐; 기다리는 시간은 `robot.yaml:119` 5초) · (나) "로봇은 안 멈췄다" → 틀림(요청 `/req`는 멀쩡히 갔으니 멈췄고, 답장만 잃음). 봉투 세 개(req · res · state) 그림으로 다시 설명했으나 "완전 이해는 못 함" → 두 줄만 들고 가기로: ① `json.loads` 실패는 그 소식 하나만 버리고 계속 돈다 ② 답장 못 받음 ≠ 요청 실패, 그래서 재전송 안 하고 "상태 칸을 보세요"
- **2단계 뼈대 4개 끝**(그림 → 길 → 묶음 표, `buildmind.md` '큰 그림'):
  - `design_store.py`(724) — 로봇 무관 **창고**. JSON 폴더판 `DesignStore` · PostgreSQL판 `PgDesignStore(DesignStore)`, `.env` `DATABASE_URL` 유무로 고름(10/26 실행은 JSON판 → `web/backend/data/designs/*.json`). 7묶음. 로봇 "설계 줘" 답은 `answer_get_design` ← `app.py:111` `mqtt.serve`
  - `design_gen.py`(905) — Claude에게 설계 **묻는 한 곳**. 길: `generate` → 창고에서 바탕 읽기 → 중계에 묻기 → 후보 3개 → 검사 → 떨어지면 이유 알려 다시(2번) → 사람이 고름 → `save`. 7묶음
  - `claude_bridge.py`(408) — **중계**: 컨테이너 안 `design_gen`의 OpenAI 형식 HTTP 요청 → 호스트에서 `claude -p` 실행 → OpenAI 모양으로 답. 5묶음. 240초 < 260초(중계가 먼저 끊어야 504 이유가 화면에)
  - `bridge_node.py`(408) — 로봇 PC **다리**, `mqtt_client.py`의 거울. `MqttBridge(Node)`. 번역만, 판단 없음(E-30). 7묶음. 이 PC `/opt/ros/jazzy` 있음 확인
- **상속** 처음 배움: `design_store.py:572` `PgDesignStore(DesignStore)`에서 "`PgDesignStore`에 없는 `get_design`을 부르면 어느 `_load`가 도나" → JSON판이라 답(틀림, 답은 Pg판). 말로 두 번 설명해도 안 됨 → `practice/04_inherit.py`(4줄) 만들어 직접 실행 → **04는 완전 이해**. BuildMind 코드와는 "한 줄씩 짝짓기 표"로 대응만("코드 자체는 아직 이해 못 함" — 10/31 본 공부 때). 오늘 상속 4번 봄: `PgDesignStore` · `GenError(Exception)` · `BridgeError(Exception)` · `MqttBridge(Node)`
- 확인 질문 결과: `design_gen` 검사가 따로 있는 이유 → "로봇이 쌓을 수 있는 구조인지 검증" 맞음(+E-69 코드가 대신 안 고침) · `claude_bridge`가 `web/` 바로 아래인 이유 → "도커 안이라서" → 반대(상자 **밖**이어야 `claude`를 부를 수 있음) · 다리 죽으면 화면 [정지] → "안 됨" 맞음, "자동 안전정지 있지 않나" → 반만(자동 급정지는 없음. 로봇 PC 안 정지 수단 Ctrl+C · 알람 · 펜던트는 그대로 E-30 ⓑ, 작업 관리자는 웹 3초 끊김에 하던 동작 끝내고 `WAIT_HMI` — SDD 109 · 783 · 820)

### 새로 배운 것 (`python-notes.md`에 정리)
- `JSONDecodeError` · 긴 Traceback 읽기(내 파일 줄은 맨 위 하나)
- 상속 `class 자식(부모):` — 부모 메서드 안 `self.메서드()`는 점 앞 물건으로 찾는다(자식 먼저). 예외도 클래스라 `class GenError(Exception)`
- 개념(노트엔 안 적음, 여기만): 호스트 vs 컨테이너(도커 상자 안에선 바깥 프로그램 안 보임) · HTTP는 프로그램끼리도 씀 · OpenAI 형식(묻는 JSON 규칙) · `subprocess`(파이썬이 명령을 대신 침) · `claude -p`(한 번 묻고 끝) · PostgreSQL(저장 전문 프로그램, SQL로 묻기) · 답장 잃음 ≠ 요청 잃음 · E-69 · E-30 ⓑ

### 모르는 것 (나올 때 기초부터)
- 답장(`/res`) · 상태(`/state`) 봉투 구분 — `mqtt_client.py` 본 공부 때 코드 보며 다시
- `design_store.py` 코드 글자: `_checked` · `_design_path` · `with self._db() as cur` · `%s`(SQL) — 10/31 이후 그 파일 차례에
- 전부터: `with self._lock:` · 데코레이터(`@staticmethod` 21 · `@property` · `@contextmanager` · `@asynccontextmanager`) · lambda · `**fields`/`**kw` · `uuid.uuid4()` · `a, b = x, y` · argparse · 새로: `functools.partial` · ROS 2 용어(Node · 서비스 · QoS · executor · future)

### 고친 것
- 코드 수정 없음. `study` 브랜치 깨끗
- 노트: `buildmind.md` '큰 그림' 4개 파일 표 + '고치고 싶은 것' 1개(`mqtt_client.py:218` 조용한 except에 로그 한 줄), `python-notes.md` 2줄, `practice/04_inherit.py`

### 선생님 메모
- **느려진 원인**: 뼈대 단계에서 좋은 질문(삼킨 예외의 결과 · 상속)이 깊이 들어가 2단계에 이틀. 질문을 막진 말되, 3단계부터는 "메서드 하나 10분" 목표. 그 파일 차례가 아닌 깊은 질문은 '모르는 것'에 적고 넘어가자고 먼저 제안
- **설명이 막힌 패턴 2개**: ① 아직 안 본 BuildMind 코드를 가리키며 설명(상속) → 연습 파일로 먼저 이해 → 한 줄씩 짝짓기 표가 먹혔다. ② 그림 한 장에 용어 5개(호스트 · 컨테이너 · HTTP · OpenAI 형식 · `claude -p`) → 용어를 번호로 하나씩 풀고 그림을 쉬운 말로 다시 그리니 됐다. **용어는 처음 나올 때 한 줄로** 규칙을 더 엄격히
- 확인 질문에서 "반대로 답하는" 일이 두 번(Pg/JSON · 도커 안/밖). 틀린 게 아니라 방향을 잡기 전이라 그런 것 — 그림의 어느 쪽인지 먼저 짚고 묻기
- 10/28 메모 그대로 유효: `mqtt_client.py` 본 공부 때 `_on_message` `try:` 밖 `_on_blob` · 미리보기 길 + paho 1.6.1 + 오늘 적은 218 로그 → '이상한 코드' 순서로 한 번에
- 노션 일정표를 새 일정으로 고침(10/31 0시)

### 멈춘 곳
- 2단계(뼈대 6/6) 끝. 3단계 시작 전 — `mqtt_client.py` `__init__`(60)부터

### 다음에 할 것 (새 일정, 모두 이틀 뒤로)
1. 10/31(토): `mqtt_client.py` 메서드 하나씩(① 켜고 끄기 → ② 상태 → ③ 콜백 … 순서, `buildmind.md` 7묶음). 선생님 메모의 '이상한 코드' 포함. 첫 문법: `with self._lock:`
2. 11/1(일): `bridge_codec.py`
3. 11/2(월): `design_store.py`
4. 11/3(화): `design_gen.py` · `claude_bridge.py`
5. 11/4(수): `bridge_node.py`(`colcon build` 먼저) + 4단계(함수 하나 다시 써 보기)
6. 11/5(목): 로보월드 — 공부 없음(노션 일정표에 있던 것)
7. 11/6(금): 5단계 말로 설명하기(면접관 역할)
8. 11/7(토): Next.js 판 올리기(10/28 정한 11/4에서 미룸). 노션 '할 일'에 새로 넣음
- 뒤 일정도 같이 미룸(사용자: "지연된 만큼 미루면 돼, 진행 상황 따라 유동적으로"): BuildMind 끝 11/3 → 11/6(사흘)이라 SortTwin 11/7~11/14 · PreWash 11/15~11/21 · IDC 11/22~11/26으로 노션 수정

---

## 2026-10-31(토) — VS Code

**일정 대비: 사흘 밀림(하루 더).** 오늘 몫은 `mqtt_client.py` 전체였는데 7묶음 중 ① 켜고 끄기 · ② 상태 2개만 끝(메서드 7/26). 깃허브 잔디용 노트 저장소 만들기(약 40분)와 `with self._lock:` 이해(연습 파일 3개, 비유로 다시)에 시간이 갔다. 새 일정은 아래 '다음에 할 것'(모두 하루씩 뒤로, 노션 반영 끝).

### 오늘 한 것
- 시작 점검: `study` 브랜치 · 작업 트리 깨끗 · origin push = `no_push`
- **깃허브 잔디**: 포크(`hwang-injae/buildmind`)의 `study` 커밋은 잔디에 안 셈(포크 + 기본 브랜치 아님 + 커밋 이메일 `pm-sim@local`). → `study-notes/`를 **그 자체로 별도 저장소**로 만들어 공개 저장소 `hwang-injae/buildmind-study`(`main`)에 올림. 이 폴더만 커밋 이름 `hwang-injae` · 이메일 깃허브 대리 주소(`280895779+hwang-injae@users.noreply.github.com` — 진짜 메일은 push가 GH007로 거절됨). 바깥 BuildMind 저장소는 이 폴더를 무시하니 안 섞임. 저장소 만들기 · remote 연결 · push는 내가 직접(gh repo create → git remote add → git push -u origin main). 잔디가 노란색 = 할로윈 테마(10/31 칸에 기여 2 확인)
- **`__init__`(60~81)** 끝: 빈 상자(상태 · 그림 딕셔너리) · 자물쇠 · 스위치 만들고 paho에 콜백 3개 + 유언(`will_set`) 맡김. 연결은 아직 안 함
- **`start`(84) 복습 · `stop`(91)**: 깨끗한 종료엔 유언이 안 나가서 `alive false`를 직접 보냄. 확인 질문(갑자기 뽑힘 → 브로커가, 정상 종료 → backend가) 맞힘
- **② 상태**: `connected`(브로커) vs `bridge_connected`(다리)는 다른 질문. `_fresh` 조건 3개(마지막 안부 true · 받은 적 있음 · 지금 − 받은 시각 < 3초). `bridge_connected`/`_fresh`를 둘로 나눈 이유 = 잠금 안에서 또 잠그면 데드락(`practice/10_double_lock.py`). `snapshot`은 복사 직원
- 연습 6개 만들고 돌림: `05_multi_assign.py`(4/4) · `06_with_lock.py`(일꾼 둘 → 잠금 없으면 1, 있으면 2) · `07_dict_while_iter.py`(RuntimeError 재현) · `08_or_value.py`(6/6) · `09_fresh.py`(5/5) · `10_double_lock.py`
- 확인 질문 결과: `Lock()` 괄호 vs `_alive_loop` 괄호 없음 → 맞음 · `pending`/`seen`은 객체 → 맞음 · `client or make_mqtt_client` 77줄 → 1번 맞음, "누가 만들면 무엇이 들어가나"는 **방향 반대**(pytest = 가짜, app.py = 진짜) · `_fresh` "2초 전 안부 뒤 전원 뽑힘" → 거짓이라 답(정답 참, 1초 뒤 거짓) → 09 연습 뒤 5/5
- `buildmind.md` '함수 설명 (내 말로)'에 `__init__` · `start` · `stop` 3개(내 말 + 한 단어씩 덧붙임)

### 새로 배운 것 (`python-notes.md`에 정리)
- `a, b = x, y` · `with 잠금:`(threading.Lock) · 딕셔너리 훑는 중 칸 추가 → RuntimeError · `A or B`를 값으로
- 개념(노트엔 안 적음): 콜백(상대가 때가 되면 대신 부르는 함수) · 유언 LWT(갑자기 죽을 때만 브로커가 올림) · `threading.Event` 스위치 · `time.monotonic`(간격 재는 시계, 시험은 가짜 시계) · 데드락 · 겉 함수가 잠그고 속 함수는 계산만 · `global` · `t.join()`(연습용)

### 모르는 것 (나올 때 기초부터)
- 06 연습의 `global` · `join` · `fn.__name__`은 연습용으로만 넘김
- 전부터: 데코레이터(`@staticmethod` · `@property` · `@contextmanager` · `@asynccontextmanager`) · lambda(시험 `clock=lambda: now[0]`에 나옴 — 11/1 `_fresh` 시험 볼 때) · `**fields`/`**kw`(169 · 302 · 327줄) · `uuid.uuid4()`(167) · argparse · `functools.partial` · ROS 2 용어 · `design_store` 글자들

### 고친 것
- 코드 수정 없음. BuildMind `study` 브랜치 깨끗
- 노트: `progress.md` 이 칸 · `python-notes.md` 4줄 · `buildmind.md` 함수 설명 3개 · `practice/05~10` · `teacher.md` '정한 것' 1줄 · 노트 저장소 `README.md` · `.gitignore`

### 선생님 메모
- **비유를 빼면 안 된다.** "비유보다 정확히"라고 요청받아 딕셔너리 · 스레드 이름으로 설명했더니 "비유를 안 하니 더 어렵다"고 됨. 비유(사무실 · 직원 셋 · 화이트보드 · 자물쇠) 하나로 끝까지 일관되게 가고, 정확한 이름은 짝짓기 표로 붙인다
- **가정 예시는 실제와 섞이면 혼란.** "`_on_blob` 둘이 동시에"는 실제로 안 일어나는 상황인데 연습과 맞추려 그렸다가 질문 2개를 만들었다. 예시는 **실제로 부딪히는 짝**(paho 쓰기 vs snapshot 읽기)으로만
- **연습 파일에 새 글자 3개(`global` · `join` · `__name__`) 들어가면 파일 자체가 막힌다.** 연습은 배우려는 문법 하나만 보이게, 장치가 필요하면 주석에 "연습용"이라 적기
- 방향 반대로 답하는 패턴 또 1번(pytest/app.py). 표로 "누가 → 무엇"을 먼저 보여 주고 묻기
- 확인 질문은 **비유로 먼저 답하게** 하고 숫자 · 이름은 그 뒤에. 09처럼 숫자를 직접 넣는 연습은 바로 먹혔다
- 세션 끝 순서(10/31부터): progress.md → 노션 일정 → `study-notes/`에서 커밋(Claude) → `git push` 명령 알려 주기(사용자가 침) → 잔디 1칸

### 멈춘 곳
- `mqtt_client.py` 7묶음 중 ① ② 끝. ③ 콜백(`_on_connect` 129 · `_on_disconnect` 138 · `_on_message` 194) 시작 전

### 다음에 할 것 (새 일정, 모두 하루씩 뒤로 — 노션 반영 끝)
1. 11/1(일): `mqtt_client.py` ③ 콜백 → ④ 살아있음 → ⑤ 웹→로봇 → ⑥ 소식 처리 → ⑦ `_emit`. `_on_message`에서 '이상한 코드' 2개(try 밖 `_on_blob` · 미리보기 길, 218줄 조용한 except)를 '이상한 코드' 순서로. 끝나면 ③~⑦ 함수 설명 내 말로
2. 11/2(월): `bridge_codec.py`
3. 11/3(화): `design_store.py`
4. 11/4(수): `design_gen.py` · `claude_bridge.py`
5. 11/5(목): 로보월드 — 공부 없음
6. 11/6(금): `bridge_node.py`(`colcon build` 먼저) + 4단계(함수 하나 다시 써 보기)
7. 11/7(토): 5단계 말로 설명하기(면접관 역할)
8. 11/8(일): Next.js 판 올리기
- 뒤 일정 하루씩: SortTwin 11/8~11/15 · PreWash 11/16~11/22 · IDC 11/23~11/27(노션 수정 끝)

---

## 2026-11-01(일) ~ 11-03(화) — VS Code (한 세션이 사흘에 걸침)

**일정 대비: 사흘 더 밀림(총 엿새).** 11/1 몫은 `mqtt_client.py` ③~⑦ 전부였는데 `_on_connect`(129) 하나를 135줄 앞 절반까지만. 공부 방식 문제가 드러나 고쳤고(아래 선생님 메모), 세션이 사흘에 걸쳐 짧게 이어졌다. 새 일정은 '다음에 할 것'.

### 오늘 한 것
- 시작 점검: `study` 브랜치 · 작업 트리 깨끗 · origin push = `no_push`. 노트 저장소도 깨끗
- **`_on_connect`(129~135 앞 절반)**: 우체국(브로커)과 전화가 연결될 **때마다** paho가 부르는 쪽지. ① `rc != 0`이면 거절이라 나감 ② 133~134 배달 명단 15칸(상태 5 + 낱개 4 + 웹이 물은 답 `/res` 4 + 로봇이 묻는 `/req` 2) ③ 135 `client.subscribe` = "이 칸들 배달해 줘"(구독). 끊기면 우체국이 명단을 지우니 `start`가 아니라 `_on_connect`에 있어야 한다(확인 질문 "다시 안 불리면?" → "전화는 돼도 아무것도 안 온다" 맞힘)
- `(t, 1)` 짝 + QoS 0(던지고 감) · 1(사인 받을 때까지) 표. 확인 질문 "손목 그림 1~2 Hz는 0? 1?" → 0, 이유도 맞힘(29줄과 일치)
- 연습 2개: `11_list_comp.py`(for 세 줄 ↔ 한 줄 짝짓기, 맞힘) · `12_list_of_dict.py`(`list(딕셔너리)` = 키만)

### 새로 배운 것 (`python-notes.md`에 정리)
- `[만들 것 for 이름 in 목록]` 리스트 컴프리헨션 · `list(딕셔너리)` = 키만 · 목록 `+` 목록 · 줄 끝 `\`
- 개념(노트엔 안 적음): 토픽 = 우체국 칸 이름 · 구독(subscribe) = "이 칸 배달해 줘" · 끊기면 구독 명단이 지워져 연결마다 다시 · `rc` 결과 번호 · 튜플은 "짝"으로만 · QoS 0/1

### 모르는 것 (나올 때 기초부터)
- 135줄 뒷절반 `for t, (_kind, qos) in BLOB_TOPICS.items()` — `.items()` · 짝 풀기(중첩 언패킹). 다음 시간 첫 번째
- 전부터: 데코레이터 · lambda · `**fields`(169 · 302 · 327) · `uuid.uuid4()`(167) · argparse · `functools.partial` · ROS 2 용어 · `design_store` 글자들 · 연습 06의 `global` · `join` · `__name__`

### 고친 것
- 코드 수정 없음. BuildMind `study` 브랜치 깨끗
- 노트: `progress.md` 이 칸 · `python-notes.md` 2줄 · `practice/11~12` · `teacher.md` '정한 것' 11/2 한 줄(아래)

### 선생님 메모
- **코드를 먼저 읽게 하고 설명한다(11/2 규칙으로 적음).** 사용자가 "코드를 안 보고 대화만 보면서 공부 중이라 정확히 이해가 안 된다"고 함. 비유만 하고 코드 줄을 다 안 붙인 게 원인. 앞으로 메서드마다 ① VS Code 링크 `[파일:줄](경로#L줄)` + 채팅에 같은 코드 블록 ② "먼저 읽어 보세요" ③ 비유 · 짝짓기 표 ④ 확인 질문
- "신청서"처럼 **비유 단어를 새로 꺼낼 때는 그 단어 = 코드 어느 줄인지 바로 붙일 것.** "신청서로 말하면"부터 막혔다 → 우체국 칸 · 배달 명단 · 시간표(0초 · 1초 · 10초 · 12초)로 다시 하니 됐다
- 방향 반대 패턴 또 1번: `list(딕셔너리)` 결과(키)를 "값"이라 부름. 콜론 왼쪽 = 키 표를 먼저 보여 주니 됨. **키 · 값 단어를 쓸 때 매번 콜론 왼쪽/오른쪽을 덧붙이기**
- `_on_connect` 함수 설명(내 말)은 아직 안 받음 — 135 뒷절반 끝나면 "한 줄 요약"으로 받아 `buildmind.md`에
- 속도: 메서드 하나에 세션 하나. 10/30 메모 "메서드 하나 10분"과 멀다. 다음부터 `_on_disconnect`(4줄) · `_alive_loop` · `check_bridge`처럼 짧은 것은 코드 + 표 하나로 바로 가고, 확인 질문은 묶음당 1개로

### 멈춘 곳
- `_on_connect` 135줄 뒷절반 `[(t, qos) for t, (_kind, qos) in BLOB_TOPICS.items()]` 직전. 136 `_emit`은 비유로만 봄

### 다음에 할 것 (새 일정, 사흘씩 뒤로 — 노션 반영)
1. 11/4(수): `mqtt_client.py` 나머지 — 135 뒷절반 → `_on_disconnect` → `_on_message`('이상한 코드' 2개: try 밖 `_on_blob` · 미리보기 길, 218 조용한 except) → ④ 살아있음 → ⑤ 웹→로봇 → ⑥ 소식 처리 → ⑦ `_emit`. 끝나면 ③~⑦ 함수 설명 내 말로
2. 11/5(목): 로보월드 — 공부 없음
3. 11/6(금): `bridge_codec.py`
4. 11/7(토): `design_store.py`
5. 11/8(일): `design_gen.py` · `claude_bridge.py`
6. 11/9(월): `bridge_node.py`(`colcon build` 먼저) + 4단계(함수 하나 다시 써 보기)
7. 11/10(화): 5단계 말로 설명하기(면접관 역할)
8. 11/11(수): Next.js 판 올리기
- 뒤 일정 사흘씩: SortTwin 11/11~11/18 · PreWash 11/19~11/25 · IDC 11/26~11/30
