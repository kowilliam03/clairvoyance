from line_notify.notify import sendLineNotify
from check_resource.check import check_mem, check_cpu

import argparse

parser = argparse.ArgumentParser(
    description="Monitor your server' CPU & Memory usage situation.")
parser.add_argument(
    "-t", "--token", help="Line Notify Token(https://notify-bot.line.me)")
parser.add_argument(
    "-c", "--cpu", default=80, help="Enter the percentage you want. Ex. 80 = 80%")
parser.add_argument(
    "-m", "--mem", default=80, help="Enter the percentage you want. Ex. 80 = 80%")

args = parser.parse_args()

# CPU situation
cpu_quota = int(args.cpu) / 100
cpu_state = check_cpu(cpu_quota)

# Memory situation
mem_quota = int(args.mem) / 100
mem_state = check_mem(mem_quota)

cpu_msg = f"The current CPU usage has exceeded {args.cpu}%"
mem_msg = f"The current Memory usage has exceeded {args.mem}%"

token = args.token
if cpu_state:
    sendLineNotify(token, cpu_msg)
if mem_state:
    sendLineNotify(token, mem_msg)
