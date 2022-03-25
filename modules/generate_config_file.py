import os
from modules.clear_console import clearConsole
def generate_config_file():
    clearConsole()
    dir = os.listdir()
    if 'config.txt' in dir:
        print('''
        config.txt already exist if you continue it will be overwritten:
        a) Continue
        b) Stop
        ''')
        cont = input()
        clearConsole()
        if cont == 'b':
            return None
    else:
        print('no')
    finalConf=[]
    
    print('Input the origin path ( This is the top most folder in your collection ):')
    inp = input()
    finalConf.append(inp)
    clearConsole()

    print('Input the destination path ( This is the folder where to put the organized files ):')
    inp = input()
    finalConf.append(inp)
    clearConsole()

    print('Input the collision path ( This is the folder for unresolved collisions ):')
    inp = input()
    finalConf.append(inp)
    clearConsole()

    print("Input which mode you prefer to use ( two modes 'episodes_by_year' or 'photos_oredered_by_month':\n\n\ta)episodes_by_year\n\n\tb)photos_oredered_by_month")
    inp = input()
    finalConf.append('episodes_by_year' if inp == 'a' else 'photos_oredered_by_month')
    clearConsole()

    file = open('config.txt', 'w')
    file.write(f'''origin_path={finalConf[0]}
destination_path={finalConf[1]}
collision_path={finalConf[2]}
# Mode either 'episodes_by_year' or 'photos_oredered_by_month'
mode={finalConf[3]}''')
    file.close()

