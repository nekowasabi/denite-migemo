# ============================================================================
# FILE: matcher/denite_migemo.py
# AUTHOR: nekowasabi
#         Shougo Matsushita <Shougo.Matsu at gmail.com>
# License: MIT license
# ============================================================================

import re
import subprocess

from denite.base.filter import Base


class Filter(Base):
    def __init__(self, vim):
        super().__init__(vim)

        self.name = "matcher/migemo"
        self.description = "migemo matcher"

        self.vars = {
            "command": ["cmigemo"],
            "dict_path": self.vim.vars.get("denite_migemo#dict_path"),
        }

    def filter(self, context):
        if context["input"] == "":
            return context["candidates"]
        candidates = context["candidates"]

        try:
            pattern = subprocess.check_output(
                self.vars["command"] + ["-w", context["input"],
                                        "-d", self.vars["dict_path"]],
            ).decode("utf-8").splitlines()[0]

        except Exception as ex:
            self.debug(ex)
            return []

        # Note: "+" must be escaped
        p = re.compile(pattern.replace("+", "\+"))
        candidates = [x for x in candidates if p.search(x["word"])]

        return candidates
