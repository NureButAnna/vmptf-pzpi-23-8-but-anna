package com.example.fitnessapp

data class Workout(
    val id: Int,
    val name: String,
    val type: String,
    val duration: Int,
    val calories: Int,
    val date: String
)
