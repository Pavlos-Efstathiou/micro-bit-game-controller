/*
Flash to your micro:bit on https://makecode.microbit.org/
on the JavaScript section
*/
basic.forever(function () {
    if (input.buttonIsPressed(Button.A)) {
        basic.pause(100)
        serial.writeNumber(1)
    }
    if (input.buttonIsPressed(Button.B)) {
        basic.pause(100)
        serial.writeNumber(2)
    }
    if (!(input.buttonIsPressed(Button.A)) && !(input.buttonIsPressed(Button.B))) {
        basic.pause(100)
        serial.writeNumber(0)
    }
})
