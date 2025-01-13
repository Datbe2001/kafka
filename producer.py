import datetime

from kafka import KafkaProducer
import json

# Tạo producer Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

event_data = {
    "event_time": str(datetime.datetime.now())
}

# Callback để in thông tin phân phối
def on_success(metadata):
    print(f"Message sent to topic: {metadata.topic}, partition: {metadata.partition}, offset: {metadata.offset}")

def on_error(exception):
    print(f"Message failed to send: {exception}")

# Gửi 10 messages và kiểm tra partition
for _ in range(10):
    future = producer.send('test-topic-1', value=event_data)
    future.add_callback(on_success).add_errback(on_error)

# Đảm bảo tất cả messages được gửi đi
producer.flush()
producer.close()
