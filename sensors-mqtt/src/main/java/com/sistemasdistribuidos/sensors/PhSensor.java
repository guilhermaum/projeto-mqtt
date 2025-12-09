package com.sistemasdistribuidos.sensors;

public class PhSensor implements Sensor {

    @Override
    public double readValue() {
        return Math.random() * 14;
    }
    
}
