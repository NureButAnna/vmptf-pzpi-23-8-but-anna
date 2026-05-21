package com.example.fitnessapp

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {

        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        JsonHelper.initializeJson(this)

        val addWorkoutBtn =
            findViewById<Button>(R.id.addWorkoutBtn)

        val openListBtn =
            findViewById<Button>(R.id.openListBtn)

        addWorkoutBtn.setOnClickListener {

            val intent =
                Intent(this, AddWorkoutActivity::class.java)

            startActivity(intent)
        }

        openListBtn.setOnClickListener {

            val intent =
                Intent(this, WorkoutListActivity::class.java)

            startActivity(intent)
        }

        val workouts = JsonHelper.loadWorkouts(this)

        val caloriesText =
            findViewById<TextView>(R.id.caloriesText)

        val workoutCount =
            findViewById<TextView>(R.id.workoutCount)

        val minutesText =
            findViewById<TextView>(R.id.minutesText)

        var totalCalories = 0
        var totalMinutes = 0

        for (workout in workouts) {

            totalCalories += workout.calories
            totalMinutes += workout.duration
        }

        caloriesText.text = totalCalories.toString()
        workoutCount.text = workouts.size.toString()
        minutesText.text = totalMinutes.toString()
    }
}