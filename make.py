from aods import (
    Context,
    default_release_flags,
    default_debug_flags,
)

import sys
import os

release_build = "--release" in sys.argv

ctx = Context("main")

ctx.add_include(
    [
        "include",
        "util",
        # other includes
    ]
)

ctx.add_dependency(
    [
        # list of dependencies
    ]
)

ctx.add_source(["src/" + f for f in os.listdir("src") if f.endswith(".c")])

if release_build:
    ctx.add_flag(default_release_flags())
else:
    ctx.add_flag(default_debug_flags())

ctx.build()
