from enum import Enum


class GameStage(str, Enum):
    OUT_OF_FIGHT = 'OUT_OF_FIGHT'
    FENCING = 'FENCING'
    WAR = 'WAR'
    GRAPPLE = 'GRAPPLE'


class StageStep(str, Enum):
    DRAW = 'DRAW'
    PLANNING = 'PLANNING'
    CLASH = 'CLASH'
    DAMAGE = 'DAMAGE'
    MOVING = 'MOVING'
