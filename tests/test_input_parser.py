# Unit test untuk input parser

import pytest
from input_parser import parse_input

def test_parse_input():
    files = parse_input("tests/sample_files")
    assert len(files["docker"]) == 1
    assert files["docker"][0].name == "Dockerfile"