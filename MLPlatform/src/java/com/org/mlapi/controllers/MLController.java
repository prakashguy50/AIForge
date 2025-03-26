package com.org.mlapi.controllers;

import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/ml")
public class MLController {

    @GetMapping("/status")
    public String getStatus() {
        return "ML Backend API is running!";
    }
}
