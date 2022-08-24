from kafka import KafkaConsumer

consumer = KafkaConsumer('test', bootstrap_servers=['localhost:51820'], auto_offset_reset='earliest')
for message in consumer:
    print (message.value)

consumer.close()

