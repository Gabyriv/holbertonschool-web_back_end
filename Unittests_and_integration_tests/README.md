# Unittests and Integration Tests

This project adds parameterized unit tests and integration tests for a
Holberton web back end. Focus areas:

- utils: `access_nested_map`, `get_json`, `memoize`
- client: `GithubOrgClient` (`org`, `_public_repos_url`, `public_repos`,
  `has_license`)

## Environment

- Python 3.9
- Ubuntu 20.04 LTS
- Use a virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install requests parameterized pycodestyle==2.5.0
```

## Style and Conventions

- All Python files include shebangs, docstrings, and type annotations.
- Lines wrapped to comply with pycodestyle
- Run style checks:

```bash
pycodestyle test_utils.py test_client.py
```

## Test Files

- `test_utils.py`

  - Parameterized tests for `utils.access_nested_map` (success and errors).
  - Parameterized tests for `utils.get_json` using mocked
    `requests.get(...).json()`.
  - `utils.memoize` verified to call the underlying method once and cache.

- `test_client.py`
  - Unit tests for `GithubOrgClient.org`, `_public_repos_url`,
    and `public_repos` with mocks for internal helpers.
  - Parameterized tests for `GithubOrgClient.has_license`.
  - Integration tests for `public_repos` using fixtures and only mocking
    external HTTP calls.

## Fixtures

- See `fixtures.py` which exposes `TEST_PAYLOAD` containing tuples:

```python
(
  org_payload,        # dict with 'repos_url'
  repos_payload,      # list of repos from the org
  expected_repos,     # list of all repo names expected
  apache2_repos,      # list of repo names filtered by Apache-2.0 license
)
```

The integration test class is parameterized with these fixtures to exercise
the real code path while mocking only network calls.

## How Integration Tests Work

- Class: `TestIntegrationGithubOrgClient`
- Decorated with `@parameterized_class` to feed in fixtures.
- `setUpClass()` starts a patcher for `requests.get` and sets a
  `side_effect` so that:
  - `requests.get("https://api.github.com/orgs/google").json()` returns
    `org_payload`
  - `requests.get(org_payload["repos_url"]).json()` returns `repos_payload`
- `tearDownClass()` stops the patcher.
- Tests:
  - `public_repos()` returns `expected_repos`
  - `public_repos(license="apache-2.0")` returns `apache2_repos`

## Running Tests

From `Unittests_and_integration_tests/` with the virtual environment active:

```bash
.venv/bin/python -m unittest -v test_utils.py
.venv/bin/python -m unittest -v test_client.py

# or run the full suite
.venv/bin/python -m unittest -v
```

## Notes

- Unit tests mock internal functions/properties (`client.get_json`,
  `GithubOrgClient.org`, `_public_repos_url`) to isolate behavior.
- Integration tests mock only external HTTP (`requests.get`) to validate the
  end-to-end behavior of `public_repos` including license filtering.
