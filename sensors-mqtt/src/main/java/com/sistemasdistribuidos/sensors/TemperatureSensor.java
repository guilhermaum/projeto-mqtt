package com.sistemasdistribuidos.sensors;

public class TemperatureSensor implements Sensor {
    
    @Override
    public double readValue() {
        return 15 + (Math.random() * 20); 
    }
}
