from kafka import KafkaConsumer
import json

# Tạo Kafka Consumer
consumer = KafkaConsumer('test-topic',
                         bootstrap_servers='localhost:9092',
                         auto_offset_reset='earliest',
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

# Nhận tin nhắn từ topic 'test-topic'
for message in consumer:
    print(f'Received: {message.value}')
