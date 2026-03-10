import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--slow", action="store_true", default=False, help="run slow tests"
    )
    parser.addoption(
        "--hypothesis",
        action="store_true",
        default=False,
        help="run property-based hypothesis tests",
    )


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line(
        "markers", "hypothesis: marks property-based tests (excluded from CI)"
    )


def pytest_collection_modifyitems(config, items):
    if not config.getoption("--slow"):
        skip = pytest.mark.skip(reason="use --slow to run")
        for item in items:
            if "slow" in item.keywords:
                item.add_marker(skip)

    if not config.getoption("--hypothesis", default=False):
        skip = pytest.mark.skip(reason="use --hypothesis to run")
        for item in items:
            if "hypothesis" in item.keywords:
                item.add_marker(skip)
