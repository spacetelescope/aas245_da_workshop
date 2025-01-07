# Setup and Installation Instructions for Workshop

To run all the workshop notebooks on your own computer, you will need
a Python enviroment configured with the required packages (and data).
These instructions describe setup using `git` and `Miniconda`.

If you have any problems with any of these steps, please
check if your problem has already been reported at [the issue
tracker](https://github.com/spacetelescope/aas245_da_workshop/issues)
or on the AAS 245 Slack channel
`#workshop-python-data-analysis-with-the-james-webb-and-roman-space-telescopes`. If not, then you can create a new issue or ask on the Slack
channel.

For the commands shown, `%` (and anything to the left of it) represents
the terminal prompt. You do not need to copy it; instead only copy the
command to the right of `%`.


## 1. Install Miniconda (if needed)

*Miniconda is a free minimal installer for conda. It is a small,
bootstrap version of Anaconda that includes only conda, Python, the
packages they depend on, and a small number of other useful packages,
including pip, zlib, and a few others. If you have either Miniconda or
the full Anaconda already installed, you can skip to the next step.*

In a terminal window, check if Miniconda is already installed.

    % conda info

If Miniconda is not already installed, follow
these instructions for your operating system:
https://conda.io/projects/conda/en/latest/user-guide/install/index.html.
Please be sure to install a **64-bit version** of Miniconda to ensure
all packages work correctly.

(On native Windows, you might also need [additional
compilers](https://github.com/conda/conda-build/wiki/Windows-Compilers),
although this should not be necessary in WSL).


## 2. Check your conda installation

Open a terminal window and verify that conda is working:

    % conda info

If you are having trouble, check your shell in a terminal window:

    % echo $SHELL

then run the initialization if needed, in that same terminal window:

    % conda init `basename $SHELL`

You should open a new terminal window after `conda init` is run.

It is advisable to update your conda to the latest version. We recommend
a minimum version of 23.10.0. Check your conda version with:

    % conda --version

Update it with:

    % conda update conda

or

    % conda update -n base conda


## 3. Install git (if needed)

At the prompt opened in the previous step, enter this command to see
whether git is already installed and accessible to this shell:

    % git --version

If the output shows a git version, proceed to the next step. Otherwise
install git by entering the following command and following the prompts:

    % conda install git


## 4. Clone this repository, or download a ZIP file

If using `git`, clone the workshop repository using
[git](https://help.github.com/articles/set-up-git/):

    % git clone https://github.com/spacetelescope/aas245_da_workshop

If you elect not to use `git`, you can download
the ZIP file by opening the green *Code* button at
https://github.com/spacetelescope/aas245_da_workshop and selecting
*Download ZIP*.


## 5. Create a conda environment for the workshop

*Miniconda includes an environment manager called conda. Environments
allow you to have multiple sets of Python packages installed at the
same time, making reproducibility and upgrades easier. You can create,
export, list, remove, and update environments that have different
versions of Python and/or packages installed in them.*

Create and activate a new Python 3.12 environment for the workshop
called da-workshop:

    % conda create -n da-workshop python=3.12 -y
    % conda activate da-workshop

The name of the new conda environment created above should be displayed next
to the terminal prompt: `(da-workshop) %`


## 6. Install the required packages and data

All the required packages are specified in the
[requirements.txt](https://github.com/spacetelescope/aas245_da_workshop/blob/main/install_and_setup/requirements.txt)
file. In a terminal, go to the directory where you cloned or downloaded the
workshop repository, and then go to to `install_and_setup` directory:

    % cd <your_path_prefix>/aas245_da_workshop/install_and_setup

Then install the required packages with:

    (da-workshop) % pip install -r requirements.txt

The `webbpsf` package also requires the installation of data files
containing such information as the JWST pupil shape, instrument
throughputs, and aperture positions. To run WebbPSF, you must download
these files and tell WebbPSF where to find them using the `WEBBPSF_PATH`
environment variable.

* Download the following file: [webbpsf-data-LATEST.tar.gz](https://stsci.box.com/shared/static/qxpiaxsjwo15ml6m4pkhtk36c9jgj70k.gz) (approx. 70 MB)

* Untar `webbpsf-data-LATEST.tar.gz` into a directory of your choosing
  and set the environment variable `WEBBPSF_PATH` to point to that
  directory. e.g., for bash/zsh:

    $ export WEBBPSF_PATH=$HOME/data/webbpsf-data

You should now be able to successfully `import webbpsf` in a Python session.


## 7. Check Installation

The name of the new conda environment created above should be displayed next
to the terminal prompt: `(da-workshop) %`

In the same `install_and_setup` directory, run the `check_env.py` script to
check the Python environment and some of the required dependencies:

    (da-workshop) % python check_env.py

If the script reports that some of the versions do not match, check first
whether the package was installed using conda or pip, then update accordingly.
The example below a fake package called `packagename`; replace it with the
actual package that you need to update.

    (da-workshop) % conda list <packagename>

If it was installed with conda, you will see (the channel column might or
might not be populated):

    # packages in environment at .../miniconda/envs/da-workshop:
    #
    # Name                    Version                   Build  Channel
    packagename               X.Y.Z        py312hf484d3e_1000

Otherwise, if it was installed with pip, you will see the channel stating the
name `pypi`:

    # packages in environment at .../miniconda/envs/da-workshop:
    #
    # Name                    Version                   Build  Channel
    packagename               X.Y.Z                     pypi_0    pypi

To update the reported package with conda:

    (da-workshop) % conda update <packagename>

Otherwise, to update with pip:

    (da-workshop) % pip install <packagename> --upgrade

The exception to this is if the `astroquery` package is reported as
out-of-date, always update to its pre-release version with pip:

    (da-workshop) % pip install astroquery --pre --upgrade


## 8. Download the Required Workshop Data

Go back to the top level `aas245_da_workshop` directory:

    (da-workshop) % cd ..

Run the following script to download the required workshop data
(~2.4 GB):

    % python install_and_setup/download_data.py

For the ASDF and gwcs notebooks, run the following script to download
the required data (~360 MB):

    % python asdf/data/download.py


## 9. Starting Jupyter Notebook

In the terminal window you used with the conda environment created
above, change directory to the top level `aas245_da_workshop` directory.

Make sure the current directory in your terminal contains all the
numbered notebook directories. Then start JupyterLab:

    (da-workshop) % jupyter lab

If successful, your browser would open a new page/tab pointing to
`localhost`. Click on the folder icon at the upper left to open the file
browser. You should see a list of directories for each of the notebook
subdirectories.

Double-click into one of the notebook directories such as `specreduce`.
Then double-click on a notebook such as `specreduce.ipynb` and wait for
it to launch. If you do not see any errors, then all is well.
