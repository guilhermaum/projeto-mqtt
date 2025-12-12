package com.sistemasdistribuidos.controller;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

import com.sistemasdistribuidos.model.SensorData;
import com.sistemasdistribuidos.sensors.LuminositySensor;
import com.sistemasdistribuidos.sensors.Sensor;

public class LuminosityController {

    private final Sensor sensor;
    private final String sensorId;

    public LuminosityController(String sensorId) {
        this.sensor = new LuminositySensor();
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
            "luminosity",
            value,
            getDateTimeAsLong()
        );
    }
}
