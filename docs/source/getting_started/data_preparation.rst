.. _data_preparation:

Data Preparation
================

Dataset Format
--------------

VideoTuna supports a unified and concise .csv dataset format as demonstrated in `VideoTuna Toy Dataset <https://github.com/VideoVerses/VideoTuna/blob/main/docs/datasets.md>`_. 

Supported Datasets
------------------

1. Vript Dataset
~~~~~~~~~~~~~~~~

`Vript <https://github.com/mutonix/Vript>`_ (Video Scripting) dataset is a fine-grained, densely-annotated, and high-quality dataset. The dataset can be downloaded from `Vript Dataset <https://huggingface.co/datasets/Mutonix/Vript/tree/main>`_.

Here we demonstrate the whole procedure of preparing a dataset for VideoTuna.

1. Download Vript from HuggingFace:

.. code-block:: bash

    huggingface-cli download \
    --resume-download Mutonix/Vript \
    --local-dir path/to/Vript \
    --local-dir-use-symlinks False

2. Unzip data:

.. code-block:: bash

    cd {PROJECT}

    python tools/unzip_vript.py \
    --output_dir path/to/Vript/vript_short_videos_clips_unzip \
    --zip_folder path/to/Vript/vript_short_videos_clips

3. Generate annotations:

.. code-block:: bash

    python tools/vript_anno_converter.py \
    --input_path path/to/Vript/vript_captions/vript_short_videos_captions.jsonl \
    --output_path data/vript_short_videos_captions.csv \
    --video_root path/to/Vript/vript_short_videos_clips_unzip

By following above steps, you can easily integrate Vript into our framework and train your own text-to-video models.
