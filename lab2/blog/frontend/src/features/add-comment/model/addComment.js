export function addComment(comments, text, author = 'User') {
  if (!text.trim()) return comments;

  const newComment = {
    id: Date.now(),
    text,
    author,
  };

  return [...comments, newComment];
}