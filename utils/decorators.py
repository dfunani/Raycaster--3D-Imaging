from typing import Union, Any, Callable

def type_checker(function, check:type[Any]=Union[int, float], isMethod:bool=True) -> Callable[..., Union[None, TypeError]]:
    def wrapper(*args, **kwargs) -> Union[None, TypeError]:
        argsExcludingSelf = args[1:] if isMethod else args
        for i, arg in enumerate(argsExcludingSelf):
            if not isinstance(arg, check):
                raise TypeError(f"Argument at Position {i} is an INVALID Type")
            
        for param in kwargs:
            if not isinstance(kwargs[param], check):
                raise TypeError(f"Argument {param}'s value of {i} is an INVALID Type")
            
        function(*args, **kwargs)
    return wrapper

def number_greater_than_checker(function, check:Union[int, float]=0, isMethod:bool=True) -> Callable[..., Union[None, ValueError]]:
    def wrapper(*args, **kwargs) -> Union[None, ValueError]:
        argsExcludingSelf = args[1:] if isMethod else args
        for i, arg in enumerate(argsExcludingSelf):
            if arg < check:
                raise ValueError(f"Argument at Position {i} is less than ZERO")
            
        for param in kwargs:
            if kwargs[param] < check:
                raise ValueError(f"Argument {param}'s value of {i} is less than ZERO")
            
        function(*args, **kwargs)
    return wrapper