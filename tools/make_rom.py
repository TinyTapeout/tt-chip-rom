from font import segment_char
import os


rom = bytearray(256)

rom_text = f"shuttle=tt04\n"
rom_text += f"repo=TinyTapeout/tinytapeout-04\n"

assert len(rom_text) < 96, "ROM text too long"

rom[0:4] = map(segment_char, "tt04")
rom[32 : 32 + len(rom_text)] = rom_text.encode("ascii")

with open(os.path.join(os.path.dirname(__file__), "../src/rom.vmem"), "w") as fh:
    for line in range(0, len(rom), 16):
        for byte in range(0, 16):
            fh.write("{:02x} ".format(rom[line + byte]))
        fh.write("\n")
