import pytest
import salt.modules.test as testmod
import saltext.kubernetes.modules.kubernetesmod as kubernetes_module
import saltext.kubernetes.states.kubernetesmod as kubernetes_state


@pytest.fixture
def configure_loader_modules():
    return {
        kubernetes_module: {
            "__salt__": {
                "test.echo": testmod.echo,
            },
        },
        kubernetes_state: {
            "__salt__": {
                "kubernetes.example_function": kubernetes_module.example_function,
            },
        },
    }


def test_replace_this_this_with_something_meaningful():
    echo_str = "Echoed!"
    expected = {
        "name": echo_str,
        "changes": {},
        "result": True,
        "comment": "The 'kubernetes.example_function' returned: '{}'".format(echo_str),
    }
    assert kubernetes_state.exampled(echo_str) == expected
