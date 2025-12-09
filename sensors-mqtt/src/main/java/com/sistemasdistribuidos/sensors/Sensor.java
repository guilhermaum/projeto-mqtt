package com.sistemasdistribuidos.sensors;

import com.sistemasdistribuidos.model.SensorData;

public interface Sensor {
    SensorData read();
}
