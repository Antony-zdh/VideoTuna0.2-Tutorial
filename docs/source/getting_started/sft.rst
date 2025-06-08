.. _sft:

Supervised Fine-tuning (SFT)
=============================

This section provides detailed instructions for fine-tuning different models in VideoTuna.

Text-to-Video (T2V)
-------------------

.. list-table:: T2V Fine-tuning Models
   :widths: 10 15 15 25 20 10
   :header-rows: 1

   * - Task
     - Model
     - Mode
     - Command
     - More Details
     - #GPUs
   * - T2V
     - Wan Video
     - Lora Fine-tune
     - ``poetry run train-wan2-1-t2v-lora``
     - :ref:`wan-video`
     - 1
   * - T2V
     - Wan Video
     - Full Fine-tune
     - ``poetry run train-wan2-1-t2v-fullft``
     - :ref:`wan-video`
     - 1
   * - T2V
     - Hunyuan Video
     - Lora Fine-tune
     - ``poetry run train-hunyuan-t2v-lora``
     - :ref:`hunyuan-video`
     - 2
   * - T2V
     - CogvideoX
     - Lora Fine-tune
     - ``poetry run train-cogvideox-t2v-lora``
     - :ref:`cogvideox`
     - 1
   * - T2V
     - CogvideoX
     - Full Fine-tune
     - ``poetry run train-cogvideox-t2v-fullft``
     - :ref:`cogvideox`
     - 4
   * - T2V
     - Open-Sora v1.0
     - Full Fine-tune
     - ``poetry run train-opensorav10``
     - 
     - 1
   * - T2V
     - VideoCrafter
     - Lora Fine-tune
     - ``poetry run train-videocrafter-lora``
     - :ref:`videocrafter`
     - 1
   * - T2V
     - VideoCrafter
     - Full Fine-tune
     - ``poetry run train-videocrafter-v2``
     - :ref:`videocrafter`
     - 1

Image-to-Video (I2V)
--------------------

.. list-table:: I2V Fine-tuning Models
   :widths: 10 15 15 25 20 10
   :header-rows: 1

   * - Task
     - Model
     - Mode
     - Command
     - More Details
     - #GPUs
   * - I2V
     - Wan Video
     - Lora Fine-tune
     - ``poetry run train-wan2-1-i2v-lora``
     - :ref:`wan-video`
     - 1
   * - I2V
     - Wan Video
     - Full Fine-tune
     - ``poetry run train-wan2-1-i2v-fullft``
     - :ref:`wan-video`
     - 1
   * - I2V
     - CogvideoX
     - Lora Fine-tune
     - ``poetry run train-cogvideox-i2v-lora``
     - :ref:`cogvideox-i2v`
     - 1
   * - I2V
     - CogvideoX
     - Full Fine-tune
     - ``poetry run train-cogvideox-i2v-fullft``
     - :ref:`cogvideox-i2v`
     - 4

Text-to-Image (T2I)
-------------------

.. list-table:: T2I Fine-tuning Models
   :widths: 10 15 15 25 20 10
   :header-rows: 1

   * - Task
     - Model
     - Mode
     - Command
     - More Details
     - #GPUs
   * - T2I
     - Flux
     - Lora Fine-tune
     - ``poetry run train-flux-lora``
     - :ref:`flux`
     - 1

Detailed Instructions
---------------------

.. _wan-video:

Wan Video
~~~~~~~~~

Wan Video supports both LoRA fine-tuning and full fine-tuning for text-to-video and image-to-video generation.

Prerequisites
^^^^^^^^^^^^^

- 1 NVIDIA GPU with 24GB memory
- CUDA 11.7 or later
- PyTorch 2.0 or later
- Install deepspeed for training:
  
  .. code-block:: bash

     poetry run install-deepspeed

Training Steps
^^^^^^^^^^^^^^

1. Prepare your dataset:
   - Download example data from `https://huggingface.co/datasets/Yingqing/VideoTuna-Datasets/resolve/main/apply_lipstick.zip`
   - Place data at `data/apply_lipstick/metadata.csv`

2. Download checkpoints:
   - T2V: `checkpoints/wan/Wan2.1-T2V-14B`
   - I2V: `checkpoints/wan/Wan2.1-I2V-14B-480P`

3. Choose training mode:

   a. LoRA Fine-tuning (T2V):
   
   .. code-block:: bash

      poetry run train-wan2-1-t2v-lora

   b. Full Fine-tuning (T2V):
   
   .. code-block:: bash

      poetry run train-wan2-1-t2v-fullft

   c. LoRA Fine-tuning (I2V):
   
   .. code-block:: bash

      poetry run train-wan2-1-i2v-lora

   d. Full Fine-tuning (I2V):
   
   .. code-block:: bash

      poetry run train-wan2-1-i2v-fullft

4. Training results will be saved at:
   - LoRA: `results/train/train_wanvideo_*_lora_${CURRENT_TIME}_${EXPNAME}`
   - Full: `results/train/train_wanvideo_*_fullft_${CURRENT_TIME}_${EXPNAME}`

5. For inference, use the corresponding inference scripts:
   - T2V LoRA: `shscripts/inference_wanvideo_t2v_lora.sh`
   - T2V Full: `shscripts/inference_wanvideo_t2v_fullft.sh`
   - I2V LoRA: `shscripts/inference_wanvideo_i2v_lora.sh`
   - I2V Full: `shscripts/inference_wanvideo_i2v_fullft.sh`

.. _hunyuan-video:

Hunyuan Video
~~~~~~~~~~~~~

Hunyuan Video supports LoRA fine-tuning for text-to-video generation. The model requires 2 GPUs for training.

Prerequisites
^^^^^^^^^^^^^

- 2 NVIDIA GPUs with at least 24GB memory each
- CUDA 11.7 or later
- PyTorch 2.0 or later
- Install deepspeed for training:
  
  .. code-block:: bash

     poetry run install-deepspeed

Training Steps
^^^^^^^^^^^^^^

1. Download the checkpoints for HunyuanVideo (see CHECKPOINTS.md)

2. Run the training command:
   
   .. code-block:: bash

      poetry run train-hunyuan-t2v-lora

3. After training, convert the deepspeed checkpoint:
   
   .. code-block:: bash

      tools/deepspeed_checkpoint_converter.py

4. For inference:
   
   .. code-block:: bash

      shscripts/inference_hunyuanvideo_t2v_lora.sh

Note: Training and inference use the default model config from `configs/007_hunyuanvideo/hunyuanvideo_diffuser.yaml`

.. _cogvideox:

CogVideoX
~~~~~~~~~

CogVideoX supports both LoRA fine-tuning and full fine-tuning for text-to-video generation.

Prerequisites
^^^^^^^^^^^^^

- For LoRA: 1 NVIDIA GPU with 24GB memory
- For Full Fine-tune: 4 NVIDIA GPUs with 24GB memory each
- CUDA 11.7 or later
- PyTorch 2.0 or later

Training Steps
^^^^^^^^^^^^^^

1. Prepare your dataset:
   - Download example data from `https://huggingface.co/datasets/Yingqing/VideoTuna-Datasets/resolve/main/apply_lipstick.zip`
   - Place data at `data/apply_lipstick/metadata.csv`

2. Download the CogvideoX checkpoints (see CHECKPOINTS.md)

3. Choose training mode:

   a. LoRA Fine-tuning (T2V):
   
   .. code-block:: bash

      poetry run train-cogvideox-t2v-lora

   b. Full Fine-tuning (T2V):
   
   .. code-block:: bash

      poetry run train-cogvideox-t2v-fullft

4. For inference:
   - T2V LoRA: `shscripts/inference_cogvideo_t2v_lora.sh`
   - T2V Full: `shscripts/inference_cogvideo_t2v_fullft.sh`

Note: Training and inference use the default model config from `configs/004_cogvideox/cogvideo5b.yaml`

.. _cogvideox-i2v:

CogVideoX I2V
~~~~~~~~~~~~~~

CogVideoX supports both LoRA fine-tuning and full fine-tuning for image-to-video generation.

Prerequisites
^^^^^^^^^^^^^

- For LoRA: 1 NVIDIA GPU with 24GB memory
- For Full Fine-tune: 4 NVIDIA GPUs with 24GB memory each
- CUDA 11.7 or later
- PyTorch 2.0 or later

Training Steps
^^^^^^^^^^^^^^

1. Prepare your dataset:
   - Download example data from `https://huggingface.co/datasets/Yingqing/VideoTuna-Datasets/resolve/main/apply_lipstick.zip`
   - Place data at `data/apply_lipstick/metadata.csv`

2. Download the CogvideoX checkpoints (see CHECKPOINTS.md)

3. Choose training mode:

   a. LoRA Fine-tuning (I2V):
   
   .. code-block:: bash

      poetry run train-cogvideox-i2v-lora

   b. Full Fine-tuning (I2V):
   
   .. code-block:: bash

      poetry run train-cogvideox-i2v-fullft

4. For inference:
   - I2V LoRA: `shscripts/inference_cogvideo_i2v_lora.sh`
   - I2V Full: `shscripts/inference_cogvideo_i2v_fullft.sh`

Note: Training and inference use the default model config from `configs/004_cogvideox/cogvideo5b-i2v.yaml`

.. _videocrafter:

VideoCrafter
~~~~~~~~~~~~

VideoCrafter supports both LoRA fine-tuning and full fine-tuning.

Prerequisites
^^^^^^^^^^^^^

- For LoRA: 1 NVIDIA GPU with 24GB memory
- For Full Fine-tune: 1 NVIDIA GPU with 24GB memory
- CUDA 11.7 or later
- PyTorch 2.0 or later

Training Steps
^^^^^^^^^^^^^^

1. Prepare your dataset:

   - Organize data in `Dataset/ToyDataset/` with structure:
     - `toydataset.csv`
     - `videos/` directory containing video files

2. Download and convert checkpoints:

   - Download from CHECKPOINTS.md
   - Convert checkpoint:

     .. code-block:: bash

        python tools/convert_checkpoint.py \
        --input_path checkpoints/videocrafter/t2v_v2_512/model.ckpt

3. Choose training mode:

   a. LoRA Fine-tuning:
   
   .. code-block:: bash

      poetry run train-videocrafter-lora

   b. Full Fine-tuning:
   
   .. code-block:: bash

      poetry run train-videocrafter-v2

4. Training results will be saved at `results/train/${CURRENT_TIME}_${EXPNAME}`

5. For inference:

   - LoRA: `shscripts/inference_vc2_t2v_320x512_lora.sh`
   - Full: `shscripts/inference_vc2_t2v_320x512.sh`

Note: Training and inference use the default model config from `configs/001_videocrafter2/vc2_t2v_lora.yaml`

.. _flux:

Flux
~~~~

Flux supports LoRA fine-tuning for text-to-image generation.

Prerequisites
^^^^^^^^^^^^^

- 1 NVIDIA GPU with 24GB memory
- CUDA 11.7 or later
- PyTorch 2.0 or later
- Hugging Face account with access to Flux.1-dev model

Training Steps
^^^^^^^^^^^^^^

1. Log in to Hugging Face:
   
   .. code-block:: bash

      huggingface-cli login

2. Set experiment configurations in:
   - `configs/006_flux/config.json`
   - `configs/006_flux/multidatabackend.json`

3. Run training:
   
   .. code-block:: bash

      poetry run train-flux-lora

4. For inference:
   
   .. code-block:: bash

      poetry run inference-flux-lora \
      --prompt "your prompt" \
      --lora_path ${lora_path} \
      --out_path ${out_path}

   Or for multiple prompts:
   
   .. code-block:: bash

      poetry run inference-flux-lora \
      --prompt data/prompts/your_prompts.txt \
      --lora_path ${lora_path} \
      --out_path ${out_path}

Note: For custom datasets, organize images and prompts in the same directory structure as `inputs/t2i/flux/plushie_teddybear`
