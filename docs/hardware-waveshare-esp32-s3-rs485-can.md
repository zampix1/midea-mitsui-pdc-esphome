# Waveshare ESP32-S3-RS485-CAN

This is the board used in the validated ESPHome port. It is convenient because the ESP32-S3, RS485 transceiver and CAN transceiver are already on the same board; this project uses the RS485 side.

Default pins used by the package:

| Signal | GPIO |
| --- | --- |
| RS485 TX | GPIO17 |
| RS485 RX | GPIO18 |
| RS485 DE/RE flow control | GPIO21 |

Serial settings:

| Setting | Value |
| --- | --- |
| Baud rate | 9600 |
| Data bits | 8 |
| Parity | none |
| Stop bits | 1 |

Override pins or serial settings in the local YAML with substitutions before including the package.

For a generic ESP32 board plus an external RS485 transceiver, the same ESPHome package can be reused by overriding `pdc_uart_tx_pin`, `pdc_uart_rx_pin` and `pdc_rs485_flow_control_pin`.
