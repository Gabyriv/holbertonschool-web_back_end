# Flask i18n (Babel) Project

Internationalization/localization demo using Flask and Flask-Babel. It adds:

- Locale selection (priority: URL > user > headers > default)
- Timezone selection (priority: URL > user > default, validated with pytz)
- Translated templates (EN/FR)
- Current time display formatted in the inferred locale and timezone


## Requirements

- Python 3.9 (project target: Ubuntu 20.04) – works on macOS as well
- Virtualenv recommended
- Dependencies in `requirements.txt`:
  - Flask, flask_babel, pytz, Babel (CLI for translations)


## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```


## Compile translations

The `.po` files live under `translations/<lang>/LC_MESSAGES/messages.po`.
Compile them to `.mo` files:

```bash
.venv/bin/pybabel compile -d translations
```


## Run the apps

Each task has its own app file. Use Flask’s app runner, e.g.:

```bash
# Task 7 (timezone selector)
flask --app 7-app.py run

# Task 8 (final app showing current time)
flask --app app.py run
```

If `flask` isn’t in PATH, prefix with venv path:

```bash
.venv/bin/flask --app app.py run
```


## Key files

- `0-app.py` … `7-app.py`: progressive tasks building i18n features
- `app.py`: Task 8 (displays current time with locale/timezone)
- `templates/`: Jinja templates (`index.html`, `*-index.html` for earlier tasks)
- `translations/en/LC_MESSAGES/messages.po` (EN)
- `translations/fr/LC_MESSAGES/messages.po` (FR)


## Locale and timezone resolution

- Locale priority: `?locale=<en|fr>` > logged-in user `locale` > `Accept-Language` > default (`en`)
- Timezone priority: `?timezone=<TZ>` > logged-in user `timezone` > default (`UTC`)
- Timezones are validated with `pytz.timezone`; invalid values fall back to `UTC`.


## Mock login

Pass `?login_as=<id>` to simulate a user. Users live in each app module:

- 1: Balou (fr, Europe/Paris)
- 2: Beyonce (en, US/Central)
- 3: Spock (invalid locale/timezone)
- 4: Teletubby (no locale, Europe/London)


## Testing URLs

- French + Paris tz via user: `/?login_as=1`
- English + Central tz via user: `/?login_as=2`
- Force locale: `/?locale=fr` or `/?locale=en`
- Force timezone: `/?timezone=US/Central`
- Invalid tz fallback to UTC: `/?timezone=Vulcan`


## Translations

Template message IDs include:

- `home_title`, `home_header`
- `logged_in_as`, `not_logged_in`
- `current_time_is` (Task 8):
  - EN: "The current time is %(current_time)s."
  - FR: "Nous sommes le %(current_time)s."


## Style and conventions

- All Python files use shebang `#!/usr/bin/env python3`
- pycodestyle 2.5 compliant
- Functions include docstrings and type annotations


## Troubleshooting

- Flask not found: use `.venv/bin/flask` or activate the venv
- Babel CLI missing: `pip install Babel` then re-run `pybabel compile`
- Jinja errors for datetime: format the time server-side (see `app.py`)

