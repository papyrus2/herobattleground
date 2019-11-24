import grpc

from protos.python.battleground_pb2 import BattlegroundRequest
from protos.python import battleground_pb2_grpc


class BattlegroundClient(object):
    def __init__(self):
        channel = grpc.insecure_channel('battleground_service:50052')
        self.stub = battleground_pb2_grpc.BattlegroundServiceStub(channel)

    def fighting(self, request, meta=None):
        """ Fighting method will decide who is the winner between two
        characters receive in the requests. 
        
        A proto BattlegroundResponse object will be returned.
        """

        request_obj = request
        if type(request) == dict:
            request_obj = BattlegroundRequest(**request)

        return self.stub.Fighting(request_obj)
