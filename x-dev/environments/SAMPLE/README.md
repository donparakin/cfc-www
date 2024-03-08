# Folder: ./x-environs:

The same app code needs to run in different "environments"
such as production (prod), development (dev), testing, staging, etc.

- Environment-specific files should **NEVER** be saved in version control (Git).

- `./x-dev/environments/SAMPLE` *is* saved in version control as a sample of
  what is required for each environment.

  - In particular, `settings.toml` has settings specific to the environment
    that are required by the app.

  - Do not store sensitive values, such as the real SECRET_KEY or real passwords,
    in any file within `./x-dev/environments/SAMPLE`

### Development Environment 

For a development environment, you can create a `./x-dev/environments/dev/` folder
within the app code.
`.gitignore` is setup to exclude a folders within `./x-dev/environments` except `SAMPLE`.

`./x-dev/environments/dev/` is also a convenient place for SQLite databases
(the location of which you must define in `settings.toml`).
