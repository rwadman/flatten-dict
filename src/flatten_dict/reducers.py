from typing import Any, Callable, Tuple, TypeVar, Optional, Union

T = TypeVar("T")


def tuple_reducer(k1, k2):
    # type: (Optional[Tuple[T,...]], T) -> Tuple[T,...]
    if k1 is None:
        return (k2,)
    else:
        return k1 + (k2,)


def path_reducer(k1, k2):
    # type: (Optional[str], str) -> str
    import os.path

    if k1 is None:
        return k2
    else:
        return os.path.join(k1, k2)


def dot_reducer(k1, k2):
    # type: (Optional[Union[T, str]], T) -> Union[T, str]
    if k1 is None:
        return k2
    else:
        return "{}.{}".format(k1, k2)


def underscore_reducer(k1, k2):
    # type: (Optional[Union[T, str]], T) -> Union[T, str]
    if k1 is None:
        return k2
    else:
        return "{}_{}".format(k1, k2)


def make_reducer(delimiter):
    # type: (Any) -> Callable[[Optional[Union[T, str]], T], Union[T, str]]
    """Create a reducer with a custom delimiter.

    Parameters
    ----------
    delimiter : str
        Delimiter to use to join keys.

    Returns
    -------
    f : Callable
        Callable that can be passed to `flatten()`'s `reducer` argument.
    """

    def f(k1, k2):
        # type: (Optional[Union[T, str]], T) -> Union[T, str]
        if k1 is None:
            return k2
        else:
            return "{}{}{}".format(k1, delimiter, k2)

    return f
