import json
from kafka import KafkaConsumer

# Initialize Kafka consumer
consumer = KafkaConsumer('attractions',
                         bootstrap_servers=['localhost:9092'],
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))
# Retrieve state-attractions data from Kafka topic based on user input
state = input("Enter a state: ")
for message in consumer:
    data = message.value
    if data['state'].lower() == state.lower():
        print(data['attraction'])
