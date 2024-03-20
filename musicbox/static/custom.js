document.addEventListener('DOMContentLoaded', function() {
    const albumSelect = document.getElementById('id_album');
    const newAlbumInput = document.getElementById('id_new_album_name');

    newAlbumInput.style.display = 'none';

    albumSelect.addEventListener('change', function() {
        if (this.value === 'new') {
            newAlbumInput.style.display = 'block';
        } else {
            newAlbumInput.style.display = 'none';
        }
    });
});
