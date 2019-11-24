from concurrent import futures
import random

import grpc
from protos.python.battleground_pb2_grpc import (
    BattlegroundServiceServicer, add_BattlegroundServiceServicer_to_server)
from protos.python import character_pb2, battleground_pb2
from characters.helpers import generate_character


class BattlegroundService(BattlegroundServiceServicer):
    """ Battleground Service will handle all the fighting mechanism. """
    def decide_playing_order(self, first_player, second_player):
        """ Decide the what player will be first to attack. 
        The player order will be decided based on the speed and chance
        """
        if first_player.speed > second_player.speed:
            return first_player, second_player
        elif first_player.speed == second_player.speed:
            if first_player.chance > second_player.chance:
                return first_player, second_player
        return second_player, first_player

    def compute_damage(self, attacker, defencer):
        """ Compute the damage done by the attacker. """
        damage = attacker.strength - defencer.defence
        return damage

    def roll_chance(self, chance):
        """ See if the player lucky strike. """
        roll = random.randint(0, 100)
        return roll <= chance

    def round(self, attacker, defencer):
        """ Play a round in the battleground, attack and defence try their lucks 
        and skills. """
        damage = self.compute_damage(attacker, defencer)

        defence_chance = self.roll_chance(defencer.chance)

        if defence_chance:
            # no damage done
            return

        for skill in defencer.skills:
            if skill.skill_type == character_pb2.DEFENCE:
                skill_chance = self.roll_chance(skill.chance)
                if skill_chance:
                    damage = int(damage / 2)

        defencer.health -= damage

        # TODO: here is a bug the Attack Skill could be executed multiple times
        for skill in attacker.skills:
            if skill.skill_type == character_pb2.ATTACK:
                skill_chance = self.roll_chance(skill_chance)
                if skill_chance:
                    self.round(attacker, defencer)

        # chance to defance

    def Fighting(self, request, context):
        """ The battleground winner will be decided in a legendery fight.

        The defense and attack will be computed here and the battle will 
        be done over a duration of 20 rounds or until one of the players is dead.
        """
        first_player = request.first_player
        second_player = request.second_player

        first_player, second_player = self.decide_playing_order(
            first_player, second_player)

        self.round(first_player, second_player)

        return battleground_pb2.BattlegroundResponse(winner=second_player)


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
