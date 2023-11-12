## Automated File Organizer for MacBooks

This is a Python script to automate the organization of your Downloads folder on a MacBook.

### Prerequisites

* Python 3

### Quick Start

1. Clone or download the repository.
2. Open a terminal and navigate to the directory containing the script files.
3. Make the script file `shell_script.sh` executable by running the following command:

```bash
chmod +u+x shell_script.sh
```
4. To run the script once, execute the following command:

```bash
PATH/shell_script.sh
```
>NOTE: `PATH` is the pathname where the script files are saved.
5. To run the script as a background job, execute the following command:

```bash
PATH/shell_script.sh auto
```
>NOTE: The `auto` argument is to run the process as a background job.

### File Structure

* After the script is run, the file structure in the base directory will look as below:
```
├── [BASE_DIRECTORY]
│   ├── Docs
│   │   ├── Others
│   │   ├── PDF
│   │   ├── SpreedSheet
│   │   ├── Text
│   │   ├── Zip
│   ├── Folders
│   ├── Images
│   ├── Vidoes
│   ├── log.txt
```
* `log.txt` will contain all the logs and information about **PID** (Process Identifier) of the process.
* `Folders` is a collection of various directors that were present in the `BASE_DIRECTORY`.

### Terminate the Background Job

* In a terminal run

```bash
kill -15 [PID]
```
* The **PID** of the process can be found in the `log.txt` file.

### Support

If you need help using the file-organizer, or have found a bug, please create an issue on the [Github repo](https://github.com/saitharun14/file-organizer/issues). If you find it useful, consider giving it a ⭐️star. **Thank you**
