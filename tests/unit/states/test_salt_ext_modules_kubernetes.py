import pytest
import salt.modules.test as testmod
import saltext.salt_ext_modules_kubernetes.modules.salt_ext_modules_kubernetes_mod as salt_ext_modules_kubernetes_module
import saltext.salt_ext_modules_kubernetes.states.salt_ext_modules_kubernetes_mod as salt_ext_modules_kubernetes_state


@pytest.fixture
def configure_loader_modules():
    return {
        salt_ext_modules_kubernetes_module: {
            "__salt__": {
                "test.echo": testmod.echo,
            },
        },
        salt_ext_modules_kubernetes_state: {
            "__salt__": {
                "salt_ext_modules_kubernetes.example_function": salt_ext_modules_kubernetes_module.example_function,
            },
        },
    }


def test_replace_this_this_with_something_meaningful():
    echo_str = "Echoed!"
    expected = {
        "name": echo_str,
        "changes": {},
        "result": True,
        "comment": "The 'salt_ext_modules_kubernetes.example_function' returned: '{}'".format(echo_str),
    }
    assert salt_ext_modules_kubernetes_state.exampled(echo_str) == expected
