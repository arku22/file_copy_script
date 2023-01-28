import os
from pathlib import Path
import shutil
import logging
from utilities import format_set_to_txt
import time


start_time = time.time()

# configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
filehandler = logging.FileHandler("mylog.log")
logger.addHandler(filehandler)
formatter = logging.Formatter("%(asctime)s:%(message)s")
filehandler.setFormatter(formatter)


num_files = 0
num_dirs = 0
files_not_copied = set()
copy_success = True
files_copied = set()

source_path = Path("/", "Users", "architkumar", "Downloads")
destination_path = Path("/", "Users", "architkumar", "Downloads", "test_copy_folder")
for i in os.listdir(source_path):
    object_path = source_path / i
    if os.path.isfile(object_path):
        try:
            shutil.copy(object_path, destination_path)
        except:
            files_not_copied.add(object_path)
            copy_success = False
        if copy_success:
            files_copied.add(object_path)
        else:
            copy_success = True

logger.debug("----------------------------------------------")
logger.debug(f"Total number of files copied = {len(files_copied)};")
logger.debug(f"Total number of files NOT copied = {len(files_not_copied)};")

format_set_to_txt(files_copied, "files_copied.txt")
format_set_to_txt(files_not_copied, "files_not_copied.txt")
# with open("files_copied.txt", "w") as f:
#     f.write(str(files_copied))
# with open("files_not_copied.txt", "w") as f:
#     f.write(str(files_not_copied))

end_time = time.time()

logger.debug(f"Time Taken (seconds) = {round(end_time - start_time)} secs")

