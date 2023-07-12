# Small hardware to run Python

## Full Python

For full Python support including latest versions most boards running Linux as OS will work just fine.
You install Python either using package manager or build it from source or have an OS distribution that has Python prebuilt.

### Recommended for full Python

* all versions of Raspberry 2, 3, 4, Zero -
  * Raspberries are hard to find in stock for regular retail price - you end up paying extra
  * https://rpilocator.com/ - Find which stores have Raspberries in stock
* Odroid - easier to find but less community support - https://www.hardkernel.com/product/


## MicroPython

[MicroPython](https://micropython.org/) is stripped down version that implements most features of Python up to 3.5 or so. It includes partial support for such niceties as f-strings (found in 3.6)

Advantage: MicroPython runs on much devices with lower specifications.

MicroPython officially supports the Pyboard, ESP32, ESP8266, Raspberry Pi Pico, BBC micro:bit, STM32 development boards, and a few Arduino boards such as the Nano 33 BLE, Nano RP2040, Giga R1, and Portenta H7. [Src: makeuseof](https://www.makeuseof.com/microcontroller-best-language-micropython-circuitpython-arduino-c)

Advice: check MicroPython forum boards for most activity
https://forum.micropython.org/ - looks like ESP32 and ESP8266 should have most activity - thus more likely someone has had the same problem and solved it

Sadly Arduino Uno is a bit too low power for MicroPython
