package com.example.blogapplication.models

data class Post(
    var id: String,
    var title: String,
    var content: String,
    var category: String,
    var date: String,
    var comments: MutableList<Comment> = mutableListOf()
)