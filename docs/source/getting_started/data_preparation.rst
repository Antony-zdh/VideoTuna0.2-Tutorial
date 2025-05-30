.. _data_preparation:

Data Preparation
================

Dataset Structure
-----------------

Keeping your datasets together in a directory is essential. 

.. code-block:: bash

    cd VideoTuna    
    mkdir Dataset
    cd Dataset

Now you may download your datasets. After downloading, Your structure with datasets should look like

.. code-block:: text

    VideoTuna/
    ├── Dataset/
        ├── DATASET1
        ├── ToyDataset/
            ├── toydataset.csv
            ├── videos/
                ├── video1.mp4
                ├── video2.mp4
                ...

Annotation Format
-----------------

VideoTuna supports a unified and concise .csv dataset format as demonstrated in `VideoTuna Toy Dataset <https://github.com/VideoVerses/VideoTuna/blob/main/docs/datasets.md>`_. 

Your CSV file should contain

**Basic format:**

.. code-block:: text

    path, caption
    path/to/video1, caption1
    path/to/video2, caption2
    ...

**Extended format with additional metadata (for multi-resolution training):**

.. code-block:: text

    path, caption, fps, frames, height, width
    path/to/video1, caption1, 30, 100, 512, 512
    path/to/video2, caption2, 30, 50, 1080, 512
    ...

For example, the toydataset.csv includes the path and the caption of the videos.

.. code-block:: text

    path, caption
    Dataset/ToyDataset/videos/QNa4eMNKYwk_2.mp4,A woman with a patch on her eye next to a park bench.
    Dataset/ToyDataset/videos/J4FJGUugMHM_0.mp4,A group of children and adults are playing with lego toys at an exhibition.
    Dataset/ToyDataset/videos/jPu8eStQrnE_2.mp4,A potted plant is growing in a glass container.
    ...

Ensure that the paths in the CSV file are either absolute or relative to the ``data_root`` of ``DatasetFromCSV`` class during initialization (details of initialization are introduced below).

In addition, to support a new dataset, you need to convert your annotations to the required CSV format.

Important Considerations
~~~~~~~~~~~~~~~~~~~~~~~~

- **Transform Functions:** If no transform functions are provided, default transforms for video and image data will be used. Ensure that your transform functions are compatible with the data format.
- **Resolution and Frame Settings:** The `resolution`, `num_frames`, and `frame_interval` arguments should be set according to your specific requirements. These parameters control the size and number of frames sampled from each video.
- **Training and Validation Split:** If `split_val` is set to `True`, the dataset will be split into training and validation sets. Ensure that the `train` parameter is set correctly to indicate whether the dataset is for training or validation.

Dataset Transformation
----------------------

Below are examples of transforming dataset to our supported format.

1. Toy Dataset
~~~~~~~~~~~~~~

The toy dataset is a model dataset provided by the VideoTuna Team. You may build your own dataset by refering to this toy dataset.

2. Vript Dataset
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

3. UCF101 Dataset
~~~~~~~~~~~~~~~~~

`UCF101 <https://www.crcv.ucf.edu/data/UCF101.php>`_ is an action recognition data set of realistic action videos, collected from YouTube, having 101 action categories. This data set is an extension of UCF50 data set which has 50 action categories. `Click here for direct download <https://www.crcv.ucf.edu/data/UCF101/UCF101.rar>`_

The 101 action categories can be divided into five types: 1)Human-Object Interaction 2) Body-Motion Only 3) Human-Human Interaction 4) Playing Musical Instruments 5) Sports. 

Dataset Usage
-------------

- The ``DatasetFromCSV`` class is designed to load video data according to a CSV file.
- You may find detailed source code in ``videotuna/data/datasets.py``.

Please follow the below instructions to finetune with your dataset.

1. Import necessary modules
