kcat -b localhost:51820,localhost:51825,localhost:51826 -t test -P -l -K: sample
kcat -b localhost:51820 -t test -P -K: -p 1
kcat -P -b localhost:51820 -t test

rpk topic create products --brokers localhost:53663

kcat -C -b localhost:53663 -t products -o beginning


docker-compose up -d
docker-compose down 

---



### Important

Change the Broker info in Python file, regenrate the docker

    rpk container start -n 1
    rpk topic create temperatures --brokers localhost:53427,localhost:53433,localhost:53432
    rpk container purge
    kcat -C -b localhost:53427,localhost:53433,localhost:53432 -t temperatures -o beginning

    kcat -C -b localhost:52785 -t testing -o beginning
    kcat -P -b localhost:52785 -t testing


    set env KAFKA_BROKERS=host.docker.internal:51209,host.docker.internal:51214,host.docker.internal:51215

#### Kowl UI

    docker run --network=host -p 8080:8080 -e KAFKA_BROKERS=localhost:54595,localhost:54601,localhost:54600 docker.redpanda.com/vectorized/console:latest
    docker run -p 8080:8080 -e KAFKA_BROKERS=localhost:54595,localhost:54601,localhost:54600 docker.redpanda.com/vectorized/console:latest

    docker run -p 8080:8080 -e KAFKA_BROKERS=host.docker.internal:9093 docker.redpanda.com/vectorized/console:latest

----
https://github.com/rickhysis/kafka-python-example


