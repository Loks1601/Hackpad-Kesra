This project is a compact RGB macro pad built around the Seeed Studio XIAO RP2040.
It uses diode-isolated push buttons for reliable key detection and SK6812 Mini addressable RGB LEDs for per-key lighting effects.

The design focuses on:

Electrical reliability

Minimal components

Clean schematic structure

Firmware flexibility

No displays, rotary encoders, or unnecessary peripherals are used.

🧩 Core Components Used

Only four component types are used in this project:

Microcontroller

Seeed Studio XIAO RP2040

Input Devices

Tactile push buttons (SW_Push)

Signal Isolation

Diodes (1N4148 / 1N47xx series)

Lighting

SK6812 Mini addressable RGB LEDs

🔌 Electrical Design Summary
🔹 Button Input Circuit

Each push button is connected in active-LOW configuration

Diodes are used for:

Signal isolation

Preventing ghosting

Safe multi-button usage

Buttons share a common ground

GPIO inputs use internal pull-ups from the RP2040

🔹 RGB LED Chain

SK6812 Mini LEDs are connected in a daisy-chain

Single GPIO pin controls the entire LED chain

Powered using +5V

Common ground shared with the microcontroller

Designed for:

Smooth animations

Per-key lighting

Status indicators

🔹 Power Distribution

XIAO RP2040 powered via VBUS / USB

LEDs powered from +5V rail

Common ground reference across all components

Designed to support transient LED current safely

![SCHEMATICS](https://github.com/user-attachments/assets/d224c85e-93a3-4687-b63d-fc73939201a6)



