from databricks.connect import DatabricksSession

print("START DBCONNECT SCRIPT")

spark = DatabricksSession.builder.getOrCreate()

print("Current catalog:", spark.catalog.currentCatalog())
print("Current schema:", spark.catalog.currentDatabase())

df = spark.range(1, 5)
print("Row count:", df.count())

print("Session OK")
