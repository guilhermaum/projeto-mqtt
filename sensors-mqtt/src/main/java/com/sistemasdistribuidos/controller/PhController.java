package com.sistemasdistribuidos.controller;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

import com.sistemasdistribuidos.model.SensorData;
import com.sistemasdistribuidos.sensors.PhSensor;
import com.sistemasdistribuidos.sensors.Sensor;

public class PhController {

    private final Sensor sensor;
    private final String sensorId;

    public PhController(String sensorId) {
        this.sensor = new PhSensor();
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
            "ph",
            value,
            getDateTimeAsLong()
        );
    }
}
