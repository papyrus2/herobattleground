import grpc

from protos.python.character_pb2 import CharacterRequest
from protos.python import character_pb2_grpc


class CharactersClient(object):

    def __init__(self):
        channel = grpc.insecure_channel('characters_service:50051')
        self.stub = character_pb2_grpc.CharactersServiceStub(channel)

    def get(self, request, meta=None):
        """Get method will be called with a request parameter that 
        can be a CharacterRequest type object or a dictionary containing
        the CharacterRequest informations.
        
        A proto CharacterResponse object will be returned.
        """

        request_obj = request
        if type(request) == dict:
            request_obj = CharacterRequest(**request)

        return self.stub.Get(request_obj)
         