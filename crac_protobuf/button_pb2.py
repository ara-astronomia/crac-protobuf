# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: crac_protobuf/button.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='crac_protobuf/button.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1a\x63rac_protobuf/button.proto\"\x10\n\x0e\x42uttonsRequest\"I\n\rButtonRequest\x12\x1d\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\r.ButtonAction\x12\x19\n\x04type\x18\x02 \x01(\x0e\x32\x0b.ButtonType\"G\n\x0b\x42uttonEntry\x12\x18\n\x03key\x18\x01 \x01(\x0e\x32\x0b.ButtonType\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0f.ButtonResponse\"0\n\x0f\x42uttonsResponse\x12\x1d\n\x07\x62uttons\x18\x01 \x03(\x0b\x32\x0c.ButtonEntry\"J\n\x0e\x42uttonResponse\x12\x1d\n\x06status\x18\x01 \x01(\x0e\x32\r.ButtonStatus\x12\x19\n\x04type\x18\x02 \x01(\x0e\x32\x0b.ButtonType*V\n\x0c\x42uttonAction\x12\x19\n\x15\x42UTTON_DEFAULT_ACTION\x10\x00\x12\x0b\n\x07TURN_ON\x10\x01\x12\x0c\n\x08TURN_OFF\x10\x02\x12\x10\n\x0c\x43HECK_BUTTON\x10\x03*f\n\nButtonType\x12\x17\n\x13\x42UTTON_DEFAULT_TYPE\x10\x00\x12\x0e\n\nCCD_SWITCH\x10\x01\x12\x0f\n\x0bTELE_SWITCH\x10\x02\x12\x0e\n\nFLAT_LIGHT\x10\x03\x12\x0e\n\nDOME_LIGHT\x10\x04*:\n\x0c\x42uttonStatus\x12\x19\n\x15\x42UTTON_DEFAULT_STATUS\x10\x00\x12\x06\n\x02ON\x10\x01\x12\x07\n\x03OFF\x10\x02\x32\x66\n\x06\x42utton\x12,\n\tSetAction\x12\x0e.ButtonRequest\x1a\x0f.ButtonResponse\x12.\n\tGetStatus\x12\x0f.ButtonsRequest\x1a\x10.ButtonsResponseb\x06proto3'
)

_BUTTONACTION = _descriptor.EnumDescriptor(
  name='ButtonAction',
  full_name='ButtonAction',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BUTTON_DEFAULT_ACTION', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TURN_ON', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TURN_OFF', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CHECK_BUTTON', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=322,
  serialized_end=408,
)
_sym_db.RegisterEnumDescriptor(_BUTTONACTION)

ButtonAction = enum_type_wrapper.EnumTypeWrapper(_BUTTONACTION)
_BUTTONTYPE = _descriptor.EnumDescriptor(
  name='ButtonType',
  full_name='ButtonType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BUTTON_DEFAULT_TYPE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CCD_SWITCH', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TELE_SWITCH', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FLAT_LIGHT', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DOME_LIGHT', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=410,
  serialized_end=512,
)
_sym_db.RegisterEnumDescriptor(_BUTTONTYPE)

ButtonType = enum_type_wrapper.EnumTypeWrapper(_BUTTONTYPE)
_BUTTONSTATUS = _descriptor.EnumDescriptor(
  name='ButtonStatus',
  full_name='ButtonStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BUTTON_DEFAULT_STATUS', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ON', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OFF', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=514,
  serialized_end=572,
)
_sym_db.RegisterEnumDescriptor(_BUTTONSTATUS)

ButtonStatus = enum_type_wrapper.EnumTypeWrapper(_BUTTONSTATUS)
BUTTON_DEFAULT_ACTION = 0
TURN_ON = 1
TURN_OFF = 2
CHECK_BUTTON = 3
BUTTON_DEFAULT_TYPE = 0
CCD_SWITCH = 1
TELE_SWITCH = 2
FLAT_LIGHT = 3
DOME_LIGHT = 4
BUTTON_DEFAULT_STATUS = 0
ON = 1
OFF = 2



_BUTTONSREQUEST = _descriptor.Descriptor(
  name='ButtonsRequest',
  full_name='ButtonsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=30,
  serialized_end=46,
)


_BUTTONREQUEST = _descriptor.Descriptor(
  name='ButtonRequest',
  full_name='ButtonRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='ButtonRequest.action', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='ButtonRequest.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=48,
  serialized_end=121,
)


_BUTTONENTRY = _descriptor.Descriptor(
  name='ButtonEntry',
  full_name='ButtonEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ButtonEntry.key', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='ButtonEntry.value', index=1,
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
  serialized_start=123,
  serialized_end=194,
)


_BUTTONSRESPONSE = _descriptor.Descriptor(
  name='ButtonsResponse',
  full_name='ButtonsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='buttons', full_name='ButtonsResponse.buttons', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=196,
  serialized_end=244,
)


_BUTTONRESPONSE = _descriptor.Descriptor(
  name='ButtonResponse',
  full_name='ButtonResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ButtonResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='ButtonResponse.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=246,
  serialized_end=320,
)

_BUTTONREQUEST.fields_by_name['action'].enum_type = _BUTTONACTION
_BUTTONREQUEST.fields_by_name['type'].enum_type = _BUTTONTYPE
_BUTTONENTRY.fields_by_name['key'].enum_type = _BUTTONTYPE
_BUTTONENTRY.fields_by_name['value'].message_type = _BUTTONRESPONSE
_BUTTONSRESPONSE.fields_by_name['buttons'].message_type = _BUTTONENTRY
_BUTTONRESPONSE.fields_by_name['status'].enum_type = _BUTTONSTATUS
_BUTTONRESPONSE.fields_by_name['type'].enum_type = _BUTTONTYPE
DESCRIPTOR.message_types_by_name['ButtonsRequest'] = _BUTTONSREQUEST
DESCRIPTOR.message_types_by_name['ButtonRequest'] = _BUTTONREQUEST
DESCRIPTOR.message_types_by_name['ButtonEntry'] = _BUTTONENTRY
DESCRIPTOR.message_types_by_name['ButtonsResponse'] = _BUTTONSRESPONSE
DESCRIPTOR.message_types_by_name['ButtonResponse'] = _BUTTONRESPONSE
DESCRIPTOR.enum_types_by_name['ButtonAction'] = _BUTTONACTION
DESCRIPTOR.enum_types_by_name['ButtonType'] = _BUTTONTYPE
DESCRIPTOR.enum_types_by_name['ButtonStatus'] = _BUTTONSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ButtonsRequest = _reflection.GeneratedProtocolMessageType('ButtonsRequest', (_message.Message,), {
  'DESCRIPTOR' : _BUTTONSREQUEST,
  '__module__' : 'crac_protobuf.button_pb2'
  # @@protoc_insertion_point(class_scope:ButtonsRequest)
  })
_sym_db.RegisterMessage(ButtonsRequest)

ButtonRequest = _reflection.GeneratedProtocolMessageType('ButtonRequest', (_message.Message,), {
  'DESCRIPTOR' : _BUTTONREQUEST,
  '__module__' : 'crac_protobuf.button_pb2'
  # @@protoc_insertion_point(class_scope:ButtonRequest)
  })
_sym_db.RegisterMessage(ButtonRequest)

ButtonEntry = _reflection.GeneratedProtocolMessageType('ButtonEntry', (_message.Message,), {
  'DESCRIPTOR' : _BUTTONENTRY,
  '__module__' : 'crac_protobuf.button_pb2'
  # @@protoc_insertion_point(class_scope:ButtonEntry)
  })
_sym_db.RegisterMessage(ButtonEntry)

ButtonsResponse = _reflection.GeneratedProtocolMessageType('ButtonsResponse', (_message.Message,), {
  'DESCRIPTOR' : _BUTTONSRESPONSE,
  '__module__' : 'crac_protobuf.button_pb2'
  # @@protoc_insertion_point(class_scope:ButtonsResponse)
  })
_sym_db.RegisterMessage(ButtonsResponse)

ButtonResponse = _reflection.GeneratedProtocolMessageType('ButtonResponse', (_message.Message,), {
  'DESCRIPTOR' : _BUTTONRESPONSE,
  '__module__' : 'crac_protobuf.button_pb2'
  # @@protoc_insertion_point(class_scope:ButtonResponse)
  })
_sym_db.RegisterMessage(ButtonResponse)



_BUTTON = _descriptor.ServiceDescriptor(
  name='Button',
  full_name='Button',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=574,
  serialized_end=676,
  methods=[
  _descriptor.MethodDescriptor(
    name='SetAction',
    full_name='Button.SetAction',
    index=0,
    containing_service=None,
    input_type=_BUTTONREQUEST,
    output_type=_BUTTONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetStatus',
    full_name='Button.GetStatus',
    index=1,
    containing_service=None,
    input_type=_BUTTONSREQUEST,
    output_type=_BUTTONSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BUTTON)

DESCRIPTOR.services_by_name['Button'] = _BUTTON

# @@protoc_insertion_point(module_scope)
