package com.example.blogapplication

import android.content.Intent
import android.os.Bundle
import android.widget.AdapterView
import android.widget.ArrayAdapter
import android.widget.EditText
import android.widget.Spinner
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.blogapplication.data.PostStorage
import com.example.blogapplication.models.Post
import com.google.android.material.floatingactionbutton.FloatingActionButton
import java.util.UUID

class MainActivity : AppCompatActivity() {

    private lateinit var recyclerView: RecyclerView
    private lateinit var adapter: PostAdapter

    private lateinit var posts: MutableList<Post>
    private lateinit var filteredPosts: MutableList<Post>

    private lateinit var spinner: Spinner
    private lateinit var categories: Array<String>

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        recyclerView = findViewById(R.id.postsRecyclerView)
        spinner = findViewById(R.id.spCategory)

        posts = PostStorage.loadPosts(this)
        filteredPosts = posts.toMutableList()

        setupSpinner()
        setupRecyclerView()

        findViewById<FloatingActionButton>(R.id.btnAddPost)
            .setOnClickListener {
                showAddDialog()
            }
    }

    private fun setupSpinner() {
        categories = resources.getStringArray(R.array.categories)

        val adapterSpinner = ArrayAdapter(
            this,
            android.R.layout.simple_spinner_item,
            categories
        )

        adapterSpinner.setDropDownViewResource(
            android.R.layout.simple_spinner_dropdown_item
        )

        spinner.adapter = adapterSpinner

        spinner.onItemSelectedListener = object : AdapterView.OnItemSelectedListener {
            override fun onItemSelected(
                parent: AdapterView<*>,
                view: android.view.View?,
                position: Int,
                id: Long
            ) {
                filterPosts(categories[position])
            }

            override fun onNothingSelected(parent: AdapterView<*>) {}
        }
    }

    private fun filterPosts(category: String) {
        filteredPosts = if (category == "All") {
            posts.toMutableList()
        } else {
            posts.filter { it.category == category }.toMutableList()
        }

        adapter.updateList(filteredPosts)
    }

    private fun setupRecyclerView() {
        adapter = PostAdapter(
            filteredPosts,

            onClick = { post ->

                val intent = Intent(this, PostActivity::class.java)
                intent.putExtra("post_id", post.id)
                startActivity(intent)
            },

            onDelete = { post ->

                posts.removeIf { it.id == post.id }
                filteredPosts.removeIf { it.id == post.id }

                PostStorage.savePosts(this, posts)
                adapter.updateList(filteredPosts)
            },

            onEdit = { post ->
                showEditDialog(post)
            }
        )

        recyclerView.layoutManager = LinearLayoutManager(this)
        recyclerView.adapter = adapter
    }

    private fun showAddDialog() {

        val view = layoutInflater.inflate(R.layout.dialog_add_post, null)

        val title = view.findViewById<EditText>(R.id.etTitle)
        val content = view.findViewById<EditText>(R.id.etContent)
        val categorySpinner = view.findViewById<Spinner>(R.id.spCategory)

        val adapterSpinner = ArrayAdapter(
            this,
            android.R.layout.simple_spinner_item,
            categories
        )

        categorySpinner.adapter = adapterSpinner

        AlertDialog.Builder(this)
            .setTitle("New Post")
            .setView(view)
            .setPositiveButton("Add") { _, _ ->

                val post = Post(
                    id = UUID.randomUUID().toString(),
                    title = title.text.toString(),
                    content = content.text.toString(),
                    category = categorySpinner.selectedItem.toString(),
                    date = System.currentTimeMillis().toString(),
                    comments = mutableListOf()
                )

                posts.add(post)
                PostStorage.savePosts(this, posts)

                filterPosts(spinner.selectedItem.toString())
            }
            .setNegativeButton("Cancel", null)
            .show()
    }

    private fun showEditDialog(post: Post) {

        val view = layoutInflater.inflate(R.layout.dialog_add_post, null)

        val title = view.findViewById<EditText>(R.id.etTitle)
        val content = view.findViewById<EditText>(R.id.etContent)
        val categorySpinner = view.findViewById<Spinner>(R.id.spCategory)

        title.setText(post.title)
        content.setText(post.content)

        val adapterSpinner = ArrayAdapter(
            this,
            android.R.layout.simple_spinner_item,
            categories
        )

        adapterSpinner.setDropDownViewResource(
            android.R.layout.simple_spinner_dropdown_item
        )

        categorySpinner.adapter = adapterSpinner

        val categoryIndex = categories.indexOf(post.category)
        if (categoryIndex >= 0) {
            categorySpinner.setSelection(categoryIndex)
        }

        AlertDialog.Builder(this)
            .setTitle("Edit Post")
            .setView(view)
            .setPositiveButton("Save") { _, _ ->

                post.title = title.text.toString()
                post.content = content.text.toString()
                post.category = categorySpinner.selectedItem.toString()

                PostStorage.savePosts(this, posts)
                adapter.notifyDataSetChanged()
            }
            .setNegativeButton("Cancel", null)
            .show()
    }
}