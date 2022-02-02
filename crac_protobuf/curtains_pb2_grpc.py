# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from crac_protobuf import curtains_pb2 as crac__protobuf_dot_curtains__pb2


class CurtainStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetAction = channel.unary_unary(
                '/Curtain/SetAction',
                request_serializer=crac__protobuf_dot_curtains__pb2.CurtainsRequest.SerializeToString,
                response_deserializer=crac__protobuf_dot_curtains__pb2.CurtainsResponse.FromString,
                )
        self.Move = channel.unary_unary(
                '/Curtain/Move',
                request_serializer=crac__protobuf_dot_curtains__pb2.CurtainsMovementRequest.SerializeToString,
                response_deserializer=crac__protobuf_dot_curtains__pb2.CurtainsResponse.FromString,
                )


class CurtainServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SetAction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Move(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CurtainServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetAction': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAction,
                    request_deserializer=crac__protobuf_dot_curtains__pb2.CurtainsRequest.FromString,
                    response_serializer=crac__protobuf_dot_curtains__pb2.CurtainsResponse.SerializeToString,
            ),
            'Move': grpc.unary_unary_rpc_method_handler(
                    servicer.Move,
                    request_deserializer=crac__protobuf_dot_curtains__pb2.CurtainsMovementRequest.FromString,
                    response_serializer=crac__protobuf_dot_curtains__pb2.CurtainsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Curtain', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Curtain(object):
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
        return grpc.experimental.unary_unary(request, target, '/Curtain/SetAction',
            crac__protobuf_dot_curtains__pb2.CurtainsRequest.SerializeToString,
            crac__protobuf_dot_curtains__pb2.CurtainsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Move(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Curtain/Move',
            crac__protobuf_dot_curtains__pb2.CurtainsMovementRequest.SerializeToString,
            crac__protobuf_dot_curtains__pb2.CurtainsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)