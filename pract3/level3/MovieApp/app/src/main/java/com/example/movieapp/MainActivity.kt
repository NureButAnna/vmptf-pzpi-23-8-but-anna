package com.example.movieapp

import android.graphics.Color
import android.os.Bundle
import android.view.LayoutInflater
import android.widget.LinearLayout
import android.widget.TextView
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import org.json.JSONArray

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)

        val container = findViewById<LinearLayout>(R.id.movieContainer)

        val inputStream = resources.openRawResource(R.raw.movies)
        val jsonText = inputStream.bufferedReader().use { it.readText() }

        val jsonArray = JSONArray(jsonText)

        for (i in 0 until jsonArray.length()) {

            val movie = jsonArray.getJSONObject(i)

            val movieView = LayoutInflater.from(this)
                .inflate(R.layout.movie_card, container, false)

            val movieName = movieView.findViewById<TextView>(R.id.movieName)
            val movieRate = movieView.findViewById<TextView>(R.id.movieRate)
            val movieGenre = movieView.findViewById<TextView>(R.id.movieGenre)

            val rating = movie.getDouble("rating")

            movieName.text = movie.getString("name")
            movieGenre.text = movie.getString("genre")
            movieRate.text = rating.toString()

            when {
                rating < 5 -> {
                    movieRate.setTextColor(Color.RED)
                }

                rating < 6.5 -> {
                    movieRate.setTextColor(Color.parseColor("#FF9800"))
                }

                rating < 8 -> {
                    movieRate.setTextColor(Color.parseColor("#FFD600"))
                }

                else -> {
                    movieRate.setTextColor(Color.parseColor("#4CAF50"))
                }
            }

            container.addView(movieView)
        }
    }
}