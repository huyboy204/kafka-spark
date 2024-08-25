import findspark

findspark.init()

import os
os.environ['PYSPARK_SUBMIT_ARGS']='--packages org.apache.spark:spark-streaming-kafka-0-10_2.13:3.4.0 pyspark-shell'

import sys
import time
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

n_secs = 1
topic = "seminar5"

conf = SparkConf().setAppName("Seminar5").setMaster("local[*]")
sc = SparkContext(conf=conf)
sc.setLogLevel("Warn")
ssc = StreamingContext(sc, n_secs)

kafkaStream=KafkaUtils.createDirectStream(ssc, [topic], {
    'bootstrap.servers':'192.168.10.90:9092',
    'group.id':'nhom',
    'fetch.message.max.bytes':'15728640',
    'auto.offset.reset':'largest'
})

lines =kvs.map(lambda x:x[1])
counts = lines.flatMap(lambda line:line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b)
counts.pprint()

ssc.start()
time.sleep(600)
ssc.stop(stopSparkContext=True, stopGraceFully=True)