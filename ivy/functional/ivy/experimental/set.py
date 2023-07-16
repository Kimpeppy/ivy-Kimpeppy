from typing import Optional, Union, Tuple
import ivy
from ivy.func_wrapper import (
    handle_out_argument,
    to_native_arrays_and_back,
    handle_nestable,
    handle_device_shifting,
)
from ivy.utils.exceptions import handle_exceptions

def difference(
        x1: Union[ivy.Array, ivy.NativeArray],
        x2: Union[ivy.Array, ivy.NativeArray],
        /,
        
) -> Tuple[Union[ivy.Array, ivy.NativeArray], Union[ivy.Array, ivy.NativeArray]]:
    return ivy.current_backend(x1, x2).difference(x1, x2)