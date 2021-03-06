"""
When you run tests with `./manage.py test` these settings are ALWAYS
imported last and overrides any other base or environment variable
settings.

The purpose of this is to guarantee that certain settings are always
set for test suite runs no matter what you do on the local system.

Ultimately, it helps make sure you never actually use real URLs. For
example, if a test incorrectly doesn't mock `requests.get()` for
example, it shouldn't actually try to reach out to a real valid URL.
"""

CACHE_MIDDLEWARE = True
CACHE_MIDDLEWARE_FILES = False

DEFAULT_PRODUCT = 'WaterWolf'

# here we deliberately "destroy" the BZAPI URL so running tests that are
# badly mocked never accidentally actually use a real working network address
BZAPI_BASE_URL = 'https://bugzilla.testrunner/rest'

# by scrubbing this to something unreal, we can be certain the tests never
# actually go out on the internet when `request.get` should always be mocked
MWARE_BASE_URL = 'http://shouldnotactuallybeused.com'

STATSD_CLIENT = 'django_statsd.clients.null'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# Because this is for running tests, we use the simplest hasher possible.
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)


# don't accidentally send anything to sentry whilst running tests
RAVEN_CONFIG = {}
SENTRY_DSN = None


BROWSERID_AUDIENCES = ['http://testserver']

# Make sure these have something but something not right
# so the tests never accidentally manage to connect to AWS
# for realz.
AWS_ACCESS_KEY = 'something'
AWS_SECRET_ACCESS_KEY = 'anything'
SYMBOLS_BUCKET_DEFAULT_NAME = 'my-lovely-bucket'
SYMBOLS_FILE_PREFIX = 'v99'
SYMBOLS_BUCKET_DEFAULT_LOCATION = 'us-west-2'


# So it never ever actually uses a real ElasticSearch server
SOCORRO_IMPLEMENTATIONS_CONFIG = {
    'elasticsearch': {
        'elasticsearch_urls': ['http://example:9123'],
    },
}


# Make sure we never actually hit a real URL when testing the
# Crash-analysis monitoring.
CRASH_ANALYSIS_URL = 'https://crashanalysis.m.c/something/'
CRASH_ANALYSIS_MONITOR_DAYS_BACK = 2

MIDDLEWARE_RETRIES = 10
MIDDLEWARE_MIDDLEWARE_RETRY_SLEEPTIME = 3
