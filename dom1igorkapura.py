import psutil
import json


ram_data = {}
disk = {}
V_memory = {}
CPU = {}


def write_file(func_to_write):
    def func_write(name_file, name_data):
        with open(name_file, 'w') as file:
            json.dump(name_data, file)
        func_to_write(name_file, name_data)
    return func_write


@write_file
def info_computer(name_file, name_data):
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


info_computer('ram_data.json',ram_data)
info_computer('disk.json',disk)
info_computer('virtual_memory.json',V_memory)
info_computer('CPU.json',CPU)


def print_info():
    print("DISK C:",
            "| Total: " + str(int((disk["total_disk"])/ (1024**3))) + " GB",
            "| Used: " + str(int((disk["used_disk"])/ (1024**3))) + " GB",
            "| Free: " + str(int((disk["free_disk"])/ (1024**3))) + " GB",
            "| Percent: " + str(disk["useddisk_percent"]) + " %", sep = '\n')
    
 
    print("Data CPU:",
            "| Cerrent Frequency: " + str(CPU["current_freq"]) + " GHz",
            "| MIN Frequency: " + str(CPU["min_freq"]) + " GHz",
            "| MAX Frequency: " + str(CPU["max_freq"]) + " GHz", sep = '\n')


    print("RAM:",
            "| Total Memory: " + str(int((ram_data["total_ram"])/(1024**3))) + " GB",
            "| Used Memory: " + str(int((ram_data["used_ram"])/(1024**3))) + " GB",
            "| Percentage Employed: " + str(ram_data["percent_ram"]) + " %",
            "| Available Memory: " + str(int((ram_data["available_ram"])/(1024**3))) +  " GB",
            "| Free Memory: " + str(int((ram_data["free_ram"])/(1024**3))) + " GB", sep = '\n')


    print("VIRTUAL_MEMORY: ",
            "| USED: " + str(int((V_memory["total"])/(1024**3))) + " GB",
            "| FREE: " + str(int((V_memory["available"])/(1024**3))) + " GB", sep = '\n')
  

print_info()


def write_file_all_info():
    to_file_json = (disk, ram_data,CPU,V_memory)

    with open('data_info_all.json', 'w') as file:
        json.dump(to_file_json, file)


write_file_all_info()  
