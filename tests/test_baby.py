import json
import unittest

import mock

from baby import Baby


class TestBaby(unittest.TestCase):

    def setUp(self):
        self.urllib2_patch = mock.patch('baby.urllib2.urlopen')
        self.urllib2_obj = self.urllib2_patch.start()

        self.url = 'http://testbaby.com'

    def tearDown(self):
        self.urllib2_patch.stop()

    def _set_data(self, data):
        self.data_obj = mock.Mock()
        self.data_obj.read.side_effect = [json.dumps(data)]
        self.urllib2_obj.return_value = self.data_obj

    def test_delivered_default(self):
        data = {"parents": ["Alice", "Bob"],
                "delivered": "October 1st, 2015"}
        self._set_data(data)
        baby = Baby(self.url)
        out = baby._announce()
        expected = ''
        self.assertEqual(out, expected)

    def test_announce_default(self):
        data = {"parents": ["Alice", "Bob"]}
        self._set_data(data)
        baby = Baby(self.url)
        out = baby._announce()
        expected = 'Alice and Bob are excited to announce ' \
                   'the impending arrival of a baby'
        self.assertEqual(out, expected)

    def test_announce_sex(self):
        data = {"parents": ["Alice", "Bob"],
                "sex": "girl"}
        self._set_data(data)
        baby = Baby(self.url)
        out = baby._announce()
        expected = 'Alice and Bob are excited to announce ' \
                   'the impending arrival of a baby girl'
        self.assertEqual(out, expected)

    def test_announce_name(self):
        data = {"parents": ["Alice", "Bob"],
                "name": "Claire"}
        self._set_data(data)
        baby = Baby(self.url)
        out = baby._announce()
        expected = 'Alice and Bob are excited to announce ' \
                   'the impending arrival of a baby, Claire'
        self.assertEqual(out, expected)

    def test_announce_due_date(self):
        data = {"parents": ["Alice", "Bob"],
                "due_date": "January 1st, 2015"}
        self._set_data(data)
        baby = Baby(self.url)
        out = baby._announce()
        expected = 'Alice and Bob are excited to announce ' \
                   'the impending arrival of a baby, due on January 1st, 2015'
        self.assertEqual(out, expected)

    def test_announce_all(self):
        data = {"parents": ["Alice", "Bob"],
                "sex": "girl",
                "name": "Claire",
                "due_date": "January 1st, 2015"}
        self._set_data(data)
        baby = Baby(self.url)
        out = baby._announce()
        expected = 'Alice and Bob are excited to announce ' \
                   'the impending arrival of a baby girl, Claire, ' \
                   'due on January 1st, 2015'
        self.assertEqual(out, expected)

    def test_cry(self):
        data = {"parents": ["Alice", "Bob"]}
        self._set_data(data)
        baby = Baby(self.url)
        out = baby._cry()
        self.assertEqual(out, "waaaaaaaaaaah")

    def test_gurgle(self):
        data = {"parents": ["Alice", "Bob"]}
        self._set_data(data)
        baby = Baby(self.url)
        out = baby._gurgle()
        self.assertEqual(out, "gooo gooo")
