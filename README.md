# Gymnasium Grid Worlds
Some minimalistic GridWrold environments for Gymnasium, implementing Example 3.5 and Example 4.1 in "Reinforcement Learning - An introduction" by Sutton and Barto. 

Code based on the [FrozenLake](https://github.com/Farama-Foundation/Gymnasium/blob/main/gymnasium/envs/toy_text/frozen_lake.py) environment.

## Installation instructions

Requirements: gymnasium and numpy

```
git clone https://github.com/magni84/gym_gridworlds.git
cd gym-gridworlds
pip install -e .
```

## Usage 
```
import gymnasium as gym
import gym_bandits

env = gym.make('GridWorld-v0') # Example 4.1
env = gym.make('GridWorld-AB-v0') # Example 3.5
```
