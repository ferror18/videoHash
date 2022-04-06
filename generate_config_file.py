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
            os.remove('config.txt')
            generate_config_file()
    else:
        finalConf=[]

        print('Input the origin path ( enter to use current working dir + data ):')
        inp = input()
        if inp == '':
            inp = os.path.join(os.getcwd(), 'data')
        finalConf.append(inp)
        clearConsole()

        print('Input the destination path ( enter to use current working dir + destination ):')
        inp = input()
        if inp == '':
            inp = os.path.join(os.getcwd(), 'destination')

        finalConf.append(inp)
        clearConsole()

        print('Input the collision path ( enter to use current working dir + collisions ):')
        inp = input()
        if inp == '':
            inp = os.path.join(os.getcwd(), 'collisions')
        finalConf.append(inp)
        clearConsole()

        print('Input the name of the database? (Enter for vh.db):')
        inp = input()
        if inp == '':
            inp = 'vh.db'
        finalConf.append(inp)
        clearConsole()

        print("Do you want to add episode names to files?\n\ta)Yes\n\tb)No")
        modeString = ''
        inp = input()
        modeString+='e' if  inp == 'a' else 'n'
        clearConsole()

        print("Do you want to keep the same names of files?\n\ta)Keep Original Name\n\tb)Use unique random Name")
        inp = input()
        modeString+='k' if  inp == 'a' else 'r'
        clearConsole()

        print("Do you want to move files into folders per Year or Month or neither?\n\ta)Year\n\tb)Month\n\tc)No order")
        inp = input()
        if inp == 'a':
            modeString+='y'
        elif inp == 'b':
            modeString+='m'
        elif inp == 'c':
            modeString+='s'
        clearConsole()

        finalConf.append(modeString)

        print("Do you want to include any extra video file extensions? Already inluded ('mp4', 'mkv', 'mov', 'webm', 'avi')\n\ta)Yes\n\tb)No")
        inp = input()
        if inp == 'a':
            while True:
                print('Type it now:')
                z = input()
                print('Is ', z, 'correct?\n\ta)Yes\n\tb)No\n\tx)cancel')
                inp = input()
                if inp == 'a':
                    finalConf.append(z)
                    break
                elif inp == 'x':
                    finalConf.append(0)
                    break
        else:
            finalConf.append(0)
        clearConsole()

        print("Do you want to include any extra photo file extensions? Already inluded ('jpg', 'png', 'tiff', 'pdf', 'raw', 'webp')\n\ta)Yes\n\tb)No")
        inp = input()
        if inp == 'a':
            while True:
                print('Type it now:')
                z = input()
                print('Is ', z, 'correct?\n\ta)Yes\n\tb)No\n\tx)cancel')
                inp = input()
                if inp == 'a':
                    finalConf.append(z)
                    break
                elif inp == 'x':
                    finalConf.append(0)
                    break
        else:
            finalConf.append(0)
        clearConsole()


        file = open('config.txt', 'w')
    #Keep files touchung this end other wise there willbe a space in the config file
        file.write(f'''origin_path={finalConf[0]}
destination_path={finalConf[1]}
collision_path={finalConf[2]}
database={finalConf[3]}
# Mode is a string with 3 letters. Each letter refers to a difrent thing
# 1st letter is about wheter or not name by episode 'e' for orginizing them 'n' for not
# 2nd letter is about wheter to keep the original file name 'k' or replace it with it's uuid 'r'
# 3rd letter is about wheter to organize the files in yearly 'y' monthly 's' or a single 's' folder.
# Example - 'ery' Will rename to a randon uuid with and episode in front in yearlyt folders.
# Example - 'nks' Will keep original file name not add an episode number to the name and put the files in a single folder
mode={finalConf[4]}
extraVidExt={finalConf[5]} 
extraPhotoExt={finalConf[6]}''')
        file.close()

# generate_config_file()