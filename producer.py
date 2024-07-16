from kafka import KafkaProducer
import json

# Tạo Kafka Producer
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Gửi tin nhắn tới topic 'test-topic'
message = {'key': f'chào anh Đạt hehehe 2'}
producer.send('test-topic', value=message)
print(f'Sent: {message}')

producer.flush()
producer.close()
