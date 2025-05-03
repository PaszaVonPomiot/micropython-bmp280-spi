from machine import Pin


class BaseSpiGpio:
    """Pseudo-interface for 4-wire SPI GPIO pins."""

    SCK: Pin  
    MOSI: Pin
    MISO: Pin
    CS: Pin

