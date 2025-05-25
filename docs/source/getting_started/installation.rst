.. _installation:

Installation
============

CUDA Installation
-----------------

Compute Unified Device Architecture (CUDA) is a parallel computing platform and programming model developed by NVIDIA that enables general-purpose computing on their GPUs. In scenarios where parallelization is possible to enhance computation efficiency, CUDA is being used intensively by both research and the industry.

Pre-installation check
- Sufficient Disk Space: Make sure your computer has at least 6 GB free disk space.
- CUDA Compatibility of your GPU: Visit `https://developer.nvidia.com/cuda-gpus < https://developer.nvidia.com/cuda-gpus>`_ to check whether your GPU is compatible with CUDA. In case you do not know your GPU, execute ``lspci | grep—i nvidia`` (Linux) in your shell terminal to check available GPUs.
- Admin Privileges: You need to have admin or sudo (superuser do) access to install CUDA on Windows or Ubuntu.

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

MacOS
~~~~~
