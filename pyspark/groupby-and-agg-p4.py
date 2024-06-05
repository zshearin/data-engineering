from pyspark.sql import SparkSession

spark =SparkSession.builder.appName('Agg').getOrCreate()

df_spark=spark.read.csv('groupby-and-agg.csv',header=True,inferSchema=True)

# df_spark.show()
df_spark.printSchema()


## GROUP BY
# df_spark.groupBy('Name') # returns data type of GroupedData
# grouped to find the maximum salary:
# df_spark.groupBy('Name').sum().show() # use group by with aggregate functions 

# groupby department
# df_spark.groupBy('Departments').sum().show()
# df_spark.groupBy('Departments').mean().show()
# df_spark.groupBy('Departments').count().show()

df_spark.agg({'Salary': 'sum'}).show()

