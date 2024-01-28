import argparse
from ast import arg
from concurrent.futures import thread
from math import dist
from os import name
from pathlib import Path
from shutil import copyfile
from threading import Thread
import logging


parser = argparse.ArgumentParser(description="Sorting folder")
parser.add_argument(*name_or_flags: "--source", "-s",help="Sorting folder", required=True)
parser.add_argument(*name_or_flags: "--output", "-s",help="Output folder", default="dist")

logging.info()
args = vars(parser.parse_args())
logging.info(args)

source = Path(args.get("source"))
output = Path(args.get("output"))

folders =[]

def searching_folder(path: Path) → None:
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            searching_folder(el)

def copy_file(path: Path) → None:
        for el in path.iterdir():
             if el.is_file():
                  ext = el.suffix[1:]
                  ext_folder = output / ext
                  try:
                       ext_folder.mkdir(exist_ok=True, perents=True)
                       copyfile(el, ext_folder / el.name)
                  except OSError as err:
                       logging.error(err)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(threadName)s %(message)s")

    folders.append(source)
    searching_folder(source)
    logging.info(folders)

    threads = []
    for folder in folders:
         th = Thread(target=copy_file, args=(folder,))
         th.start()
         threads.append(th)                       
                