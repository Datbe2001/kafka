# kafka
- run: docker compose up
- bash container: docker exec -it <container name> bash
- list topic: kafka-topics.sh --bootstrap-server localhost:9092 --list
- detail topic: kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic <topic name>
- create topic: kafka-topics.sh --bootstrap-server localhost:9092 --create --topic <topic name> --partitions 3 --replication-factor 1
- delete topic: kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic <topic name>
