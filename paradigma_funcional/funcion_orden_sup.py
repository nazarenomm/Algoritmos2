from typing import Callable

def wrapper(f: Callable[[*args], None], *args: tuple) -> None:
    f(*args)
    print("Ejecutada f()")

# ChatGPT
# def wrapper(f: Callable[..., Any], *args: Any, **kwargs: Any) -> None:
#     f(*args, **kwargs)
#     print("Ejecutada f()")