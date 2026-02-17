import pandas as pd
from pyspark.sql import SparkSession

url = (
    "https://huggingface.co/datasets/UrvishAhir1/"
    "Electric-Vehicle-Specs-Dataset-2025/resolve/main/"
    "electric_vehicles_spec_2025.csv"
)

# 1. Read from URL locally (in VS Code) but executed on cluster via Databricks extension
pdf = pd.read_csv(url)

spark = SparkSession.builder.getOrCreate()

# 2. Convert pandas → Spark
df_spark = spark.createDataFrame(pdf)

# 3. Write CSV into the existing volume
(
    df_spark.write
    .mode("overwrite")
    .option("header", "true")
    .csv("/Volumes/workspace/onedrive/ev_data/ev_2025_raw_csv")
)

