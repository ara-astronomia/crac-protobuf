# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import telescope_pb2 as telescope__pb2


class ButtonStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetAction = channel.unary_unary(
                '/Button/SetAction',
                request_serializer=telescope__pb2.TelescopeRequest.SerializeToString,
                response_deserializer=telescope__pb2.TelescopeResponse.FromString,
                )


class ButtonServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SetAction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ButtonServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetAction': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAction,
                    request_deserializer=telescope__pb2.TelescopeRequest.FromString,
                    response_serializer=telescope__pb2.TelescopeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Button', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Button(object):
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
        return grpc.experimental.unary_unary(request, target, '/Button/SetAction',
            telescope__pb2.TelescopeRequest.SerializeToString,
            telescope__pb2.TelescopeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
