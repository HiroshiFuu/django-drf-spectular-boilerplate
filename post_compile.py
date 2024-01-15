import os
import glob

build_dir_name = os.getcwd() + '/build/lib.linux-x86_64-3.9/'
dir_name = os.getcwd() + '/'

app_names = ['core', 'backend', 'backend/v1', 'backend/v2']
for app_name in app_names:
    app_path = dir_name + app_name
    useless_files = []
    useless_files += glob.glob(app_path + '/*.py')
    useless_files += glob.glob(app_path + '/*.c')
    useless_files += glob.glob(app_path + '/*.so')
    for useless_file in useless_files:
        try:
            os.remove(useless_file)
            print('Delete: ' + useless_file)
        except:
            pass

    builded_app_path = build_dir_name + app_name
    app_path = dir_name + app_name
    os.system('cp ' + builded_app_path + '/* ' + app_path)
    print('Copy: ' + builded_app_path + '/* TO' + app_path)
    print(app_name + ' done!')

print('All done!')
