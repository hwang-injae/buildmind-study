# BuildMind 코드 노트

## 큰 그림 (2단계 · 클래스 · 함수 목록)

### `web/backend/mqtt_client.py` (332줄) — 10/28
함수 1개 `make_mqtt_client`(44) + 클래스 1개 `MqttClient`(52, 메서드 26개). 역할별 7묶음:
| 묶음 | 메서드 |
|---|---|
| ① 켜고 끄기 | `__init__`(60) · `start`(84) · `stop`(91) |
| ② 상태 물어보기 | `connected`(103) · `bridge_connected`(107) · `_fresh`(112) · `snapshot`(117) |
| ③ 브로커(paho)가 부르는 콜백 | `_on_connect`(129) · `_on_disconnect`(138) · `_on_message`(194) |
| ④ 살아있음 신호 | `_alive_loop`(143) · `check_bridge`(150) · `_on_bridge_alive`(306) |
| ⑤ 웹 → 로봇 (routes · app이 부름, 밑줄 없음) | `request`(160) · `listen`(175) · `blob`(184) · `serve`(189) |
| ⑥ 로봇 → 웹 소식 종류별 처리 (`_on_message`가 나눠 줌) | `_on_state`(221) · `_progress_stale`(246) · `_on_blob`(256) · `_on_preview`(273) · `_on_preview_cloud`(290) · `_answer_robot`(317) |
| ⑦ 화면에 알리기 | `_emit`(329) |
부르는 쪽: `routes/robot.py`(request · snapshot · blob · bridge_connected) · `routes/ws.py`(snapshot) · `routes/voice.py`(listen) · `app.py`(serve · start · stop, lifespan 118~126)

### `web/backend/design_store.py` (724줄) — 10/30
로봇과 무관한 **창고**: 설계 · 조립 기록을 디스크에 저장하고 꺼내 준다. 모듈 함수 3 + 클래스 2(`DesignStore` = JSON 폴더, `PgDesignStore(DesignStore)` = PostgreSQL 판). app.py가 `.env`에 `DATABASE_URL`이 있으면 Pg, 없으면 JSON 폴더.
길: 화면 "목록" → `list_designs` → 하나 고름 → `get_design` → 로봇 "설계 줘" → `answer_get_design` → 조립 끝 → `answer_save_build` → `save_build`
| 묶음 | 메서드 |
|---|---|
| ① 모듈 함수(이름 자르기 · 요약) | `family_of`(43) · `split_design_id`(53) · `build_summary`(61) |
| ② 켜기 | `__init__`(81) · `register_bases`(94) · `register_base`(110) |
| ③ 읽기(밖에서 부름) | `get_design`(128) · `list_designs`(140) · `children`(150) · `builds_for`(154) · `examples_for`(159) · `match_scan`(172) · `templates`(222) · `base_recipe`(239) |
| ④ 쓰기(밖에서 부름) | `new_design_id`(295) · `save_design`(315) · `set_display_name`(404) · `save_build`(433) · `save_gen_log`(447) |
| ⑤ 로봇 요청에 답하기 | `answer_get_design`(456) · `answer_save_build`(465) — `app.py:111-112` `mqtt.serve(...)`로 연결 |
| ⑥ 조수(밑줄) | `_checked`(133) · `_bottom_center`(211) · `_rows`(248) · `_size_mm`(284) · `_mark_gen_log`(366) · `_check_template`(380) · `_template_or_none`(387) · `_template_number`(395) · `_design_path`(543) · `_safe`(551) · `_write`(558) |
| ⑦ 창고 문(디스크 접근, 밑줄) | JSON판: `_load`(485) · `_has`(492) · `_ids`(499) · `_designs`(503) · `_put_base`(513) · `_insert_design`(517) · `_set_display`(525) · `_builds`(271) · `_insert_build`(535). **Pg판이 같은 이름을 SQL로 바꿔 끼움**(624~718) + `_db`(600, `@contextmanager`) · `_row`(612) |
부르는 쪽: `routes/designs.py` · `design_gen.py` · `voice.py`(③ ④) · `app.py`(`register_bases` · `serve` 연결)
새 문법(나올 때): 상속 `class PgDesignStore(DesignStore)` · `@staticmethod` 7개 · `@contextmanager` 1개 · `re.compile`(정규식) · `Path`

### `web/backend/design_gen.py` (905줄) — 10/30
AI(Claude)에게 설계를 만들어 달라고 **묻는 한 곳**. 로봇 없음. 클래스 2(`GenError(Exception)` = 실패 종류 봉투, `DesignGenerator` = 본체, 메서드 30) + 모듈 함수 2.
길([AI 설계] 버튼): 화면 글 → `routes/designs.py:114` → `generate(text, base_id)` → ① store에서 바탕 설계 읽기 → ② 중계(`claude_bridge.py`)에 OpenAI 형식으로 묻기 → 후보 3개 → ③ `store.new_design_id` + 검사(`check`) → ④ 떨어진 건 이유 알려 다시(최대 2번) → 합격 후보만 화면에 → 사람이 하나 고름 → `save(result, index)` → `store.save_design`. 스캔 [저장]은 `save_scan` → `scan_fill`(AI가 빈 칸 채움) → 검사 → 저장.
| 묶음 | 메서드 |
|---|---|
| ① 바깥 작은 것 | `GenError`(79) · `scan_actions`(89) · `load_grasp_options`(95) |
| ② 켜기 · 설정 | `__init__`(114) · `client`(135, `@property`) · `templates`(150) · `ai_judgment`(165) |
| ③ 큰 길(밖에서 부름) | `generate`(176) · `save`(308) · `scan_fill`(327) · `save_scan`(474) |
| ④ AI에게 묻기 | `_read_and_answer`(537) · `_tool_answer`(572) · `_chat`(592) · `_parse`(638) · `_tool`(861) · `_candidates_format`(872) · `_format`(889) |
| ⑤ 검사 · 떨어진 이유 | `_check`(650) · `_row_grasp`(675) · `_no_pass_error`(699) · `_feedback`(715) · `_where`(741) · `_moved`(524) |
| ⑥ 프롬프트 글 만들기 | `_request_text`(773) · `_template_rules`(788) · `_row_line`(841) · `_examples_text`(850) |
| ⑦ 기록(NFR-17) | `_new_log`(894) · `_save_log`(899) → `store.save_gen_log` |
부르는 쪽: `routes/designs.py`(generate · save · save_scan · templates) · `app.py`(만들기). 안에서 쓰는 것: `store`(창고) · `check`(검사 묶음) · OpenAI 라이브러리(주소만 중계로).
새 문법(나올 때): `class GenError(Exception)` = 예외도 클래스라 상속으로 만든다 · `@property` · `@staticmethod` 9개 · `**kw` · `yaml`

### `web/claude_bridge.py` (408줄) — 10/30
**중계**: `design_gen`이 OpenAI 형식으로 보낸 HTTP 요청을 받아, 웹 PC 호스트에 로그인된 Claude Code(`claude -p`)를 명령으로 실행해 답을 받고, 다시 OpenAI 형식으로 포장해 돌려준다. 백엔드는 도커 컨테이너 안, 이 파일은 호스트(컨테이너 밖)에서 따로 켠다(`python3 web/claude_bridge.py --host 172.17.0.1`). API 키 없음(로그인 계정 한도). 클래스 3 + 모듈 함수 4.
길(Claude에게 한 번 묻기): `design_gen._chat` → HTTP `/v1/chat/completions` → `make_handler`(184) → `ClaudeBridge.complete`(82) → `transcript`(대화를 한 글로) → `_ask`(137) → `_run`(158, `claude -p --json-schema …` 실행, 240초 상한) → `_response`(173, OpenAI 모양 포장) → JSON 답
| 묶음 | 함수 · 메서드 |
|---|---|
| ① 바깥 작은 것 | `is_usage_limit`(43, 한도 글인지) · `BridgeError(Exception)`(50) · `find_claude`(59, claude 명령 위치 찾기) |
| ② 중계 본체 `ClaudeBridge` | `complete`(82) · `model_of`(110) · `transcript`(116) · `_forced_tool`(129) · `_ask`(137) · `_run`(158) · `_response`(173) |
| ③ 웹 서버 문 | `make_handler`(184) — 파이썬 기본 `http.server`로 요청 받기(FastAPI 아님) |
| ④ 준비 점검 `SetupCheck` (`--check`) | `run`(250) · `used_flags` · `_flags` · `_login` · `_address` · `_health` · `_container` · `_cmd` · `_fetch` · `report`(364) |
| ⑤ 켜기 | `main`(377) — argparse `--host` · `--port` · `--model` · `--check` |
부르는 쪽: 아무 파이썬도 import하지 않는다 — `design_gen`이 **HTTP로** 부른다(`D2_LLM_URL`). 시험: `tests/`에 가짜 `run`을 넣어 claude 없이 돈다(`run=None` 인자)
팀 결정: RUN_TIMEOUT_S 240 < design_gen 260 — 중계가 먼저 끊어야 claude가 혼자 남지 않고 화면에 504 이유가 간다(10/13 PL)
새 문법(나올 때): `subprocess`(다른 명령 실행) · `http.server` · `tempfile` · `**kw`

### `src/d2_bridge/d2_bridge/bridge_node.py` (408줄) — 10/30
로봇 PC 쪽 **다리(브리지)**. `mqtt_client.py`의 거울: 웹 PC에는 ROS가 없으니, 이 노드가 ROS 2 ↔ MQTT 브로커 사이를 **번역만** 한다(판단 없음, 로봇 직접 안 움직임, 죽어도 로봇 PC 안 정지는 그대로 — E-30). 클래스 1 `MqttBridge(Node)`(ROS 2 Node 상속, 메서드 20) + 모듈 함수 3 + `main`.
길([정지] 버튼, 10/28 bridge_codec 6단계의 다리 쪽): MQTT `d2/safety/stop/req` 도착 → `_on_message`(280) → `_call_robot`(306, ROS 서비스 호출) → 정지 노드 답 → `_on_robot_answer`(333) → MQTT `…/res`에 `typed_response` 발행
반대 길(로봇 "설계 줘"): ROS 서비스 `/d2/hmi/get_design` 호출 들어옴 → `_ask_web`(352) → MQTT `…/req` 발행 → 웹 `mqtt_client.serve`가 답 → `…/res` → `_on_reply`(378) → ROS 서비스 응답
| 묶음 | 함수 · 메서드 |
|---|---|
| ① 바깥 작은 것 | `load_robot_yaml`(62) · `encode_jpeg`(69) · `make_mqtt_client`(77) |
| ② 켜고 끄기 | `__init__`(96) · `start`(136) · `close`(142) · `main`(389) |
| ③ 브로커(paho) 콜백 | `_on_connect`(153) · `_on_disconnect`(170) · `_on_message`(280) |
| ④ 살아있음 | `_send_alive`(181) → `d2/bridge/alive` (mqtt_client `_on_bridge_alive`가 받음) |
| ⑤ 로봇 → 웹 (ROS 구독 → MQTT 발행) | `_on_state`(186) · `_on_scan_preview`(252) · `_send_scan_media`(194) · `_read_scan_image`(218) · `_read_scan_cloud`(240) · `_on_wrist_image`(275) · `_publish`(175) · `_forward`(299) |
| ⑥ 웹 → 로봇 (MQTT req → ROS 서비스 → res) | `_call_robot`(306) · `_on_robot_answer`(333) · `_reply_fail`(346) |
| ⑦ 로봇 → 웹 요청 (ROS 서비스 서버 → MQTT req → 웹 res) | `_ask_web`(352) · `_on_reply`(378) |
상수: `STATE_TOPICS`(36, 로봇→웹 상태 5개 · 모두 retained) · `WEB_CALLS`(44, 웹이 부르는 서비스) · `ROBOT_CALLS`(50, 로봇이 부르는 get_design · save_build) · `CLIENT_ID`(57, 다리는 하나뿐) · `MQTT_KEEPALIVE_S`(58)
시험: ROS import(`rclpy` · `d2_interfaces`)가 있어 이 PC에선 `colcon build` 뒤에만 돈다(teacher.md 10/28). 번역 규칙 자체는 `bridge_codec.py` 시험 22개가 로봇 없이 확인
새 문법(나올 때): `class MqttBridge(Node)` 상속 · `functools.partial` · ROS 2 용어(Node · 서비스 · QoS · executor) · `future`

## 함수 설명 (내 말로)

## 고치고 싶은 것
- [ ] **Next.js 16.4.0 보안 경고** (`web/frontend/package.json:14` `"next": "16.4"`). 10/26 `npm ci` 때 16.0.0 ~ 16.4.0 critical 3건(이미지 최적화 · Server Actions · `use cache`). 셋 다 Next.js 서버 기능인데 BuildMind는 `next.config` `output: 'export'`라 Next.js 서버가 안 떠서 로컬 실행 영향 적음. 고치는 법: `npm audit`이 알려 주는 판으로 올림 → `npm install` → `npm run build` → 띄워서 화면 확인 → 커밋 → 내 포크에 push. 날짜는 미정(파이썬 6개 뒤).
- [ ] **`mqtt_client.py:218` 깨진 소식을 조용히 버림** (`except (ValueError, KeyError, TypeError): pass`). 이 파일엔 로그가 한 줄도 없어서 로봇 PC가 깨진 JSON을 보내도 아무 흔적이 없다. 삼키는 것 자체는 맞음(안 삼키면 paho 1.6.1이 예외를 다시 던져 소식 받는 스레드가 죽음). 후보: `except … as e:` 뒤에 `log.warning(토픽, e)` 한 줄. README · docs 결정 기록에서 근거 못 찾음(10/30). `mqtt_client.py` 본 공부 때 '이상한 코드' 순서로 — `try:` 밖에 있는 `_on_blob` · 미리보기 길 문제와 같이.
