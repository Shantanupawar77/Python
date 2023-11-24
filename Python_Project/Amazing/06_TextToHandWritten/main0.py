import pywhatkit as pw
text="""Features of the Arduino UNO:
• Microcontroller: ATmega328.
• Operating Voltage: 5V. (% V and 3.3 Volts available on 
board.
• Input Voltage (recommended): 7-12V.
• Input Voltage (limits): 6-20V.
• Digital I/O Pins: 14 (of which 6 provide PWM output)
• Analog Input Pins: 6.
• DC Current per I/O Pin: 40 mA.
• DC Current for 3.3V Pin: 50 mA.

"""
pw.text_to_handwriting(text,"demo3.png",[0,0,138])
print("Done")