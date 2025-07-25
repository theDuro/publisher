import json
import time
import paho.mqtt.client as mqtt

broker = "74.248.76.140"  # Azure broker IP
port = 1883
topic = "maszyna/dane"

payload = {
    "machine_id": 1,
    "is_running": True,
    "has_error": False,
    "cycle_completed": 42,
    "tag1": 14.34,
    "tag2": 56.78,
    "tag3": 910.12,
    "tag4": 34.56
}

def on_connect(client, userdata, flags, rc):
    print("✅ Połączono z brokerem" if rc == 0 else f"❌ Błąd połączenia: {rc}")

def on_publish(client, userdata, mid):
    print(f"📤 Wiadomość opublikowana")

client = mqtt.Client(protocol=mqtt.MQTTv311)  # MQTT v3.1.1
client.on_connect = on_connect
client.on_publish = on_publish

try:
    client.connect(broker, port, 60)  # timeout keepalive 60s
    client.loop_start()
    client.publish(topic, json.dumps(payload))
    time.sleep(2)  # Poczekaj, aby mieć pewność, że wiadomość została wysłana
    client.loop_stop()
    client.disconnect()
except Exception as e:
    print("❌ Błąd połączenia:", e)