from typing import Tuple, Union, Optional
import mxnet as mx

from ivy.utils.exceptions import IvyNotImplementedException


def unique_all(
    x: Union[(None, mx.ndarray.NDArray)], /, *, axis: Optional[int] = None
) -> Tuple[
    (
        Union[(None, mx.ndarray.NDArray)],
        Union[(None, mx.ndarray.NDArray)],
        Union[(None, mx.ndarray.NDArray)],
        Union[(None, mx.ndarray.NDArray)],
    )
]:
    raise IvyNotImplementedException()


def unique_counts(
    x: Union[(None, mx.ndarray.NDArray)], /
) -> Tuple[(Union[(None, mx.ndarray.NDArray)], Union[(None, mx.ndarray.NDArray)])]:
    raise IvyNotImplementedException()


def unique_inverse(
    x: Union[(None, mx.ndarray.NDArray)], /
) -> Tuple[(Union[(None, mx.ndarray.NDArray)], Union[(None, mx.ndarray.NDArray)])]:
    raise IvyNotImplementedException()


def unique_values(
    x: Union[(None, mx.ndarray.NDArray)],
    /,
    *,
    out: Optional[Union[(None, mx.ndarray.NDArray)]] = None,
) -> Union[(None, mx.ndarray.NDArray)]:
    raise IvyNotImplementedException()


def difference(
    x1: Union[None, mx.ndarray.NDArray],
    x2: Union[None, mx.ndarray.NDArray],
    /,
) -> Tuple[Union[None, mx.ndarray.NDArray], Union[None, mx.ndarray.NDArray]]:
    diff1 = mx.nd.setdiff1d(x1, x2)
    diff2 = mx.nd.setdiff1d(x2, x1)
    return diff1, diff2