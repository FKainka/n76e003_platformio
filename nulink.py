#
# python3 script for uploading firmware to Nuvoton MCUs via NuLink programmer using their windows apps.
# arad.rgb@gmail.com 01/05/2021
#
import os.path
import warnings

Import('env')

env.Append(LINKFLAGS=["--model-medium"])

NULINK_CLI_EXE = '"%PROGRAMFILES(X86)%\\Nuvoton Tools\\NuLink Command Tool\\NuLink_8051OT.exe"'
NULINK_NOT_FOUND_MSG = '''
Please install %s from:
    https://www.nuvoton.com/tool-and-software/software-development-tool/programmer
'''

def on_upload(source, target, env):
    firmware_path = os.path.abspath(str(source[0]))
    # erase APROM and write firmware to APROM
    try:
        env.Execute(f'{NULINK_CLI_EXE} -e APROM')
        env.Execute(f'{NULINK_CLI_EXE} -w APROM "{firmware_path}"')
        # env.Execute(f'{NULINK_CLI_EXE} -disconnect') # doesn't disconnect....
    except:
        warnings.warn(NULINK_NOT_FOUND_MSG % 'NuLinkCLI')
        exit(2)
    # warn user to manually disconnect by pressing the button on the NuLink because -disconnect doesn't work..
    __import__('time').sleep(0.1)
    warnings.warn('''
        Press NuLink button to release (disconnect) mcu if needed!''')


env.Replace(UPLOADCMD=on_upload)
