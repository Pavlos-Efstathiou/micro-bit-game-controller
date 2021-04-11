/*
Flash to the micro:bit on https://makecode.microbit.org/
on the JavaScript section
*/
basic.forever(function () {
    if (input.buttonIsPressed(Button.A))
        serial.writeNumber(1)
    if (input.buttonIsPressed(Button.B))
        serial.writeNumber(2)
    if (!(input.buttonIsPressed(Button.A)) && !(input.buttonIsPressed(Button.B)))
        serial.writeNumber(0)
})