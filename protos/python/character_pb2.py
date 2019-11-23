# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: character.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='character.proto',
  package='character',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0f\x63haracter.proto\x12\tcharacter\"D\n\x10\x43haracterRequest\x12\x30\n\x0e\x63haracter_type\x18\x01 \x01(\x0e\x32\x18.character.CharacterType\"<\n\x11\x43haracterResponse\x12\'\n\tcharacter\x18\x01 \x01(\x0b\x32\x14.character.Character\"\xb2\x01\n\tCharacter\x12\x30\n\x0e\x63haracter_type\x18\x01 \x01(\x0e\x32\x18.character.CharacterType\x12\x0e\n\x06health\x18\x02 \x01(\x05\x12\x10\n\x08strength\x18\x03 \x01(\x05\x12\x0f\n\x07\x64\x65\x66\x65nce\x18\x04 \x01(\x05\x12\r\n\x05speed\x18\x05 \x01(\x05\x12\x0e\n\x06\x63hance\x18\x06 \x01(\x05\x12!\n\x06skills\x18\x07 \x01(\x0b\x32\x11.character.Skills\"_\n\x06Skills\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x63hance\x18\x02 \x01(\x05\x12(\n\nskill_type\x18\x03 \x01(\x0e\x32\x14.character.SkillType\x12\r\n\x05power\x18\x04 \x01(\x02*<\n\rCharacterType\x12\x15\n\x11UNKNOWN_CHARACTER\x10\x00\x12\t\n\x05HUMAN\x10\x01\x12\t\n\x05\x42\x45\x41ST\x10\x02*7\n\tSkillType\x12\x11\n\rUNKNOWN_SKILL\x10\x00\x12\x0b\n\x07\x44\x45\x46\x45NCE\x10\x01\x12\n\n\x06\x41TTACK\x10\x02\x32U\n\x11\x43haractersService\x12@\n\x03Get\x12\x1b.character.CharacterRequest\x1a\x1c.character.CharacterResponseb\x06proto3')
)

_CHARACTERTYPE = _descriptor.EnumDescriptor(
  name='CharacterType',
  full_name='character.CharacterType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_CHARACTER', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HUMAN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BEAST', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=440,
  serialized_end=500,
)
_sym_db.RegisterEnumDescriptor(_CHARACTERTYPE)

CharacterType = enum_type_wrapper.EnumTypeWrapper(_CHARACTERTYPE)
_SKILLTYPE = _descriptor.EnumDescriptor(
  name='SkillType',
  full_name='character.SkillType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_SKILL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEFENCE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ATTACK', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=502,
  serialized_end=557,
)
_sym_db.RegisterEnumDescriptor(_SKILLTYPE)

SkillType = enum_type_wrapper.EnumTypeWrapper(_SKILLTYPE)
UNKNOWN_CHARACTER = 0
HUMAN = 1
BEAST = 2
UNKNOWN_SKILL = 0
DEFENCE = 1
ATTACK = 2



_CHARACTERREQUEST = _descriptor.Descriptor(
  name='CharacterRequest',
  full_name='character.CharacterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='character_type', full_name='character.CharacterRequest.character_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_end=98,
)


_CHARACTERRESPONSE = _descriptor.Descriptor(
  name='CharacterResponse',
  full_name='character.CharacterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='character', full_name='character.CharacterResponse.character', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=100,
  serialized_end=160,
)


_CHARACTER = _descriptor.Descriptor(
  name='Character',
  full_name='character.Character',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='character_type', full_name='character.Character.character_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='health', full_name='character.Character.health', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strength', full_name='character.Character.strength', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='defence', full_name='character.Character.defence', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='speed', full_name='character.Character.speed', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chance', full_name='character.Character.chance', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='skills', full_name='character.Character.skills', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_end=341,
)


_SKILLS = _descriptor.Descriptor(
  name='Skills',
  full_name='character.Skills',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='character.Skills.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chance', full_name='character.Skills.chance', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='skill_type', full_name='character.Skills.skill_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='power', full_name='character.Skills.power', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=343,
  serialized_end=438,
)

_CHARACTERREQUEST.fields_by_name['character_type'].enum_type = _CHARACTERTYPE
_CHARACTERRESPONSE.fields_by_name['character'].message_type = _CHARACTER
_CHARACTER.fields_by_name['character_type'].enum_type = _CHARACTERTYPE
_CHARACTER.fields_by_name['skills'].message_type = _SKILLS
_SKILLS.fields_by_name['skill_type'].enum_type = _SKILLTYPE
DESCRIPTOR.message_types_by_name['CharacterRequest'] = _CHARACTERREQUEST
DESCRIPTOR.message_types_by_name['CharacterResponse'] = _CHARACTERRESPONSE
DESCRIPTOR.message_types_by_name['Character'] = _CHARACTER
DESCRIPTOR.message_types_by_name['Skills'] = _SKILLS
DESCRIPTOR.enum_types_by_name['CharacterType'] = _CHARACTERTYPE
DESCRIPTOR.enum_types_by_name['SkillType'] = _SKILLTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CharacterRequest = _reflection.GeneratedProtocolMessageType('CharacterRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHARACTERREQUEST,
  '__module__' : 'character_pb2'
  # @@protoc_insertion_point(class_scope:character.CharacterRequest)
  })
_sym_db.RegisterMessage(CharacterRequest)

CharacterResponse = _reflection.GeneratedProtocolMessageType('CharacterResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHARACTERRESPONSE,
  '__module__' : 'character_pb2'
  # @@protoc_insertion_point(class_scope:character.CharacterResponse)
  })
_sym_db.RegisterMessage(CharacterResponse)

Character = _reflection.GeneratedProtocolMessageType('Character', (_message.Message,), {
  'DESCRIPTOR' : _CHARACTER,
  '__module__' : 'character_pb2'
  # @@protoc_insertion_point(class_scope:character.Character)
  })
_sym_db.RegisterMessage(Character)

Skills = _reflection.GeneratedProtocolMessageType('Skills', (_message.Message,), {
  'DESCRIPTOR' : _SKILLS,
  '__module__' : 'character_pb2'
  # @@protoc_insertion_point(class_scope:character.Skills)
  })
_sym_db.RegisterMessage(Skills)



_CHARACTERSSERVICE = _descriptor.ServiceDescriptor(
  name='CharactersService',
  full_name='character.CharactersService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=559,
  serialized_end=644,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='character.CharactersService.Get',
    index=0,
    containing_service=None,
    input_type=_CHARACTERREQUEST,
    output_type=_CHARACTERRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CHARACTERSSERVICE)

DESCRIPTOR.services_by_name['CharactersService'] = _CHARACTERSSERVICE

# @@protoc_insertion_point(module_scope)
