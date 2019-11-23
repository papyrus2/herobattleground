from concurrent import futures

import grpc
from protos.python.character_pb2_grpc import (
    CharactersServiceServicer, add_CharactersServiceServicer_to_server)
from protos.python.character_pb2 import CharacterResponse, Character, HUMAN, Skills, ATTACK


class CharacterService(CharactersServiceServicer):
    def Get(self, request, context):
        return CharacterResponse(character=Character(
            character_type=HUMAN,
            health=70,
            strength=70,
            defence=45,
            speed=40,
            chance=10,
            skills=Skills(
                name="Rapid strike", chance=10, skill_type=ATTACK, power=2)))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_CharactersServiceServicer_to_server(CharacterService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
