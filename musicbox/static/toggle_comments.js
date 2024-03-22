document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.toggle-comments').forEach(button => {
        button.addEventListener('click', function() {
            const albumId = this.dataset.albumId;
            const commentsContainer = document.getElementById(`comments-for-album-${albumId}`);
            commentsContainer.style.display = commentsContainer.style.display === 'none' ? 'block' : 'none';
        });
    });
});
