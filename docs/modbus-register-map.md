# Modbus Register Map

This map is derived from a validated Mitsui/Midea-compatible installation. Other rebrands may differ.

## Core Controls

| Register | Direction | Meaning |
| --- | --- | --- |
| 0 | read | power/status flags |
| 1 | read | requested mode |
| 2 | read | setpoint packed word |
| 10 | read | function flags |
| 11 | read/write | water target setpoint |
| 12 | read | raw parameter |
| 13 | read | raw parameter |

## Runtime

| Range | Direction | Meaning |
| --- | --- | --- |
| 100..119 | read | compressor, operating mode, temperatures, pressures, electrical values |
| 122..129 | read | faults, status bits, output bits, target frequency |
| 132..135 | read | DC bus, module temperature |
| 138 | read | water flow |
| 140 | read | hydraulic power |
| 143..144 | read | cumulative energy words |

## Configuration/Diagnostics

| Range | Direction | Meaning |
| --- | --- | --- |
| 200 | read | appliance type |
| 209..232 | read | DHW/cooling/heating parameters |
| 241..246 | read | weather curve and power limit parameters |
| 260..272 | read | packed/diagnostic parameters |

Validate every register before applying this map to another brand.

