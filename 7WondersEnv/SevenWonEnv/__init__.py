from gym.envs.registration import register

register(
    id='SevenWonderEnv-v0',
    entry_point='SevenWonEnv.envs:SevenWonderEnv',
)
