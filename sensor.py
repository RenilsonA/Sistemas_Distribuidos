import os
from google.cloud import pubsub_v1

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "publisher.json"
topic_path = "projects/emergency-398719/topics/factory"
publisher = pubsub_v1.PublisherClient()

# Mensagem a ser publicada
SENSOR_MACHINE_1 = 1
SENSOR_MACHINE_2 = 2
SENSOR_TEMPERATURE = 3
SENSOR_PRESSURE = 4
SENSOR_GAS = 5
level = [1, 2, 3, 4, 5]
buffer = "ksdjhdglkjsdklfj"

# Publica a mensagem no tópico
future = publisher.publish(topic_path, buffer)
print(future.result())