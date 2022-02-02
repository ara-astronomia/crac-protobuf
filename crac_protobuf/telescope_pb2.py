# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: crac_protobuf/telescope.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='crac_protobuf/telescope.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1d\x63rac_protobuf/telescope.proto\"4\n\x10TelescopeRequest\x12 \n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\x10.TelescopeAction\"J\n\"TelescopeEquatorialMovementRequest\x12$\n\teq_coords\x18\x01 \x01(\x0b\x32\x11.EquatorialCoords\"L\n#TelescopeAltazimutalMovementRequest\x12%\n\taz_coords\x18\x01 \x01(\x0b\x32\x12.AltazimutalCoords\"+\n\x10\x45quatorialCoords\x12\n\n\x02\x61r\x18\x01 \x01(\x01\x12\x0b\n\x03\x64\x65\x63\x18\x02 \x01(\x01\",\n\x11\x41ltazimutalCoords\x12\x0b\n\x03\x61lt\x18\x01 \x01(\x01\x12\n\n\x02\x61z\x18\x02 \x01(\x01\"\xc2\x01\n\x11TelescopeResponse\x12 \n\x06status\x18\x01 \x01(\x0e\x32\x10.TelescopeStatus\x12$\n\teq_coords\x18\x02 \x01(\x0b\x32\x11.EquatorialCoords\x12%\n\taa_coords\x18\x03 \x01(\x0b\x32\x12.AltazimutalCoords\x12\x10\n\x08tracking\x18\x04 \x01(\x08\x12\x0f\n\x07slewing\x18\x05 \x01(\x08\x12\x1b\n\x08pierSide\x18\x06 \x01(\x0e\x32\t.PierSide*}\n\x0fTelescopeAction\x12\x1c\n\x18TELESCOPE_DEFAULT_ACTION\x10\x00\x12\x11\n\rSYNC_POSITION\x10\x01\x12\x11\n\rPARK_POSITION\x10\x02\x12\x11\n\rFLAT_POSITION\x10\x03\x12\x13\n\x0f\x43HECK_TELESCOPE\x10\x04*\xb9\x01\n\x0fTelescopeStatus\x12\x1c\n\x18TELESCOPE_DEFAULT_STATUS\x10\x00\x12\n\n\x06PARKED\x10\x01\x12\x0b\n\x07\x46LATTER\x10\x02\x12\n\n\x06SECURE\x10\x03\x12\r\n\tNORTHEAST\x10\x04\x12\x08\n\x04\x45\x41ST\x10\x05\x12\r\n\tSOUTHEAST\x10\x06\x12\r\n\tSOUTHWEST\x10\x07\x12\x08\n\x04WEST\x10\x08\x12\r\n\tNORTHWEST\x10\t\x12\x08\n\x04LOST\x10\n\x12\t\n\x05\x45RROR\x10\x0b*>\n\x08PierSide\x12\x14\n\x10\x44\x45\x46\x41ULT_PIERSIDE\x10\x00\x12\r\n\tEAST_SIDE\x10\x01\x12\r\n\tWEST_SIDE\x10\x02\x32\xc6\x01\n\tTelescope\x12\x32\n\tSetAction\x12\x11.TelescopeRequest\x1a\x12.TelescopeResponse\x12\x41\n\x06\x45qMove\x12#.TelescopeEquatorialMovementRequest\x1a\x12.TelescopeResponse\x12\x42\n\x06\x41\x41Move\x12$.TelescopeAltazimutalMovementRequest\x1a\x12.TelescopeResponseb\x06proto3'
)

_TELESCOPEACTION = _descriptor.EnumDescriptor(
  name='TelescopeAction',
  full_name='TelescopeAction',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TELESCOPE_DEFAULT_ACTION', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SYNC_POSITION', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PARK_POSITION', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FLAT_POSITION', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CHECK_TELESCOPE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=529,
  serialized_end=654,
)
_sym_db.RegisterEnumDescriptor(_TELESCOPEACTION)

TelescopeAction = enum_type_wrapper.EnumTypeWrapper(_TELESCOPEACTION)
_TELESCOPESTATUS = _descriptor.EnumDescriptor(
  name='TelescopeStatus',
  full_name='TelescopeStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TELESCOPE_DEFAULT_STATUS', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PARKED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FLATTER', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SECURE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NORTHEAST', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EAST', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SOUTHEAST', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SOUTHWEST', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WEST', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NORTHWEST', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOST', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=657,
  serialized_end=842,
)
_sym_db.RegisterEnumDescriptor(_TELESCOPESTATUS)

TelescopeStatus = enum_type_wrapper.EnumTypeWrapper(_TELESCOPESTATUS)
_PIERSIDE = _descriptor.EnumDescriptor(
  name='PierSide',
  full_name='PierSide',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT_PIERSIDE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EAST_SIDE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WEST_SIDE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=844,
  serialized_end=906,
)
_sym_db.RegisterEnumDescriptor(_PIERSIDE)

PierSide = enum_type_wrapper.EnumTypeWrapper(_PIERSIDE)
TELESCOPE_DEFAULT_ACTION = 0
SYNC_POSITION = 1
PARK_POSITION = 2
FLAT_POSITION = 3
CHECK_TELESCOPE = 4
TELESCOPE_DEFAULT_STATUS = 0
PARKED = 1
FLATTER = 2
SECURE = 3
NORTHEAST = 4
EAST = 5
SOUTHEAST = 6
SOUTHWEST = 7
WEST = 8
NORTHWEST = 9
LOST = 10
ERROR = 11
DEFAULT_PIERSIDE = 0
EAST_SIDE = 1
WEST_SIDE = 2



_TELESCOPEREQUEST = _descriptor.Descriptor(
  name='TelescopeRequest',
  full_name='TelescopeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='TelescopeRequest.action', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=33,
  serialized_end=85,
)


_TELESCOPEEQUATORIALMOVEMENTREQUEST = _descriptor.Descriptor(
  name='TelescopeEquatorialMovementRequest',
  full_name='TelescopeEquatorialMovementRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='eq_coords', full_name='TelescopeEquatorialMovementRequest.eq_coords', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=87,
  serialized_end=161,
)


_TELESCOPEALTAZIMUTALMOVEMENTREQUEST = _descriptor.Descriptor(
  name='TelescopeAltazimutalMovementRequest',
  full_name='TelescopeAltazimutalMovementRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='az_coords', full_name='TelescopeAltazimutalMovementRequest.az_coords', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=163,
  serialized_end=239,
)


_EQUATORIALCOORDS = _descriptor.Descriptor(
  name='EquatorialCoords',
  full_name='EquatorialCoords',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ar', full_name='EquatorialCoords.ar', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dec', full_name='EquatorialCoords.dec', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=241,
  serialized_end=284,
)


_ALTAZIMUTALCOORDS = _descriptor.Descriptor(
  name='AltazimutalCoords',
  full_name='AltazimutalCoords',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='alt', full_name='AltazimutalCoords.alt', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='az', full_name='AltazimutalCoords.az', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=286,
  serialized_end=330,
)


_TELESCOPERESPONSE = _descriptor.Descriptor(
  name='TelescopeResponse',
  full_name='TelescopeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='TelescopeResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='eq_coords', full_name='TelescopeResponse.eq_coords', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='aa_coords', full_name='TelescopeResponse.aa_coords', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tracking', full_name='TelescopeResponse.tracking', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='slewing', full_name='TelescopeResponse.slewing', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pierSide', full_name='TelescopeResponse.pierSide', index=5,
      number=6, type=14, cpp_type=8, label=1,
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
  serialized_start=333,
  serialized_end=527,
)

_TELESCOPEREQUEST.fields_by_name['action'].enum_type = _TELESCOPEACTION
_TELESCOPEEQUATORIALMOVEMENTREQUEST.fields_by_name['eq_coords'].message_type = _EQUATORIALCOORDS
_TELESCOPEALTAZIMUTALMOVEMENTREQUEST.fields_by_name['az_coords'].message_type = _ALTAZIMUTALCOORDS
_TELESCOPERESPONSE.fields_by_name['status'].enum_type = _TELESCOPESTATUS
_TELESCOPERESPONSE.fields_by_name['eq_coords'].message_type = _EQUATORIALCOORDS
_TELESCOPERESPONSE.fields_by_name['aa_coords'].message_type = _ALTAZIMUTALCOORDS
_TELESCOPERESPONSE.fields_by_name['pierSide'].enum_type = _PIERSIDE
DESCRIPTOR.message_types_by_name['TelescopeRequest'] = _TELESCOPEREQUEST
DESCRIPTOR.message_types_by_name['TelescopeEquatorialMovementRequest'] = _TELESCOPEEQUATORIALMOVEMENTREQUEST
DESCRIPTOR.message_types_by_name['TelescopeAltazimutalMovementRequest'] = _TELESCOPEALTAZIMUTALMOVEMENTREQUEST
DESCRIPTOR.message_types_by_name['EquatorialCoords'] = _EQUATORIALCOORDS
DESCRIPTOR.message_types_by_name['AltazimutalCoords'] = _ALTAZIMUTALCOORDS
DESCRIPTOR.message_types_by_name['TelescopeResponse'] = _TELESCOPERESPONSE
DESCRIPTOR.enum_types_by_name['TelescopeAction'] = _TELESCOPEACTION
DESCRIPTOR.enum_types_by_name['TelescopeStatus'] = _TELESCOPESTATUS
DESCRIPTOR.enum_types_by_name['PierSide'] = _PIERSIDE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TelescopeRequest = _reflection.GeneratedProtocolMessageType('TelescopeRequest', (_message.Message,), {
  'DESCRIPTOR' : _TELESCOPEREQUEST,
  '__module__' : 'crac_protobuf.telescope_pb2'
  # @@protoc_insertion_point(class_scope:TelescopeRequest)
  })
_sym_db.RegisterMessage(TelescopeRequest)

TelescopeEquatorialMovementRequest = _reflection.GeneratedProtocolMessageType('TelescopeEquatorialMovementRequest', (_message.Message,), {
  'DESCRIPTOR' : _TELESCOPEEQUATORIALMOVEMENTREQUEST,
  '__module__' : 'crac_protobuf.telescope_pb2'
  # @@protoc_insertion_point(class_scope:TelescopeEquatorialMovementRequest)
  })
_sym_db.RegisterMessage(TelescopeEquatorialMovementRequest)

TelescopeAltazimutalMovementRequest = _reflection.GeneratedProtocolMessageType('TelescopeAltazimutalMovementRequest', (_message.Message,), {
  'DESCRIPTOR' : _TELESCOPEALTAZIMUTALMOVEMENTREQUEST,
  '__module__' : 'crac_protobuf.telescope_pb2'
  # @@protoc_insertion_point(class_scope:TelescopeAltazimutalMovementRequest)
  })
_sym_db.RegisterMessage(TelescopeAltazimutalMovementRequest)

EquatorialCoords = _reflection.GeneratedProtocolMessageType('EquatorialCoords', (_message.Message,), {
  'DESCRIPTOR' : _EQUATORIALCOORDS,
  '__module__' : 'crac_protobuf.telescope_pb2'
  # @@protoc_insertion_point(class_scope:EquatorialCoords)
  })
_sym_db.RegisterMessage(EquatorialCoords)

AltazimutalCoords = _reflection.GeneratedProtocolMessageType('AltazimutalCoords', (_message.Message,), {
  'DESCRIPTOR' : _ALTAZIMUTALCOORDS,
  '__module__' : 'crac_protobuf.telescope_pb2'
  # @@protoc_insertion_point(class_scope:AltazimutalCoords)
  })
_sym_db.RegisterMessage(AltazimutalCoords)

TelescopeResponse = _reflection.GeneratedProtocolMessageType('TelescopeResponse', (_message.Message,), {
  'DESCRIPTOR' : _TELESCOPERESPONSE,
  '__module__' : 'crac_protobuf.telescope_pb2'
  # @@protoc_insertion_point(class_scope:TelescopeResponse)
  })
_sym_db.RegisterMessage(TelescopeResponse)



_TELESCOPE = _descriptor.ServiceDescriptor(
  name='Telescope',
  full_name='Telescope',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=909,
  serialized_end=1107,
  methods=[
  _descriptor.MethodDescriptor(
    name='SetAction',
    full_name='Telescope.SetAction',
    index=0,
    containing_service=None,
    input_type=_TELESCOPEREQUEST,
    output_type=_TELESCOPERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='EqMove',
    full_name='Telescope.EqMove',
    index=1,
    containing_service=None,
    input_type=_TELESCOPEEQUATORIALMOVEMENTREQUEST,
    output_type=_TELESCOPERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AAMove',
    full_name='Telescope.AAMove',
    index=2,
    containing_service=None,
    input_type=_TELESCOPEALTAZIMUTALMOVEMENTREQUEST,
    output_type=_TELESCOPERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TELESCOPE)

DESCRIPTOR.services_by_name['Telescope'] = _TELESCOPE

# @@protoc_insertion_point(module_scope)