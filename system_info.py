
import platform
import shutil

print("=== SYSTEM INFORMATION ===")
print(f"Computer Name: {platform.node()}")
print(f"Operating System: {platform.system()}")
print(f"OS Version: {platform.version()}")
print(f"ProcessorL: {platform.processor()}")

total, used, free = shutil.disk_usage("/")

print("\n=== DISK SPACE ===")
print(f"Total: {total // (2**30)} GB")
print(f"Used: {used // (2**30)} GB")
print(f"Free: {free // (2**30)} GB")
