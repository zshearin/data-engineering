from pyspark.sql import SparkSession
spark=SparkSession.builder.appName('Missing').getOrCreate()


trainingData = spark.read.csv('machine-learning.csv', header=True,inferSchema=True)
#trainingData.show()
#trainingData.printSchema()
#trainingData.columns # is an array of the columns

# Creating inputs and output
from pyspark.ml.feature import VectorAssembler
featureAssembler=VectorAssembler(inputCols=["Age","Experience"],outputCol="Independent Features")
output=featureAssembler.transform(trainingData)
# output.show()
# output.columns

finalizedData=output.select("Independent Features", "Salary")
# finalizedData.show()

# Creating a model to predict salary based on age and experience
from pyspark.ml.regression import LinearRegression
## train test split
# means train_data will take 75% of the data, and test_data will take 25%
train_data,test_data = finalizedData.randomSplit([0.75,0.25])
regressor=LinearRegression(featuresCol="Independent Features", labelCol='Salary')
regressor=regressor.fit(train_data)

# print(regressor.coefficients)
# print(regressor.intercept)

pred_results=regressor.evaluate(test_data)

# pred_results.predictions.show()
print(pred_results.meanAbsoluteError)
print(pred_results.meanSquaredError)