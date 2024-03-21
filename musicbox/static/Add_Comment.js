document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.add-comment-btn').forEach(button => {
    button.addEventListener('click', function() {
      const albumId = this.getAttribute('data-album-id');
      document.getElementById('add-comment-form').action = `/albums/${albumId}/add_comment/`;
      document.getElementById('comment-album-id').value = albumId;
      document.getElementById('add-comment-form-container').style.display = 'block';
    });
  });
});
