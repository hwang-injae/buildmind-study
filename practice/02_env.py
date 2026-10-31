import os
host = os.environ.get("MQTT_HOST", "localhost")
print("브로커 주소:", host)
