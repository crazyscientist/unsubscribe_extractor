#!/usr/bin/env python3
import argparse
import collections
import mailbox

from bs4 import BeautifulSoup


Match = collections.namedtuple("Match", ("sender", "domain", "link"))


class Extractor:
    def _get_args(self):
        parser = argparse.ArgumentParser(
            description="Extract unsubscription links from an 'mbox' file"
        )
        parser.add_argument('mbox', nargs="+", type=argparse.FileType("r"))

        return parser.parse_args()

    def parse(self, message):
        parser = BeautifulSoup(message.as_string(), "html.parser")
        matches = parser.find_all("a")
        import code
        code.interact(local=locals())
        for x in matches:
            match = Match(
                sender=message.get("From"),

            )
            print(x)

    def __init__(self):
        self.options = self._get_args()
        self.results = set()

    def __call__(self):
        for mbox in self.options.mbox:
            opened_mbox = mailbox.mbox(mbox.name)
            for message in opened_mbox:
                self.parse(message)
                return


if __name__ == "__main__":
    e = Extractor()
    e()
