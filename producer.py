
from google.cloud import storage
import csv
import json
from kafka import KafkaProducer

# Initialize Google Cloud Storage client
client = storage.Client.from_service_account_json('tourist attractions\key.json')

# Initialize Kafka producer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Load state-attractions data from CSV file
bucket_name = 'attraction12'
blob_name = 'attractions.csv'
bucket = client.get_bucket(bucket_name)
blob = bucket.blob(blob_name)
data = blob.download_as_string().decode('utf-8').splitlines()
reader = csv.reader(data)
attractions = {}
for row in reader:
    if row[0] not in attractions:
        attractions[row[0]] = []
    attractions[row[0]].append(row[1])

# Send state-attractions data to Kafka topic
for state, attractions in attractions.items():
    producer.send('attractions', value={'state': state, 'attraction': attractions})

producer.flush()

