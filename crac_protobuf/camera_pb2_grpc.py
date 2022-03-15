# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from crac_protobuf import camera_pb2 as crac__protobuf_dot_camera__pb2


class CameraStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetAction = channel.unary_unary(
                '/Camera/SetAction',
                request_serializer=crac__protobuf_dot_camera__pb2.CameraRequest.SerializeToString,
                response_deserializer=crac__protobuf_dot_camera__pb2.CameraResponse.FromString,
                )
        self.Video = channel.unary_stream(
                '/Camera/Video',
                request_serializer=crac__protobuf_dot_camera__pb2.CameraRequest.SerializeToString,
                response_deserializer=crac__protobuf_dot_camera__pb2.CameraResponse.FromString,
                )


class CameraServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SetAction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Video(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CameraServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetAction': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAction,
                    request_deserializer=crac__protobuf_dot_camera__pb2.CameraRequest.FromString,
                    response_serializer=crac__protobuf_dot_camera__pb2.CameraResponse.SerializeToString,
            ),
            'Video': grpc.unary_stream_rpc_method_handler(
                    servicer.Video,
                    request_deserializer=crac__protobuf_dot_camera__pb2.CameraRequest.FromString,
                    response_serializer=crac__protobuf_dot_camera__pb2.CameraResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Camera', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Camera(object):
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
        return grpc.experimental.unary_unary(request, target, '/Camera/SetAction',
            crac__protobuf_dot_camera__pb2.CameraRequest.SerializeToString,
            crac__protobuf_dot_camera__pb2.CameraResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Video(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Camera/Video',
            crac__protobuf_dot_camera__pb2.CameraRequest.SerializeToString,
            crac__protobuf_dot_camera__pb2.CameraResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
