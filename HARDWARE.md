# Small hardware to run Python

## Full Python

For full Python support including latest versions most boards running Linux as OS will work just fine.
You install Python either using package manager or build it from source or have an OS distribution that has it prebuilt.

### Recommended for full Python

* all versions of Raspberry 2, 3, 4, Zero -
  * Raspberries are hard to find in stock for regular retail price - you end up paying extra
  * https://rpilocator.com/ - Find which stores have Raspberries in stock
* Odroid - easier to find but less support


## MicroPython

MicroPython is stripped down version that implements most features of Python up to 3.5 or so. It includes partial support for such niceties as f-strings (found in 3.6)

Advantage: MicroPython runs on much devices with lower specifications.
