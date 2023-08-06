import os

with open(os.path.join(os.path.dirname(__file__), "../src/rom.vmem")) as fh:
    lines = fh.readlines()
rom = []
for line in lines:
    rom.extend([int(x, 16) for x in line.split()])

rom_text = ""
for i in range(32, 32 + 96):
    if rom[i] == 0:
        break
    rom_text += chr(rom[i])

print(rom_text, end="")
