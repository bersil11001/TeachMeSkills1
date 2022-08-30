from os import system
from time import sleep
import keyboard
import psutil


def user_name():
    info_user = psutil.users()
    return info_user[0].name
    
def get_proceses():
    return psutil.process_iter()
def show():
    name_user=user_name()

    proceses= get_proceses()
    dmemory=dict()
    for process in proceses:
        memory_info=process.memory_info()
        if dmemory.get(process.name())==None:
            dmemory[process.name()]=0
        dmemory[process.name()]+=memory_info.data
    print('user{0:<12}, name process{0:<17},data{0:<16}{1:>30}'.format(' ','"u" for update info "c" for exit  '))
    for key in dmemory.keys():
        if dmemory[key]!=0:
            print('{0:<16}, {1:<29},{2:<10}KB'.format(name_user,key,dmemory[key]//1024))


def main():
    print('"u" for update info "c" for exit')
    while(True):
        if  keyboard.is_pressed('c'):
            return
        if keyboard.is_pressed('u'):
            system('clear')
            show()
            sleep(0.5)
            

if __name__ == '__main__':
    main()