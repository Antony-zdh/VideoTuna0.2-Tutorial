.. _inference:

Inference
=========

This section provides detailed instructions for running inference with different models in VideoTuna.

Inputs
------

VideoTuna supports swift inference. Prompts for T2I and T2V are both stored in ``inputs/t2v/prompts.txt``. 
For I2V, prompts and images are stored in ``inputs/i2v/576x1024``. 

We demonstrate an I2V example here.

The structure of the ``inputs/i2v/576x1024`` directory:

.. code-block:: text

    inputs/
    └── i2v/
        └── 576x1024/
            ├── astronaut04.png
            ├── bike_chineseink.png
            ├── bloom01.png
            ├── firework03.png
            ├── girl07.png
            ├── pour_bear.png
            ├── robot01.png
            ├── test_prompts.txt
            └── zreal_penguin.png

In ``test_prompts.txt``, each line is a prompt, ordered with respect to the images in alphabetical order.

.. code-block:: text

    a man in an astronaut suit playing a guitar
    riding a bike under a bridge
    time-lapse of a blooming flower with leaves and a stem
    fireworks display
    a beautiful woman with long hair and a dress blowing in the wind
    pouring beer into a glass of ice and beer
    a robot is walking through a destroyed city
    a group of penguins walking on a beach

Now you may create your own prompts and images!

Inference State-of-the-Art Models
---------------------------------

Text-to-Video (T2V)
-------------------

.. list-table:: T2V Models
   :widths: 10 15 20 10 15 15 15
   :header-rows: 1

   * - Task
     - Model
     - Command
     - Length (#Frames)
     - Resolution
     - Inference Time
     - GPU Memory (GB)
   * - T2V
     - HunyuanVideo
     - ``poetry run inference-hunyuan-t2v``
     - 129
     - 720x1280
     - 32min
     - 60G
   * - T2V
     - WanVideo
     - ``poetry run inference-wanvideo-t2v-720p``
     - 81
     - 720x1280
     - 32min
     - 70G
   * - T2V
     - StepVideo
     - ``poetry run inference-stepvideo-t2v-544x992``
     - 51
     - 544x992
     - 8min
     - 61G
   * - T2V
     - Mochi
     - ``poetry run inference-mochi``
     - 84
     - 480x848
     - 2min
     - 26G
   * - T2V
     - CogVideoX-5b
     - ``poetry run inference-cogvideo-t2v-diffusers``
     - 49
     - 480x720
     - 2min
     - 3G
   * - T2V
     - CogVideoX-2b
     - ``poetry run inference-cogvideo-t2v-diffusers``
     - 49
     - 480x720
     - 2min
     - 3G
   * - T2V
     - Open Sora V1.0
     - ``poetry run inference-opensora-v10-16x256x256``
     - 16
     - 256x256
     - 11s
     - 24G
   * - T2V
     - VideoCrafter-V2-320x512
     - ``poetry run inference-vc2-t2v-320x512``
     - 16
     - 320x512
     - 26s
     - 11G
   * - T2V
     - VideoCrafter-V1-576x1024
     - ``poetry run inference-vc1-t2v-576x1024``
     - 16
     - 576x1024
     - 2min
     - 15G

Image-to-Video (I2V)
--------------------

.. list-table:: I2V Models
   :widths: 10 15 20 10 15 15 15
   :header-rows: 1

   * - Task
     - Model
     - Command
     - Length (#Frames)
     - Resolution
     - Inference Time
     - GPU Memory (GB)
   * - I2V
     - WanVideo
     - ``poetry run inference-wanvideo-i2v-720p``
     - 81
     - 720x1280
     - 28min
     - 77G
   * - I2V
     - HunyuanVideo
     - ``poetry run inference-hunyuan-i2v-720p``
     - 129
     - 720x1280
     - 29min
     - 43G
   * - I2V
     - CogVideoX-5b-I2V
     - ``poetry run inference-cogvideox-15-5b-i2v``
     - 49
     - 480x720
     - 5min
     - 5G
   * - I2V
     - DynamiCrafter
     - ``poetry run inference-dc-i2v-576x1024``
     - 16
     - 576x1024
     - 2min
     - 53G
   * - I2V
     - VideoCrafter-V1
     - ``poetry run inference-vc1-i2v-320x512``
     - 16
     - 320x512
     - 26s
     - 11G

Text-to-Image (T2I)
-------------------

.. list-table:: T2I Models
   :widths: 10 15 20 10 15 15 15
   :header-rows: 1

   * - Task
     - Model
     - Command
     - Length (#Frames)
     - Resolution
     - Inference Time
     - GPU Memory (GB)
   * - T2I
     - Flux-dev
     - ``poetry run inference-flux-dev``
     - 1
     - 768x1360
     - 4s
     - 37G
   * - T2I
     - Flux-dev
     - ``poetry run inference-flux-dev --enable_vae_tiling --enable_sequential_cpu_offload``
     - 1
     - 768x1360
     - 4.2min
     - 2G
   * - T2I
     - Flux-schnell
     - ``poetry run inference-flux-schnell``
     - 1
     - 768x1360
     - 1s
     - 37G
   * - T2I
     - Flux-schnell
     - ``poetry run inference-flux-schnell --enable_vae_tiling --enable_sequential_cpu_offload``
     - 1
     - 768x1360
     - 24s
     - 2G
