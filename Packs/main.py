import Packs.checkRequirements
from Packs.Commands import install, remove
import sys
import os


def main():
    if hasattr(sys, 'real_prefix'):
       
        commands = {
            'install': install.Installer, 
            'i': install.Installer, 
            'uninstall': remove.Remover, 
            'remove': remove.Remover, 
            'rm': remove.Remover
        }

        if len(sys.argv) <= 2:
            print("\nChoose an option and package\n")

            print('\033[92m install   <package>\033[37m  to install a package')
            print('\033[92m i         <package>\033[37m  to install a package')
            print('\033[92m -r       <filePath>\033[37m  to list of packages')
            print('\033[92m --dev or -d        \033[37m  to install development packages')
            print('\033[92m -u                 \033[37m  to update a package\n')
            
            print('\033[92m uninstall <package>\033[37m  to uninstall a package')
            print('\033[92m remove    <package>\033[37m  to uninstall a package')
            print('\033[92m rm        <package>\033[37m  to uninstall a package')
            print('\033[92m --yes or -y        \033[37m  to accept all\n')

        elif sys.argv[1].lower() not in commands:
            print('\033[91m Invalid command\033[37m')

        else:
            commands[sys.argv[1].lower()](sys.argv)

    else:
        print("\n\033[91mPlease activate the virtual environment to use Packs\n\033[37m")



if __name__ == '__main__':
    main()