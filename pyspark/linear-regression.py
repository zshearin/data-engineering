from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.regression import LinearRegression

spark=SparkSession.builder.appName('Missing').getOrCreate()
# File location and type
file_location = "tips.csv"
file_type = "csv"

# CSV options
infer_schema = "true"
first_row_is_header = "true"
delimiter = ","

# The applied options are for CSV files. For other file types, these will be ignored.
df = spark.read.format(file_type) \
  .option("inferSchema", infer_schema) \
  .option("header", first_row_is_header) \
  .option("sep", delimiter) \
  .load(file_location)

# df.printSchema()
# df.columns

# change categorical variables to ordinal (e.g. column with values ["Male", "Female"] -> [0, 1])
# one column:
indexer=StringIndexer(inputCol="sex",outputCol="sex_i")
df_r=indexer.fit(df).transform(df)
# df_r.show()

# multiple columns:
indexer=StringIndexer(inputCols=["smoker","day","time"],outputCols=["smoker_i","day_i","time_i"])
df_r=indexer.fit(df_r).transform(df_r)
# df_r.show()
# df_r.columns

# put independent variables all in a single vector:
featureAssembler=VectorAssembler(inputCols=['tip', 'size','sex_i', 'smoker_i', 'day_i', 'time_i'], outputCol='Independent Variables')
output=featureAssembler.transform(df_r)
# output.show()

output.select('Independent Variables').show()

finalized_data=output.select('Independent Variables','total_bill')

## train test split
train_data, test_data = finalized_data.randomSplit([0.75,0.25]) #randomly splits, 75% to train_data and 25% to test_data
# create linear regression object
regressor=LinearRegression(featuresCol='Independent Variables',labelCol='total_bill')
# create linear regression fit line based on train_data
regressor=regressor.fit(train_data)

# take a look at the results 
print(regressor.coefficients)
print(regressor.intercept)

# evaluate model that's based on train_data using test_data
pred_results=regressor.evaluate(test_data)
# show results:
pred_results.predictions.show()
print("r^2 value: %.6f" % (pred_results.r2))
print("mean absolute err: %.3f" % (pred_results.meanAbsoluteError))
print("mean squared err: %.3f" % (pred_results.meanSquaredError))


