# raygun-logger
Use Python's standard logging library to send messages to Raygun (https://raygun.io/)

# Features
  - Implements a standard `logging.Handler`.
  - Automatic Django request logging.
  - Like any other handler, it can be filtered and have its level set.

# Install
    `pip install rglogger`

# Usage
    ```python
    import logging
    import rglogger
    root_logger = logging.getLogger()
    raygun_handler = rglogger.Handler('<your_api_key>')
    root_logger.addHandler(raygun_handler)
    ```

# Options
`rglogger.Handler` accepts the following arguments:

  - `api_key`: Your Raygun.io API key. Required.
  - `raygun_endpoint`: An alternative endpoint. Defaults to `https://api.raygun.io/entries`.
  - `version`: Your app's version. Defaults to `''`.
  - `transmit_local_variables`: Should we gather and send local variables with the message? Defaults to `True`.
  - `transmit_global_variables`: Should we gather and send global variables with the message? Defaults to `True`.
  - `timeout`: How long to wait on HTTP connections to the API, in seconds.  Defaults to `30`.
  - `machine_name`: A string representing the current host.  Defaults to `socket.gethostname()`.
  - `tags`: A list of strings with which to tag outgoing messages.  Defaults to `[]`.

# Customization Examples

## Log all uncaught exceptions.
```python
    from rglogger import Handler

    raygun_handler = Handler('<your_api_key')
    rglogger.catch_all(raygun_handler)  # Hooks into sys.excepthook for you!
```

## Log messages above a certain level.
The following example only logs errors and exceptions.  Calls to logging.debug() will work, but won't be sent to Raygun.
```python
    import logging
    from rglogger import Handler

    logger = logging.getLogger()
    logger.addHandler(Handler('<your_api_key>', level=logging.ERROR))
```

## Conditionally disable Raygun messages.
Want to disable logging to Raygun if a certain condition is met on a per-message basis?  Add a filter to your Logger!  Here's an example which only logs to Raygun when Django's `DEBUG` setting is set to `False`:

```python
    import logging
    from rglogger import Handler
    from django.conf import settings

    logger = logging.getLogger()
    logger.addFilter(lambda logrecord: not settings.DEBUG)
    logger.addHandler(Handler('<your_api_key'))
```

# License
MIT. See LICENSE for more details.

# Contributions
Pull Requests welcome.  Please try to adhere to PEP-8, but don't worry about line lengths.
