#!/bin/bash

spark-submit --master spark://master:7077 \
    --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.1,\
    org.apache.spark:spark-avro_2.12:3.2.1,\
    com.datastax.spark:spark-cassandra-connector_2.12:3.2.0 \
    main.py