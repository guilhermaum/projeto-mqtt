package com.sistemasdistribuidos.model;

public class SensorData {
    
    private String type;
    private double value;
    private long timestamp;
    
    public SensorData(String type, double value, long timestamp) {
        this.type = type;
        this.value = value;
        this.timestamp = timestamp;
    }

    public String getType() {
        return type;
    }

    public double getValue() {
        return value;
    }

    public long getTimestamp() {
        return timestamp;
    }

}
