import unittest
from one_hot_encoder import fit_transform


class TestFitTransform(unittest.TestCase):
    def test_fit_transform_default_case(self):
        actual = fit_transform(["Moscow", "New York", "Moscow", "London"])
        expected = [
            ("Moscow", [0, 0, 1]),
            ("New York", [0, 1, 0]),
            ("Moscow", [0, 0, 1]),
            ("London", [1, 0, 0]),
        ]
        self.assertEqual(actual, expected)

    def test_fit_transform_empty_case(self):
        actual = fit_transform([])
        expected = []
        self.assertIsInstance(actual, list)

    def test_fit_transform_wo_args(self):
        with self.assertRaises(TypeError):
            fit_transform()

    def test_fit_transform_noniter_args_bad_seq(self):
        with self.assertRaises(TypeError):
            fit_transform(2, "Moscow")

    def test_fit_transform_noniter_args_good_seq(self):
        actual = fit_transform("Moscow", 2)
        expected = [("Moscow", [0, 1]), (2, [1, 0])]

        self.assertListEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
