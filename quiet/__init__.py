from typing import Any, Callable
from functools import wraps
import sys


def quiet(callable: Callable):
    """Supress the output of a function.

    Parameters
    ----------
    callable : Callable
        The function to call.

    Returns
    -------
    callable : Callable
        The decorated quiet function.
    """

    @wraps(callable)
    def wrapper(*args, **kwargs) -> Any:
        with open('/dev/null', 'w') as null:
            sys.stdout = null
            output = callable(*args, **kwargs)
            sys.stdout = sys.__stdout__
            
        return output
    return wrapper
