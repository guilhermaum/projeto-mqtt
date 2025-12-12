package com.sistemasdistribuidos.controller;

import static com.sistemasdistribuidos.utils.FormatData.getDateTimeAsLong;

import com.sistemasdistribuidos.model.SensorData;
import com.sistemasdistribuidos.sensors.HumiditySensor;
import com.sistemasdistribuidos.sensors.Sensor;

public class HumidityController {

    private final Sensor sensor;
    private final String sensorId;

    public HumidityController(String sensorId) {
        this.sensor = new HumiditySensor();
        this.sensorId = sensorId;
    }

    public SensorData readData() {
        double value = sensor.readValue();
        return new SensorData(
            sensorId,
            "humidity",
            value,
            getDateTimeAsLong()
        );
    }
}
