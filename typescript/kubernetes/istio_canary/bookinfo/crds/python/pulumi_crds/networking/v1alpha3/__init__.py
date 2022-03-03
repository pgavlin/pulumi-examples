# coding=utf-8
# *** WARNING: this file was generated by crd2pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .DestinationRule import *
from .EnvoyFilter import *
from .Gateway import *
from .ServiceEntry import *
from .Sidecar import *
from .VirtualService import *
from .WorkloadEntry import *
from .WorkloadGroup import *
from ._inputs import *
from . import outputs

def _register_module():
    import pulumi
    from ... import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "kubernetes:networking.istio.io/v1alpha3:DestinationRule":
                return DestinationRule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:networking.istio.io/v1alpha3:EnvoyFilter":
                return EnvoyFilter(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:networking.istio.io/v1alpha3:Gateway":
                return Gateway(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:networking.istio.io/v1alpha3:ServiceEntry":
                return ServiceEntry(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:networking.istio.io/v1alpha3:Sidecar":
                return Sidecar(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:networking.istio.io/v1alpha3:VirtualService":
                return VirtualService(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:networking.istio.io/v1alpha3:WorkloadEntry":
                return WorkloadEntry(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:networking.istio.io/v1alpha3:WorkloadGroup":
                return WorkloadGroup(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("crds", "networking.istio.io/v1alpha3", _module_instance)

_register_module()