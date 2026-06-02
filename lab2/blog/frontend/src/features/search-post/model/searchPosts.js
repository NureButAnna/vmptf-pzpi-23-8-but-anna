export function searchPosts(posts, query) {
  if (!query.trim()) {
    return posts;
  }

  const search = query.toLowerCase();

  return posts.filter((post) =>
    post.title.toLowerCase().includes(search) ||
    post.text.toLowerCase().includes(search) ||
    post.tags.some((tag) =>
      tag.toLowerCase().includes(search)
    )
  );
}