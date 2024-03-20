// toggle_reviews.js
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.toggle-reviews-btn').forEach(button => {
        button.addEventListener('click', function() {
            const songId = this.getAttribute('data-song-id');
            const reviewSection = document.getElementById('reviews-for-song-' + songId);
            reviewSection.style.display = reviewSection.style.display === 'none' ? 'block' : 'none';
        });
    });
});
