# This is a simple script
from datetime import *


# Press F5 to execute it

# Log
def LogMessage(message: str):
    with open(r"D:\AtidAutomation\FullStackFinalProject\TextLogs\ExecutionLog.txt", "a") as logFile:
        logFile.write(f"\n{datetime.now()} " + message)


def print_hi(message):
    print(f'Hi, \n{message}')


greeting = "This is a greeting message,\nWellcome to my final Full Stack Automation project,\n" \
           "this project is a complete " \
           "Automation infrastructure for sanity tests,\ne2e flows and much more see the ReadMe file" \
           " for instructions,\nuse requirements file to install appropriate versions.\n" \
           "This infrastructure can be run separately for every platform, just execute every test case"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(message=greeting)
    LogMessage(message="Hello from main" + "\n" + greeting)
