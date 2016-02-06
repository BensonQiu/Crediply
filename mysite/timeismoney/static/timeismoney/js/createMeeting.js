 //Date picker
        $(function() {
            $('input[name="daterange"]').daterangepicker({
                timePicker: true,
                timePickerIncrement: 15,
                locale: {
                    format: 'MM/DD/YYYY h:mm A'
                }
            });
        });

        //Search box
        $(function() {
            var usernames = []
            $.ajax({
                url: '/getUsernames',
                type: 'GET',
                dataType: "json",
                async: false}).done(function(response) {
                    response.usernames.forEach(function(username) {
                        usernames.push({id: username, text: username})
                    })
                })
            $(".people-search-multiple").select2({
              data: usernames
            });
        });