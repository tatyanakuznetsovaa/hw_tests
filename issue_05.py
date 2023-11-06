import json
import unittest
from unittest.mock import patch, MagicMock
from what_is_year_now import what_is_year_now


def _patch_with_value(function, value: str):
    cm = MagicMock()
    cm.getcode.return_value = 200
    content = json.dumps(
        {
            "currentDateTime": value,
        }
    )
    cm.read.return_value = content
    cm.__enter__.return_value = cm
    function.return_value = cm


class TestWhatIsYearNow(unittest.TestCase):
    @patch("urllib.request.urlopen")
    def test_what_is_year_now_format_1(self, mock_urlopen):
        _patch_with_value(mock_urlopen, "2019-03-01")

        self.assertEqual(what_is_year_now(), 2019)

    @patch("urllib.request.urlopen")
    def test_what_is_year_now_format_2(self, mock_urlopen):
        _patch_with_value(mock_urlopen, "01.03.2019")

        self.assertEqual(what_is_year_now(), 2019)

    @patch("urllib.request.urlopen")
    def test_what_is_year_now_error_format(self, mock_urlopen):
        _patch_with_value(mock_urlopen, "01-03-2019")

        with self.assertRaises(ValueError):
            what_is_year_now()


if __name__ == "__main__":
    unittest.main()
