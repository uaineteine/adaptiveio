import os
import sys

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
# Add the parent directory to sys.path
parent_dir = os.path.join(current_dir, '..')
sys.path.append(os.path.abspath(parent_dir))

from adaptiveio import save_raw_text

from pyspark.sql import SparkSession

# Create Spark session
print("Creating Spark session")
sparkSession = (
    SparkSession.builder
        .master("local[*]")
        .appName("Unit Test")
        .config("spark.driver.memory", "2g")
        .config(
            "spark.jars.packages",
            "org.apache.hadoop:hadoop-azure:3.3.0,com.microsoft.azure:azure-storage:8.6.6"
        )
        # ✅ Storage account key for Azurite
        .config("spark.hadoop.fs.azure.account.key.devstoreaccount1.blob.core.windows.net",
            "Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==")
        # ✅ Point the blob endpoint to Azurite
        .config("spark.hadoop.fs.azure.localhost.account.key.devstoreaccount1.blob.core.windows.net",
            "Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==")
        .config("spark.hadoop.fs.azure.account.blob.endpoint.devstoreaccount1.blob.core.windows.net",
            "http://127.0.0.1:10000/devstoreaccount1")
        .getOrCreate()
)

print("Saving some file")
test_str = "hello there, this is the 1st test."
dest_pth = "wasb://test@devstoreaccount1.blob.core.windows.net/test.txt"

save_raw_text(dest_pth, test_str, spark=sparkSession)
