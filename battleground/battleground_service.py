from concurrent import futures

import grpc
from protos.python.battleground_pb2_grpc import (
    BattlegroundServiceServicer, add_BattlegroundServiceServicer_to_server)
from protos.python import character_pb2, battleground_pb2
from characters.helpers import generate_character


class BattlegroundService(BattlegroundServiceServicer):
    """ Battleground Service will handle all the fighting mechanism. """
    def Fighting(self, request, context):
        """ Get a generated character base on the request character type.

        The generated character will have different stats based on the 
        character attributes configuration.
        """
        first_player = request.first_player
        second_player = request.second_player

        return battleground_pb2.BattlegroundResponse(winner=first_player)


def serve():
    """ Starting the service and listen on a specific port for incoming 
    requests. """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_BattlegroundServiceServicer_to_server(BattlegroundService(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
