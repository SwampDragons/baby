#!/usr/bin/env python
# encoding: utf-

import urllib2
import json


class Baby(object):

    def __init__(self, url):
        baby_json = urllib2.urlopen(url).read()
        self.baby_dict = json.loads(baby_json)

    def _announce(self):
        delivered = self.baby_dict.get('delivered', None)

        if delivered:
            return ""
        else:
            parents = " and ".join(self.baby_dict['parents'])
            sex = self.baby_dict.get('sex', None)
            name = self.baby_dict.get('name', None)
            due_date = self.baby_dict.get('due_date', None)

            announcement = str("%s are excited to announce the impending "
                               "arrival of a baby" % parents)
            if sex:
                announcement += " {}".format(sex)
            if name:
                announcement += ", {}".format(name)
            if due_date:
                announcement += ", due on {}".format(due_date)
            return announcement

    def _cry(self):
        return "waaaaaaaaaaah"

    def _gurgle(self):
        return "gooo gooo"

    def announce(self):
        print(self._announce())

    def hungry(self):
        print(self._cry())

    def change(self):
        print(self._cry())

    def tired(self):
        print(self._cry())

    def tickle(self):
        print(self._gurgle())

    def toy(self):
        print(self._gurgle())
