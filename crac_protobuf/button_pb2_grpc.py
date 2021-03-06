# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from crac_protobuf import button_pb2 as crac__protobuf_dot_button__pb2


class ButtonStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetAction = channel.unary_unary(
                '/Button/SetAction',
                request_serializer=crac__protobuf_dot_button__pb2.ButtonRequest.SerializeToString,
                response_deserializer=crac__protobuf_dot_button__pb2.ButtonResponse.FromString,
                )
        self.GetStatus = channel.unary_unary(
                '/Button/GetStatus',
                request_serializer=crac__protobuf_dot_button__pb2.ButtonsRequest.SerializeToString,
                response_deserializer=crac__protobuf_dot_button__pb2.ButtonsResponse.FromString,
                )


class ButtonServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SetAction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ButtonServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetAction': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAction,
                    request_deserializer=crac__protobuf_dot_button__pb2.ButtonRequest.FromString,
                    response_serializer=crac__protobuf_dot_button__pb2.ButtonResponse.SerializeToString,
            ),
            'GetStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStatus,
                    request_deserializer=crac__protobuf_dot_button__pb2.ButtonsRequest.FromString,
                    response_serializer=crac__protobuf_dot_button__pb2.ButtonsResponse.SerializeToString,
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
            crac__protobuf_dot_button__pb2.ButtonRequest.SerializeToString,
            crac__protobuf_dot_button__pb2.ButtonResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Button/GetStatus',
            crac__protobuf_dot_button__pb2.ButtonsRequest.SerializeToString,
            crac__protobuf_dot_button__pb2.ButtonsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
