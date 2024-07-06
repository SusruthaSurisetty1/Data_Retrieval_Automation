import os, time
from datetime import date
def set_date(file, file_name):
    today = date.today()
    # add day
    file_name += str(today.day) + "_"
    # add month
    month = today.month
    if month <= 9:
        month = "0" + str(month)

    # added month & year
    file_name += month + "_" + str(today.year) + "_"

    return file_name

def set_time(file, file_name, folder_path):
    path = folder_path + file

    # Get the time of last
    # modification of the specified
    # path since the epoch
    modification_time = os.path.getmtime(path)

    # convert the time in
    # seconds since epoch
    # to local time
    local_time = time.ctime(modification_time)
    # got timestamp of file 'HH:MM:SS'
    local_time = local_time[11:19]
    hours, minutes, seconds = local_time[:2], local_time[3:5], local_time[6:]

    file_name += hours + "-" + minutes
    return file_name


# main
# 1. get files names̥

# ***************** Path Change̥ Cheyyi *****************̥
# Directory containing the files
folder_path ="D:/GRADIOUS/datasets/"

# Get list of all files in the directory̥
files = [file for file in os.listdir(folder_path) if file.endswith('.xlsx')]

# 2. each file change format
for file in files:
    file_name = ""
    file_name = set_date(file, file_name)
    file_name = set_time(file, file_name, folder_path)
    print(file_name)

    # 3. change file name to new format
    cur_file_path = folder_path + file
    # i.e., old name of file in path format

    new_cur_file_path = folder_path + file_name
    # i.e., new name of file in path format

    os.rename(cur_file_path, new_cur_file_path)