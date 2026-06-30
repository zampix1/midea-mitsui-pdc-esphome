# Midea Mitsui PDC ESPHome

ESPHome Modbus RTU bridge for Midea/Mitsui heat pumps and compatible rebranded units.

This repository is an ESPHome-first port of a Raspberry Pi Modbus exporter. It targets the Waveshare ESP32-S3-RS485-CAN board and exposes the heat pump registers directly to Home Assistant through ESPHome.

## Description / Descrizione

**Italiano**

Questo progetto porta su ESPHome il monitoraggio e il controllo Modbus RTU di una pompa di calore Mitsui/Midea compatibile. La prima versione girava su Raspberry Pi 4B con adattatore USB/FTDI RS485, un exporter HTTP in Python e un logger locale. La versione ESPHome sposta il lavoro direttamente su un ESP32-S3 Waveshare con RS485 integrata, riducendo componenti, servizi Linux e punti di manutenzione.

Il progetto e stato validato su una PDC Mitsui basata su piattaforma Midea, ma puo essere un buon punto di partenza per molti cloni e rebrand Midea venduti con altri marchi, anche italiani. La regola e semplice: prima letture read-only, poi confronto con HMI/controller, infine eventuali scritture solo dopo conferma della mappa registri.

**English**

This project ports Modbus RTU monitoring and controlled writes for a Mitsui/Midea-compatible heat pump to ESPHome. The first working version ran on a Raspberry Pi 4B with a USB/FTDI RS485 adapter, a Python HTTP exporter and a local logger. The ESPHome version moves the bridge directly onto a Waveshare ESP32-S3 board with built-in RS485, reducing Linux services, moving parts and maintenance overhead.

It has been validated on one Mitsui-branded Midea-platform heat pump, but it may also be useful for many Midea clones and rebranded units sold under other local brands. Treat every clone as untrusted at first: start read-only, compare values with the wired HMI/controller, then enable writes only after the register map is confirmed.

## Status

- Tested on one Mitsui-branded Midea-compatible heat pump.
- Hardware target tested: Waveshare ESP32-S3-RS485-CAN.
- Transport: Modbus RTU over RS485, holding registers, slave address `1`, `9600 8N1`.
- Other Midea-based rebrands may work, but their register map must be validated before enabling writes.

## Materials Used / Materiali Usati

Validated setup:

- Waveshare ESP32-S3-RS485-CAN board;
- USB-C power/programming cable;
- RS485 A/B wiring from the heat pump HMI/controller Modbus terminals;
- Home Assistant with ESPHome;
- optional enclosure or DIN rail mounting accessories.

Previous Raspberry Pi setup:

- Raspberry Pi 4B;
- USB/FTDI RS485 adapter;
- Python Modbus HTTP exporter;
- local CSV/JSONL logger;
- Home Assistant REST sensors and templates.

More details: [materials and migration guide](docs/materials-and-migration.md).

## Why This May Fit Other Rebrands

Many air-to-water heat pumps sold under local brands are Midea platform variants or close rebrands. The Modbus map used here may therefore match, partially match, or be a useful starting point for other units.

Do not assume write safety on an unvalidated clone. Start with read-only sensors, compare live values with the wired controller/HMI, then enable controlled writes only after register `11` setpoint semantics are confirmed.

## Quick Start

Create a local ESPHome YAML in your Home Assistant ESPHome folder:

```yaml
substitutions:
  devicename: pdc-mitsui-esp32
  friendly_name: "PDC Mitsui ESP32"
  wifi_domain: .example.lan

packages:
  pdc_mitsui:
    url: https://github.com/zampix1/midea-mitsui-pdc-esphome
    ref: main
    file: esphome/packages/midea_mitsui_waveshare_esp32s3_rs485_can.yaml

wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password
  domain: ${wifi_domain}
  power_save_mode: none
  ap:
    ssid: "${devicename}-setup"
    password: !secret fallback_ap_password
```

Copy `esphome/examples/secrets.yaml.example` to your ESPHome `secrets.yaml` and fill local values.

## Package

Main package:

```text
esphome/packages/midea_mitsui_waveshare_esp32s3_rs485_can.yaml
```

The package contains:

- ESP32-S3 board setup for Waveshare ESP32-S3-RS485-CAN;
- UART/RS485 pins with substitutions;
- Modbus controller settings;
- read sensors for runtime, diagnostics and configuration registers;
- controlled setpoint write entity for register `11`;
- Home Assistant friendly binary sensors and template sensors.

Network settings are intentionally not included in the package. Keep Wi-Fi, local domain, static IPs and passwords in your private local YAML/secrets.

## Home Assistant

Optional Home Assistant examples are included:

```text
home-assistant/packages/pdc_mitsui.yaml
home-assistant/dashboards/pdc_mitsui_dashboard.yaml
```

They are provided as a migration aid for users moving away from a Raspberry Pi exporter. Review entity IDs before installing.

## Safety

The read path is low risk. Writes are intentionally limited to water setpoint register `11` and guarded by mode-specific ranges in ESPHome.

Before enabling writes on a different brand/rebrand:

1. Confirm Modbus slave address, baud rate and parity.
2. Confirm read registers against the HMI.
3. Confirm setpoint register behavior with a reversible one-degree test.
4. Watch the physical unit while testing.

## Privacy

Do not publish your real Wi-Fi credentials, Home Assistant token, LAN IPs, MAC addresses, local domain, controller screenshots with serial numbers, private paths, or raw logs from your installation.

The repository contains examples and placeholders only.
