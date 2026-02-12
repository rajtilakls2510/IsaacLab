# Copyright (c) 2022-2025, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Sub-module for utilities for working with external functions."""

from typing import Any
from importlib import import_module


def call_externally_defined_function(function_path: str, *args: Any, **kwargs: Any) -> Any:
    # Dynamically import the function from the path and call it.
    module_path, fn_name = function_path.rsplit(".", 1)
    module = import_module(module_path)
    fn = getattr(module, fn_name)
    return fn(*args, **kwargs)
