def is_blob_path(input_path:str) -> bool:
    """Returns True if an abfss path"""
    if input_path.startswith("abfss:"):
        return True
    
    #else
    return False

def _isvalidpath(input_path:str) -> bool:
    """Returns if path is acceptable or not"""
    if type(input_path) != "str":
        print("PE0002 Warning: input_path must be a string")
        return False
    if input_path == "":
        print("PE0003 Warning: input_path must not be empty")
        return False

    #else
    return True

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
    input_path = remove_trailing_slashes()
    
    #cloud type conversions
    if input_path.startswith("az:/"):
        input_path = input_path.replace("az:", "abfss:")
        
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
