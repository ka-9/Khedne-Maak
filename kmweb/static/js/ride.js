function initMap() {
    var myLatLng = {lat: 34.2544, lng: 35.6544};

    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 15,
        center: myLatLng
    });

    var marker = new google.maps.Marker({
        position: myLatLng,
        map: map,
        title: 'My Location'
    });
}

initMap();