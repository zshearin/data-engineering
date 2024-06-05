from pyspark.sql import SparkSession

spark=SparkSession.builder.appName('dataframe').getOrCreate()

df_spark = spark.read.csv('filters.csv', header=True, inferSchema=True)
# df_spark.show()

## Filter operations

## salary of people less than 50k:

# df_spark.filter("Salary<= 50000").show()
# df_spark.filter("Salary<= 50000").select(['Name', 'Age']).show()

# multiple filter operations
# df_spark.filter((df_spark['Salary']<50000) & 
                # (df_spark['Salary']>=40000)).show()


# not operation (it's this character: ~):
df_spark.filter(~(df_spark['Salary']<50000)).show()

