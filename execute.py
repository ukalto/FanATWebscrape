import runpy

script = r"/Users/maxig/Desktop/Coding/Scripts/script.py"

while True:
    try:
        runpy.run_path(path_name=script)
    except:
        print("error")
        continue
