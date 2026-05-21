package com.example.fitnessapp

import android.content.Context
import org.json.JSONArray
import org.json.JSONObject
import java.io.File

object JsonHelper {

    private const val FILE_NAME = "workouts.json"

    fun initializeJson(context: Context) {

        val file = File(context.filesDir, FILE_NAME)

        if (!file.exists()) {

            val inputStream =
                context.resources.openRawResource(R.raw.workouts)

            val jsonText =
                inputStream.bufferedReader().use { it.readText() }

            file.writeText(jsonText)
        }
    }

    fun loadWorkouts(context: Context): MutableList<Workout> {

        val workoutList = mutableListOf<Workout>()

        val file = File(context.filesDir, FILE_NAME)

        val jsonText = file.readText()

        val jsonArray = JSONArray(jsonText)

        for (i in 0 until jsonArray.length()) {

            val obj = jsonArray.getJSONObject(i)

            val workout = Workout(
                obj.getInt("id"),
                obj.getString("name"),
                obj.getString("type"),
                obj.getInt("duration"),
                obj.getInt("calories"),
                obj.getString("date")
            )

            workoutList.add(workout)
        }

        return workoutList
    }

    fun addWorkout(
        context: Context,
        workout: Workout
    ) {

        val file = File(context.filesDir, FILE_NAME)

        val jsonText = file.readText()

        val jsonArray = JSONArray(jsonText)

        val jsonObject = JSONObject()

        jsonObject.put("id", workout.id)
        jsonObject.put("name", workout.name)
        jsonObject.put("type", workout.type)
        jsonObject.put("duration", workout.duration)
        jsonObject.put("calories", workout.calories)
        jsonObject.put("date", workout.date)

        jsonArray.put(jsonObject)

        file.writeText(jsonArray.toString())
    }
}