import logging
import os
import time
import shutil
from subprocess import PIPE, run
import sys

DEFAULT_DIR = ["Docs", "Folders", "Images", "Videos"]
VALID_VIDEO_FORMATS = [
    ".mp4",
    ".mp2",
    ".mpg",
    ".mov",
    ".wmv",
    ".avi",
    ".avm",
    ".MTS",
    ".M2TS",
    ".TS",
    ".flv",
    ".f4v",
    ".f4p",
    ".f4a",
    ".f4b",
    ".webm",
    ".gif",
    ".gifv",
    ".mkv",
]
VALID_IMAGE_FORMATS = [
    ".jpg",
    ".fig",
    ".jpeg",
    ".jfif",
    ".pjpeg",
    ".pjp",
    ".png",
    ".gif",
    ".apng",
    ".wbep",
    ".tif",
    ".tiff",
    ".bmp",
    ".heic",
    ".svg",
    ".eps",
    ".epsf",
    ".epsi",
    ".psd",
    ".ai",
    ".ico",
    ".cur",
    ".raw",
]
VALID_TEXT_FORMATS = [".txt", ".doc", ".rtf", ".md", ".markdown"]
VALID_PDF_FORMATS = [".pdf"]
VALID_SPREADSHEET_FORMATS = [
    ".xlsx",
    ".xls",
    ".xlsm",
    ".csv",
    ".gsheet",
    ".numbers",
    ".xlsb",
    ".xltx",
    ".xltm",
    ".xlam",
]
VALID_COMPRESSED_FORMATS = [".zip", ".rar", ".7z", ".xip", ".zipx"]

dirPath = os.getcwd()
foldersDirPath = os.path.join(dirPath, "Folders")
docsDirPath = os.path.join(dirPath, "Docs")
textDirPath = os.path.join(docsDirPath, "Text")
pdfDirPath = os.path.join(docsDirPath, "PDF")
sheetDirPath = os.path.join(docsDirPath, "SpreadSheet")
othersDirPath = os.path.join(docsDirPath, "Others")
zipDirPath = os.path.join(docsDirPath, "Zip")
imagesDirPath = os.path.join(dirPath, "Images")
videosDirPath = os.path.join(dirPath, "Videos")


def create_default_dirs(dirs):
    if dirs == DEFAULT_DIR:
        logging.debug("All default directories are present")
        return

    if "Videos" not in dirs:
        os.makedirs(videosDirPath)
        logging.info("created videos folder in Downloads")

    if "Images" not in dirs:
        os.makedirs(imagesDirPath)
        logging.info("created Images directory in Downloads")

    if "Docs" not in dirs:
        os.makedirs(docsDirPath)
        logging.info("created Docs directory in Downloads")

    docs_dir_contents = os.listdir(docsDirPath)
    if "Text" not in docs_dir_contents:
        os.makedirs(textDirPath)
        logging.info("created Text directory in Downloads/Docs")
    if "PDF" not in docs_dir_contents:
        os.makedirs(pdfDirPath)
        logging.info("created PDF directory in Downloads/Docs")
    if "SpreadSheet" not in docs_dir_contents:
        os.makedirs(sheetDirPath)
        logging.info("created SpreadSheet directory in Downloads/Docs")
    if "Others" not in docs_dir_contents:
        os.makedirs(othersDirPath)
        logging.info("created Others directory in Downloads/Docs")
    if "Zip" not in docs_dir_contents:
        os.makedirs(zipDirPath)
        logging.info("created Zip directory in Downloads/Docs")

    if "Folders" not in dirs:
        os.makedirs(foldersDirPath)
        logging.info("created Folders directory in Downloads")


def copy_and_delete(src, dest):
    shutil.copy2(src, dest)
    if os.path.exists(src):
        os.remove(src)


def main():
    for _, dirs, files in os.walk(dirPath):
        files_to_organize = list(filter(file_filter, files))
        if len(files_to_organize) > 1:
            for file in files_to_organize:
                file_name, file_extension = os.path.splitext(file)
                if file_extension in VALID_COMPRESSED_FORMATS:
                    copy_and_delete(file, zipDirPath)
                elif file_extension in VALID_PDF_FORMATS:
                    copy_and_delete(file, pdfDirPath)
                elif file_extension in VALID_IMAGE_FORMATS:
                    copy_and_delete(file, imagesDirPath)
                elif file_extension in VALID_SPREADSHEET_FORMATS:
                    copy_and_delete(file, sheetDirPath)
                elif file_extension in VALID_TEXT_FORMATS:
                    if file_name != "log":
                        copy_and_delete(file, textDirPath)
                elif file_extension in VALID_VIDEO_FORMATS:
                    copy_and_delete(file, videosDirPath)
                else:
                    copy_and_delete(file, othersDirPath)
        if dirs != DEFAULT_DIR:
            for directory in dirs:
                if directory not in DEFAULT_DIR:
                    shutil.move(directory, foldersDirPath)
        break


def file_filter(file: str):
    file_name, _ = os.path.splitext(file)
    if file_name.startswith("."):
        return False
    else:
        return True


if __name__ == "__main__":
    for root, dirs, files in os.walk(dirPath):
        logging.basicConfig(
            filename="log.txt",
            filemode="w",
            level=logging.DEBUG,
            format="%(asctime)s-%(levelname)s-%(message)s",
            datefmt="%d/%m/%y %H:%M:%S",
        )
        logging.debug("logger is successfully created")
        logging.info("PID of the process is: " + str(os.getpid()))
        create_default_dirs(dirs)
        break

    isAuto = False
    if len(sys.argv) > 1 and sys.argv[1] == "auto":
        logging.debug("Automation of the process is underway")
        isAuto = True

    counter = 0
    if isAuto:
        while True:
            main()
            if counter % 1800 == 0:
                logging.debug("Process is working fine")
            counter += 1
            time.sleep(1)
    else:
        main()
        logging.info("process ran once and is successfully done")
