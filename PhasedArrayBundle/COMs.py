
import serial

from serial.tools import list_ports
print([p.device for p in list_ports.comports()])
# Pick the COMxx that just appeared, e.g. "COM16"
#ser = serial.Serial("COM15", 115200, timeout=1)
