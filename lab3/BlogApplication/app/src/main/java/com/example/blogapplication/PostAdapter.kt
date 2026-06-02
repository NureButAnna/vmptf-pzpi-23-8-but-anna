package com.example.blogapplication

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageButton
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.example.blogapplication.models.Post

class PostAdapter(
    private var posts: List<Post>,
    private val onClick: (Post) -> Unit,
    private val onDelete: (Post) -> Unit,
    private val onEdit: (Post) -> Unit
) : RecyclerView.Adapter<PostAdapter.PostViewHolder>() {

    class PostViewHolder(view: View) : RecyclerView.ViewHolder(view) {

        val category: TextView = itemView.findViewById(R.id.tvCategory)
        val title: TextView = view.findViewById(R.id.tvPostTitle)
        val content: TextView = view.findViewById(R.id.tvPostContent)
        val deleteBtn: ImageButton = view.findViewById(R.id.btnDelete)
        val editBtn: ImageButton = view.findViewById(R.id.btnEdit)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): PostViewHolder {
        val view = LayoutInflater.from(parent.context)
            .inflate(R.layout.item_post, parent, false)

        return PostViewHolder(view)
    }

    override fun getItemCount(): Int = posts.size

    override fun onBindViewHolder(holder: PostViewHolder, position: Int) {

        val post = posts[position]

        holder.title.text = post.title
        holder.content.text = post.content
        holder.category.text = post.category

        holder.itemView.setOnClickListener {
            onClick(post)
        }

        holder.deleteBtn.setOnClickListener {
            onDelete(post)
        }

        holder.editBtn.setOnClickListener {
            onEdit(post)
        }
    }

    fun updateList(newPosts: List<Post>) {
        posts = newPosts
        notifyDataSetChanged()
    }
}