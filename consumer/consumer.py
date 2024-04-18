from kafka import KafkaConsumer
import json 
import io
import avro.io
import avro.schema

with open('config.json', 'r') as f:
    config = json.load(f)

# define the consumer to read from the Kafka topic

# define kafka servers from the config file (KAFKA_SERVER variable)
kafka_servers=[config['KAFKA_SERVER'] + config['KAFKA_PORT']
consumer = KafkaConsumer(
    config['KAFKA_TOPIC_NAME'],
    bootstrap_servers = kafka_servers,
    api_version=(0, 10, 1)
    )

# define the Avro schema that corresponds to the encoded data
schema = avro.schema.parse(open('trades.avsc').read())

for message in consumer:
    # asssume 'byte_string' contains the Avro-encoded byte string,
    # we need to decode it using avro library
    bytes_reader = io.BytesIO(message.value)
    decoder = avro.io.BinaryDecoder(bytes_reader)
    reader = avro.io.DatumReader(schema)
    data = reader.read(decoder)
    print(data)
    
