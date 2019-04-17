# ============================================================================
# FILE: matcher/denite_migemo.py
# AUTHOR: nekowasabi
# License: MIT license
# ============================================================================

import subprocess

from denite.base.filter import Base


class Filter(Base):
    def __init__(self, vim):
        super().__init__(vim)

        self.debug('migemo start')

        self.name = "matcher/migemo"
        self.description = "migemo matcher"

    def filter(self, context):
        if context["input"] == "":
            return context["candidates"]
        candidates = context["candidates"]
        self.debug(candidates)

        try:
            dict_path = "/usr/local/share/migemo/utf-8/migemo-dict"
            process = subprocess.call(
                ["/usr/local/bin/cmigemo", "-w", context["input"], "-d", dict_path],
                stdout=subprocess.PIPE,
            )
            p = process.stdout.read().decode("utf-8")
            self.debug(p)

        except Exception:
            return []
        candidates = [x for x in candidates if x["word"] in p]

        return candidates
