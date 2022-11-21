# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: crac_protobuf/telescope.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from crac_protobuf import button_pb2 as crac__protobuf_dot_button__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x63rac_protobuf/telescope.proto\x1a\x1a\x63rac_protobuf/button.proto\"G\n\x10TelescopeRequest\x12 \n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\x10.TelescopeAction\x12\x11\n\tautolight\x18\x02 \x01(\x08\"J\n\"TelescopeEquatorialMovementRequest\x12$\n\teq_coords\x18\x01 \x01(\x0b\x32\x11.EquatorialCoords\"L\n#TelescopeAltazimutalMovementRequest\x12%\n\taz_coords\x18\x01 \x01(\x0b\x32\x12.AltazimutalCoords\"+\n\x10\x45quatorialCoords\x12\n\n\x02ra\x18\x01 \x01(\x01\x12\x0b\n\x03\x64\x65\x63\x18\x02 \x01(\x01\",\n\x11\x41ltazimutalCoords\x12\x0b\n\x03\x61lt\x18\x01 \x01(\x01\x12\n\n\x02\x61z\x18\x02 \x01(\x01\"\xe1\x01\n\x11TelescopeResponse\x12 \n\x06status\x18\x01 \x01(\x0e\x32\x10.TelescopeStatus\x12$\n\teq_coords\x18\x02 \x01(\x0b\x32\x11.EquatorialCoords\x12%\n\taa_coords\x18\x03 \x01(\x0b\x32\x12.AltazimutalCoords\x12\x1e\n\x05speed\x18\x04 \x01(\x0e\x32\x0f.TelescopeSpeed\x12\x1c\n\tpier_side\x18\x06 \x01(\x0e\x32\t.PierSide\x12\x1f\n\x0b\x62uttons_gui\x18\x07 \x03(\x0b\x32\n.ButtonGui*\xa5\x01\n\x0fTelescopeAction\x12\x1c\n\x18TELESCOPE_DEFAULT_ACTION\x10\x00\x12\x08\n\x04SYNC\x10\x01\x12\x11\n\rPARK_POSITION\x10\x02\x12\x11\n\rFLAT_POSITION\x10\x03\x12\x13\n\x0f\x43HECK_TELESCOPE\x10\x04\x12\x15\n\x11TELESCOPE_CONNECT\x10\x05\x12\x18\n\x14TELESCOPE_DISCONNECT\x10\x06*\xcb\x01\n\x0fTelescopeStatus\x12\x1c\n\x18TELESCOPE_DEFAULT_STATUS\x10\x00\x12\n\n\x06PARKED\x10\x01\x12\x0b\n\x07\x46LATTER\x10\x02\x12\n\n\x06SECURE\x10\x03\x12\r\n\tNORTHEAST\x10\x04\x12\x08\n\x04\x45\x41ST\x10\x05\x12\r\n\tSOUTHEAST\x10\x06\x12\r\n\tSOUTHWEST\x10\x07\x12\x08\n\x04WEST\x10\x08\x12\r\n\tNORTHWEST\x10\t\x12\x08\n\x04LOST\x10\n\x12\t\n\x05\x45RROR\x10\x0b\x12\x10\n\x0c\x44ISCONNECTED\x10\x0c*>\n\x08PierSide\x12\x14\n\x10\x44\x45\x46\x41ULT_PIERSIDE\x10\x00\x12\r\n\tEAST_SIDE\x10\x01\x12\r\n\tWEST_SIDE\x10\x02*u\n\x0eTelescopeSpeed\x12\x16\n\x12SPEED_NOT_TRACKING\x10\x00\x12\x12\n\x0eSPEED_TRACKING\x10\x01\x12\x13\n\x0fSPEED_CENTERING\x10\x02\x12\x11\n\rSPEED_SLEWING\x10\x03\x12\x0f\n\x0bSPEED_ERROR\x10\x04\x32\xc6\x01\n\tTelescope\x12\x32\n\tSetAction\x12\x11.TelescopeRequest\x1a\x12.TelescopeResponse\x12\x41\n\x06\x45qMove\x12#.TelescopeEquatorialMovementRequest\x1a\x12.TelescopeResponse\x12\x42\n\x06\x41\x41Move\x12$.TelescopeAltazimutalMovementRequest\x1a\x12.TelescopeResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'crac_protobuf.telescope_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TELESCOPEACTION._serialized_start=608
  _TELESCOPEACTION._serialized_end=773
  _TELESCOPESTATUS._serialized_start=776
  _TELESCOPESTATUS._serialized_end=979
  _PIERSIDE._serialized_start=981
  _PIERSIDE._serialized_end=1043
  _TELESCOPESPEED._serialized_start=1045
  _TELESCOPESPEED._serialized_end=1162
  _TELESCOPEREQUEST._serialized_start=61
  _TELESCOPEREQUEST._serialized_end=132
  _TELESCOPEEQUATORIALMOVEMENTREQUEST._serialized_start=134
  _TELESCOPEEQUATORIALMOVEMENTREQUEST._serialized_end=208
  _TELESCOPEALTAZIMUTALMOVEMENTREQUEST._serialized_start=210
  _TELESCOPEALTAZIMUTALMOVEMENTREQUEST._serialized_end=286
  _EQUATORIALCOORDS._serialized_start=288
  _EQUATORIALCOORDS._serialized_end=331
  _ALTAZIMUTALCOORDS._serialized_start=333
  _ALTAZIMUTALCOORDS._serialized_end=377
  _TELESCOPERESPONSE._serialized_start=380
  _TELESCOPERESPONSE._serialized_end=605
  _TELESCOPE._serialized_start=1165
  _TELESCOPE._serialized_end=1363
# @@protoc_insertion_point(module_scope)
