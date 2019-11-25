from concurrent import futures

import grpc
from protos.python.character_pb2_grpc import (CharactersServiceServicer, add_CharactersServiceServicer_to_server)
from protos.python import character_pb2
from characters.helpers import generate_character


class CharacterService(CharactersServiceServicer):
    """ Character Service will handle all the Characters in the battleground. """

    def Get(self, request, context):
        """ Get a generated character base on the request character type.

        The generated character will have different stats based on the 
        character attributes configuration.
        """
        character_type = request.character_type

        return character_pb2.CharacterResponse(character=generate_character(character_type))


def serve():
    """ Starting the service and listen on a specific port for incoming 
    requests. """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_CharactersServiceServicer_to_server(CharacterService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
