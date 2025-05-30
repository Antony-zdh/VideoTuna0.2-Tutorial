.. _installation:

Installation
============

CUDA Installation
-----------------

Compute Unified Device Architecture (CUDA) is a parallel computing platform and programming model developed by NVIDIA that enables general-purpose computing on their GPUs. In scenarios where parallelization is possible to enhance computation efficiency, CUDA is being used intensively by both research and the industry.

Pre-installation check
~~~~~~~~~~~~~~~~~~~~~~
- **Sufficient Disk Space**: Make sure your computer has at least 6 GB free disk space.  
- **CUDA Compatibility of your GPU**:

  - Visit `CUDA GPU List <https://developer.nvidia.com/cuda-gpus>`_ to check compatibility.  
  - Run ``lspci | grep -i nvidia`` (Linux) to identify your GPU (run ``sudo apt install pciutils`` if 'lspci' not found).
  - For Windows, press ``Ctrl + Shift + Esc`` to open Task Manager, you can find your GPU in Performance > GPU 0.
  - For Windows, you may also execute ``Get-WmiObject Win32_VideoController | Select-Object Name, Description`` in PowerShell.

- **Admin Privileges**: You need `sudo` (Linux) or Administrator access (Windows) to install CUDA. 

Linux
~~~~~

1. Ensure CUDA support

.. code-block:: bash

    uname -m && cat /etc/*release

``uname -m`` returns architecture information, e.g. ``x86_64``. Note that CUDA supports only 64-bit machines. ``cat /etc/*release`` checks Linux distribution. Example output:

.. code-block:: bash

    DISTRIB_ID=Ubuntu
    DISTRIB_RELEASE=22.04

CUDA also supports ``DISTRIB_ID`` of RHEL/CentOS, Debian, SLES. Check `https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#system-requirements <https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#system-requirements>`_ for details.

2. Ensure GNU Compiler Collection (GCC) installed

.. code-block:: bash

    gcc --version

Example output:

.. code-block:: bash

    gcc (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0

If GCC is not installed, you may install it with

.. code-block:: bash

    sudo apt install gcc

3. Ensure Nvidia Drivers installed

Check your installation with ``nvidia-smi``. If not installed, you may install it with

.. code-block:: bash

    # For Ubuntu/Debian
    sudo apt update
    sudo apt install nvidia-driver-535  # Recommended driver for CUDA
    sudo reboot

4. Install CUDA Toolkit

Find your target CUDA Toolkit from `CUDA Toolkit Archive <https://developer.nvidia.com/cuda-toolkit-archive>`_. Here we demonstrate with `CUDA 12.9 <https://developer.nvidia.com/cuda-12-9-0-download-archive/>`_. 

    .. image:: ../assets/CUDA12.9-demo-version-panel.png

In case you installed some other version before and would like to uninstall, you may execute ``sudo /usr/local/cuda-11.8/bin/cuda-uninstaller`` (change the version manually). Alternatively, you may:

.. code-block:: bash

    sudo rm -r /usr/local/cuda-11.8/
    sudo apt clean && sudo apt autoclean

Following the instruction from Nvidia download archive, we proceed to install from web:

.. code-block:: bash

    wget https://developer.download.nvidia.com/compute/cuda/12.9.0/local_installers/cuda_12.9.0_575.51.03_linux.run
    sudo sh cuda_12.9.0_575.51.03_linux.run

After installation, you may double check with ``nvcc -V``. 

Windows
~~~~~~~

1. Ensure system version supported
Find your system version from Settings > System > About. Make sure your system version is in the list below:

.. list-table::
   :widths: 50
   :header-rows: 1

   * - Versions supported
   * - Microsoft Windows 11 21H2
   * - Microsoft Windows 11 22H2-SV2
   * - Microsoft Windows 11 23H2
   * - Microsoft Windows 10 21H2
   * - Microsoft Windows 10 22H2
   * - Microsoft Windows Server 2022

2. Install CUDA Toolkit

Find your target CUDA Toolkit from `CUDA Toolkit Archive <https://developer.nvidia.com/cuda-toolkit-archive>`_. Here we demonstrate with `CUDA 12.9 <https://developer.nvidia.com/cuda-12-9-0-download-archive/>`_.

  .. image:: ../assets/CUDA12.9-demo-version-panel-windows.png

Following the instruction from Nvidia download archive, we proceed to install:

  .. image:: ../assets/install_instr_windows.png

Steps to install: 

- Accept the End User License Agreement 
- Choose the CUDA option (Simply installs CUDA would be enough for most cases) 

The above installation process takes about 3 minutes.

After installation, you may double check with ``nvcc -V``. If nvcc still not found, you should check Setting > System > About > Advanced system settings > Environment Variables, and ensure your cuda path is included in the PATH list (e.g. ``C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.9\bin``). 

VideoTuna Repository Clone
--------------------------
Clone videotuna repo from `VideoTuna GitHub <https://github.com/VideoVerses/VideoTuna>`_. In the GitHub interface, click ``<> Code`` to clone through HTTPS, SSH, or GitHub CLI. 

e.g. git clone through HTTPS:

.. code-block:: bash

    git clone https://github.com/VideoVerses/VideoTuna.git
    cd VideoTuna

If failed to clone, you may try some other methods (HTTPS, SSH, GitHub CLI).

VideoTuna Environment Preparation
---------------------------------
(1) If you use Linux and Conda (Recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We create a new environment named "videotuna" (you name it) with python version 3.10, activate it, and use ``pip`` (Python's package installer) to install poetry. Poetry is a dependency management and packaging tool for Python projects. After installing poetry, we use poetry to initialize and install project dependencies by finding ``pyproject.toml`` file under the current directory.

.. code-block:: bash

    conda create -n videotuna python=3.10 -y
    conda activate videotuna
    pip install poetry
    poetry install

(The above process takes around 3 minutes)

Optional: Flash-attn installation

Hunyuan model uses it to reduce memory usage and speed up inference. If it is not installed, the model will run in normal mode. Install the flash-attn via:

.. code-block:: bash

    poetry run install-flash-attn 

(The above process takes around 1 minute)

Optional: Video-to-video enhancement

.. code-block:: bash

    poetry run pip install "modelscope[cv]" -f https://modelscope.oss-cn-beijing.aliyuncs.com/releases/repo.html

(If this command above get stucked, kill and re-run it will solve the issue)

(2) If you use Linux and Poetry (without Conda)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Install `Poetry <https://python-poetry.org/docs/#installation>`_. Similar to conda, use poetry to prepare the environment:

.. code-block:: bash

    poetry config virtualenvs.in-project true # optional but recommended, will ensure the virtual env is created in the project root
    poetry config virtualenvs.create true # enable this argument to ensure the virtual env is created in the project root
    poetry env use python3.10 # will create the virtual env, check with `ls -l .venv`.
    poetry env activate # optional because Poetry commands (e.g. `poetry install` or `poetry run <command>`) will always automatically load the virtual env.
    poetry install

Optional: Flash-attn installation

Hunyuan model uses it to reduce memory usage and speed up inference. If it is not installed, the model will run in normal mode. Install the flash-attn via:

.. code-block:: bash

    poetry run install-flash-attn 

(The above process takes around 1 minute)

Optional: Video-to-video enhancement

.. code-block:: bash

    poetry run pip install "modelscope[cv]" -f https://modelscope.oss-cn-beijing.aliyuncs.com/releases/repo.html

(If this command above get stucked, kill and re-run it will solve the issue)

(3) If you use MacOS
~~~~~~~~~~~~~~~~~~~~

On MacOS with Apple Silicon chip use `docker compose <https://docs.docker.com/compose/>`_ because some dependencies are not supporting arm64 (e.g. bitsandbytes, decord, xformers).

Build VideoTuna using docker compose:

.. code-block:: bash

    docker compose build videotuna

To preserve the project's files permissions set those env variables:

.. code-block:: bash

    export HOST_UID=$(id -u)
    export HOST_GID=$(id -g)

Install and check dependencies:

.. code-block:: bash

    docker compose run --remove-orphans videotuna poetry env use /usr/local/bin/python
    docker compose run --remove-orphans videotuna poetry run python -m pip install --upgrade pip setuptools wheel
    docker compose run --remove-orphans videotuna poetry install
    docker compose run --remove-orphans videotuna poetry run pip install "modelscope[cv]" -f https://modelscope.oss-cn-beijing.aliyuncs.com/releases/repo.html
    docker compose run --remove-orphans videotuna poetry add wheel
    
    docker compose run --remove-orphans videotuna poetry run pip freeze # Check dependencies

(Installing swissarmytransformer might hang. Just try again and it should work)

Run Poetry commands:

.. code-block:: bash

    docker compose run --remove-orphans videotuna poetry run format

Start a terminal:

.. code-block:: bash

    docker compose run -it --remove-orphans videotuna bash





