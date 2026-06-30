# Materials and Migration / Materiali e Migrazione

## Italiano

Questo progetto nasce come porting pratico di un sistema che funzionava gia su Raspberry Pi 4B. Il Raspberry leggeva la pompa di calore via Modbus RTU su RS485, pubblicava uno stato HTTP per Home Assistant e salvava log locali. Funzionava, ma richiedeva un sistema Linux sempre acceso, un adattatore USB-RS485, servizi systemd, script Python e manutenzione separata rispetto a Home Assistant.

La versione ESPHome usa invece un ESP32-S3 con RS485 integrata. Il dispositivo parla direttamente con la PDC via Modbus RTU e Home Assistant vede sensori, binary sensor e controlli tramite l'integrazione ESPHome. L'obiettivo non e solo "fare la stessa cosa su un microcontrollore", ma ridurre i pezzi intermedi: niente exporter HTTP, niente servizio logger obbligatorio, meno cablaggio USB e configurazione piu vicina a Home Assistant.

### Materiali usati nella configurazione validata

| Materiale | Ruolo |
| --- | --- |
| Waveshare ESP32-S3-RS485-CAN | Nodo ESPHome con RS485 integrata |
| Cavo USB-C | Alimentazione, flash iniziale e debug seriale |
| Collegamento RS485 A/B | Bus Modbus verso morsetti HMI/controller della PDC |
| Home Assistant | Raccolta sensori, automazioni e dashboard |
| ESPHome | Firmware, OTA, API nativa Home Assistant |
| Box o supporto DIN opzionale | Installazione ordinata vicino alla PDC |

### Setup precedente su Raspberry Pi 4B

| Componente | Ruolo precedente |
| --- | --- |
| Raspberry Pi 4B | Host Linux sempre acceso |
| Adattatore USB/FTDI RS485 | Interfaccia seriale verso la PDC |
| Exporter Python HTTP | Lettura Modbus e pubblicazione JSON |
| Logger locale CSV/JSONL | Storico indipendente da Home Assistant |
| Home Assistant REST/template | Sensori e comandi basati sull'exporter |

### Cosa cambia con ESPHome

- Le letture Modbus diventano entita ESPHome native.
- Il setpoint acqua e controllato da una entity `number` con limiti per modalita.
- Gli aggiornamenti OTA passano da ESPHome.
- Il Raspberry non e piu necessario per il bridge Modbus.
- Eventuali log storici di lungo periodo vanno gestiti in Home Assistant, database esterni o servizi separati.

### Nota sui cloni e rebrand

Molte PDC aria-acqua vendute con marchi locali derivano da piattaforme Midea o usano mappe Modbus molto simili. Questo progetto puo quindi essere utile anche fuori dal marchio Mitsui, ma non va copiato alla cieca.

Procedura prudente:

1. Collegare RS485 e partire solo con letture.
2. Confrontare temperature, modalita, setpoint e stati con HMI/controller.
3. Verificare che il registro setpoint sia davvero quello atteso.
4. Fare una prova reversibile di un solo grado.
5. Abilitare l'uso normale dei comandi solo dopo conferma.

## English

This project started as a practical port of a system that already worked on a Raspberry Pi 4B. The Raspberry Pi read the heat pump over Modbus RTU on RS485, exposed an HTTP state endpoint for Home Assistant and wrote local logs. It worked, but it required an always-on Linux host, a USB-RS485 adapter, systemd services, Python scripts and maintenance outside ESPHome.

The ESPHome version uses an ESP32-S3 with built-in RS485. The device talks directly to the heat pump over Modbus RTU, while Home Assistant receives sensors, binary sensors and controls through the native ESPHome integration. The goal is not just to run the same logic on a microcontroller, but to remove intermediate parts: no HTTP exporter, no mandatory local logger service, less USB wiring and a configuration model closer to Home Assistant.

### Materials used in the validated setup

| Material | Role |
| --- | --- |
| Waveshare ESP32-S3-RS485-CAN | ESPHome node with integrated RS485 |
| USB-C cable | Power, initial flashing and serial debugging |
| RS485 A/B wiring | Modbus bus to the heat pump HMI/controller terminals |
| Home Assistant | Sensors, automations and dashboard |
| ESPHome | Firmware, OTA and native Home Assistant API |
| Optional enclosure or DIN rail support | Cleaner installation near the heat pump |

### Previous Raspberry Pi 4B setup

| Component | Previous role |
| --- | --- |
| Raspberry Pi 4B | Always-on Linux host |
| USB/FTDI RS485 adapter | Serial interface to the heat pump |
| Python HTTP exporter | Modbus polling and JSON publication |
| Local CSV/JSONL logger | History independent from Home Assistant |
| Home Assistant REST/template entities | Sensors and commands based on the exporter |

### What changes with ESPHome

- Modbus readings become native ESPHome entities.
- Water setpoint is controlled through a guarded `number` entity.
- OTA updates are handled by ESPHome.
- The Raspberry Pi is no longer required for the Modbus bridge.
- Long-term historical logging can be handled by Home Assistant, external databases or a separate optional service.

### Clone and rebrand note

Many air-to-water heat pumps sold under local brands are derived from Midea platforms or use similar Modbus maps. This project can therefore be useful beyond Mitsui, but it should not be copied blindly.

Safe validation flow:

1. Wire RS485 and start with read-only values.
2. Compare temperatures, mode, setpoint and status with the HMI/controller.
3. Confirm that the setpoint register is really the expected one.
4. Run a reversible one-degree test.
5. Enable normal command usage only after confirmation.

