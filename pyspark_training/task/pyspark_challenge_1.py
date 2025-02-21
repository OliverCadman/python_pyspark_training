from pyspark.sql import SparkSession
from pyspark.sql.functions import *
 
"""
[
    ("1", "Apple", "Large", "green"),
    ("2", "Apple", "Large", "yellow"),
    ("3", "Apple", "Large", "red"),
    ("4", "Apple", "small", "red"),
    ("5", "Apple", "small", "green"),
    ("6", "Apple", "Large", "red"),
    ("7", "Apple", "small", "yellow")
]
 
 
Using pyspark write a simple application that reads above data into a dataframe (structure above).
 
Columns after loading should be (id, fruit, size, colour)
 
- Add an extra column "test_apple" which is a boolean flag. If apple is small and red set it to 1, otherwise to 0
- remove any duplicates from the data
- filter out all rows where test_apple is set to 0
- save data locally to a json format
 
"""
 
spark = SparkSession.builder.appName("PySpark Challenge 1").getOrCreate()
 
data = [  
    ("1", "Apple", "Large", "green"),
    ("2", "Apple", "Large", "yellow"),
    ("3", "Apple", "Large", "red"),
    ("4", "Apple", "small", "red"),
    ("5", "Apple", "small", "green"),
    ("6", "Apple", "Large", "red"),
    ("7", "Apple", "small", "yellow")
]
 
columns = ["id", "fruit", "size", "colour"]
 
df = spark.createDataFrame(data, columns)
 
df_with_test_apple_col_df = df.withColumn(
    "test_apple",
    when((lower(col("fruit")) == "apple") & (lower(col("size")) == "small") & (lower(col("colour")) == "red"), 1)
    .otherwise(0)
)
 
# df_with_test_apple_col_df.show()
 
deduped_df = df_with_test_apple_col_df.dropDuplicates()
# deduped_df.show()
 
rows_zero_test_apple_removed_df = deduped_df.filter(~(col("test_apple") == 0))
 
# rows_zero_test_apple_removed_df.show()
 
# rows_zero_test_apple_removed_df.write.mode("overwrite").format("json").save("/opt/spark/data/output.json")
 
json_df = spark.read.json("/opt/spark/data/output.json")
json_df.show()