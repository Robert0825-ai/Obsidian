# Build 黑夜骑士 layer-0 rooms into MetSys MapData.txt (keep sample layers 1–2).
from __future__ import annotations

from pathlib import Path

SRC = Path(r"C:\Users\yehai\Downloads\Metroidvania-System-master\Metroidvania-System-master\SampleProject\Maps\MapData.txt")
R, D, L, U = 0, 1, 2, 3
NBR = ((1, 0, R, L), (0, 1, D, U), (-1, 0, L, R), (0, -1, U, D))

# Olive like Hollow Knight Greenpath. Rooms are irregular polyominoes, not boxes.
F, FD, H, SH, DN, PL, ST, STT, CP = (
    "4a5c42",
    "354534",
    "3d5238",
    "454c32",
    "3a4238",
    "355044",
    "2a2a32",
    "4a4a28",
    "3f3a28",
)

ROOMS: dict[str, dict] = {
    "spawn": {"color": STT, "cells": [(1, 18), (2, 18), (2, 19)]},
    "mouth": {"color": F, "cells": [(3, 18), (4, 18), (4, 17), (5, 17)]},
    "dropwell": {"color": F, "cells": [(4, 19), (4, 20), (5, 19), (5, 20), (6, 20), (7, 20), (7, 19)]},
    "camp": {"color": CP, "cells": [(1, 20), (2, 20), (2, 21), (3, 21), (3, 20)]},
    "west_secret": {"color": FD, "cells": [(0, 15), (0, 16), (0, 17), (1, 15), (1, 16), (1, 17)]},
    "snake1": {"color": F, "cells": [(6, 17), (7, 17), (7, 16), (8, 16)]},
    "sprawl": {
        "color": H,
        "cells": [
            (5, 11), (6, 11), (7, 11), (8, 11), (9, 11),
            (5, 12), (6, 12), (7, 12), (8, 12), (9, 12),
            (4, 13), (5, 13), (6, 13), (7, 13), (8, 13), (9, 13), (10, 13), (11, 13),
            (5, 14), (6, 14), (7, 14), (8, 14), (9, 14), (10, 14),
            (6, 15), (7, 15), (8, 15),
        ],
    },
    "shaft": {
        "color": SH,
        "cells": [(8, 6), (8, 7), (8, 8), (8, 9), (8, 10), (9, 8), (7, 9), (9, 10)],
        "symbol": (8, 8, 0),
    },
    "north": {"color": F, "cells": [(6, 5), (7, 5), (8, 5), (9, 5), (10, 5), (7, 4), (8, 4), (9, 4)]},
    "castle": {"color": ST, "cells": [(8, 1), (8, 2), (8, 3)]},
    "alcove": {"color": FD, "cells": [(10, 4), (11, 4), (11, 5), (12, 4), (12, 5)]},
    "vine": {"color": SH, "cells": [(4, 8), (4, 9), (4, 10), (5, 9), (5, 10), (6, 10)]},
    "grove": {
        "color": F,
        "cells": [(10, 8), (11, 8), (12, 8), (10, 9), (11, 9), (12, 9), (13, 9), (12, 7), (13, 8)],
    },
    "high_east": {"color": F, "cells": [(10, 6), (11, 6), (12, 6), (11, 7)]},
    "thin": {"color": SH, "cells": [(14, 3), (14, 4), (14, 5), (14, 6), (15, 5), (13, 4)]},
    "pool": {
        "color": PL,
        "cells": [
            (11, 14), (11, 15), (12, 14), (12, 15), (12, 16),
            (13, 14), (13, 15), (13, 16),
            (14, 14), (14, 15), (14, 16),
            (15, 14), (15, 15), (16, 15),
        ],
    },
    "east_wind": {
        "color": F,
        "cells": [(11, 12), (12, 12), (13, 12), (14, 12), (15, 12), (15, 13), (16, 13), (16, 14), (17, 14)],
    },
    "chamber": {
        "color": DN,
        "cells": [
            (17, 12), (18, 12), (19, 12),
            (17, 13), (18, 13), (19, 13), (20, 13),
            (18, 14), (19, 14),
            (18, 11), (19, 11),
        ],
    },
    "cem": {"color": ST, "cells": [(21, 13), (22, 13), (21, 14)]},
    "south_snake": {
        "color": F,
        "cells": [
            (8, 17), (9, 17), (10, 17), (11, 17), (12, 17), (13, 17), (14, 17),
            (13, 18), (14, 18), (15, 18), (16, 18), (15, 19), (16, 19),
        ],
    },
    "south_arch": {
        "color": F,
        "cells": [(5, 18), (6, 18), (7, 18), (8, 18), (8, 19), (9, 19), (10, 19), (11, 19), (10, 18), (11, 18)],
    },
    "cache": {"color": FD, "cells": [(16, 16), (16, 17), (17, 16), (17, 17), (18, 16), (18, 17), (19, 17), (19, 18)]},
    "mist": {
        "color": F,
        "cells": [(14, 9), (14, 10), (15, 9), (15, 10), (16, 9), (16, 10), (17, 10), (17, 11)],
    },
    "overlook": {"color": FD, "cells": [(2, 11), (2, 12), (2, 13), (3, 11), (3, 12), (3, 13), (3, 14)]},
}

LABELS = [
    (1, 18, "出生穴"),
    (7, 13, "荆棘腔"),
    (8, 8, "爬藤竖井"),
    (13, 15, "荆棘池"),
    (12, 8, "枯树丛"),
    (18, 13, "虫巢厅"),
    (8, 2, "以后城堡"),
    (21, 13, "以后墓园"),
    (2, 20, "篝火袋"),
]


def main() -> None:
    owner: dict[tuple[int, int], str] = {}
    color_of: dict[tuple[int, int], str] = {}
    symbol_of: dict[tuple[int, int], int] = {}
    for name, spec in ROOMS.items():
        for cell in spec["cells"]:
            if cell in owner:
                raise SystemExit(f"overlap {cell} {owner[cell]} {name}")
            owner[cell] = name
            color_of[cell] = spec["color"]
        if "symbol" in spec:
            x, y, s = spec["symbol"]
            symbol_of[(x, y)] = s

    from collections import deque

    start = (1, 18)
    if start not in owner:
        raise SystemExit("spawn missing")
    q = deque([start])
    seen = {start}
    while q:
        x, y = q.popleft()
        for dx, dy, *_ in NBR:
            n = (x + dx, y + dy)
            if n in owner and n not in seen:
                seen.add(n)
                q.append(n)
    missing = sorted(set(owner) - seen)
    if missing:
        xs = [c[0] for c in owner]
        ys = [c[1] for c in owner]
        print("ASCII")
        for yy in range(min(ys), max(ys) + 1):
            row = ""
            for xx in range(min(xs), max(xs) + 1):
                row += "#" if (xx, yy) in seen else ("." if (xx, yy) not in owner else "x")
            print(f"{yy:3d} {row}")
        raise SystemExit(f"disconnected {len(missing)} cells e.g. {missing[:12]}")

    header: list[str] = ["$ln;荆棘林;Shadia;Renegia"]
    groups: list[str] = []
    elements: list[str] = []
    old_cells: list[str] = []

    text = SRC.read_text(encoding="utf-8")
    raw = text.splitlines()
    i = 0
    while i < len(raw):
        line = raw[i]
        if line.startswith("$ln"):
            i += 1
            continue
        if line.startswith("[") and line.endswith("]"):
            x, y, z = map(int, line[1:-1].split(","))
            i += 1
            body = raw[i] if i < len(raw) else ""
            i += 1
            if z != 0:
                old_cells.append(f"[{x},{y},{z}]")
                old_cells.append(body)
            continue
        if "/" in line and not line.startswith("["):
            z = int(line.split("/")[0].split(",")[2])
            if z != 0:
                elements.append(line)
            i += 1
            continue
        if line.startswith(":") or (line and line[0].isdigit() and ":" in line):
            groups.append(line)
            i += 1
            continue
        i += 1

    for x, y, name in LABELS:
        elements.append(f"{x},{y},0/label/1x1/{name}")

    new_cells: list[str] = []
    for (x, y), room in sorted(owner.items(), key=lambda kv: (kv[0][1], kv[0][0])):
        borders = [0, 0, 0, 0]
        for dx, dy, mine, theirs in NBR:
            n = (x + dx, y + dy)
            if n not in owner:
                borders[mine] = 0
            elif owner[n] == room:
                borders[mine] = -1
            else:
                borders[mine] = 1
        col = color_of[(x, y)]
        sym = symbol_of.get((x, y), "")
        cell = f"{borders[0]},{borders[1]},{borders[2]},{borders[3]}|{col},,,,|{sym}|"
        new_cells.append(f"[{x},{y},0]")
        new_cells.append(cell)

    out = header + groups + elements + old_cells + new_cells

    backup = SRC.with_suffix(".txt.bak-before-nightknight")
    if not backup.exists():
        backup.write_text(text, encoding="utf-8")
    SRC.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"wrote {len(owner)} layer-0 cells -> {SRC}")
    print(f"backup {backup}")


if __name__ == "__main__":
    main()
