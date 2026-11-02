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
| `a, b = x, y` (여러 개 한꺼번에 넣기) | 왼쪽 이름들과 오른쪽 값들을 순서대로 짝지어 한 줄에 넣는다. 오른쪽을 **먼저 다 계산**한 뒤 넣으므로 `a, b = b, a`는 임시 변수 없이 서로 바꾸기. | `mqtt_client.py:62` `self.host, self.port = host, int(port)` · 70 · 264. 연습 `practice/05_multi_assign.py`(4/4 맞힘) |
| `with 잠금:` (`threading.Lock()`) | 스레드가 여럿일 때 같은 딕셔너리를 **베끼는 일과 새 칸 붙이는 일이 동시에 일어나지 않게** 줄 세운다. `with` 줄에 온 스레드는 잠겨 있으면 거기서 기다리고, 안의 스레드가 들여쓰기를 나오면(에러가 나도) 자동으로 풀린다. 만지는 **모두가 같은 자물쇠**를 써야 효과 있음. 잠금 안에는 꼭 필요한 몇 줄만. `with open(...)`과 같은 문법(들어갈 때 열고 나올 때 반드시 닫기). | `mqtt_client.py:68` `self._lock = threading.Lock()` · `snapshot` 122(베끼기) · `_on_blob` 262(붙이기) 등 10번. 안 잠그면 `snapshot` 123이 `self.state`를 훑는 중 `_on_blob` 270이 칸을 추가 → `RuntimeError: dictionary changed size during iteration`. 연습 `practice/06_with_lock.py`(일꾼 둘 → 잠금 없으면 1, 있으면 2) · `07_dict_while_iter.py`(에러 재현). 06의 `global` · `t.join()`(끝날 때까지 기다림) · `fn.__name__`은 연습용 장치 |
| 딕셔너리 훑는 중 칸 추가 | `for k in 딕셔너리:`로 훑는 도중에 새 키를 넣으면 `RuntimeError: dictionary changed size during iteration`. 스레드 하나로도 난다. | `practice/07_dict_while_iter.py`. BuildMind에서는 잠금으로 막음(위 줄) |
| `A or B` 를 값으로 쓰기 | `or`는 참/거짓이 아니라 **두 값 중 하나를 그대로** 돌려준다: A가 비어 있지 않으면 A, 비어 있으면(`None` · `0` · `""` · `[]` · `{}` · `False`) B. `if` 안에서 "A 또는 B가 참"으로 쓰이는 것도 같은 규칙의 결과. "안 줬으면 기본으로 만들어라" 패턴. | `mqtt_client.py:77` `self.client = client or make_mqtt_client(CLIENT_ID)` — pytest가 `client=FakePaho()`를 주면 가짜, `app.py:108`은 안 주니(`None`) 진짜 paho. `app.py:108` `mqtt = mqtt or MqttClient(...)`도 같은 꼴. 연습 `practice/08_or_value.py`(6/6 맞힘) |
| `[만들 것 for 이름 in 목록]` (리스트 컴프리헨션) | 목록을 하나씩 꺼내 바꿔서 **새 목록**을 한 줄로 만든다. `out=[]` · `for` · `append` 세 줄과 같은 일, 다만 '바꾸기'를 맨 앞에 적는다. | `mqtt_client.py:134` `[res_topic(n) for n in WEB_CALLS]` — ROS 이름 4개 → 응답 칸 이름 4개. 연습 `practice/11_list_comp.py`(맞힘) |
| `list(딕셔너리)` · 목록 `+` 목록 | `list(딕셔너리)`는 **키만**(콜론 왼쪽) 뽑아 목록으로. 값은 안 나온다. 목록끼리 `+`는 이어 붙이기. 줄 끝 `\`는 "다음 줄에 이어 씀" 표시일 뿐. | `mqtt_client.py:133` `list(STATE_TOPICS)` — 키 = 우체국(브로커) 칸 이름(토픽), 값 = 화면용 꼬리표. 구독에는 칸 이름이 필요해서 키. 연습 `practice/12_list_of_dict.py`(처음엔 키를 값이라 부름 → 표로 바로잡음) |

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
