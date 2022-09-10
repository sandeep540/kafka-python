#!/usr/bin/env python
import time
import schedule
import random
import uuid
import datetime;

from kafka import KafkaProducer
from json import dumps  
from kafka.admin import KafkaAdminClient, NewTopic

kafka_nodes=['localhost:9092','localhost:9093','localhost:9094']
myTopic = 'input'

admin_client = KafkaAdminClient(
    bootstrap_servers=kafka_nodes, 
    client_id='python-test-01'
)
topics = []
topics = admin_client.list_topics()
print("List of topics -----> ", topics)


if myTopic not in topics:
    # create topic
    print("Creating topic as it does not exist")
    topic_list = []
    topic_list.append(NewTopic(name=myTopic, num_partitions=1, replication_factor=1))
    admin_client.create_topics(new_topics=topic_list, validate_only=False)


def gen_data():

    # Producer instance
    my_data = {'temperature' : random.randint(75, 200), 'id' : str(uuid.uuid4()), 'date': str(datetime.datetime.now())}
    prod = KafkaProducer(bootstrap_servers=kafka_nodes,value_serializer = lambda x:dumps(x).encode('utf-8'))
    print(my_data)
    prod.send(topic=myTopic, value=my_data)
    prod.flush()

if __name__ == "__main__":

    gen_data()
    schedule.every(2).seconds.do(gen_data)

    while True:
        schedule.run_pending()
        time.sleep(1)