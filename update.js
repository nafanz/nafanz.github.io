function update(div_id) {
    var url = "https://api.github.com/repos/nafanz/nafanz.github.io";
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var repos = JSON.parse(xhr.responseText);
            document.getElementById(div_id).innerHTML = repos['updated_at'];
        }
    };
    xhr.send();
}