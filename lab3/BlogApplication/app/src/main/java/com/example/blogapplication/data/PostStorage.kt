package com.example.blogapplication.data

import android.content.Context
import com.example.blogapplication.models.Post
import com.google.gson.Gson
import com.google.gson.reflect.TypeToken

object PostStorage {

    private const val PREFS_NAME = "blog_prefs"
    private const val POSTS_KEY = "posts"

    private val gson = Gson()

    // ---------------- SAVE ----------------

    fun savePosts(context: Context, posts: List<Post>) {
        val prefs = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)

        val json = gson.toJson(posts)

        prefs.edit()
            .putString(POSTS_KEY, json)
            .apply()
    }

    // ---------------- LOAD ----------------

    fun loadPosts(context: Context): MutableList<Post> {
        val prefs = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)

        val json = prefs.getString(POSTS_KEY, null)

        if (json.isNullOrEmpty()) {
            return mutableListOf()
        }

        return try {
            val type = object : TypeToken<MutableList<Post>>() {}.type
            gson.fromJson(json, type) ?: mutableListOf()
        } catch (e: Exception) {
            mutableListOf()
        }
    }

    // ---------------- CLEAR (optional but useful) ----------------

    fun clearPosts(context: Context) {
        val prefs = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)

        prefs.edit()
            .remove(POSTS_KEY)
            .apply()
    }
}