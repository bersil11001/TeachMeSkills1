from os import system
from time import sleep
import keyboard
import psutil
import json

def user_name():
    def wrapper():
        info_user = psutil.users()
        return info_user[0].name
    return wrapper()


def get_proceses():
    return psutil.process_iter()


def convert_pc(process):
    def wrapper(proceses):
        dmemory=dict()
        for process in proceses:
            memory_info=process.memory_info()
            if dmemory.get(process.name())==None:
                dmemory[process.name()]=0
            dmemory[process.name()]+=memory_info.data
        return dmemory
    return wrapper(process)


def show_process_info(dmemory,name_user):
    output_str='user{0:<12}, name process{0:<17},data{0:<16}'    
    print(output_str.format(' '))
    y = json.dumps(dmemory)
    with open("sample.json", "w") as outfile:
        outfile.write(y)
    for key in dmemory.keys():
        if dmemory[key]!=0:
            print('{0:<16}, {1:<29},{2:<10}KB'.format(
                name_user,
                key,
                dmemory[key]//1024
                )
                )


def print_info_process():
    show_process_info(convert_pc(get_proceses()),user_name())

    
def info_cpu():
    def wrapper():
        system_load_all=[x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
        return system_load_all[0]
    return wrapper()

def info_net():
    return psutil.net_io_counters()


def print_info_net():
    network=info_net()
    template = f'{network.bytes_sent//1024:>10}KB/\
{network.bytes_recv//1024:<10}KB\
{network.packets_sent:>12}/{network.bytes_recv:<12}'
    print("{0:>12}/{1:<12} {0:>12}/{1:<12}".format('sent','recieved')) 
    print(template)


def print_info_cpu():
    info= int(info_cpu()*0.5)
    print(info,'%')
    print("[",'|'*info,' '*(50-info),']',sep='')


def print_menu():
    print('"u" print info about cpu, \
    "c" for exit,"i" print info about process, \
    "n" print info about net, \
    "a" print all ')


def show_all():
    print_info_cpu()
    print_info_net()
    print_info_process()
    print_menu()


def main():
    print_menu()
    while(True):
        if  keyboard.is_pressed('c'):
            return
        if keyboard.is_pressed('u'):
            print_info_cpu()
            sleep(0.5)
        if keyboard.is_pressed('i'):
            print_info_process()
            sleep(0.5)
        if keyboard.is_pressed('n'):
            print_info_net()
            sleep(0.5)
        if keyboard.is_pressed('a'):
            system('clear')
            show_all()
            sleep(0.5)        


if __name__ == '__main__':
    main()
