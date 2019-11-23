# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import protos.python.character_pb2 as character__pb2


class CharactersServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Get = channel.unary_unary(
        '/character.CharactersService/Get',
        request_serializer=character__pb2.CharacterRequest.SerializeToString,
        response_deserializer=character__pb2.CharacterResponse.FromString,
        )


class CharactersServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Get(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CharactersServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=character__pb2.CharacterRequest.FromString,
          response_serializer=character__pb2.CharacterResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'character.CharactersService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
