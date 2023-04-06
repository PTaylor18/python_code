import json
from confluent_kafka import Producer
from confluent_kafka.serialization import SerializationContext, MessageField
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.json_schema import JSONSerializer
from read_config import read_ccloud_config

from config import config, sr_config

with open("order_schema.json", mode="r") as f:
    schema_str = json.load(f)
    schema_str = json.dumps(schema_str, indent=2)

def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" %
              (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))
        print(
            f"Topic: {msg.topic()}\nPartition: {msg.partition()}\nOffset: {msg.offset()}\nTimestamp: {msg.timestamp()[1]}"
        )


def order_producer(key, message):
    topic = "orders"
    schema_registry_client = SchemaRegistryClient(sr_config)

    json_serializer = JSONSerializer(schema_str, schema_registry_client)

    producer = Producer(config)
    producer.produce(topic, key=key,
                     value=json_serializer(message,
                                           SerializationContext(topic, MessageField.VALUE)),
                     callback=acked)
    producer.flush()

# send a kafka message which has order id as the key and the value is a json file of the cart, price, payment success ...
