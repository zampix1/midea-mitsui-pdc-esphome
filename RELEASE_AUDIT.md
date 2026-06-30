# Release Audit

## Repository Candidate

- Intended repository: `zampix1/midea-mitsui-pdc-esphome`.
- Publication status: local release candidate.
- Current recommendation: publishable after final privacy scan and a clean ESPHome compile from the example.

## Public Positioning

ESPHome Modbus RTU bridge for Midea/Mitsui heat pumps and compatible rebranded units.

This is not a Home Assistant HACS integration. It is an ESPHome package plus optional Home Assistant examples.

## Included Files

- Root metadata: `README.md`, `LICENSE`, `CHANGELOG.md`, `SECURITY.md`, `CONTRIBUTING.md`.
- ESPHome package: `esphome/packages/midea_mitsui_waveshare_esp32s3_rs485_can.yaml`.
- ESPHome examples: `esphome/examples/pdc-mitsui-esp32.example.yaml`, `secrets.yaml.example`.
- Home Assistant examples: package and dashboard YAML.
- Docs: compatibility, hardware, Home Assistant and Modbus register map.
- Bilingual project explanation and materials/migration guide.
- Static privacy check: `tests/static_privacy_check.py`.

## Privacy Rules

No real Wi-Fi credential, Home Assistant token, LAN IP, MAC address, local domain, serial number, private path, Raspberry Pi password or raw installation log should be embedded.

Network and secret values belong only in private local ESPHome YAML/secrets.

## Hardware Validation

- Tested board: Waveshare ESP32-S3-RS485-CAN.
- Tested serial path: RS485, `9600 8N1`, slave `1`.
- Tested write path: register `11` water setpoint with controlled reversible changes.

## Residual Work Before Push

- Run static privacy check.
- Compile the example with local secrets.
- Decide whether optional Home Assistant examples should stay in the first public release or move to `examples/`.
- Add screenshots only if they are fully anonymized.
