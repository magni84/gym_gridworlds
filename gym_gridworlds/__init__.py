from gymnasium.envs.registration import register

register(
    id='GridWorld-v0',
    entry_point='gym_gridworlds.envs:GridWorldEnv',
)
