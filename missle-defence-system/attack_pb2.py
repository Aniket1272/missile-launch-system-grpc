# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: attack.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x61ttack.proto\x12\x06\x61ttack\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1c\n\x0cReadyRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nReadyReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x0e\n\x01N\x12\t\n\x01N\x18\x01 \x01(\x05\"$\n\x10SoldiersPosition\x12\x10\n\x08soldiers\x18\x01 \x01(\x05\x32\xf1\x01\n\x07Greeter\x12\x36\n\x08SayHello\x12\x14.attack.HelloRequest\x1a\x12.attack.HelloReply\"\x00\x12\x43\n\x13SayHelloStreamReply\x12\x14.attack.HelloRequest\x1a\x12.attack.HelloReply\"\x00\x30\x01\x12\x36\n\x08SayReady\x12\x14.attack.ReadyRequest\x1a\x12.attack.ReadyReply\"\x00\x12\x31\n\x08Position\x12\t.attack.N\x1a\x18.attack.SoldiersPosition\"\x00\x42.\n\x17io.grpc.examples.attackB\x0b\x41ttackProtoP\x01\xa2\x02\x03\x41TTb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'attack_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027io.grpc.examples.attackB\013AttackProtoP\001\242\002\003ATT'
  _globals['_HELLOREQUEST']._serialized_start=24
  _globals['_HELLOREQUEST']._serialized_end=52
  _globals['_HELLOREPLY']._serialized_start=54
  _globals['_HELLOREPLY']._serialized_end=83
  _globals['_READYREQUEST']._serialized_start=85
  _globals['_READYREQUEST']._serialized_end=113
  _globals['_READYREPLY']._serialized_start=115
  _globals['_READYREPLY']._serialized_end=144
  _globals['_N']._serialized_start=146
  _globals['_N']._serialized_end=160
  _globals['_SOLDIERSPOSITION']._serialized_start=162
  _globals['_SOLDIERSPOSITION']._serialized_end=198
  _globals['_GREETER']._serialized_start=201
  _globals['_GREETER']._serialized_end=442
# @@protoc_insertion_point(module_scope)