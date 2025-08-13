#!/usr/bin/env python3
"""Unit tests for utilities in `utils.py`.

This module currently tests `utils.access_nested_map` to ensure it returns
expected values for valid nested paths.
"""

from typing import Any, Mapping, Sequence
import unittest
from parameterized import parameterized

from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test suite for `utils.access_nested_map`."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self,
        nested_map: Mapping[str, Any],
        path: Sequence[str],
        expected: Any,
    ) -> None:
        """It returns the value at `path` inside `nested_map`."""
        self.assertEqual(access_nested_map(nested_map, path), expected)
