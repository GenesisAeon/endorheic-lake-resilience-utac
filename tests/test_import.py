import importlib

import pytest

MODULES = ["ingest", "surface", "waterbalance", "ews", "compare", "report"]


def test_version():
    import endorheic_lake_resilience as elr

    assert elr.__version__ == "0.0.1"


@pytest.mark.parametrize("name", MODULES)
def test_submodules_import(name):
    importlib.import_module(f"endorheic_lake_resilience.{name}")
