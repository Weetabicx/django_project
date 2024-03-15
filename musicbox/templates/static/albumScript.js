function editAlbum() {
    // 获取表单数据
    let formData = new FormData(document.getElementById('editForm'));
    // 发送异步请求到后端进行编辑
    fetch('/edit', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        alert('专辑已更新');
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('更新失败');
    });
}

function deleteAlbum() {
    let albumName = document.getElementById('deleteAlbumName').value;
    // 发送异步请求到后端进行删除
    fetch(`/delete?name=${albumName}`, {
        method: 'DELETE',
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        alert('专辑已删除');
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('删除失败');
    });
}
