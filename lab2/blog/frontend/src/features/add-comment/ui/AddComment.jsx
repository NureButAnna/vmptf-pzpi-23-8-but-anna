function CommentForm({ value, onChange, onAdd }) {
  const handleSubmit = (e) => {
    e.preventDefault();
    onAdd();
  };

  return (
    <form className="comment-form" onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Напишіть коментар..."
        value={value}
        onChange={(e) => onChange(e.target.value)}
      />

      <button type="submit">
        Додати
      </button>
    </form>
  );
}

export default CommentForm;