# Modbus Register Map

This map is validated on one Mitsui/Midea-compatible unit. Other Midea-platform rebrands may match, partially match or differ. Treat writes as unsafe until the target unit has been validated.

## Bus Settings

| Setting | Value |
| --- | --- |
| Protocol | Modbus RTU |
| Function used by sensors | Holding registers / FC03 |
| Default slave address | `1` |
| Serial mode | `9600 8N1` |
| ESPHome base update interval | `10s` |
| `skip_updates: 2` effective cadence | about `30s` |
| `skip_updates: 5` effective cadence | about `60s` |

`force_new_range: true` is used only to split ESPHome Modbus read batches at practical boundaries. It is not part of the heat pump protocol.

## Data Types

| Type | Meaning |
| --- | --- |
| `U_WORD` | unsigned 16-bit holding register |
| `S_WORD` | signed 16-bit holding register |
| `Raw` suffix | value is intentionally exposed without decoding |
| `Diagnostic` | useful for validation/troubleshooting; not always meant as a daily control |

## Mode Values

Registers `1` and `101` are rendered by the firmware with the same mapping:

| Value | Meaning |
| --- | --- |
| `0` | off |
| `1` | auto |
| `2` | cooling |
| `3` | heating |

## Full Register Table

### HMI / Low Registers

| Register | Direction | ESPHome entity | Type | Unit/scale | Meaning |
| --- | --- | --- | --- | --- | --- |
| `0` | read | `PDC Mitsui Power Flags Raw` | `U_WORD` | raw | Packed power/status flags from the controller area. Exposed raw until individual bits are confirmed. |
| `1` | read | `PDC Mitsui Mode Set Raw` | `U_WORD` | enum | Requested/set mode. Decoded as off/auto/cooling/heating. |
| `2` | read | `PDC Mitsui Setpoint Word Raw` | `U_WORD` | packed | Packed setpoint word. High and low bytes are also exposed as derived diagnostics. |
| `5` | read | `PDC Mitsui Function Flags Raw` | `U_WORD` | raw, ~30s | Packed function flags. Exposed raw until all bits are confirmed. |
| `10` | read | `PDC Mitsui SG Max Time` | `U_WORD` | h | Smart-grid or special-function max time candidate. Diagnostic. |
| `11` | read/write | `PDC Mitsui Setpoint Water` / `PDC Mitsui Setpoint Water Target` | `U_WORD` | C | Water target setpoint. Only exposed write register in this project. |
| `12` | read | `PDC Mitsui Register 12 Raw` | `U_WORD` | raw | Low-register diagnostic candidate. Meaning still kept raw. |
| `13` | read | `PDC Mitsui Register 13 Raw` | `U_WORD` | raw | Low-register diagnostic candidate. Meaning still kept raw. |

### Runtime Registers

| Register | Direction | ESPHome entity | Type | Unit/scale | Meaning |
| --- | --- | --- | --- | --- | --- |
| `100` | read | `PDC Mitsui Compressor Frequency` | `U_WORD` | Hz | Current compressor frequency. |
| `101` | read | `PDC Mitsui Operating Mode Raw` | `U_WORD` | enum | Current operating mode. Decoded as off/auto/cooling/heating. |
| `102` | read | `PDC Mitsui Fan Speed` | `U_WORD` | rpm | Outdoor/unit fan speed. |
| `103` | read | `PDC Mitsui PMV Steps` | `U_WORD` | steps | Electronic expansion valve/PMV position in steps. |
| `104` | read | `PDC Mitsui Water Inlet` | `S_WORD` | C | Water inlet/return temperature. |
| `105` | read | `PDC Mitsui Water Outlet` | `S_WORD` | C | Water outlet/supply temperature. |
| `106` | read | `PDC Mitsui T3 Condenser` | `S_WORD` | C, ~30s | Condenser temperature. |
| `107` | read | `PDC Mitsui T4 Outdoor` | `S_WORD` | C | Outdoor temperature. |
| `108` | read | `PDC Mitsui Tp Discharge` | `S_WORD` | C | Compressor discharge temperature. |
| `109` | read | `PDC Mitsui Th Suction` | `S_WORD` | C | Suction temperature. |
| `110` | read | `PDC Mitsui T1 Total Water Outlet` | `S_WORD` | C | Total water outlet temperature. |
| `111` | read | `PDC Mitsui T1B Aux Outlet` | `S_WORD` | C | Auxiliary/secondary outlet temperature. |
| `112` | read | `PDC Mitsui T2 Refrigerant Liquid` | `S_WORD` | C | Refrigerant liquid temperature. |
| `113` | read | `PDC Mitsui T2B Refrigerant Gas` | `S_WORD` | C | Refrigerant gas temperature. |
| `114` | read | `PDC Mitsui Ta Room` | `S_WORD` | C | Room/ambient temperature as reported by the controller. |
| `115` | read | `PDC Mitsui T5 Tank` | `S_WORD` | C | Tank/DHW temperature candidate. |
| `116` | read | `PDC Mitsui High Pressure` | `U_WORD` | kPa | High pressure sensor. |
| `117` | read | `PDC Mitsui Low Pressure` | `U_WORD` | kPa | Low pressure sensor. |
| `118` | read | `PDC Mitsui Outdoor Current Raw` | `U_WORD` | A raw | Outdoor current value, kept raw because scaling may vary by unit. |
| `119` | read | `PDC Mitsui Outdoor Voltage` | `U_WORD` | V | Outdoor/main voltage. |

### Fault, Status and Output Registers

| Register | Direction | ESPHome entity | Type | Unit/scale | Meaning |
| --- | --- | --- | --- | --- | --- |
| `122` | read | `PDC Mitsui Compressor Hours` | `U_WORD` | h, ~60s | Compressor runtime counter. |
| `123` | read | `PDC Mitsui ODU Model Raw` | `U_WORD` | raw | Outdoor unit model/family identifier candidate. |
| `124` | read | `PDC Mitsui Current Fault` | `U_WORD` | code | Current active fault code. |
| `125` | read | `PDC Mitsui Fault 1` | `U_WORD` | code/raw | Fault history or fault slot 1. |
| `126` | read | `PDC Mitsui Fault 2` | `U_WORD` | code/raw | Fault history or fault slot 2. |
| `127` | read | `PDC Mitsui Fault 3` | `U_WORD` | code/raw | Fault history or fault slot 3. |
| `128` | read | `PDC Mitsui Status Bits Raw` | `U_WORD` | bitfield | Status bitfield. Decoded bits are listed below. |
| `129` | read | `PDC Mitsui Output Bits Raw` | `U_WORD` | bitfield | Output/actuator bitfield. Decoded bits are listed below. |
| `132` | read | `PDC Mitsui Target Frequency` | `U_WORD` | Hz | Target compressor frequency. |
| `133` | read | `PDC Mitsui DC Bus Current Raw` | `U_WORD` | A raw, ~30s | DC bus current raw/diagnostic value. |
| `134` | read | `PDC Mitsui DC Bus Voltage Raw` | `U_WORD` | raw | DC bus voltage raw value. Derived voltage multiplies by 10. |
| `135` | read | `PDC Mitsui TF Module` | `S_WORD` | C | Power module temperature. |
| `138` | read | `PDC Mitsui Water Flow` | `U_WORD` | raw x 0.01 m3/h | Water flow. ESPHome applies `multiply: 0.01`. |
| `140` | read | `PDC Mitsui Hydraulic Power` | `U_WORD` | raw x 0.01 kW | Hydraulic power. ESPHome applies `multiply: 0.01`. |
| `143` | read | `PDC Mitsui Energy Consumption High Raw` | `U_WORD` | high word, ~60s | High word of cumulative energy. |
| `144` | read | `PDC Mitsui Energy Consumption Low Raw` | `U_WORD` | low word | Low word of cumulative energy. |

### Appliance and DHW / Cooling / Heating Parameters

| Register | Direction | ESPHome entity | Type | Unit/scale | Meaning |
| --- | --- | --- | --- | --- | --- |
| `200` | read | `PDC Mitsui Home Appliance Type Raw` | `U_WORD` | raw, ~60s | Appliance type/family identifier candidate. |
| `209` | read | `PDC Mitsui DHW Pump Running Time` | `U_WORD` | min, ~60s | DHW pump running time parameter. |
| `210` | read | `PDC Mitsui Parameter Setting 1 Raw` | `U_WORD` | raw | Packed parameter setting 1. |
| `211` | read | `PDC Mitsui Parameter Setting 2 Raw` | `U_WORD` | raw | Packed parameter setting 2. |
| `212` | read | `PDC Mitsui dT5 On` | `U_WORD` | C | DHW/tank differential parameter. |
| `213` | read | `PDC Mitsui dT1S5` | `U_WORD` | C | DHW/tank differential parameter. |
| `214` | read | `PDC Mitsui DHW Interval` | `U_WORD` | min | DHW interval parameter. |
| `215` | read | `PDC Mitsui T4 DHW Max` | `U_WORD` | C | Max outdoor temperature for DHW operation. |
| `216` | read | `PDC Mitsui T4 DHW Min` | `S_WORD` | C | Min outdoor temperature for DHW operation. |
| `217` | read | `PDC Mitsui TBH Delay` | `U_WORD` | min | Tank backup heater delay. |
| `218` | read | `PDC Mitsui dT5 TBH Off` | `U_WORD` | C | Tank backup heater off differential. |
| `219` | read | `PDC Mitsui T4 TBH On` | `S_WORD` | C | Outdoor temperature threshold for backup heater. |
| `220` | read | `PDC Mitsui T5s Disinfection` | `U_WORD` | C | Disinfection target temperature. |
| `221` | read | `PDC Mitsui Disinfection Max Time` | `U_WORD` | min | Disinfection maximum duration. |
| `222` | read | `PDC Mitsui Disinfection High Temp Time` | `U_WORD` | min | Required high-temperature time during disinfection. |
| `223` | read | `PDC Mitsui Cooling Interval Candidate` | `U_WORD` | min | Cooling interval candidate parameter. |
| `224` | read | `PDC Mitsui dT1SC` | `U_WORD` | C | Cooling water differential parameter. |
| `225` | read | `PDC Mitsui dTSC` | `U_WORD` | C | Cooling differential parameter. |
| `226` | read | `PDC Mitsui T4 Cooling Max` | `U_WORD` | C | Max outdoor temperature for cooling operation. |
| `227` | read | `PDC Mitsui T4 Cooling Min` | `S_WORD` | C | Min outdoor temperature for cooling operation. |
| `228` | read | `PDC Mitsui Heating Interval Candidate` | `U_WORD` | min | Heating interval candidate parameter. |
| `229` | read | `PDC Mitsui dT1SH` | `U_WORD` | C | Heating water differential parameter. |
| `230` | read | `PDC Mitsui dTSH` | `U_WORD` | C | Heating differential parameter. |
| `231` | read | `PDC Mitsui T4 Heating Max` | `U_WORD` | C | Max outdoor temperature for heating operation. |
| `232` | read | `PDC Mitsui T4 Heating Min` | `S_WORD` | C | Min outdoor temperature for heating operation. |

### Weather Curve, Power Limit and Misc Parameters

| Register | Direction | ESPHome entity | Type | Unit/scale | Meaning |
| --- | --- | --- | --- | --- | --- |
| `241` | read | `PDC Mitsui DHW Heat Pump Max Time` | `U_WORD` | min, ~60s | Max DHW heat pump time. |
| `242` | read | `PDC Mitsui DHW Heat Pump Restrict Time` | `U_WORD` | min | DHW heat pump restriction time. |
| `243` | read | `PDC Mitsui T4 Auto Cooling Min` | `S_WORD` | C | Auto mode cooling outdoor threshold. |
| `244` | read | `PDC Mitsui T4 Auto Heating Max` | `S_WORD` | C | Auto mode heating outdoor threshold. |
| `245` | read | `PDC Mitsui Holiday Heating Setpoint` | `U_WORD` | C | Holiday heating setpoint. |
| `246` | read | `PDC Mitsui Holiday DHW Setpoint` | `U_WORD` | C | Holiday DHW setpoint. |
| `260` | read | `PDC Mitsui First Floor Heating Setpoint` | `U_WORD` | C, ~60s | First-floor heating setpoint parameter. |
| `261` | read | `PDC Mitsui Cooling Curve T1 C1` | `U_WORD` | C | Cooling weather curve water point C1. |
| `262` | read | `PDC Mitsui Cooling Curve T1 C2` | `U_WORD` | C | Cooling weather curve water point C2. |
| `263` | read | `PDC Mitsui Cooling Curve T4 C1` | `S_WORD` | C | Cooling weather curve outdoor point C1. |
| `264` | read | `PDC Mitsui Cooling Curve T4 C2` | `S_WORD` | C | Cooling weather curve outdoor point C2. |
| `265` | read | `PDC Mitsui Heating Curve T1 H1` | `U_WORD` | C | Heating weather curve water point H1. |
| `266` | read | `PDC Mitsui Heating Curve T1 H2` | `U_WORD` | C | Heating weather curve water point H2. |
| `267` | read | `PDC Mitsui Heating Curve T4 H1` | `S_WORD` | C | Heating weather curve outdoor point H1. |
| `268` | read | `PDC Mitsui Heating Curve T4 H2` | `S_WORD` | C | Heating weather curve outdoor point H2. |
| `269` | read | `PDC Mitsui Power Input Limitation Type` | `U_WORD` | raw | Power input limitation type/strategy. |
| `270` | read | `PDC Mitsui T4 Fresh Packed Raw` | `U_WORD` | packed/raw | Packed outdoor/fresh-air related parameter candidate. |
| `271` | read | `PDC Mitsui Pump I Delay Raw` | `U_WORD` | raw | Internal pump delay raw parameter. |
| `272` | read | `PDC Mitsui Emission Type Raw` | `U_WORD` | raw | Emission system type raw parameter. |

## Derived ESPHome Entities

These are not separate Modbus registers. They are computed from one or more raw registers.

| Entity | Source | Formula / meaning |
| --- | --- | --- |
| `PDC Mitsui Setpoint Word High Byte` | register `2` | `(reg2 >> 8) & 0xFF`, exposed in C for diagnostics. |
| `PDC Mitsui Setpoint Word Low Byte` | register `2` | `reg2 & 0xFF`, exposed in C for diagnostics. |
| `PDC Mitsui PMV Percent` | register `103` | `PMV steps * 100 / 480`, clamped to 0..100 percent. |
| `PDC Mitsui Delta T Outlet Minus Inlet` | registers `104`, `105` | `water_outlet - water_inlet`. |
| `PDC Mitsui Energy Consumption` | registers `143`, `144` | `high_word * 65536 + low_word`, exposed as kWh. |
| `PDC Mitsui DC Bus Voltage` | register `134` | `raw * 10`, exposed as V. |
| `PDC Mitsui Thermal Power Estimated` | registers `104`, `105`, `138`, `101` | `flow_m3h * delta_T * 1.163`. In cooling mode the delta is inverted. Negative values are clamped to zero. |
| `PDC Mitsui Operating Mode` | register `101` | Text decoding of current mode. |
| `PDC Mitsui Mode Set` | register `1` | Text decoding of requested/set mode. |

## Decoded Status Bits

Register `128` is exposed raw as `PDC Mitsui Status Bits Raw`. The package also exposes these decoded binary sensors:

| Bit | Binary sensor | Meaning |
| --- | --- | --- |
| `1` | `PDC Mitsui Defrosting` | Defrosting active. |
| `2` | `PDC Mitsui Antifreeze` | Antifreeze/protection active. |
| `4` | `PDC Mitsui Remote On Off` | Remote on/off input state. |
| `6` | `PDC Mitsui Room Stat Heating` | Room thermostat heating request/input. |
| `7` | `PDC Mitsui Room Stat Cooling` | Room thermostat cooling request/input. |
| `8` | `PDC Mitsui Solar Input` | Solar input state. |
| `10` | `PDC Mitsui SG Normal Price` | Smart-grid normal-price input/state. |
| `11` | `PDC Mitsui EUV Free Electricity` | EUV/free-electricity input/state. |

## Decoded Output Bits

Register `129` is exposed raw as `PDC Mitsui Output Bits Raw`. The package also exposes these decoded binary sensors:

| Bit | Binary sensor | Meaning |
| --- | --- | --- |
| `3` | `PDC Mitsui Pump I` | Internal pump I output. |
| `4` | `PDC Mitsui SV1` | Valve SV1 output. |
| `5` | `PDC Mitsui Output Bit 5` | Output bit 5, diagnostic until confirmed. |
| `6` | `PDC Mitsui Pump O` | Pump O output. |
| `9` | `PDC Mitsui SV2 Doc Bit 9` | SV2 candidate/documented bit 9. Diagnostic. |
| `12` | `PDC Mitsui Alarm` | Alarm output/problem state. |
| `13` | `PDC Mitsui Run` | Run output/state. |

## Write Safety

Register `11` is the only exposed write in the package:

| Mode source | Allowed write range |
| --- | --- |
| `101 = 2` cooling | `5..25 C` |
| `101 = 3` heating | `25..60 C` |
| any other mode | write refused |
| mode unavailable | write refused |

The exposed Home Assistant number has a broad `5..60 C` UI range, but the ESPHome `write_lambda` refuses unsafe values based on the live operating mode.

For unvalidated units, disable or avoid writes until the register map and setpoint behavior are confirmed on the physical heat pump.

