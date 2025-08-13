#!/usr/bin/env python3
"""Unit tests for utilities in `utils.py`.

This module currently tests `utils.access_nested_map` to ensure it returns
expected values for valid nested paths.
"""

from typing import Any, Mapping, Sequence
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock

from utils import access_nested_map, get_json


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

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(
        self,
        nested_map: Mapping[str, Any],
        path: Sequence[str],
        missing_key: str,
    ) -> None:
        """It raises KeyError and the message contains the missing key."""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(cm.exception.args[0], missing_key)


class TestGetJson(unittest.TestCase):
    """Tests for `utils.get_json` that avoid real HTTP calls."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: dict) -> None:
        """It returns payload from the mocked requests.get().json()."""
        with patch("utils.requests.get") as mock_get:
            mock_resp: Mock = Mock()
            mock_resp.json.return_value = test_payload
            mock_get.return_value = mock_resp

            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)
