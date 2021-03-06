import os


def get_env_variable(env_variable: str, default=None, required:bool=False):
    """[summary]
    Args:
        env_variable (str): Env variable to be fetched
        default (str, optional): Default value of the env variable. Defaults to None.
        required (bool, optional): Defines whether or not the variable is required. Defaults to False.
    Raises:
        Exception[Exception]: Exception raised when a variable is required but not set
    Returns:
        value[type]: Set value of the env variable
    """
    value = os.getenv(env_variable, default)
    if required and not value:
        error_msg = f"Set the {env_variable} environment variable"
        raise Exception(error_msg)
    return value