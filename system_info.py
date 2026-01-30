import platform
import socket
import psutil
import shutil

# Trying to importing GPUtil
try:
    import GPUtil
except ImportError:
    GPUtil = None

print("———- System Info ———-")
print("Hostname :", socket.gethostname())
print("System :", platform.system())
print("Kernel :", platform.release())
print("Processor :", platform.processor())

memory_total = round(psutil.virtual_memory().total / (1024**3))
disk_total = round(shutil.disk_usage('/').total / (1024**3))
print("Memory :", memory_total, "GiB")
print("Disk :", disk_total, "GiB")

print("———- GPU ———-")
if GPUtil:
    gpus = GPUtil.getGPUs()
    if gpus:
        for gpu in gpus:
            print(f"GPU Name: {gpu.name}")
            print(f"  Total Memory: {round(gpu.memoryTotal / 1024)} GiB")
            print(f"  Free Memory: {round(gpu.memoryFree / 1024)} GiB")
            print(f"  Used Memory: {round(gpu.memoryUsed / 1024)} GiB")
            print(f"  GPU Load: {gpu.load*100:.1f}%")
            print(f"  GPU Temperature: {gpu.temperature} °C")
    else:
        print("No GPU detected")
else:
    print("GPUtil not installed, cannot detect GPU")

# RAM & Disk usage
ram = psutil.virtual_memory()
disk = shutil.disk_usage('/')
print("———- RAM & Disk Usage ———-")
print(f"RAM Used : {round(ram.used/(1024**3))} GiB / {memory_total} GiB ({ram.percent}%)")
print(f"Disk Used : {round(disk.used/(1024**3))} GiB / {disk_total} GiB ({round(disk.used/disk.total*100)}%)")
