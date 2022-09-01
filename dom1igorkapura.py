

import psutil


def info_RAM():
    global ram_data
    ram_data = {}
    ram = psutil.virtual_memory()
    ram_data.update(total_ram = ram.total,
                    used_ram = ram.used,
                    percent_ram = ram.percent,
                    available_ram = ram.available,
                    free_ram = ram.used)
                    
    return ram

def info_disk():
    global disk
    disk = {}
    data_disk = psutil.disk_usage('/')
    disk.update(total_disk = data_disk.total,
                used_disk = data_disk.used,
                free_disk = data_disk.free,   
                useddisk_percent = data_disk.percent)  
                
    return disk


def info_battery():
    global battery
    battery = {}
    data_baterry = psutil.sensors_battery()
    battery.update(charge_percantage = data_baterry.percent,
                    on_charge = data_baterry.power_plugged)
    
    return battery                


def info_CPU_frequency():
    global CPU
    CPU = {}
    data_CPU = psutil.cpu_freq()
    CPU.update(current_freq = data_CPU.current,
                min_freq = data_CPU.min,
                max_freq = data_CPU.max)
    
    return CPU


def out_info():
    info_disk()
    info_battery()
    info_RAM()
    info_CPU_frequency()


out_info()
def change_info_all():
    def change_info_disk():
        global _DISK_C
        _DISK_C = ("DISK C:",
        "| Total: " + str(int((disk["total_disk"])/ (1024**3))) + "GB",
        "| Used: " + str(int((disk["used_disk"])/ (1024**3))) + " GB",
        "| Free: " + str(int((disk["free_disk"])/ (1024**3))) + " GB",
        "| Percent: " + str(disk["useddisk_percent"]) + " %")
    change_info_disk()


    def change_info_CPU_frequency():
        global _Data_CPU
        _Data_CPU = ("Data CPU:",
        "| Cerrent Frequency: " + str(CPU["current_freq"]) + " GHz",
        "| MIN Frequency: " + str(CPU["min_freq"]) + " GHz",
        "| MAX Frequency: " + str(CPU["max_freq"]) + " GHz")
    change_info_CPU_frequency()

    def change_info_ram():
        global _RAM
        _RAM = ("RAM:",
        "| Total Memory: " + str(int((ram_data["total_ram"])/(1024**3))) + " GB",
        "| Used Memory: " + str(int((ram_data["used_ram"])/(1024**3))) + " GB",
        "| Percentage Employed: " + str(ram_data["percent_ram"]) + " %",
        "| Available Memory: " + str(int((ram_data["available_ram"])/(1024**3))) +  " GB",
        "| Free Memory: " + str(int((ram_data["free_ram"])/(1024**3))) + " GB")
    change_info_ram()


    def change_info_baterry():
        global _Baterry
        _Baterry = ("BATERRY: ",
        "| Baterry:" + str(battery["charge_percantage"]) + " %",
        "| ON Charge: " + str(battery["on_charge"]))
    change_info_baterry()

change_info_all()

def print_info_all():
    print(*_DISK_C, sep = '\n')
    print(*_Data_CPU, sep = '\n')
    print(*_RAM, sep = '\n')
    print(*_Baterry, sep = '\n')


print_info_all()