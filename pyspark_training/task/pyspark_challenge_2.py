import pyspark

from pyspark.sql import SparkSession

"""
We have two separate tables in the following format: 
     
|col|   |col|
-----   -----
|A  |   |E  |
|B  |   |F  |
|C  |   |A  |
|D  |   |B  |
|E  |   |Z  |

Combine the rows of these two datasets together to create a single table 
in the following format:

Example output:

|col|
-----
|AE |
|BF |
|AC |
|BD |
|EZ |

"""

spark = SparkSession.builder.appName("Pyspark Challenge").getOrCreate()

columns = ["col"]

left_data = [
    ["A"],
    ["B"],
    ["C"],
    ["D"],
    ["E"]
]

right_data = [
    ["E"],
    ["F"],
    ["A"],
    ["B"],
    ["Z"]
]

left_dataset = spark.createDataFrame(left_data, columns)
left_dataset.show()

right_dataset = spark.createDataFrame(right_data, columns)
right_dataset.show()

# END GIVEN CODE
