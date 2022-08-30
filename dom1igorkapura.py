
import psutil

# В связи с тем что пропустил несколько занятий надо было много нагонять.
# И перед тем как выпонлить домашние задание надо было просмотреть много пропущенной информации.
# Часть инфы стал гуглить, и один из методов что нашел и решил попробовать это словари.
def _RAM():
    print("RAM:")
    ram_dict = {}
    ram = psutil.virtual_memory()
    ram_dict['Used'] = str(int(ram.used / (1024 ** 3))) + " GB"
    ram_dict['Free'] = str(int(ram.available / (1024 ** 3))) + " GB"
    ram_dict['Total'] = str(int(ram.total / (1024 ** 3))) + " GB"
    
    return ram_dict


def info_disk():
    print ("Disc Information:")
    disk = {}
    data_disk = psutil.disk_usage('/')
    disk.update(total_disk = str(int(data_disk.total/(1024**3))) + " GB",
                used_disk = str(int(data_disk.used / (1024**3))) + " GB",
                free_disk = str(int(data_disk.free / (1024**3))) + " GB",   
                useddisk_percent = str(data_disk.percent) + "%" )  
                
    return disk


def info_battery():
    print("Battery Information:")
    battery = {}
    data_baterry = psutil.sensors_battery()
    battery.update(charge_percantage = str(data_baterry.percent) + "%",
                    on_charge = data_baterry.power_plugged)
    
    return battery                


def CPU_frequency():
    print("CPU frequency:")
    CPU = {}
    data_CPU = psutil.cpu_freq()
    CPU.update(current_freq = str(data_CPU.current) + " GHz",
                min_freq = str(data_CPU.min) + " GHz",
                max_freq = str(data_CPU.max) + " GHz")
    
    return CPU


def info_system():
    print(CPU_frequency())
    print(_RAM())
    print(info_disk())
    print(info_battery())


info_system()