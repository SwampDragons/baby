#!/usr/bin/env python
# encoding: utf-

# import urllib2
import json


class Baby(object):

    def __init__(self, url):
        # baby_json = urllib2.urlopen(url)
        baby_json = open(url, 'r').read()
        self.baby_dict = json.loads(baby_json)

    def announce(self):

        if self.baby_dict['delivered']:
            pass
        else:
            parents = " and ".join(self.baby_dict['parents'])
            announcement = str("%s are excited to announce the impending "
                               "arrival of a baby" % parents)
            if self.baby_dict['sex']:
                announcement += (" " + self.baby_dict['sex'])
            if self.baby_dict['name']:
                announcement += ", %s" % self.baby_dict['name']
            if self.baby_dict['due_date']:
                announcement += ", due on %s" % self.baby_dict['due_date']

            print announcement

    def _cry(self):
        print "waaaaaaaaaaah"

    def _gurgle(self):
        print "gooo gooo"

    def hungry(self):
        self._cry()

    def change(self):
        self._cry()

    def tired(self):
        self._cry()

    def tickle(self):
        self._gurgle()

    def toy(self):
        self._gurgle()
