import unittest
from argparse_parser import parse_args

class TestArgParse(unittest.TestCase):
    def test_bool_flag(self):
        arg_pattern = {"l": "bool"}
        args = ["program.py", "-l"]
        self.assertEqual(parse_args(args, arg_pattern), {"l": True})

    def test_int_flag(self):
        arg_pattern = {"p": "int"}
        args = ["program.py", "-p", "8080"]
        self.assertEqual(parse_args(args, arg_pattern), {"p": 8080})

    def test_str_flag(self):
        arg_pattern = {"d": "str"}
        args = ["program.py", "-d", "/usr/logs"]
        self.assertEqual(parse_args(args, arg_pattern), {"d": "/usr/logs"})

    def test_list_flag(self):
        arg_pattern = {"g": "list"}
        args = ["program.py", "-g", "this", "is", "a", "list"]
        self.assertEqual(parse_args(args, arg_pattern), {"g": ["this", "is", "a", "list"]})

    def test_default_values(self):
        arg_pattern = {"l": "bool", "p": "int", "d": "str", "g": "list"}
        args = ["program.py"]
        self.assertEqual(parse_args(args, arg_pattern), {"l": False, "p": 0, "d": "", "g": []})

    def test_unknown_flag(self):
        arg_pattern = {"l": "bool"}
        args = ["program.py", "-x"]
        self.assertEqual(parse_args(args, arg_pattern), "Error: Unknown flag 'x'")

    def test_invalid_value(self):
        arg_pattern = {"p": "int"}
        args = ["program.py", "-p", "not_an_int"]
        self.assertEqual(parse_args(args, arg_pattern), "Error: Value 'not_an_int' for flag 'p' must be an integer")

    def test_invalid_value_type(self):
        arg_pattern = {"g": "invalid_type"}
        args = ["program.py", "-g", "this", "is", "a", "list"]
        self.assertEqual(parse_args(args, arg_pattern), "Error: Unknown value type 'invalid_type' for flag 'g'")

    def test_unassigned_value(self):
        arg_pattern = {"l": "bool"}
        args = ["program.py", "value_without_flag"]
        self.assertEqual(parse_args(args, arg_pattern), "Error: Value 'value_without_flag' does not belong to any flag")

if __name__ == "__main__":
    unittest.main()
