def is_blob_path(input_path:str) -> bool:
    """Returns True if an abfss path"""
    if input_path.startswith("abfss:"):
        return True
    if input_path.startswith("abfs:"):
        return True
    if input_path.startswith("wasb:"):
        return True
    if input_path.startswith("wasbs:"):
        return True
    
    #else
    return False

def _isvalidpath(input_path:str) -> bool:
    """Returns if path is acceptable or not"""
    if not isinstance(input_path, str):
        print("PE0002 Warning: input_path must be a string")
        return False
    if input_path == "":
        print("PE0003 Warning: input_path must not be empty")
        return False

    #else
    return True

def _fix_protocols(input_path:str) -> str:
    """
    Fixing protocols in os paths

    Args:
        input_path (str)

    Returns:
        str: The normalised path
    """
    new_path = input_path

    if not input_path.startswith("abfss://") and input_path.startswith("abfss:/"):
        new_path = input_path.replace("abfss:/", "abfss://")
    elif not input_path.startswith("abfs://") and input_path.startswith("abfs:/"):
        new_path = input_path.replace("abfs:/", "abfs://")
    elif not input_path.startswith("dbfs://") and input_path.startswith("dbfs:/"):
        new_path = input_path.replace("dbfs:/", "dbfs://")
    elif not input_path.startswith("https://") and input_path.startswith("https:/"):
        new_path = input_path.replace("https:/", "https://")
    elif not input_path.startswith("http://") and input_path.startswith("http:/"):
        new_path = input_path.replace("http:/", "http://")
    
    if new_path != input_path:
        print("PE0010 Warning: protocol in path has been fixed from {input_path} to {new_path}")

    return new_path

def normalisePaths(input_path:str) -> str:
    """
    Apply a standardisation of naming conventions for filepaths

    Args:
        input_path (str)

    Returns:
        str: The normalised path
    """
    
    _isvalidpath(input_path)
    
    #treatments
    input_path = remove_trailing_slashes(input_path)
    
    #cloud type conversions
    if input_path.startswith("az:/"):
        input_path = input_path.replace("az:", "abfss:")
    
    input_path = _fix_protocols(input_path)

    return input_path

def remove_trailing_slashes(input_path:str) -> str:
    """
    Remove trailing slashes in path

    Args:
        input_path (str)

    Returns:
        str: The treated path
    """
    
    _isvalidpath(input_path)
    
    #remove trailing / at the end if it exists, but only the last character
    if input_path.endswith("/") or input_path.endswith("\\"):
        try:
            input_path = input_path[:-1] #remove that end slash
        except Exception as e:
            print(f"PE0001 Warning: Exception while removing trailing slash: {e}")
    
    return input_path
