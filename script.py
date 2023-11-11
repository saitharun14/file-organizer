import os
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
VALID_COMPRESSED_FORMATS = [".zip", ".rar", ".7z", ".zipx"]

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
    if "Videos" not in dirs:
        os.makedirs(videosDirPath)
        print("created videos folder in Downloads")

    if "Images" not in dirs:
        os.makedirs(imagesDirPath)
        print("created Images directory in Downloads")

    if "Docs" not in dirs:
        os.makedirs(docsDirPath)
        print("created Docs directory in Downloads")

    docsDirContents = os.listdir(docsDirPath)
    if "Text" not in docsDirContents:
        os.makedirs(textDirPath)
        print("created Text directory in Downloads/Docs")
    if "PDF" not in docsDirContents:
        os.makedirs(pdfDirPath)
        print("created PDF directory in Downloads/Docs")
    if "SpreadSheet" not in docsDirContents:
        os.makedirs(sheetDirPath)
        print("created SpreadSheet directory in Downloads/Docs")
    if "Others" not in docsDirContents:
        os.makedirs(othersDirPath)
        print("created Others directory in Downloads/Docs")
    if "Zip" not in docsDirContents:
        os.makedirs(zipDirPath)
        print("created Zip directory in Downloads/Docs")

    if "Folders" not in dirs:
        os.makedirs(foldersDirPath)
        print("created Folders directory in Downloads")


def copy_and_delete(src, dest):
    shutil.copy2(src, dest)
    if os.path.exists(src):
        os.remove(src)


if __name__ == "__main__":
    for root, dirs, files in os.walk(dirPath):
        create_default_dirs(dirs)
        for file in files:
            fileName, fileExtension = os.path.splitext(file)
            if not fileName.startswith("."):
                if fileExtension in VALID_COMPRESSED_FORMATS:
                    copy_and_delete(file, zipDirPath)
                elif fileExtension in VALID_PDF_FORMATS:
                    copy_and_delete(file, pdfDirPath)
                elif fileExtension in VALID_IMAGE_FORMATS:
                    copy_and_delete(file, imagesDirPath)
                elif fileExtension in VALID_SPREADSHEET_FORMATS:
                    copy_and_delete(file, sheetDirPath)
                elif fileExtension in VALID_TEXT_FORMATS:
                    copy_and_delete(file, textDirPath)
                elif fileExtension in VALID_VIDEO_FORMATS:
                    copy_and_delete(file, videosDirPath)
                else:
                    copy_and_delete(file, othersDirPath)
        for directory in dirs:
            if directory not in DEFAULT_DIR:
                shutil.move(directory, foldersDirPath)
        break
