# Introduction

This is a fork from: https://github.com/arduino12/n76e003_platformio
It allows to compile and upload to a Nuvoton N76E003 or a MS51FB9AE. Many other Nuvoton controllers may be compatible.

## Changes

This is a simplified version. The python script now only support the NuLink Command Line Tool.
The script now uses the the NuLink_8051OT.exe instead of the NuLink.exe. An issues with long paths including spaces has been resolved. A line has been added that allows to use the --model-medium build flag in the pio-file (base on https://community.platformio.org/t/platformio-8051-model-medium-linker-err/18099/4).

# Getting Started

- Download and install [Visual code](https://code.visualstudio.com/download)
- Install [PlatformIO](https://platformio.org/platformio-ide) extension to Visual code.
- Download and install NuLink CLI tool (Nu-Link_Command_Tool_VXXX.zip) from [Nuvoton tools](https://www.nuvoton.com/tool-and-software/software-development-tool/programmer).
- Clone or download this [repo](https://github.com/fkainka/n76e003_platformio), open it with VSCode and upload it via PlatformIO-upload command.

![](/vscode.png)

## Testet Hardware

I used a Nu-Link-Me V3.0 programmer (simliar to https://www.techdesign.com/market/nuvoton/product-detail/ntc000108/nutiny-n76e003) to programm a MS51FB9AE controller.

## What's happeing

PlatformIO will compile your source-code with the SDCC-Compiler (if possible) to the .pio\build\n76e003\firmware.hex file.
The main magic is happening in the nulink.py python script, which will be called due to the extra_script option in the platformio.ini.
The script will try to call the CLI-Tool-Exe-File to first erase the APROM and upload the compiled hex to the APROM afterwards.
