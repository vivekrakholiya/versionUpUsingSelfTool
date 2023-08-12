import hou
import os
current_file = hou.hipFile.name()


file_dir = os.path.dirname(current_file)
file_name = os.path.splitext(os.path.basename(current_file))[0]
file_ext = os.path.splitext(os.path.basename(current_file))[1]
version_number = int(file_name[-2:]) + 1
new_name = "{}/{}{:02d}{}".format(file_dir, file_name[:-2], version_number, file_ext)

hou.hipFile.save(new_name)
