import pytest
import salt.modules.test as testmod
import saltext.salt_ext_modules_kubernetes.modules.salt_ext_modules_kubernetes_mod as salt_ext_modules_kubernetes_module


@pytest.fixture
def configure_loader_modules():
    module_globals = {
        "__salt__": {"test.echo": testmod.echo},
    }
    return {
        salt_ext_modules_kubernetes_module: module_globals,
    }


def test_replace_this_this_with_something_meaningful():
    echo_str = "Echoed!"
    assert salt_ext_modules_kubernetes_module.example_function(echo_str) == echo_str
