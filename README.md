# Computer Vs Computer Bar Game

## Demo

https://github.com/aditya23043/CvC_BarGame/assets/66688960/4dffd926-741e-4ef4-bf9b-3dce2b955c13


## Dependencies
- adafruit-ampy
- minicom (optional)

```bash
paru -S adafruit-ampy
paru -S minicom
```

## Installation
```bash
git clone https://github.com/aditya23043/CvC_BarGame
```

## How to run?
```bash
cd CvC_BarGame
ampy --port /dev/ttyACM0 run main.py
```
- OR
```bash
cd CvC_BarGame
minicom --device /dev/ttyACM0 --baudrate 115200
> import main
```

## How to make it such that my pico runs this game when powered everytime?
```bash
cd CvC_BarGame
ampy --port /dev/ttyACM0 put main.py
ampy --port /dev/ttyACM0 put sh1106.py
ampy --port /dev/ttyACM0 put ssd1306.py
```
- Now unplug your micro-controller and plug it back in
