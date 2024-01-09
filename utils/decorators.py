from typing import TypedDict, Union, Any, Callable
from utils.types.exceptions import ArgumentError


def type_checker(
    checks: Union[type, dict],
    isMethod: bool = True,
) -> Callable[..., Union[None, TypeError]]:
    def checker(function):
        def wrapper(*args, **kwargs) -> Union[None, TypeError]:
            argsExcludingSelf = args[1:] if isMethod else args
            if not isinstance(isMethod, bool):
                raise ArgumentError(f"isMethod must be {bool}")
            
            for i, arg in enumerate(argsExcludingSelf):
                if isinstance(checks, dict) and not isinstance(
                    arg, list(checks.values())[i]
                ):
                    raise TypeError(f"Argument at Position {i} is an INVALID {list(checks.values())[i]}")
                if not isinstance(checks, dict) and not isinstance(arg, checks):
                    raise TypeError(f"Argument at Position {i} is an INVALID {checks}")

            for param in kwargs:
                if isinstance(checks, dict) and not isinstance(
                    kwargs[param], checks.get(param)
                ):
                    raise TypeError(
                        f"Argument {param}'s value of {kwargs[param]} is an INVALID {checks.get(param)}"
                    )
                if not isinstance(checks, dict) and not isinstance(
                    kwargs[param], checks
                ):
                    raise TypeError(
                        f"Argument {param}'s value of {kwargs[param]} is an INVALID {checks}"
                    )

            result = function(*args, **kwargs)
            return result

        return wrapper

    return checker


def number_greater_than_checker(
    check: Union[int, float] = 0, isMethod: bool = True
) -> Callable[..., Union[None, ValueError]]:
    def checker(function):
        def wrapper(*args, **kwargs) -> Union[None, ValueError]:
            argsExcludingSelf = args[1:] if isMethod else args
            if not isinstance(check, Union[int, float]):
                raise ArgumentError(f"Check must be {Union[int, float]}")
            if not isinstance(isMethod, bool):
                raise ArgumentError(f"isMethod must be {bool}")
            
            for i, arg in enumerate(argsExcludingSelf):
                if isinstance(arg, Union[int, float]) and arg < check:
                    raise ValueError(f"Argument at Position {i} is less than {check}")

            for param in kwargs:
                if isinstance(kwargs[param], Union[int, float]) and kwargs[param] < check:
                    raise TypeError(
                        f"Argument {param}'s value of {kwargs[param]} is less than {check}"
                    )

            function(*args, **kwargs)

        return wrapper

    return checker
