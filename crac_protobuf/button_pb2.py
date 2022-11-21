# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: crac_protobuf/button.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x63rac_protobuf/button.proto\"\x10\n\x0e\x42uttonsRequest\"I\n\rButtonRequest\x12\x1d\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\r.ButtonAction\x12\x19\n\x04type\x18\x02 \x01(\x0e\x32\x0b.ButtonType\"3\n\x0f\x42uttonsResponse\x12 \n\x07\x62uttons\x18\x01 \x03(\x0b\x32\x0f.ButtonResponse\"j\n\x0e\x42uttonResponse\x12\x1d\n\x06status\x18\x01 \x01(\x0e\x32\r.ButtonStatus\x12\x19\n\x04type\x18\x02 \x01(\x0e\x32\x0b.ButtonType\x12\x1e\n\nbutton_gui\x18\x03 \x01(\x0b\x32\n.ButtonGui\"\xf1\x01\n\tButtonGui\x12\x10\n\x08metadata\x18\x01 \x01(\x05\x12\x1b\n\x05label\x18\x02 \x01(\x0e\x32\x0c.ButtonLabel\x12\x13\n\x0bis_disabled\x18\x03 \x01(\x08\x12\"\n\x0c\x62utton_color\x18\x04 \x01(\x0b\x32\x0c.ButtonColor\x12\x12\n\nis_visible\x18\x05 \x01(\x08\x12+\n\x15\x64isabled_button_color\x18\x06 \x01(\x0b\x32\x0c.ButtonColor\x12\"\n\x0c\x62utton_image\x18\x07 \x01(\x0b\x32\x0c.ButtonImage\x12\x17\n\x03key\x18\x08 \x01(\x0e\x32\n.ButtonKey\";\n\x0b\x42uttonColor\x12\x12\n\ntext_color\x18\x01 \x01(\t\x12\x18\n\x10\x62\x61\x63kground_color\x18\x02 \x01(\t\"Z\n\x0b\x42uttonImage\x12\x12\n\nimage_data\x18\x01 \x01(\t\x12\x17\n\x0fimage_subsample\x18\x02 \x01(\x05\x12\x1e\n\x04size\x18\x03 \x01(\x0b\x32\x10.ButtonImageSize\"0\n\x0f\x42uttonImageSize\x12\r\n\x05width\x18\x01 \x01(\x05\x12\x0e\n\x06height\x18\x02 \x01(\x05*V\n\x0c\x42uttonAction\x12\x19\n\x15\x42UTTON_DEFAULT_ACTION\x10\x00\x12\x0b\n\x07TURN_ON\x10\x01\x12\x0c\n\x08TURN_OFF\x10\x02\x12\x10\n\x0c\x43HECK_BUTTON\x10\x03*f\n\nButtonType\x12\x17\n\x13\x42UTTON_DEFAULT_TYPE\x10\x00\x12\x0e\n\nCCD_SWITCH\x10\x01\x12\x0f\n\x0bTELE_SWITCH\x10\x02\x12\x0e\n\nFLAT_LIGHT\x10\x03\x12\x0e\n\nDOME_LIGHT\x10\x04*:\n\x0c\x42uttonStatus\x12\x19\n\x15\x42UTTON_DEFAULT_STATUS\x10\x00\x12\x06\n\x02ON\x10\x01\x12\x07\n\x03OFF\x10\x02*\xd6\x03\n\x0b\x42uttonLabel\x12\x11\n\rDEFAULT_LABEL\x10\x00\x12\x0c\n\x08LABEL_ON\x10\x01\x12\r\n\tLABEL_OFF\x10\x02\x12\x10\n\x0cLABEL_ENABLE\x10\x03\x12\x11\n\rLABEL_DISABLE\x10\x04\x12\x0e\n\nLABEL_SYNC\x10\x05\x12\x0e\n\nLABEL_PARK\x10\x06\x12\x0e\n\nLABEL_FLAT\x10\x07\x12\x0e\n\nLABEL_OPEN\x10\x08\x12\x0f\n\x0bLABEL_CLOSE\x10\t\x12\x11\n\rLABEL_OPENING\x10\n\x12\x11\n\rLABEL_CLOSING\x10\x0b\x12\x13\n\x0fLABEL_CALIBRATE\x10\x0c\x12\x1d\n\x19LABEL_TELESCOPE_CONNECTED\x10\r\x12 \n\x1cLABEL_TELESCOPE_DISCONNECTED\x10\x0e\x12\x1d\n\x19LABEL_CAMERA_DISCONNECTED\x10\x0f\x12\x1a\n\x16LABEL_CAMERA_CONNECTED\x10\x10\x12\x17\n\x13LABEL_CAMERA_HIDDEN\x10\x11\x12\x16\n\x12LABEL_CAMERA_SHOWN\x10\x12\x12\x1b\n\x17LABEL_CAMERA_IR_ENABLED\x10\x13\x12\x1c\n\x18LABEL_CAMERA_IR_DISABLED\x10\x14*\x90\x05\n\tButtonKey\x12\x0f\n\x0b\x44\x45\x46\x41ULT_KEY\x10\x00\x12\x0c\n\x08KEY_SYNC\x10\x01\x12\x0c\n\x08KEY_PARK\x10\x02\x12\x0c\n\x08KEY_FLAT\x10\x03\x12\x10\n\x0cKEY_CURTAINS\x10\x04\x12\x11\n\rKEY_CALIBRATE\x10\x05\x12\x0c\n\x08KEY_ROOF\x10\x06\x12\x13\n\x0fKEY_TELE_SWITCH\x10\x07\x12\x12\n\x0eKEY_CCD_SWITCH\x10\x08\x12\x12\n\x0eKEY_FLAT_LIGHT\x10\t\x12\x12\n\x0eKEY_DOME_LIGHT\x10\n\x12#\n\x1fKEY_TELESCOPE_CONNECTION_TOGGLE\x10\x0b\x12\x1a\n\x16KEY_CAMERA1_CONNECTION\x10\x0c\x12\x17\n\x13KEY_CAMERA1_DISPLAY\x10\r\x12\x1a\n\x16KEY_CAMERA2_CONNECTION\x10\x0e\x12\x17\n\x13KEY_CAMERA2_DISPLAY\x10\x0f\x12\x18\n\x14KEY_CAMERA_STOP_MOVE\x10\x10\x12\x16\n\x12KEY_CAMERA_MOVE_UP\x10\x11\x12\x1d\n\x19KEY_CAMERA_MOVE_TOP_RIGHT\x10\x12\x12\x19\n\x15KEY_CAMERA_MOVE_RIGHT\x10\x13\x12 \n\x1cKEY_CAMERA_MOVE_BOTTOM_RIGHT\x10\x14\x12\x18\n\x14KEY_CAMERA_MOVE_DOWN\x10\x15\x12\x1f\n\x1bKEY_CAMERA_MOVE_BOTTOM_LEFT\x10\x16\x12\x18\n\x14KEY_CAMERA_MOVE_LEFT\x10\x17\x12\x1c\n\x18KEY_CAMERA_MOVE_TOP_LEFT\x10\x18\x12\x19\n\x15KEY_CAMERA1_IR_TOGGLE\x10\x19\x12\x19\n\x15KEY_CAMERA2_IR_TOGGLE\x10\x1a\x32\x66\n\x06\x42utton\x12,\n\tSetAction\x12\x0e.ButtonRequest\x1a\x0f.ButtonResponse\x12.\n\tGetStatus\x12\x0f.ButtonsRequest\x1a\x10.ButtonsResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'crac_protobuf.button_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BUTTONACTION._serialized_start=731
  _BUTTONACTION._serialized_end=817
  _BUTTONTYPE._serialized_start=819
  _BUTTONTYPE._serialized_end=921
  _BUTTONSTATUS._serialized_start=923
  _BUTTONSTATUS._serialized_end=981
  _BUTTONLABEL._serialized_start=984
  _BUTTONLABEL._serialized_end=1454
  _BUTTONKEY._serialized_start=1457
  _BUTTONKEY._serialized_end=2113
  _BUTTONSREQUEST._serialized_start=30
  _BUTTONSREQUEST._serialized_end=46
  _BUTTONREQUEST._serialized_start=48
  _BUTTONREQUEST._serialized_end=121
  _BUTTONSRESPONSE._serialized_start=123
  _BUTTONSRESPONSE._serialized_end=174
  _BUTTONRESPONSE._serialized_start=176
  _BUTTONRESPONSE._serialized_end=282
  _BUTTONGUI._serialized_start=285
  _BUTTONGUI._serialized_end=526
  _BUTTONCOLOR._serialized_start=528
  _BUTTONCOLOR._serialized_end=587
  _BUTTONIMAGE._serialized_start=589
  _BUTTONIMAGE._serialized_end=679
  _BUTTONIMAGESIZE._serialized_start=681
  _BUTTONIMAGESIZE._serialized_end=729
  _BUTTON._serialized_start=2115
  _BUTTON._serialized_end=2217
# @@protoc_insertion_point(module_scope)
