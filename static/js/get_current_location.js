if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(position => {
        const lat = position.coords.latitude;
        const lon = position.coords.longitude;
        if (!(isNaN(lat) || isNaN(lon))){
            document.getElementById('lat').value = lat;
            document.getElementById('lon').value = lon;
        }
    }, error => {
        alert('Please allow to get current location.');
    });
}