from pyspark.sql import SparkSession

spark=SparkSession.builder.appName('Practice').getOrCreate()
df_spark=spark.read.csv('missing-vals.csv', header=True,inferSchema=True)
df_spark.show()

# df_spark.drop('Name').show()

# handling null values
# on `na` data object, you have `drop`, `fill` and `replace`

# drops any row with a null value anywhere:
# df_spark.na.drop().show()

## How param:

# Drop rows where all the values are null:
# df_spark.na.drop(how='all')
# Drop rows where any of the values are null:
# df_spark.na.drop(how='any')

# Thresh param (threshold for how many non null values are required)
# df_spark.na.drop(how="any", thresh=2).show()

## Subset param
# deletes any rows where the value for column 'Experience' is null
# df_spark.na.drop(how="any", subset=['Experience'] ).show()

## Fill the missing value
# fills all null values with the value 'Missing Values'
# df_spark.na.fill('Missing Values').show()
# fills all null values in column 'Experience' with 'Not Specified'
# df_spark.na.fill('Not Specified', 'Name').show()

# strange I ran into weird error fixed by this:
# https://stackoverflow.com/questions/69919970/no-module-named-distutils-but-distutils-installed
from pyspark.ml.feature import Imputer

imputer = Imputer(
    inputCols=['Age', 'Experience', 'Salary'],
    outputCols=["{}_imputed".format(c) for c in ['Age', 'Experience', 'Salary']]
    ).setStrategy("mean") # can use median, mode, etc

imputer.fit(df_spark).transform(df_spark).show()

## Paused at 44:00 in the video here: https://www.youtube.com/watch?v=_C8kWso4ne4&ab_channel=freeCodeCamp.org


