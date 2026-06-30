# Compatibility

This project is validated on one Mitsui-branded Midea-compatible air-to-water heat pump.

It may also help with other Midea platform units and rebrands sold under local brands, but compatibility must be proven register by register.

## Known Good Baseline

- Modbus RTU over RS485.
- Holding registers.
- Slave address `1`.
- Serial mode `9600 8N1`.
- Water setpoint write observed on register `11`.

## Clone Validation Checklist

1. Start with read-only sensors.
2. Confirm inlet/outlet water temperatures against the HMI.
3. Confirm outdoor temperature and operating mode.
4. Confirm fault/status bits during known states.
5. Confirm setpoint register `11` with a one-degree reversible test.
6. Only then enable regular write use.

If a clone differs, contribute a brand/model note and the differing registers without publishing private installation data.

