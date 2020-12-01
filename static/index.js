function search(){
    var user = document.getElementById('user').value;
    document.write('Loading..');
    window.location.href = '/' + user;
}