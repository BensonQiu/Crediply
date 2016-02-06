function initMap() {

  var geocoder = new google.maps.Geocoder();

  document.getElementById('submit').addEventListener('click', function() {
    geocodeAddress(geocoder);
  });
}

// function geocodeAddress(geocoder) {
//   var address = document.getElementById('address').value;
//   geocoder.geocode({'address': address}, function(results, status) {
//     // if (status === google.maps.GeocoderStatus.OK) {
//       // resultsMap.setCenter(results[0].geometry.location);
//       // var marker = new google.maps.Marker({
//         // map: resultsMap,
//         // position: results[0].geometry.location
//       // });
//     // } else {
//       // alert('Geocode was not successful for the following reason: ' + status);
//     // }
//     console.log(results[0].geometry.location.lat());
//     console.log(results[0].geometry.location.lng());
//   });
// }

function geocodeAddress() {
  var geocoder = new google.maps.Geocoder();

  var meetingName = document.getElementById('meetingName').value;
  var date = document.getElementById('date').value;
  var address = document.getElementById('address').value;
  var attendeesList = document.getElementsByClassName('people-search-multiple');
  var attendees = []
  for(i = 0;i < attendeesList[0]['length']; i++) {
      console.log(attendeesList[0][i].value);
      attendees.push(attendeesList[0][i].value);
  }

  geocoder.geocode({'address': address}, function(results, status) {
    var lat = results[0].geometry.location.lat();
    var lng = results[0].geometry.location.lng();
    console.log(lat);
    console.log(lng);
    console.log(meetingName);
    console.log(date);
    console.log(address);
    console.log(attendees);

    $.ajax({
        url: '/createMeeting',
        type: 'GET',
        data: {
          meetingName: meetingName,
          date: date,
          address: address,
          lat: lat,
          lng: lng,
          attendees: attendees,
        },
        dataType: "json",
        async: false}).done(function(response) {
          alert('made a fooAjax call')
          // response.meetings.forEach(function(meeting) {
          //   var currentEvent = {
          //     title: meeting.meetingName,
          //     start: moment(meeting.startDT),
          //                   end: moment(meeting.endDT)
          //   }
          //   events.push(currentEvent)
          // })
        })
  });
}