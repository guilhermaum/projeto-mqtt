package com.sistemasdistribuidos.utils;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class FormatData {
    public static long getDateTimeAsLong() {
    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("ddMMyyyyHHmm");
    String formatted = LocalDateTime.now().format(formatter);
    return Long.parseLong(formatted);
    }
}
