package com.sistemasdistribuidos.controller;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

import com.sistemasdistribuidos.model.SensorData;
import com.sistemasdistribuidos.sensors.Sensor;
import com.sistemasdistribuidos.sensors.TemperatureSensor;

public class TemperatureController {

    private final Sensor sensor;
    private final String sensorId;

    public TemperatureController(String sensorId) {
        this.sensor = new TemperatureSensor();
        this.sensorId = sensorId;
    }

    public static long getDateTimeAsLong() {
    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("ddMMyyyyHHmm");
    String formatted = LocalDateTime.now().format(formatter);
    return Long.parseLong(formatted);
    }

    public SensorData readData() {
        double value = sensor.readValue();
        return new SensorData(
            sensorId,
            "temperature",
            value,
            getDateTimeAsLong()
        );
    }
}
