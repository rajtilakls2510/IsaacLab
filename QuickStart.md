# QuickStart

This file lists instructions to run inference on some pre-trained checkpoints.
This file assumes all the steps in `SETUP.md` have been completed and Isaac Lab container is built and running. If the container is not running, use the following command to build and run it:
```
cd /path/to/some_dir/IsaacLab/docker && ./container.py start
``` 

## Download checkpoints and Copy Inside Container

Download the trained agents, metrics and charts from the [drive link](https://drive.google.com/file/d/1Tg1DVgExrzedf-CszeBC69pDxoBrZtQJ/view?usp=drive_link).
Then, unzip the contents into the docker container. The path should look like `/workspace/isaaclab/logs/rl_games/...`.

## Run Inference on CartPole

Navigate inside the container
```
./container.py enter
```
You should be in the `/workspace/isaaclab/` directory inside the container.

Run the following command with the path to a PPO agent checkpoint:
```
./isaaclab.sh -p scripts/reinforcement_learning/rl_games/play.py --task Isaac-Cartpole-Down-Direct-v0 --num_envs 32 --checkpoint /workspace/isaaclab/logs/rl_games/cartpole_direct_ppo/2026-02-15_06-15-18/nn/last_cartpole_direct_ppo_ep_1000_rew_182.24527.pth
```

Run the following command with the path to a SAC agent checkpoint:
```
./isaaclab.sh -p scripts/reinforcement_learning/rl_games/play.py --task Isaac-Cartpole-Down-Direct-SAC-v0 --num_envs 32 --checkpoint /workspace/isaaclab/logs/rl_games/cartpole_direct_sac/2026-02-15_06-35-32/nn/last_cartpole_direct_sac_ep_4000_rew_123.230034.pth
```

Run the following command with the path to a TD3 agent checkpoint:
```
./isaaclab.sh -p scripts/reinforcement_learning/rl_games/play.py --task Isaac-Cartpole-Down-Direct-TD3-v0 --num_envs 32 --checkpoint /workspace/isaaclab/logs/rl_games/cartpole_direct_td3/2026-02-15_06-57-49/nn/last_cartpole_direct_td3_ep_4000_rew_56.698353.pth
```

## Run Inference on Double Inverted Pendulum

Navigate inside the container:
```
./container.py enter
```
You should be in the `/workspace/isaaclab/` directory inside the container.

Run the following command with the path to a PPO agent checkpoint:
```
./isaaclab.sh -p scripts/reinforcement_learning/rl_games/play.py --task Isaac-Cart-Double-Pendulum-Down-Direct-v0 --num_envs 32 --checkpoint /workspace/isaaclab/logs/rl_games/cart_double_pendulum_direct_ppo/2026-02-15_07-14-55/nn/last_cart_double_pendulum_direct_ppo_ep_975_rew_198.99982.pth
```

Run the following command with the path to a SAC agent checkpoint:
```
./isaaclab.sh -p scripts/reinforcement_learning/rl_games/play.py --task Isaac-Cart-Double-Pendulum-Down-Direct-SAC-v0 --num_envs 32 --checkpoint /workspace/isaaclab/logs/rl_games/cart_double_pendulum_direct_sac/2026-02-15_07-35-33/nn/last_cart_double_pendulum_direct_sac_ep_5000_rew_-47.462193.pth
```

Run the following command with the path to a TD3 agent checkpoint:
```
./isaaclab.sh -p scripts/reinforcement_learning/rl_games/play.py --task Isaac-Cart-Double-Pendulum-Down-Direct-TD3-v0 --num_envs 32 --checkpoint /workspace/isaaclab/logs/rl_games/cart_double_pendulum_direct_td3/2026-02-15_08-00-43/nn/last_cart_double_pendulum_direct_td3_ep_5000_rew_14.4245.pth
```

**All the above commands bring up the Issac Sim GUI with 32 parallel environments and show the behaviour of the respective agents.**

## Next Steps
Follow `Training.md` for instructions to perform training and metric visualization of agents.