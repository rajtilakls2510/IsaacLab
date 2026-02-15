# Training, Visualization and Inference
We describe the procedure to train RL agents on Cartpole and Double Inverted Pendulum environments. 
We assume that the Isaac Lab container is setup following `SETUP.md` file.

## Train an RL agent
To train an RL agent, first navigate inside the container
```
./container.py enter
```

To start a training run, run the following command:
```
./isaaclab.sh -p scripts/reinforcement_learning/rl_games/train.py --task <TASK_NAME> --headless --num_envs 8192
```

The `TASK_NAME` describes the training environment and agent taht will be used. Possible values:
- CartPole + PPO Agent: `Isaac-Cartpole-Down-Direct-v0`
- CartPole + SAC Agent: `Isaac-Cartpole-Down-Direct-SAC-v0`
- CartPole + TD3 Agent: `Isaac-Cartpole-Down-Direct-TD3-v0`

To resume training from a checkpoint, add an extra `--checkpoint` argument to the command with a path to an existing checkpoint, typically found in `/workspace/isaaclab/logs/rl_games/<AGENT_NAME>/<TIMESTAMP>`:
```
./isaaclab.sh -p scripts/reinforcement_learning/rl_games/train.py --task <TASK_NAME> --headless --num_envs 8192 --checkpoint /path/to/checkpoint.pth
```

## Visualize the Metrics of a Training Run
Training metrics such as losses, rewards and episode lengths for a training run are tracked through `Tensorboard`.
To visualize the metrics, run from `/workspace/isaaclab/`:
```
./isaaclab.sh -p -m tensorboard.main --logdir logs/rl_games/
```
This starts a web server at `http://localhost:6006/`. Open this URL in any browser to visualize the training metrics.

## Infer an RL agent
To see how well the recently trained agent does, navigate inside the container
```
./container.py enter
```

Run:
```
./isaaclab.sh -p scripts/reinforcement_learning/rl_games/play.py --task <TASK_NAME> --num_envs 32 --checkpoint /path/to/checkpoint
```

This will bring up the Isaac Sim GUI with 32 parallel environments with the agent performing inference.