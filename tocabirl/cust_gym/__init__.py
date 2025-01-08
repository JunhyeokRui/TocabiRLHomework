import gym
from gym.envs.registration import registry, make, spec

def register(id, *args, **kvargs):
    if id in registry.env_specs:
        return 
    else:
        return gym.envs.registration.register(id, *args, **kvargs)

# Registering environment requires a version ID and entry point
# The entry point is really a python module import statement, then the
# colon (:XXX) means import the XXX class name that we want

register(id='tocabi-walk-v0', 
        entry_point = 'tocabirl.cust_gym.tocabi_walk:DYROSTocabiEnv',
        max_episode_steps=8000)