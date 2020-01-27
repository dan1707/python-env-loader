from enum import Enum


class EnvTypes(Enum):
    DEFAULT_ENV = "default"
    PRODUCTION_ENV = "production"
    DEVELOPMENT_ENV = "development"
    TEST_ENV = "test"


HIERARCHY = {
    EnvTypes.DEFAULT_ENV: (
        ".env",
        ".env.local",
    ),
    EnvTypes.PRODUCTION_ENV: (
        ".env",
        ".env.local",
        ".env.production",
        ".env.production.local",
    ),
    EnvTypes.TEST_ENV: (
        ".env",
        ".env.test",
        ".env.test.local",
    ),
    EnvTypes.DEVELOPMENT_ENV: (
        ".env",
        ".env.local",
        ".env.development",
        ".env.development.local",
    )
}

BOOL_TRUE_VALUES = [
    "true", "True", "y",
]
BOOL_FALSE_VALUES = [
    "false", "False", "n",
]
NULL_VALUES = [
    "", "null", "None",
]