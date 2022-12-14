import psutil
import json


ram_data = {}
disk = {}
V_memory = {}
CPU = {}


def info_computer():
    ram = psutil.virtual_memory()
    ram_data.update(total_ram = ram.total,
                    used_ram = ram.used,
                    percent_ram = ram.percent,
                    available_ram = ram.available,
                    free_ram = ram.free)
                    
    
    data_disk = psutil.disk_usage('/')
    disk.update(total_disk = data_disk.total,
                used_disk = data_disk.used,
                free_disk = data_disk.free,   
                useddisk_percent = data_disk.percent)  
                
    
    data_memory = psutil.virtual_memory()
    V_memory.update( total = data_memory.total,
                    available = data_memory.available)
    
                  
    data_CPU = psutil.cpu_freq()
    CPU.update(current_freq = data_CPU.current,
                min_freq = data_CPU.min,
                max_freq = data_CPU.max)
    
    return disk, ram_data, CPU, V_memory


info_computer()


def change_info():
    global disk_c, _cpu, _ram_d, _mem
    disk_c = ("DISK C:",
            "| Total: " + str(int((disk["total_disk"])/ (1024**3))) + " GB",
            "| Used: " + str(int((disk["used_disk"])/ (1024**3))) + " GB",
            "| Free: " + str(int((disk["free_disk"])/ (1024**3))) + " GB",
            "| Percent: " + str(disk["useddisk_percent"]) + " %",)
    
 
    _cpu = ("Data CPU:",
            "| Cerrent Frequency: " + str(CPU["current_freq"]) + " GHz",
            "| MIN Frequency: " + str(CPU["min_freq"]) + " GHz",
            "| MAX Frequency: " + str(CPU["max_freq"]) + " GHz")


    _ram_d = ("RAM:",
            "| Total Memory: " + str(int((ram_data["total_ram"])/(1024**3))) + " GB",
            "| Used Memory: " + str(int((ram_data["used_ram"])/(1024**3))) + " GB",
            "| Percentage Employed: " + str(ram_data["percent_ram"]) + " %",
            "| Available Memory: " + str(int((ram_data["available_ram"])/(1024**3))) +  " GB",
            "| Free Memory: " + str(int((ram_data["free_ram"])/(1024**3))) + " GB")


    _mem = ("VIRTUAL_MEMORY: ",
            "| USED: " + str(int((V_memory["total"])/(1024**3))) + " GB",
            "| FREE: " + str(int((V_memory["available"])/(1024**3))) + " GB")

    return disk_c, _ram_d, _cpu, _mem


change_info()


def print_info():
    disk_c = print("DISK C:",
            "| Total: " + str(int((disk["total_disk"])/ (1024**3))) + " GB",
            "| Used: " + str(int((disk["used_disk"])/ (1024**3))) + " GB",
            "| Free: " + str(int((disk["free_disk"])/ (1024**3))) + " GB",
            "| Percent: " + str(disk["useddisk_percent"]) + " %", sep = '\n')
    
 
    _cpu = print("Data CPU:",
            "| Cerrent Frequency: " + str(CPU["current_freq"]) + " GHz",
            "| MIN Frequency: " + str(CPU["min_freq"]) + " GHz",
            "| MAX Frequency: " + str(CPU["max_freq"]) + " GHz", sep = '\n')


    _ram_d = print("RAM:",
            "| Total Memory: " + str(int((ram_data["total_ram"])/(1024**3))) + " GB",
            "| Used Memory: " + str(int((ram_data["used_ram"])/(1024**3))) + " GB",
            "| Percentage Employed: " + str(ram_data["percent_ram"]) + " %",
            "| Available Memory: " + str(int((ram_data["available_ram"])/(1024**3))) +  " GB",
            "| Free Memory: " + str(int((ram_data["free_ram"])/(1024**3))) + " GB", sep = '\n')


    _mem = print("VIRTUAL_MEMORY: ",
            "| USED: " + str(int((V_memory["total"])/(1024**3))) + " GB",
            "| FREE: " + str(int((V_memory["available"])/(1024**3))) + " GB", sep = '\n')

    
    
    return disk_c, _ram_d, _cpu, _mem


print_info()


def write_file():
    to_file_json = [disk_c, _ram_d,_cpu,_mem]

    with open('data_infoproba.json', 'w') as file:
        json.dump(to_file_json, file)

    return to_file_json


write_file()    