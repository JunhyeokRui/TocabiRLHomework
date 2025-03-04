# TOCABI Reinforcement Learning
This package includes MuJoCo environment for humanoid TOCABI reinforcement learning. TOCABI is a human-sized humanoid developed in Seoul National University [DYROS LAB](http://dyros.snu.ac.kr/). The `main` branch includes an end-to-end torque control RL. 

# **Installation**
## **Prerequisites**
This package requires Python 3.6+ and uses MuJoCo as a simulator (We assume that your graphic driver is installed).
1. Download the MuJoCo version 2.1 binaries for [Linux](https://mujoco.org/download/mujoco210-linux-x86_64.tar.gz).
2. Extract the downloaded file into ~/.mujoco/mujoco210.
```
    mkdir ~/.mujoco/
    tar -xzvf ~/Downloads/mujoco210-linux-x86_64.tar.gz -C ~/.mujoco/
    sudo apt install libosmesa6-dev libgl1-mesa-glx libglfw3
```

You may need to add environment variables such as to your '~/.bashrc' file:

    export LD_LIBRARY_PATH=/home/$user_name$/.mujoco/mujoco210/bin
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/nvidia
    export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libGLEW.so:/usr/lib/x86_64-linux-gnu/libGL.so

## **Install using pip**

It is recommended to create a new [Anaconda](https://www.anaconda.com/download) environment and use it. Refer to [this website](https://jongsky.tistory.com/21) to install Anaconda and create a python environment with Anaconda (make sure to use Python 3.6+ when you create an Anaconda environment). 

    conda create -n tocabirl python=3.6
    conda activate tocabirl

When the python environment is activated, go to the project directory and run
`pip install .` (Notice period).

This should install the `tocabirl` package in site-packages of your python environment. 

# **How to run**
    python run_new.py

You can change the task or the robot to be trained by changing parameters of `class args:` in `run_new.py`.

**Training**:  
For example, you should set `run_type = train`  to train the robot. If you set `n_cpu = 1` and `render = True` when the `run_type = train`, you can visualize the training procedure (but the training will take very long). 

**Testing** :  
When the training is finished, you can visualize the trained policy by setting `run_type = enjoy` and `play_model = "$name_of_the_trained_model$"`. You can see the trained model in the `trained model/$task_name$/` directory (such as 'ppo2_DYROSTocabi_2023-11-23 15:37:06.338899' of the given file).

## **Possible Errors**

1) <span style="color:red">FileNotFoundError: [Errno 2] No such file or directory: 'patchelf': 'patchelf'</span> &rarr; sudo apt-get install patchelf

2) <span style="color:red">/mujoco-py/mujoco_py/cymj.pyx:127:21: Cannot assign type 'void (const char *) except * nogil' to 'void (*)(const char *) noexcept nogil'</span> &rarr; pip install "cython<3"

3) <span style="color:red"> for ubuntu 24.04

    **Package Install**
    
    `sudo apt install libosmesa6-dev libgl1-mesa-glx libglfw3`

    may cause problem. Do

    `sudo apt install libosmesa6-dev libglfw3 libegl1-mesa-dev libgl1 libglx-mesa0 libglew-dev`
    
    **error with GLEW**

    `export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libGLEW.so:/usr/lib/x86_64-linux-gnu/libGL.so` 
    
    may cause problem. Do

    `export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libGLEW.so.2.2:/usr/lib/x86_64-linux-gnu/libGL.so`

## Brief Directory Description
`data`: Mean and variance of states

`motions`: Reference motion files used during training

`result`: Weight and bias of the trained model.

`tocabirl`: Training-related codes and models. For example, you should modify `tocabirl/cust_gym/tocabi_walk.py` and `tocabirl/cust_gym/tocabi_walk_env.py` file to set a environment for the walking task.

`trained model`: Trained models. After training is completed, a file such as `'ppo2_DYROSTocabi_2023-11-13 16:28:29.323250'` is saved to this directory.


