package com.example.fitnessapp

import android.content.Intent
import android.os.Bundle
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class WorkoutListActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {

        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_workout_list)

        val backHome =
            findViewById<TextView>(R.id.backHome)

        backHome.setOnClickListener {

            val intent =
                Intent(this, MainActivity::class.java)

            startActivity(intent)
        }

        val recycler =
            findViewById<RecyclerView>(R.id.workoutRecycler)

        recycler.layoutManager =
            LinearLayoutManager(this)

        val workouts = JsonHelper.loadWorkouts(this)

        recycler.adapter =
            WorkoutAdapter(workouts)
    }
}