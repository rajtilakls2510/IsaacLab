# Setup

We describe how to setup Isaac Sim and Isaac Lab environments to train and infer RL algorithms. A complete documentation to Isaac Lab can be found [here](https://isaac-sim.github.io/IsaacLab/main/index.html).

**Assumes a fresh install of Ubuntu.**

## Download Isaac Sim and Isaac Lab Containers

### Setup Docker

Follow the steps in this [link](https://isaac-sim.github.io/IsaacLab/main/source/deployment/docker.html#docker-and-docker-compose) to:
- Install Docker
- Install Docker Compose
- Follow the post-installation steps for Docker on the post-installation steps page. These steps allow you to run Docker without using sudo.
- Install NVIDIA Container Toolkit.

### Pull Issac Sim Container 

```
docker pull nvcr.io/nvidia/isaac-sim:5.1.0
```

### Pull Isaac Lab Container

```
docker pull nvcr.io/nvidia/isaac-lab:2.3.2
```

### Enable Rendering through X11 forwarding
```
xhost +
docker run --name isaac-lab --entrypoint bash -it --gpus all -e "ACCEPT_EULA=Y" --rm --network=host \
   -e "PRIVACY_CONSENT=Y" \
   -e DISPLAY \
   -v $HOME/.Xauthority:/root/.Xauthority \
   -v ~/docker/isaac-sim/cache/kit:/isaac-sim/kit/cache:rw \
   -v ~/docker/isaac-sim/cache/ov:/root/.cache/ov:rw \
   -v ~/docker/isaac-sim/cache/pip:/root/.cache/pip:rw \
   -v ~/docker/isaac-sim/cache/glcache:/root/.cache/nvidia/GLCache:rw \
   -v ~/docker/isaac-sim/cache/computecache:/root/.nv/ComputeCache:rw \
   -v ~/docker/isaac-sim/logs:/root/.nvidia-omniverse/logs:rw \
   -v ~/docker/isaac-sim/data:/root/.local/share/ov/data:rw \
   -v ~/docker/isaac-sim/documents:/root/Documents:rw \
   nvcr.io/nvidia/isaac-lab:2.3.2
```

**This should setup the Isaac Lab container**

## Download and Build the Forked Isaac Lab Repo

### Download the following repo
Navigate to a directory in your local system
```
mkdir /path/to/some_dir && cd /path/to/some_dir
```

Clone the forked Isaac Lab repo:
```
git clone https://github.com/rajtilakls2510/IsaacLab
```

### Build the Isaac Lab Container
Navigate inside the `IsaacLab/docker` directory: 
```
cd ./IsaacLab/docker
```

Build the container using:
```
./container.py start
```

To enter the container, use:
```
./container.py enter
```

## Next Steps
Following the `QuickStart.md` file to download and run some pre-trained checkpoints.