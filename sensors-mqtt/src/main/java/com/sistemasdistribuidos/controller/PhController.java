package com.sistemasdistribuidos.controller;

import com.sistemasdistribuidos.model.SensorData;
import com.sistemasdistribuidos.sensors.Sensor;

public class PhController {

    private final Sensor sensor;
    private final String sensorId;

    public PhController(Sensor sensor, String sensorId) {
        this.sensor = sensor;
        this.sensorId = sensorId;
    }

    public SensorData readData() {
        double value = sensor.readValue();
        return new SensorData(
            sensorId,
            "ph",
            value,
            System.currentTimeMillis()
        );
    }
}
