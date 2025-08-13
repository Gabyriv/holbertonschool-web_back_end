#!/usr/bin/env python3
"""Unit tests for `client.GithubOrgClient`.

Focus: verify that `GithubOrgClient.org` returns the mocked payload and
calls `client.get_json` exactly once with the expected URL.
"""

from typing import Any, Dict
import unittest
from parameterized import parameterized
from unittest.mock import Mock, patch, PropertyMock

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for `client.GithubOrgClient`."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name: str, mock_get_json: Mock) -> None:
        """It returns payload and calls get_json once with the correct URL."""
        expected: Dict[str, Any] = {"org": org_name}
        mock_get_json.return_value = expected

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected)

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self) -> None:
        """It returns repos_url derived from the mocked `org` property."""
        expected_repos_url = "https://api.github.com/orgs/google/repos"
        with patch(
            "client.GithubOrgClient.org", new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = {"repos_url": expected_repos_url}
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, expected_repos_url)
