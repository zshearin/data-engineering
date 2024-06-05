from pyspark.sql import SparkSession

spark=SparkSession.builder.appName('Dataframe').getOrCreate()

## read the dataset
# inferSchema - interprets schema from data set (would all be strings otherwise)
# df_pyspark=spark.read.option('header', 'true').csv('test2.csv', inferSchema=True)
df_pyspark=spark.read.csv('basic.csv', header=True, inferSchema=True)
df_pyspark.show()

## Check the schema
df_pyspark.printSchema()
dataType = type(df_pyspark)

# Get columns
columnList = df_pyspark.columns

# get 1 column from data set
df_pyspark.select('Name').show()

# get mulitple columns from data set - without .show() is dataframe object
df_pyspark.select(['Name', 'Age']).show()

#show data types of columns in dataframe
df_pyspark.dtypes

# show description metrics about the given data frame
df_pyspark.describe().show()

# add columns into data frame (reassigning it to that variable makes it that variable again)
newColumnName = 'Experience After 2 years'
df_pyspark=df_pyspark.withColumn(newColumnName, df_pyspark['Experience']+2)

# drop column from data frame 
df_pyspark=df_pyspark.drop(newColumnName)

# rename the columns - changing name column to first name
df_pyspark.withColumnRenamed('Name', 'First Name').show()