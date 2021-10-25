
"""
Salt state module
"""
import logging

log = logging.getLogger(__name__)

__virtualname__ = "kubernetes"


def __virtual__():
    # To force a module not to load return something like:
    #   return (False, "The salt-ext-modules-kubernetes state module is not implemented yet")

    # Replace this with your own logic
    if "kubernetes.example_function" not in __salt__:
        return False, "The 'kubernetes' execution module is not available"
    return __virtualname__


def exampled(name):
    """
    This example function should be replaced
    """
    ret = {"name": name, "changes": {}, "result": False, "comment": ""}
    value = __salt__["kubernetes.example_function"](name)
    if value == name:
        ret["result"] = True
        ret["comment"] = "The 'kubernetes.example_function' returned: '{}'".format(value)
    return ret
