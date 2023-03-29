"""
generate_map.py
Jason Choi and Shashank Bandaru
Creates maps of variable sizes and benchmarks Dijkstra's algorithm.
"""
from numpy import random
from time import time
import glob, os, subprocess, re

def generate_map(size: int) -> None:
    tiles: list[tuple[str, int]] = [
        ("f", 3),
        ("g", 1),
        ("G", 2),
        ("h", 4),
        ("m", 7),
        ("r", 5),
    ]

    # Generate random map.
    map: list[str] = []
    for i in range(size ** 2):
        map.append(tiles[random.randint(0, 1000) % len(tiles)][0])
    
    # Create input file.
    if os.path.exists(f"../benchmark/gm_input_{size}.txt"):
        os.remove(f"../benchmark/gm_input_{size}.txt")
    f = open(f"../benchmark/gm_input_{size}.txt", "w")

    # Write tiles header.
    f.write(str(len(tiles)) + "\n")
    for i in tiles:
        f.write(f"{i[0]} {i[1]}\n")
    f.write(f"{size} {size}\n")

    # Write map.
    for i in range(0, len(map), size):
        f.write(''.join(map[i : i + size]) + "\n")
    
    # Start and end coordinates
    f.write("0 0\n")
    f.write(f"{size - 1} {size - 1}\n")


def benchmark() -> None:
    if not os.path.exists("bin/dijkstras"):
        subprocess.run("make")

    sizes: list[int] = [10, 20, 50, 100, 200, 500, 1000]
    mem_ptrn = re.compile(r'total heap usage:.*?,\s*(\d[\d,]*)\s*bytes allocated')

    print("Benchmark:")
    for size in sizes:
        times: list[float] = []
        memory: list[int] = []
        generate_map(size)

        for _ in range(5):
            with open(f"benchmark/gm_input_{size}.txt", "r") as input:
                # Timing
                start: float = time()
                subprocess.run("bin/dijkstras", stdin=input, stdout=subprocess.DEVNULL)
                end: float = time()
                assert end > start, "Time not working"
                times.append(end - start)

                # Memory
                output = subprocess.run(["valgrind", "bin/dijkstras"], stdin=input, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE).stderr.decode()
                match = mem_ptrn.search(output)
                if match:
                    mem_usage = match.group(1).replace(',', '')
                    memory.append(int(mem_usage))
        

        print(f"{size} x {size}:")
        print(f"      Average Time: {sum(times) / len(times):.2f} sec")
        print(f"    Average Memory: {sum(memory) / len(memory):.2f} bytes allocated")
    


def clean() -> None:
    for file in glob.glob("benchmark/*.txt"):
        os.remove(file)

if __name__ == "__main__":
    clean()
    benchmark()
    clean()