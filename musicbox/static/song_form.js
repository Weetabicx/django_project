document.addEventListener('DOMContentLoaded', function() {
    var albumSelect = document.getElementById('id_album');
    var newAlbumDiv = document.getElementById('new_album_name_div');

    albumSelect.addEventListener('change', function() {
        if (albumSelect.value === 'new') {
            newAlbumDiv.style.display = 'block';
        } else {
            newAlbumDiv.style.display = 'none';
        }
    });
});
