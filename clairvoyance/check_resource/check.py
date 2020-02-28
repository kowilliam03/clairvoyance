import psutil


def check_mem(quota):
    mem = psutil.virtual_memory()
    mem_usage = mem.used / mem.total

    return mem_usage > quota


def check_cpu(quota):
    return psutil.cpu_percent() > quota
