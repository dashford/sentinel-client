import logging

from blinker import signal
from ds18b20 import DS18B20 as Sensor


class DS18B20:

    def __init__(self, address):
        logging.info('Initialising DS18B20 sensor with address {}'.format(address))
        self._address = address
        self._sensor = Sensor(sensor_id=address)

    def get_temperature(self):
        """
        Return measured temperature from the sensor.
        :return:
        """
        logging.debug('Measuring temperature')
        temperature = self._sensor.get_temperature()
        logging.info('Broadcasting temperature: {}'.format(temperature))

        temperature_signal = signal('temperature')
        temperature_signal.send(
            self,
            temperature=temperature,
            address=self._address
        )


