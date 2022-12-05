# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: crac_protobuf/chart.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x63rac_protobuf/chart.proto\"\xa7\x01\n\x05\x43hart\x12\r\n\x05value\x18\x01 \x01(\x02\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0b\n\x03min\x18\x03 \x01(\x02\x12\x0b\n\x03max\x18\x04 \x01(\x02\x12\x0b\n\x03urn\x18\x05 \x01(\t\x12\x1e\n\nthresholds\x18\x06 \x03(\x0b\x32\n.Threshold\x12\x1b\n\x13unit_of_measurement\x18\x07 \x01(\t\x12\x1c\n\x06status\x18\x08 \x01(\x0e\x32\x0c.ChartStatus\"]\n\tThreshold\x12&\n\x0ethreshold_type\x18\x01 \x01(\x0e\x32\x0e.ThresholdType\x12\x13\n\x0bupper_bound\x18\x02 \x01(\x02\x12\x13\n\x0blower_bound\x18\x03 \x01(\x02\"\x10\n\x0eWeatherRequest\"o\n\x0fWeatherResponse\x12\x12\n\nupdated_at\x18\x07 \x01(\x05\x12\x16\n\x06\x63harts\x18\x08 \x03(\x0b\x32\x06.Chart\x12\x1e\n\x06status\x18\t \x01(\x0e\x32\x0e.WeatherStatus\x12\x10\n\x08interval\x18\n \x01(\x05*w\n\x0b\x43hartStatus\x12\x1c\n\x18\x43HART_STATUS_UNSPECIFIED\x10\x00\x12\x17\n\x13\x43HART_STATUS_NORMAL\x10\x01\x12\x18\n\x14\x43HART_STATUS_WARNING\x10\x02\x12\x17\n\x13\x43HART_STATUS_DANGER\x10\x03*\x81\x01\n\rThresholdType\x12\x1e\n\x1aTHRESHOLD_TYPE_UNSPECIFIED\x10\x00\x12\x19\n\x15THRESHOLD_TYPE_NORMAL\x10\x01\x12\x1a\n\x16THRESHOLD_TYPE_WARNING\x10\x02\x12\x19\n\x15THRESHOLD_TYPE_DANGER\x10\x03*\x81\x01\n\rWeatherStatus\x12\x1e\n\x1aWEATHER_STATUS_UNSPECIFIED\x10\x00\x12\x19\n\x15WEATHER_STATUS_NORMAL\x10\x01\x12\x1a\n\x16WEATHER_STATUS_WARNING\x10\x02\x12\x19\n\x15WEATHER_STATUS_DANGER\x10\x03\x32\x39\n\x07Weather\x12.\n\tGetStatus\x12\x0f.WeatherRequest\x1a\x10.WeatherResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'crac_protobuf.chart_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CHARTSTATUS._serialized_start=425
  _CHARTSTATUS._serialized_end=544
  _THRESHOLDTYPE._serialized_start=547
  _THRESHOLDTYPE._serialized_end=676
  _WEATHERSTATUS._serialized_start=679
  _WEATHERSTATUS._serialized_end=808
  _CHART._serialized_start=30
  _CHART._serialized_end=197
  _THRESHOLD._serialized_start=199
  _THRESHOLD._serialized_end=292
  _WEATHERREQUEST._serialized_start=294
  _WEATHERREQUEST._serialized_end=310
  _WEATHERRESPONSE._serialized_start=312
  _WEATHERRESPONSE._serialized_end=423
  _WEATHER._serialized_start=810
  _WEATHER._serialized_end=867
# @@protoc_insertion_point(module_scope)
