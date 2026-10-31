# 배운 파이썬 문법

| 문법 | 한 줄 설명 | BuildMind에서 나온 예 |
|---|---|---|
| `딕셔너리.get(키, 기본값)` | 키가 있으면 그 값(이때 기본값은 안 쓴다), 없으면 기본값을 돌려준다(기본값을 안 주면 `None`). `딕셔너리[키]`는 키가 없으면 `KeyError`로 멈춘다. | `mqtt_client.py:263` `seq = self._blob_seq.get(kind, 0) + 1` (종류별 번호 세기). 처음 들어온 종류는 기본값 0 → 1번. 기본값이 없으면 `None + 1` → `TypeError`, `[kind]`였으면 `KeyError`. |
| 에러 글(Traceback) 읽기 | 아래에서 위로 읽는다. 맨 끝 줄 = 에러 종류와 이유, 그 위 `line N` = 에러가 난 줄, `~~~^^^` = 그 줄에서 문제가 된 곳. | (연습) `practice/01_dict_get.py` 5번째 줄 `print(robot["color"])` → `KeyError: 'color'` |
| `os.environ.get(이름, 기본값)` | 환경 변수(프로그램 밖에서 `이름=값`으로 넘겨준 설정)를 읽는다. `os.environ`은 딕셔너리처럼 쓰고, 없으면 기본값. | `app.py:108` `os.environ.get('MQTT_HOST', 'localhost')` (브로커 주소) |
| `_이름` (밑줄 하나로 시작) | "클래스 안에서만 쓰는 것, 밖에서 부르지 마세요"라는 사람끼리의 약속. 문법으로 막히진 않는다. 밑줄 없는 것만 바깥 파일이 부른다. | `mqtt_client.py` 메서드 26개 중 15개가 `_`(`_on_message` · `_emit` 등). routes가 부르는 `request` · `snapshot` · `blob` 등 8개는 밑줄 없음 |
| `함수` vs `함수()` | 괄호 없으면 함수 그 자체(이름표), 괄호 있으면 그 자리에서 실행한 결과. 누구에게 "나중에 이걸 돌려 줘"라고 넘길 때는 괄호 없이. | `mqtt_client.py:89` `threading.Thread(target=self._alive_loop, daemon=True).start()`. 괄호를 붙이면 그 자리에서 `_alive_loop`가 돌기 시작해 `start()`가 영원히 안 끝난다(화면 안 뜸, 에러도 없음) |
| `threading.Thread(target=함수).start()` | 새 일꾼(스레드)을 만들어 그 함수를 따로 돌린다. 부른 쪽은 기다리지 않고 바로 다음 줄로. `daemon=True` = 본 프로그램이 끝나면 같이 끝남. | `mqtt_client.py:89` 연결 신호 보내는 `_alive_loop` |
| `while not 이벤트.wait(초)` | `초`만큼 기다리다 깨어나 반복. 다른 곳에서 `이벤트.set()`을 하면 즉시 멈춤. "N초마다 하다가 끄라면 끈다" 패턴. | `mqtt_client.py:145` `while not self._stop.wait(self.alive_s):` · `stop()`의 `self._stop.set()` |
| `json.dumps(딕셔너리)` · `json.loads(글자)` | JSON = 두 프로그램이 똑같이 읽을 수 있게 정한 글자 형식(딕셔너리 모양, 반드시 큰따옴표, `true`/`false`/`null`). `dumps` = 딕셔너리 → 글자(s = string), `loads` = 글자 → 딕셔너리. s 없는 `dump`/`load`는 파일에 쓰기/읽기. | `bridge_codec.py:44` `json.dumps({'alive': …})` · `mqtt_client.py:169` `json.dumps({**fields, 'req_id': req_id})`. 연습 `practice/03_json.py` |
| `JSONDecodeError` · 긴 Traceback 읽기 | `json.loads`에 JSON 규칙에 안 맞는 글자(작은따옴표 등)를 주면 나는 에러. `ValueError`의 한 종류라서 `except ValueError:`로도 잡힌다. Traceback에 `File` 줄이 여러 개면 **내 파일 줄은 맨 위 하나**, 아래는 파이썬 꾸러미 안(`/usr/lib/python3.12/json/…`). 맨 끝 줄의 이유 글 + `line 1 column 2` = 몇 번째 글자에서 막혔는지. | (연습) `practice/03_json.py` 14번째 줄 `json.loads("{'a': 1}")` → `Expecting property name enclosed in double quotes`. BuildMind: `mqtt_client.py:218` `except (ValueError, KeyError, TypeError): pass` — 로봇 쪽에서 깨진 JSON이 와도 여기서 잡혀 paho 스레드가 안 죽는다 |
| `A if 조건 else B` | 한 줄짜리 if. 조건이 참이면 A, 아니면 B를 값으로. | `bridge_codec.py:29` `ros_name[1:] if ros_name.startswith('/') else ros_name` |
| `글자[1:]` · `글자.startswith('/')` | 글자 자르기: 0번부터 세고 `[1:]`은 1번부터 끝까지(첫 글자 떼기). `startswith`는 그 글자로 시작하면 참. | `bridge_codec.py:29` ROS 이름 `/d2/…`의 맨 앞 `/` 떼기 |
| 상속 `class 자식(부모):` | 괄호 안 부모의 메서드를 다 물려받고, 자식이 다시 적은 메서드만 바꿔 끼운다. 부모 메서드 안의 `self.메서드()`는 **점 앞 물건이 누구냐**로 찾는다(자식 먼저, 없으면 부모). 어디에 적혀 있느냐는 상관없다. | `design_store.py:572` `class PgDesignStore(DesignStore):`. 부모 `get_design`(128) 안의 `self._load()`가 Pg판 물건이면 Pg `_load`(624, DB 읽기), JSON판이면 JSON `_load`(485, 파일 읽기). 연습 `practice/04_inherit.py` |

## 명령 · 도구

| 명령 · 도구 | 한 줄 설명 | BuildMind에서 나온 예 |
|---|---|---|
| uvicorn | 웹 서버 프로그램. 문(포트)을 열고 기다리다 요청이 오면 FastAPI `app`에 넘기고, 답을 브라우저에 돌려준다. FastAPI는 '어떤 요청에 어떤 답'을 적는 쪽. | backend 띄우기 `python3 -m uvicorn app:app --host 127.0.0.1 --port 8000` |
| `python3 -m 꾸러미` | 설치된 꾸러미를 이름으로 실행한다(`python3 파일.py`는 파일을 실행). | `python3 -m uvicorn` |
| `파일:변수` | uvicorn에게 어느 파일의 어느 변수를 띄울지 알려 준다. | `app:app` = `app.py` 144번째 줄 `app = create_app()` |
| `--옵션 값` | 명령 뒤에 붙여 그 프로그램에 넘기는 설정. | `--host 127.0.0.1`(이 PC 안에서만 = localhost) · `--port 8000`(8000번 문) |
| `이름=값 명령` · `export 이름=값` | 환경 변수 주기. 앞의 것은 그 명령 하나에만, `export`는 그 터미널을 닫을 때까지. 코드 · 설정 파일은 안 바뀐다. | `MQTT_HOST=localhost python3 -m uvicorn …` |
| paho (`import paho.mqtt.client as mqtt`) | 파이썬에서 MQTT를 쓰게 해 주는 남이 만든 꾸러미. 붙기 · 구독 · 보내기를 다 해 주고 `MqttClient`는 그 위에 BuildMind 모양으로 한 겹 감싼 것. `loop_start()`가 소식 받는 스레드를 띄운다. | `mqtt_client.py:12` |
| `connect_async` vs `connect` | `connect`는 붙을 때까지 그 줄에서 기다림. `connect_async`는 "붙어 봐" 시켜만 놓고 다음 줄로(비동기 = 기다리지 않고 나중에). 실제 붙기는 `loop_start()` 스레드가. | `mqtt_client.py:87` 브로커가 없어도 backend는 먼저 떠야 하니까 |
