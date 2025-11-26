"""
textio.py

Utility functions for reading and writing raw text files.
Supports both local file paths and abfss: paths for Azure Data Lake Storage.
Uses Spark for distributed file operations when working with abfss: paths.

Functions:
    read_raw_text(path: str, spark=None) -> str
        Read a text file and return its content as a single string.

    save_raw_text(path: str, text: str, spark=None)
        Save a string to a text file.

Author: Daniel
Created: September 2025
"""
from pyspark.sql import SparkSession
import pandas as pd

from .pathing import is_blob_path, normalisePaths

def read_raw_text(path:str, spark=None) -> str:
    """Read a text file and return its content as a single string.

    Args:
        path (str): Path to the text file. Supports local paths and abfss: paths.
        spark (SparkSession, optional): Spark session for reading from abfss: paths. Defaults to None.
    """
    #fix any pathing syntax
    path = normalisePaths(path)
    
    if is_blob_path(path):
        if spark is None:
            raise ValueError("PE010 Spark session must be provided for reading from abfss: paths.")
        df = spark.read.text(path)
        lines = df.rdd.map(lambda row: row[0]).collect()
        txt = "\n".join(lines)
        return txt
    else:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

def save_raw_text(path:str, text:str, spark:SparkSession=None):
    """Save a string to a text file.

    Args:
        path (str): Path to the text file. Supports local paths and blob paths.
        text (str): The text content to save.
        spark (SparkSession, optional): Spark session for writing to blob paths. Defaults to None.
    """
    #fix any pathing syntax
    path = normalisePaths(path)
    
    if is_blob_path(path):
        if spark is None:
            raise ValueError("PE011 Spark session must be provided for writing to blob paths.")
        
        #make into dataframe
        # split text into lines and wrap in DataFrame
        lines = text.splitlines()
        pd_df = pd.DataFrame(lines, columns=["value"])

        # convert to Spark DataFrame
        df = spark.createDataFrame(pd_df)

        # write as text file - coalese to 1 part
        df.coalesce(1).write.mode("overwrite").text(path)
    else:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
