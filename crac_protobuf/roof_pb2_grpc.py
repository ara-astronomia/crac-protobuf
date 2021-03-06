# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from crac_protobuf import roof_pb2 as crac__protobuf_dot_roof__pb2


class RoofStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetAction = channel.unary_unary(
                '/Roof/SetAction',
                request_serializer=crac__protobuf_dot_roof__pb2.RoofRequest.SerializeToString,
                response_deserializer=crac__protobuf_dot_roof__pb2.RoofResponse.FromString,
                )


class RoofServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SetAction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RoofServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetAction': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAction,
                    request_deserializer=crac__protobuf_dot_roof__pb2.RoofRequest.FromString,
                    response_serializer=crac__protobuf_dot_roof__pb2.RoofResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Roof', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Roof(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SetAction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Roof/SetAction',
            crac__protobuf_dot_roof__pb2.RoofRequest.SerializeToString,
            crac__protobuf_dot_roof__pb2.RoofResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
