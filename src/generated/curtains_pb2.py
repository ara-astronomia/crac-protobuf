# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: generated/curtains.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='generated/curtains.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18generated/curtains.proto\"i\n\x0e\x43urtainRequest\x12(\n\x0borientation\x18\x01 \x01(\x0e\x32\x13.CurtainOrientation\x12\x1e\n\x06\x61\x63tion\x18\x02 \x01(\x0e\x32\x0e.CurtainAction\x12\r\n\x05steps\x18\x03 \x01(\x05\"_\n\x0f\x43urtainsRequest\x12%\n\x0c\x63urtain_east\x18\x01 \x01(\x0b\x32\x0f.CurtainRequest\x12%\n\x0c\x63urtain_west\x18\x02 \x01(\x0b\x32\x0f.CurtainRequest\"j\n\x0f\x43urtainResponse\x12(\n\x0borientation\x18\x01 \x01(\x0e\x32\x13.CurtainOrientation\x12\r\n\x05steps\x18\x02 \x01(\x05\x12\x1e\n\x06status\x18\x03 \x01(\x0e\x32\x0e.CurtainStatus\"b\n\x10\x43urtainsResponse\x12&\n\x0c\x63urtain_east\x18\x01 \x01(\x0b\x32\x10.CurtainResponse\x12&\n\x0c\x63urtain_west\x18\x02 \x01(\x0b\x32\x10.CurtainResponse*o\n\rCurtainAction\x12\x1a\n\x16\x43URTAIN_DEFAULT_ACTION\x10\x00\x12\n\n\x06\x45NABLE\x10\x01\x12\x0b\n\x07\x44ISABLE\x10\x02\x12\x16\n\x12\x43\x41LIBRATE_CURTAINS\x10\x03\x12\x11\n\rCHECK_CURTAIN\x10\x04*Y\n\x12\x43urtainOrientation\x12\x1f\n\x1b\x43URTAIN_DEFAULT_ORIENTATION\x10\x00\x12\x10\n\x0c\x43URTAIN_EAST\x10\x01\x12\x10\n\x0c\x43URTAIN_WEST\x10\x02*\xcf\x01\n\rCurtainStatus\x12\x1a\n\x16\x43URTAIN_DEFAULT_STATUS\x10\x00\x12\x14\n\x10\x43URTAIN_DISABLED\x10\x01\x12\x12\n\x0e\x43URTAIN_CLOSED\x10\x02\x12\x13\n\x0f\x43URTAIN_STOPPED\x10\x03\x12\x12\n\x0e\x43URTAIN_OPENED\x10\x04\x12\x13\n\x0f\x43URTAIN_CLOSING\x10\x05\x12\x13\n\x0f\x43URTAIN_OPENING\x10\x06\x12\x12\n\x0e\x43URTAIN_DANGER\x10\x07\x12\x11\n\rCURTAIN_ERROR\x10\x08\x32;\n\x07\x43urtain\x12\x30\n\tSetAction\x12\x10.CurtainsRequest\x1a\x11.CurtainsResponseb\x06proto3'
)

_CURTAINACTION = _descriptor.EnumDescriptor(
  name='CurtainAction',
  full_name='CurtainAction',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CURTAIN_DEFAULT_ACTION', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENABLE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DISABLE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CALIBRATE_CURTAINS', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CHECK_CURTAIN', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=440,
  serialized_end=551,
)
_sym_db.RegisterEnumDescriptor(_CURTAINACTION)

CurtainAction = enum_type_wrapper.EnumTypeWrapper(_CURTAINACTION)
_CURTAINORIENTATION = _descriptor.EnumDescriptor(
  name='CurtainOrientation',
  full_name='CurtainOrientation',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CURTAIN_DEFAULT_ORIENTATION', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CURTAIN_EAST', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CURTAIN_WEST', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=553,
  serialized_end=642,
)
_sym_db.RegisterEnumDescriptor(_CURTAINORIENTATION)

CurtainOrientation = enum_type_wrapper.EnumTypeWrapper(_CURTAINORIENTATION)
_CURTAINSTATUS = _descriptor.EnumDescriptor(
  name='CurtainStatus',
  full_name='CurtainStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CURTAIN_DEFAULT_STATUS', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CURTAIN_DISABLED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CURTAIN_CLOSED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CURTAIN_STOPPED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CURTAIN_OPENED', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CURTAIN_CLOSING', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CURTAIN_OPENING', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CURTAIN_DANGER', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CURTAIN_ERROR', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=645,
  serialized_end=852,
)
_sym_db.RegisterEnumDescriptor(_CURTAINSTATUS)

CurtainStatus = enum_type_wrapper.EnumTypeWrapper(_CURTAINSTATUS)
CURTAIN_DEFAULT_ACTION = 0
ENABLE = 1
DISABLE = 2
CALIBRATE_CURTAINS = 3
CHECK_CURTAIN = 4
CURTAIN_DEFAULT_ORIENTATION = 0
CURTAIN_EAST = 1
CURTAIN_WEST = 2
CURTAIN_DEFAULT_STATUS = 0
CURTAIN_DISABLED = 1
CURTAIN_CLOSED = 2
CURTAIN_STOPPED = 3
CURTAIN_OPENED = 4
CURTAIN_CLOSING = 5
CURTAIN_OPENING = 6
CURTAIN_DANGER = 7
CURTAIN_ERROR = 8



_CURTAINREQUEST = _descriptor.Descriptor(
  name='CurtainRequest',
  full_name='CurtainRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='orientation', full_name='CurtainRequest.orientation', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='action', full_name='CurtainRequest.action', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='steps', full_name='CurtainRequest.steps', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=133,
)


_CURTAINSREQUEST = _descriptor.Descriptor(
  name='CurtainsRequest',
  full_name='CurtainsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='curtain_east', full_name='CurtainsRequest.curtain_east', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='curtain_west', full_name='CurtainsRequest.curtain_west', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=230,
)


_CURTAINRESPONSE = _descriptor.Descriptor(
  name='CurtainResponse',
  full_name='CurtainResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='orientation', full_name='CurtainResponse.orientation', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='steps', full_name='CurtainResponse.steps', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='CurtainResponse.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=232,
  serialized_end=338,
)


_CURTAINSRESPONSE = _descriptor.Descriptor(
  name='CurtainsResponse',
  full_name='CurtainsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='curtain_east', full_name='CurtainsResponse.curtain_east', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='curtain_west', full_name='CurtainsResponse.curtain_west', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=340,
  serialized_end=438,
)

_CURTAINREQUEST.fields_by_name['orientation'].enum_type = _CURTAINORIENTATION
_CURTAINREQUEST.fields_by_name['action'].enum_type = _CURTAINACTION
_CURTAINSREQUEST.fields_by_name['curtain_east'].message_type = _CURTAINREQUEST
_CURTAINSREQUEST.fields_by_name['curtain_west'].message_type = _CURTAINREQUEST
_CURTAINRESPONSE.fields_by_name['orientation'].enum_type = _CURTAINORIENTATION
_CURTAINRESPONSE.fields_by_name['status'].enum_type = _CURTAINSTATUS
_CURTAINSRESPONSE.fields_by_name['curtain_east'].message_type = _CURTAINRESPONSE
_CURTAINSRESPONSE.fields_by_name['curtain_west'].message_type = _CURTAINRESPONSE
DESCRIPTOR.message_types_by_name['CurtainRequest'] = _CURTAINREQUEST
DESCRIPTOR.message_types_by_name['CurtainsRequest'] = _CURTAINSREQUEST
DESCRIPTOR.message_types_by_name['CurtainResponse'] = _CURTAINRESPONSE
DESCRIPTOR.message_types_by_name['CurtainsResponse'] = _CURTAINSRESPONSE
DESCRIPTOR.enum_types_by_name['CurtainAction'] = _CURTAINACTION
DESCRIPTOR.enum_types_by_name['CurtainOrientation'] = _CURTAINORIENTATION
DESCRIPTOR.enum_types_by_name['CurtainStatus'] = _CURTAINSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CurtainRequest = _reflection.GeneratedProtocolMessageType('CurtainRequest', (_message.Message,), {
  'DESCRIPTOR' : _CURTAINREQUEST,
  '__module__' : 'generated.curtains_pb2'
  # @@protoc_insertion_point(class_scope:CurtainRequest)
  })
_sym_db.RegisterMessage(CurtainRequest)

CurtainsRequest = _reflection.GeneratedProtocolMessageType('CurtainsRequest', (_message.Message,), {
  'DESCRIPTOR' : _CURTAINSREQUEST,
  '__module__' : 'generated.curtains_pb2'
  # @@protoc_insertion_point(class_scope:CurtainsRequest)
  })
_sym_db.RegisterMessage(CurtainsRequest)

CurtainResponse = _reflection.GeneratedProtocolMessageType('CurtainResponse', (_message.Message,), {
  'DESCRIPTOR' : _CURTAINRESPONSE,
  '__module__' : 'generated.curtains_pb2'
  # @@protoc_insertion_point(class_scope:CurtainResponse)
  })
_sym_db.RegisterMessage(CurtainResponse)

CurtainsResponse = _reflection.GeneratedProtocolMessageType('CurtainsResponse', (_message.Message,), {
  'DESCRIPTOR' : _CURTAINSRESPONSE,
  '__module__' : 'generated.curtains_pb2'
  # @@protoc_insertion_point(class_scope:CurtainsResponse)
  })
_sym_db.RegisterMessage(CurtainsResponse)



_CURTAIN = _descriptor.ServiceDescriptor(
  name='Curtain',
  full_name='Curtain',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=854,
  serialized_end=913,
  methods=[
  _descriptor.MethodDescriptor(
    name='SetAction',
    full_name='Curtain.SetAction',
    index=0,
    containing_service=None,
    input_type=_CURTAINSREQUEST,
    output_type=_CURTAINSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CURTAIN)

DESCRIPTOR.services_by_name['Curtain'] = _CURTAIN

# @@protoc_insertion_point(module_scope)
