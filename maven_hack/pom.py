import re

PACKAGING_RE = re.compile("<packaging>(.*)</packaging>")


class Pom(object):

    def __init__(self, file_name):
        self.packaging = None
        with open(file_name) as f:
            for l in f:
                m = PACKAGING_RE.match(l)
                if m:
                    self.packaging = m.group(1)