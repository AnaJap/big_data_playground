# -*- coding: utf-8 -*-
"""spark.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1keMDpJq95gAvpxFsI5Qeh5DvCU5Jas-A

SparkSession
"""

from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, split, lit, array_except, length, size, array, explode, count, array_remove
from pyspark.sql.types import *



if __name__ == "__main__":

	app_name = 'DataEngineering'

	spark = SparkSession \
	      .builder \
	      .appName(app_name) \
	      .getOrCreate()\

	sc = spark.sparkContext

	rdd = sc.parallelize([1, 2, 3, 4, 5])

	# rdd.collect()
	print('##### Fold result: ' + str(rdd.fold(zeroValue=100, op=lambda x, y: x+y)))

	rdd2 = sc.parallelize(list('ABCDAAA'))

	# rdd.collect()
	rdd2.map(lambda x: (x, 1)).foldByKey(zeroValue=100, func=lambda x, y: x+y).collect()



	df = sc.parallelize([('A B.C:D!E?FGH', 1)]).toDF(['col1', 'col2'])

	res = df.select('col1')\
		    .withColumn('Words', split(col('col1'), ' |\.|,|\:|\!|\?'))
	
	res.show()
	# res.write.mode('append').format('csv').save('/airflow/jobs/result')

	print('##### Helloooooo there')
	spark.stop()