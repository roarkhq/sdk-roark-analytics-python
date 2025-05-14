from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `roark_analytics.resources` module.

    This is used so that we can lazily import `roark_analytics.resources` only when
    needed *and* so that users can just import `roark_analytics` and reference `roark_analytics.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("roark_analytics.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
