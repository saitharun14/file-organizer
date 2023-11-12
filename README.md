This is a automated file organizer specially made to automate the Downloads folders no macbooks.

## Getting started

#### Perquisites
- Python 3.

## Quick Start

- Clone or download the repo
> *NOTE:* make sure the `script.py` and `shell_script.py` are in the same folder
- Open the terminal in the folder were the shell_script is saved run
  ```bash
  $ chmod +u+x shell_script.sh
  ```
- Open a terminal in the folder you want the file organisation to happen.<br>
  > *NOTE:* If you want to automate the process of file organization it's suggested to run the script in the folder that's designated to be the file of downloads.
- Run the `shell_script.sh` as show below to run the script only once<br>
  ```bash 
  $ PATH/shell_script.sh
  ```
  > *NOTE:* `PATH` is the pathname where the `shell_script.sh` is saved
- If you want a background job to run which organizer the file as they are saved to the file run the below command.<br>
  ```bash
  $ PATH/shell_script.sh auto
  ```
  > *NOTE:* `auto` is argument to run the script as a background job by default it runs only once organizing the directory.

## How To Kill the background job

- when you run the script either as a one time script or a background job it generates a `log.txt` log in the directory where the script is present.
- The log will contains the PID (Process Identifier) of the background job.
- Run<br>
  ```bash
  $ kill -15 {PID}
  ```
