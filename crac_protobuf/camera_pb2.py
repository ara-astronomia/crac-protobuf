# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: crac_protobuf/camera.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from crac_protobuf import button_pb2 as crac__protobuf_dot_button__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x63rac_protobuf/camera.proto\x1a\x1a\x63rac_protobuf/button.proto\"f\n\rCameraRequest\x12\x1d\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\r.CameraAction\x12\x13\n\x04move\x18\x02 \x01(\x0e\x32\x05.Move\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x61utodisplay\x18\x04 \x01(\x08\"y\n\x0e\x43\x61meraResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05video\x18\x02 \x01(\x0c\x12\n\n\x02ir\x18\x03 \x01(\x08\x12\x1d\n\x06status\x18\x04 \x01(\x0e\x32\r.CameraStatus\x12\x1f\n\x0b\x62uttons_gui\x18\x05 \x03(\x0b\x32\n.ButtonGui\"Q\n\x0f\x43\x61merasResponse\x12\x1e\n\x07\x63\x61mera1\x18\x01 \x01(\x0b\x32\r.CameraDevice\x12\x1e\n\x07\x63\x61mera2\x18\x02 \x01(\x0b\x32\r.CameraDevice\":\n\x0c\x43\x61meraDevice\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1c\n\x08\x66\x65\x61tures\x18\x02 \x03(\x0e\x32\n.ButtonKey*\xba\x01\n\x04Move\x12\x14\n\x10MOVE_UNSPECIFIED\x10\x00\x12\x0b\n\x07MOVE_UP\x10\x01\x12\x12\n\x0eMOVE_TOP_RIGHT\x10\x02\x12\x0e\n\nMOVE_RIGHT\x10\x03\x12\x15\n\x11MOVE_BOTTOM_RIGHT\x10\x04\x12\r\n\tMOVE_DOWN\x10\x05\x12\x14\n\x10MOVE_BOTTOM_LEFT\x10\x06\x12\r\n\tMOVE_LEFT\x10\x07\x12\x11\n\rMOVE_TOP_LEFT\x10\x08\x12\r\n\tMOVE_STOP\x10\t*\xd3\x01\n\x0c\x43\x61meraAction\x12\x12\n\x0e\x43\x41MERA_INVALID\x10\x00\x12\x12\n\x0e\x43\x41MERA_CONNECT\x10\x01\x12\x15\n\x11\x43\x41MERA_DISCONNECT\x10\x02\x12\x14\n\x10\x43\x41MERA_IR_ENABLE\x10\x03\x12\x15\n\x11\x43\x41MERA_IR_DISABLE\x10\x04\x12\x0f\n\x0b\x43\x41MERA_SHOW\x10\x05\x12\x0f\n\x0b\x43\x41MERA_HIDE\x10\x06\x12\x0f\n\x0b\x43\x41MERA_MOVE\x10\x07\x12\x10\n\x0c\x43\x41MERA_CHECK\x10\x08\x12\x12\n\x0e\x43\x41MERA_IR_AUTO\x10\t*g\n\x0c\x43\x61meraStatus\x12\x19\n\x15\x43\x41MERA_INVALID_STATUS\x10\x00\x12\x17\n\x13\x43\x41MERA_DISCONNECTED\x10\x02\x12\x11\n\rCAMERA_HIDDEN\x10\x03\x12\x10\n\x0c\x43\x41MERA_SHOWN\x10\x04\x32\x93\x01\n\x06\x43\x61mera\x12,\n\tSetAction\x12\x0e.CameraRequest\x1a\x0f.CameraResponse\x12*\n\x05Video\x12\x0e.CameraRequest\x1a\x0f.CameraResponse0\x01\x12/\n\x0bListCameras\x12\x0e.CameraRequest\x1a\x10.CamerasResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'crac_protobuf.camera_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MOVE']._serialized_start=429
  _globals['_MOVE']._serialized_end=615
  _globals['_CAMERAACTION']._serialized_start=618
  _globals['_CAMERAACTION']._serialized_end=829
  _globals['_CAMERASTATUS']._serialized_start=831
  _globals['_CAMERASTATUS']._serialized_end=934
  _globals['_CAMERAREQUEST']._serialized_start=58
  _globals['_CAMERAREQUEST']._serialized_end=160
  _globals['_CAMERARESPONSE']._serialized_start=162
  _globals['_CAMERARESPONSE']._serialized_end=283
  _globals['_CAMERASRESPONSE']._serialized_start=285
  _globals['_CAMERASRESPONSE']._serialized_end=366
  _globals['_CAMERADEVICE']._serialized_start=368
  _globals['_CAMERADEVICE']._serialized_end=426
  _globals['_CAMERA']._serialized_start=937
  _globals['_CAMERA']._serialized_end=1084
# @@protoc_insertion_point(module_scope)
