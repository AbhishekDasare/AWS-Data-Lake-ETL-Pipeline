from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("AWS Data Lake ETL") \
    .getOrCreate()

df = spark.read.csv(
    "data/raw_sales.csv",
    header=True,
    inferSchema=True
)

df = df.withColumn(
    "total_amount",
    col("quantity") * col("price")
)

df.show()

df.write.mode("overwrite") \
    .csv(
        "data/curated_sales.csv",
        header=True
    )

spark.stop()
