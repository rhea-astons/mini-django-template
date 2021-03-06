import os

from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name, default=None):
    """
    Get the environment variable or return exception
    """
    try:
        return os.environ[var_name]
    except KeyError:
        if default is not None:
            return default
        else:
            error_msg = "Set the %s environment variable" % var_name
            raise ImproperlyConfigured(error_msg)
