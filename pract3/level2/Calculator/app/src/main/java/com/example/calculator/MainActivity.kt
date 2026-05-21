package com.example.calculator

import android.os.Bundle
import android.view.View
import android.widget.Button
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import com.example.calculator.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        enableEdgeToEdge()

        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        ViewCompat.setOnApplyWindowInsetsListener(binding.main) { v, insets ->

            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())

            v.setPadding(
                systemBars.left,
                systemBars.top,
                systemBars.right,
                systemBars.bottom
            )

            insets
        }
    }

    fun numberAction(view: View) {

        if (view is Button) {
            binding.workingsTV.append(view.text)
        }
    }

    fun operationAction(view: View) {

        if (view is Button) {
            binding.workingsTV.append(view.text)
        }
    }

    fun allClearAction(view: View) {

        binding.workingsTV.text = ""
        binding.resultsTV.text = ""
    }

    fun backSpaceAction(view: View) {

        val length = binding.workingsTV.length()

        if (length > 0) {

            binding.workingsTV.text =
                binding.workingsTV.text.subSequence(0, length - 1)
        }
    }

    fun equalsAction(view: View) {

        try {

            val expression = binding.workingsTV.text.toString()

            var operator = ' '

            when {
                expression.contains("+") -> operator = '+'
                expression.contains("-") -> operator = '-'
                expression.contains("x") -> operator = 'x'
                expression.contains("÷") -> operator = '÷'
                expression.contains("%") -> operator = '%'
            }

            val parts = expression.split(operator)

            val number1 = parts[0].toDouble()
            val number2 = parts[1].toDouble()

            val result = when (operator) {

                '+' -> number1 + number2
                '-' -> number1 - number2
                'x' -> number1 * number2
                '÷' -> number1 / number2
                '%' -> number1 % number2

                else -> 0
            }

            binding.resultsTV.text = result.toString()

        } catch (e: Exception) {

            binding.resultsTV.text = "Error"
        }
    }
}