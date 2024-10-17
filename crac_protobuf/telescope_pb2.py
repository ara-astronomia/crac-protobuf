# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: crac_protobuf/telescope.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from crac_protobuf import button_pb2 as crac__protobuf_dot_button__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x63rac_protobuf/telescope.proto\x1a\x1a\x63rac_protobuf/button.proto\"G\n\x10TelescopeRequest\x12 \n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\x10.TelescopeAction\x12\x11\n\tautolight\x18\x02 \x01(\x08\"J\n\"TelescopeEquatorialMovementRequest\x12$\n\teq_coords\x18\x01 \x01(\x0b\x32\x11.EquatorialCoords\"L\n#TelescopeAltazimutalMovementRequest\x12%\n\taz_coords\x18\x01 \x01(\x0b\x32\x12.AltazimutalCoords\"+\n\x10\x45quatorialCoords\x12\n\n\x02ra\x18\x01 \x01(\x01\x12\x0b\n\x03\x64\x65\x63\x18\x02 \x01(\x01\",\n\x11\x41ltazimutalCoords\x12\x0b\n\x03\x61lt\x18\x01 \x01(\x01\x12\n\n\x02\x61z\x18\x02 \x01(\x01\"\x1a\n\x07\x41irmass\x12\x0f\n\x07\x61irmass\x18\x01 \x01(\x01\"\x1a\n\x07Transit\x12\x0f\n\x07transit\x18\x01 \x01(\t\"(\n\rTimeToTransit\x12\x17\n\x0ftime_to_transit\x18\x01 \x01(\t\"\xc0\x02\n\x11TelescopeResponse\x12 \n\x06status\x18\x01 \x01(\x0e\x32\x10.TelescopeStatus\x12$\n\teq_coords\x18\x02 \x01(\x0b\x32\x11.EquatorialCoords\x12%\n\taa_coords\x18\x03 \x01(\x0b\x32\x12.AltazimutalCoords\x12\x1e\n\x05speed\x18\x04 \x01(\x0e\x32\x0f.TelescopeSpeed\x12\x1c\n\tpier_side\x18\x06 \x01(\x0e\x32\t.PierSide\x12\x1f\n\x0b\x62uttons_gui\x18\x07 \x03(\x0b\x32\n.ButtonGui\x12\x19\n\x07\x61irmass\x18\x08 \x01(\x0b\x32\x08.Airmass\x12\x19\n\x07transit\x18\t \x01(\x0b\x32\x08.Transit\x12\'\n\x0ftime_to_transit\x18\n \x01(\x0b\x32\x0e.TimeToTransit*\xa5\x01\n\x0fTelescopeAction\x12\x1c\n\x18TELESCOPE_DEFAULT_ACTION\x10\x00\x12\x08\n\x04SYNC\x10\x01\x12\x11\n\rPARK_POSITION\x10\x02\x12\x11\n\rFLAT_POSITION\x10\x03\x12\x13\n\x0f\x43HECK_TELESCOPE\x10\x04\x12\x15\n\x11TELESCOPE_CONNECT\x10\x05\x12\x18\n\x14TELESCOPE_DISCONNECT\x10\x06*\xcb\x01\n\x0fTelescopeStatus\x12\x1c\n\x18TELESCOPE_DEFAULT_STATUS\x10\x00\x12\n\n\x06PARKED\x10\x01\x12\x0b\n\x07\x46LATTER\x10\x02\x12\n\n\x06SECURE\x10\x03\x12\r\n\tNORTHEAST\x10\x04\x12\x08\n\x04\x45\x41ST\x10\x05\x12\r\n\tSOUTHEAST\x10\x06\x12\r\n\tSOUTHWEST\x10\x07\x12\x08\n\x04WEST\x10\x08\x12\r\n\tNORTHWEST\x10\t\x12\x08\n\x04LOST\x10\n\x12\t\n\x05\x45RROR\x10\x0b\x12\x10\n\x0c\x44ISCONNECTED\x10\x0c*>\n\x08PierSide\x12\x14\n\x10\x44\x45\x46\x41ULT_PIERSIDE\x10\x00\x12\r\n\tEAST_SIDE\x10\x01\x12\r\n\tWEST_SIDE\x10\x02*u\n\x0eTelescopeSpeed\x12\x16\n\x12SPEED_NOT_TRACKING\x10\x00\x12\x12\n\x0eSPEED_TRACKING\x10\x01\x12\x13\n\x0fSPEED_CENTERING\x10\x02\x12\x11\n\rSPEED_SLEWING\x10\x03\x12\x0f\n\x0bSPEED_ERROR\x10\x04\x32\xc6\x01\n\tTelescope\x12\x32\n\tSetAction\x12\x11.TelescopeRequest\x1a\x12.TelescopeResponse\x12\x41\n\x06\x45qMove\x12#.TelescopeEquatorialMovementRequest\x1a\x12.TelescopeResponse\x12\x42\n\x06\x41\x41Move\x12$.TelescopeAltazimutalMovementRequest\x1a\x12.TelescopeResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'crac_protobuf.telescope_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TELESCOPEACTION']._serialized_start=801
  _globals['_TELESCOPEACTION']._serialized_end=966
  _globals['_TELESCOPESTATUS']._serialized_start=969
  _globals['_TELESCOPESTATUS']._serialized_end=1172
  _globals['_PIERSIDE']._serialized_start=1174
  _globals['_PIERSIDE']._serialized_end=1236
  _globals['_TELESCOPESPEED']._serialized_start=1238
  _globals['_TELESCOPESPEED']._serialized_end=1355
  _globals['_TELESCOPEREQUEST']._serialized_start=61
  _globals['_TELESCOPEREQUEST']._serialized_end=132
  _globals['_TELESCOPEEQUATORIALMOVEMENTREQUEST']._serialized_start=134
  _globals['_TELESCOPEEQUATORIALMOVEMENTREQUEST']._serialized_end=208
  _globals['_TELESCOPEALTAZIMUTALMOVEMENTREQUEST']._serialized_start=210
  _globals['_TELESCOPEALTAZIMUTALMOVEMENTREQUEST']._serialized_end=286
  _globals['_EQUATORIALCOORDS']._serialized_start=288
  _globals['_EQUATORIALCOORDS']._serialized_end=331
  _globals['_ALTAZIMUTALCOORDS']._serialized_start=333
  _globals['_ALTAZIMUTALCOORDS']._serialized_end=377
  _globals['_AIRMASS']._serialized_start=379
  _globals['_AIRMASS']._serialized_end=405
  _globals['_TRANSIT']._serialized_start=407
  _globals['_TRANSIT']._serialized_end=433
  _globals['_TIMETOTRANSIT']._serialized_start=435
  _globals['_TIMETOTRANSIT']._serialized_end=475
  _globals['_TELESCOPERESPONSE']._serialized_start=478
  _globals['_TELESCOPERESPONSE']._serialized_end=798
  _globals['_TELESCOPE']._serialized_start=1358
  _globals['_TELESCOPE']._serialized_end=1556
# @@protoc_insertion_point(module_scope)
