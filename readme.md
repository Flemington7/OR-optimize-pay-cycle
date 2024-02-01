pi python version : 3.9.2
conda info :
     active environment : base
    active env location : /home/pi/miniconda3
            shell level : 1
       user config file : /home/pi/.condarc
 populated config files : 
          conda version : 4.9.2
    conda-build version : not installed
         python version : 3.7.10.final.0
       virtual packages : __glibc=2.31=0
                          __unix=0=0
                          __archspec=1=aarch64
       base environment : /home/pi/miniconda3  (writable)
           channel URLs : https://repo.anaconda.com/pkgs/main/linux-aarch64
                          https://repo.anaconda.com/pkgs/main/noarch
                          https://repo.anaconda.com/pkgs/r/linux-aarch64
                          https://repo.anaconda.com/pkgs/r/noarch
          package cache : /home/pi/miniconda3/pkgs
                          /home/pi/.conda/pkgs
       envs directories : /home/pi/miniconda3/envs
                          /home/pi/.conda/envs
               platform : linux-aarch64
             user-agent : conda/4.9.2 requests/2.25.1 CPython/3.7.10 Linux/6.1.21-v8+ debian/11 glibc/2.31
                UID:GID : 1000:1000
             netrc file : None
           offline mode : False
After multiple attempts, I have not been able to create a new environment with python 3.9.1 or python 3.8.18, only python 3.7.10.
Conda user-guide : https://conda.io/projects/conda/en/latest/user-guide/index.html
We can't run or debug the test.py if we using conda environment, but we can run or debug the test.py if we using system environment 
whose interpreter is python 3.9.2 and the path is /usr/bin/python3. And the environment OR-OptimizePayCycle's interpreter path is /usr/local/lib/python3.11.
So, I think the problem is that the conda environment is not compatible with the current version of python in Raspberry Pi OS,
which is 3.11.5.
I reset the python soft link to python 3.9.2, and then I can run or debug the test.py in the conda environment. BUG FIXED.

SCCLab python version : 3.10.13


