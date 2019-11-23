from concurrent import futures

import grpc
from protos.python.character_pb2_grpc import (
    CharactersServiceServicer, add_CharactersServiceServicer_to_server)
from protos.python import character_pb2


class CharacterService(CharactersServiceServicer):
    def Get(self, request, context):
        return character_pb2.CharacterResponse(
            character=character_pb2.Character(
                character_type=character_pb2.HUMAN,
                health=70,
                strength=70,
                defence=45,
                speed=40,
                chance=10,
                skills=[
                    character_pb2.Skills(name="Rapid strike",
                                         chance=10,
                                         skill_type=character_pb2.ATTACK,
                                         power=2),
                    character_pb2.Skills(name="Magic shield",
                                         chance=20,
                                         skill_type=character_pb2.ATTACK,
                                         power=2)
                ]))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_CharactersServiceServicer_to_server(CharacterService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
