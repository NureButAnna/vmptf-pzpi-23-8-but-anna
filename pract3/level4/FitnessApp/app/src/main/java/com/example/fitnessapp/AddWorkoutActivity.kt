package com.example.fitnessapp

import android.app.DatePickerDialog
import java.util.Calendar
import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity

class AddWorkoutActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {

        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_add_workout)

        val backHome =
            findViewById<TextView>(R.id.backHome)

        backHome.setOnClickListener {

            val intent =
                Intent(this, MainActivity::class.java)

            startActivity(intent)
        }

        val nameInput =
            findViewById<EditText>(R.id.nameInput)

        val typeInput =
            findViewById<EditText>(R.id.typeInput)

        val durationInput =
            findViewById<EditText>(R.id.durationInput)

        val caloriesInput =
            findViewById<EditText>(R.id.caloriesInput)

        val dateInput =
            findViewById<EditText>(R.id.dateInput)

        val saveBtn =
            findViewById<Button>(R.id.saveBtn)

        // Вибір дати
        dateInput.setOnClickListener {

            val calendar = Calendar.getInstance()

            val year = calendar.get(Calendar.YEAR)
            val month = calendar.get(Calendar.MONTH)
            val day = calendar.get(Calendar.DAY_OF_MONTH)

            val datePickerDialog = DatePickerDialog(
                this,
                { _, selectedYear, selectedMonth, selectedDay ->

                    val date =
                        "$selectedDay.${selectedMonth + 1}.$selectedYear"

                    dateInput.setText(date)
                },
                year,
                month,
                day
            )

            datePickerDialog.show()
        }

        saveBtn.setOnClickListener {

            val name =
                nameInput.text.toString().trim()

            val type =
                typeInput.text.toString().trim()

            val durationText =
                durationInput.text.toString().trim()

            val caloriesText =
                caloriesInput.text.toString().trim()

            val date =
                dateInput.text.toString().trim()

            if (name.isEmpty()) {

                nameInput.error = "Введіть назву активності"
                return@setOnClickListener
            }

            if (type.isEmpty()) {

                typeInput.error = "Введіть тип активності"
                return@setOnClickListener
            }

            if (durationText.isEmpty()) {

                durationInput.error = "Введіть тривалість"
                return@setOnClickListener
            }

            val duration = durationText.toIntOrNull()

            if (duration == null || duration <= 0) {

                durationInput.error =
                    "Тривалість має бути позитивним числом"

                return@setOnClickListener
            }

            if (caloriesText.isEmpty()) {

                caloriesInput.error = "Введіть калорії"
                return@setOnClickListener
            }

            val calories = caloriesText.toIntOrNull()

            if (calories == null || calories <= 0) {

                caloriesInput.error =
                    "Значення калорій має бути додатнім числом"

                return@setOnClickListener
            }

            if (date.isEmpty()) {

                dateInput.error = "Оберіть дату"
                return@setOnClickListener
            }

            val workouts =
                JsonHelper.loadWorkouts(this)

            val workout = Workout(

                id = workouts.size + 1,

                name = name,

                type = type,

                duration = duration,

                calories = calories,

                date = date
            )

            JsonHelper.addWorkout(this, workout)

            Toast.makeText(
                this,
                "Workout saved",
                Toast.LENGTH_SHORT
            ).show()

            finish()
        }
    }
}