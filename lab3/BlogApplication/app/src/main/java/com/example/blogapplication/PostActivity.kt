package com.example.blogapplication

import android.os.Bundle
import android.widget.*
import androidx.appcompat.app.AppCompatActivity
import com.example.blogapplication.data.PostStorage
import com.example.blogapplication.models.Comment
import com.example.blogapplication.models.Post

class PostActivity : AppCompatActivity() {

    private lateinit var post: Post
    private lateinit var title: TextView
    private lateinit var date: TextView
    private lateinit var content: TextView
    private lateinit var commentsContainer: LinearLayout
    private lateinit var etComment: EditText

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_post)

        title = findViewById(R.id.tvPostTitle)
        date = findViewById(R.id.tvDate)
        content = findViewById(R.id.tvContent)
        commentsContainer = findViewById(R.id.commentsContainer)
        etComment = findViewById(R.id.etComment)

        val btnBack = findViewById<ImageButton>(R.id.btnBack)
        val btnSend = findViewById<Button>(R.id.btnSendComment)

        btnBack.setOnClickListener {
            finish()
        }

        val postId = intent.getStringExtra("post_id")

        val posts = PostStorage.loadPosts(this)
        post = posts.firstOrNull { it.id == postId } ?: return

        renderPost()
        renderComments()

        btnSend.setOnClickListener {
            val text = etComment.text.toString().trim()

            if (text.isNotEmpty()) {
                val comment = Comment(
                    id = System.currentTimeMillis().toString(),
                    text = text
                )

                post.comments.add(comment)

                PostStorage.savePosts(this, posts)

                etComment.setText("")
                renderComments()
            }
        }
    }

    private fun renderPost() {
        title.text = post.title
        date.text = post.date
        content.text = post.content
    }

    private fun renderComments() {
        commentsContainer.removeAllViews()

        for (comment in post.comments) {
            val tv = TextView(this)

            tv.text = "• ${comment.text}"
            tv.textSize = 16f
            tv.setPadding(0, 8, 0, 8)

            commentsContainer.addView(tv)
        }
    }
}