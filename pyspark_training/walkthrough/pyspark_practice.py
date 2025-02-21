from pyspark.sql import SparkSession
from pyspark.sql import functions

# Main Entrypoint - Works on the Driver Node
# There can only be one driver node in a cluster - Can't be scaled horizontally.
# There can be many worker nodes. - CAN be scaled horizontally.
spark = SparkSession.builder.appName("Pyspark practice").getOrCreate()

# RDDS
# RDD - Resilient Distributed Dataset
# Data objects, partitioned to be processed in parallel in a Spark Cluster.
# Fault Tolerant - If one node fails, the RDD will persist until a new node becomes available.
# The allocation of a new node is managed by the Yarn Resource Manager.

# There are two abstraction layers on top of RDDS
# Dataframes - Used in PySpark, queried using pyspark.sql.functions

# Datasets - Exclusive to Scala and Java only. Guarantees a degree of security 
# by guarding against type mismatch errors. 

# DATAFRAMES

data = [
    ("Alice", "Sales", 1000),
    ("Bob", "Sales", 1500),
    ("Charlie", "HR", 1200),
    ("David", "HR", 800),
    ("Eve", "IT", 2000),
    ("Frank", "IT", 2200),
    ("Jim", "ATA", 1300),
    ("Millie", "Finance", 2300),
    ("Samantha", "Sales", 1000)
]

columns = ["Name", "Department", "Salary"]

employee_df = spark.createDataFrame(data, columns)

# Select Name and Department
name_dep_df = employee_df.select("Name", "Department") # Lazy
finance_dep_df = name_dep_df.filter(name_dep_df["Department"] == "Finance") # Lazy

print("Showing only Employees within the Finance Department...")
# finance_dep_df.show()

# Stages of running a Spark Job (A Spark Application can contain multiple Spark Jobs).
# Analysis - Logical Plan - Optimized Logical Plan - Physical Plan - Code Generation

# Transformations vs Actions
# Transformations: filter, select, groupBy, agg, orderBy, withColumn, .na.drop() ...
# Spark leverages LAZY EVALUATION. 
# Actions: .show(), .write(), .read(), .count(), .collect()

# Logical Plan & Optimized Logical Plan involve creating a DAG. (Directed Acyclic Graph)

# Filtering on an integer type
high_salary_df = employee_df.filter(employee_df["Salary"] > 1100)
# high_salary_df.show()

# Filtering using a negation operator ("~")
non_it_df = employee_df.filter(~(employee_df["Department"] == "IT"))
# non_it_df.show()

# Grouping and Aggregating
# SELECT SUM(total_salary) from employee GROUP BY department;

total_salary_per_department = employee_df.groupBy("Department").sum("Salary")\
    .withColumnRenamed("sum(Salary)", "Total Salary")
# total_salary_per_department.show()

num_employees_per_department = employee_df.groupBy("Department").count()\
    .withColumnRenamed("count", "Number of Employees")
# num_employees_per_department.show()

# Adding new columns
# Return a dataset which contains a new column 'Salary with Bonus', and this column
# should contain the Employee's salary with 30% added.
employees_with_bonus_df = employee_df.withColumn(
    "Salary with Bonus", 
    employee_df["Salary"] + (employee_df["Salary"] * 0.3)
    )

employees_with_bonus_df.show()

# Writing to CSV
employees_with_bonus_df.write.mode("overwrite").format("csv").save("/opt/spark/data/employee_with_bonus.csv", header=True)

# path = "/opt/spark/data/employee_with_bonus.csv"
# employees_with_bonus_df = spark.read.options(header=True).csv(path)

dept_data = [
    ("Sales", "New York"),
    ("HR", "San Francisco"),
    ("IT", "Seattle"),
    ("Entertainment", "Boston"),
    ("Schmoozing", "London")
]

columns = ["Department", "City"]

dept_data_df = spark.createDataFrame(dept_data, columns)
dept_data_df.show()


inner_joined_df = employees_with_bonus_df.join(dept_data_df, on="Department", how="inner")

left_join_df = employees_with_bonus_df.join(dept_data_df, on="Department", how="left")

inner_joined_df.show()
left_join_df.show()


spark.sparkContext.setLogLevel("ERROR")