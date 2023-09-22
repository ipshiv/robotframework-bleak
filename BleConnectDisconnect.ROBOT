*** Settings ***
Documentation     Connect and Disconnect to BLE device
Library    BleakLibrary.py

*** Variables ***
${DEVICE}    C7:30:C4:B6:A1:C9

*** Test Cases ***
Connect Disconnect with delay
    Connect    ${DEVICE}
    Sleep    10s
    Disconnect
    Sleep    10s
    Connect    ${DEVICE}
    Sleep    10s
    Disconnect
    Sleep    10s
 