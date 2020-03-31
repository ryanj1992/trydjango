  function ajax_request(clicked_id){
    $.ajax({
        type: "POST",
        url: "/add_flight/",
        data: {
            'carrier': $("#carrier-code" + clicked_id).html(),
            'dep-time': $("#dep-time" + clicked_id).html(),
            'dep-place': $("#dep-place" + clicked_id).html(),
            'flight-time': $("#flight-time" + clicked_id).html(),
            'flight-stops': $("#flight-stops1" + clicked_id).html(),
            'arrival-time': $("#arrival-time" + clicked_id).html(),
            'arrival-place': $("#arrival-place" + clicked_id).html(),
            'flight-price': $("#" + clicked_id).html()
        }
    })
    .done(function (data) {
    if (data.success) {
        window.location.href = data.url;
    }
    });
}

var options = {
	url: "/static/js/countries.json",

    getValue: function(element) {
        return element.name + ' ' + element.code;
    },

    theme: "dark",

	list: {
		match: {
			enabled: true
		},
        showAnimation: {
			type: "fade", //normal|slide|fade
			time: 400,
			callback: function() {}
		},

		hideAnimation: {
			type: "slide", //normal|slide|fade
			time: 400,
			callback: function() {}
		}

	}
};

//   var options = {
//
//   url: function(phrase) {
//     return "https://test.api.amadeus.com/v1/reference-data/locations?subType=AIRPORT,CITY&keyword=" + phrase + "&page[limit]=5";
//   },
//
//   listLocation: "data",
//
//   getValue: function(element) {
//     return element.address.cityName + " " + element.name  + " " + element.iataCode;
//   },
//
//   ajaxSettings: {
//       beforeSend: function (xhr) {
//           xhr.setRequestHeader("Authorization", "Bearer 6kuyCD2hYsq3B0r2f3LCMUoUlKzL");
//       },
//
//       method: "GET"
//   },
//       theme: 'dark'
//
// };

$("#id_origin_place").easyAutocomplete(options);
$("#id_dest_place").easyAutocomplete(options);


$(document).ready(function(){
  $('#id_return_flight').change(function(){
    $('#id_inbound_date').attr('disabled', $(this).val() == "oneway").val('')
  });
});

// HOTELS

var map;

function initialize(lat, lng) {
  var mapProp = {
    center: new google.maps.LatLng(lat, lng),
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    zoom: 15
  };
  map = new google.maps.Map(document.getElementById('map'), mapProp);
}

// function hotels_request() {
//     $.ajax({
//         url: "https://test.api.amadeus.com/v2/shopping/hotel-offers?cityCode=PAR&roomQuantity=1&adults=2&radius=5&radiusUnit=KM&paymentPolicy=NONE&includeClosed=false&bestRateOnly=true&view=FULL&sort=NONE",
//         type: "GET",
//         beforeSend: function (xhr) {
//             xhr.setRequestHeader('Authorization', 'Bearer GgDN6Joteh9FSylrQ5c84o0eQbKI');
//         },
//         success: function (result) {
//             initialize(result.data[1].hotel.latitude, result.data[1].hotel.longitude);
//             for (var i = 0; i < result.data.length; i++) {
//                 var lat = result.data[i].hotel.latitude;
//                 var lng = result.data[i].hotel.longitude;
//                 var marker = new google.maps.Marker({
//                 map: map,
//                 position: new google.maps.LatLng(lat, lng),
//                 title: result.data[i].hotel.name
//               });
//             }
//         }
//     })
// }



// TRIPS