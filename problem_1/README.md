
## Instructions and Descriptions for setting up and running the package.
> Note : The following code has been tested in Ubuntu 20.04 LTS.
### DESCRIPTION
#### include 
> contains the main cpp file that will be included as a header in main.cpp
#### input
> contains the xml file listing the bins of specified dimensions
#### Makefile
> this file contains the libraries to be linked while running main.cpp also takes care of its compilation and converting into an executable.

### INSTRUCTIONS
> Before proceeding to run the file make sure the following dependencies have been installed.
> -lboost_serialization -lboost_iostreams -lboost_system

1. Update the package list:

    ```sh
    sudo apt-get update
    ```

2. Install the Boost libraries:

    ```sh
    sudo apt-get install libboost-all-dev
    ```

> Once this is done just run the following inside the problem_1 directory

  ```sh
  make all
  ```
> The run the output executable file.

 ```sh
  ./main.out
 ```

