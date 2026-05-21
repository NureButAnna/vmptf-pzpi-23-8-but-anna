package com.example.fitnessapp

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

class WorkoutAdapter(
    private val workoutList: List<Workout>
) : RecyclerView.Adapter<WorkoutAdapter.WorkoutViewHolder>() {

    class WorkoutViewHolder(view: View) : RecyclerView.ViewHolder(view) {

        val workoutName: TextView =
            view.findViewById(R.id.workoutName)

        val workoutCalories: TextView =
            view.findViewById(R.id.workoutCalories)

        val workoutInfo: TextView =
            view.findViewById(R.id.workoutInfo)
    }

    override fun onCreateViewHolder(
        parent: ViewGroup,
        viewType: Int
    ): WorkoutViewHolder {

        val view = LayoutInflater.from(parent.context)
            .inflate(R.layout.workout_item, parent, false)

        return WorkoutViewHolder(view)
    }

    override fun onBindViewHolder(
        holder: WorkoutViewHolder,
        position: Int
    ) {

        val workout = workoutList[position]

        holder.workoutName.text = workout.name

        holder.workoutCalories.text =
            "${workout.calories} kcal"

        holder.workoutInfo.text =
            "${workout.duration} min • ${workout.date}"
    }

    override fun getItemCount(): Int {
        return workoutList.size
    }
}