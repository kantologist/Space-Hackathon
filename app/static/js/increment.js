jQuery(document).ready(function(){
    // This button will increment the value
    function Increase(id){
        // Get the field name
        // Get its current value
        var currentVal = parseInt($('input[rel='+id+']').val());
        // If is not undefined
        if (!isNaN(currentVal)) {
            // Increment
            $('input[rel='+id+']').val(currentVal + 1);
        } else {
            // Otherwise put a 0 there
            $('input[rel='+id+']').val(0);
        }
        GlobalPower(inc=True)
    };

    // This button will decrement the value till 0
    function Decrease(id) {
        // Get its current value
        var currentVal = parseInt($('input[rel='+id+']').val());
        // If it isn't undefined or its greater than 0
        if (!isNaN(currentVal) && currentVal > 0) {
            // Decrement one
            $('input[rel='+id+']').val(currentVal - 1);
        } else {
            // Otherwise put a 0 there
            $('input[rel='+id+']').val(0);
        }
        GlobalPower(inc=False)
    };

    function GlobalPower(id, inc){
      if (inc){
      // Power = Power + $('p[rel='+id+"]").val().match(/\d+\);
      console.log($('p[rel='+id+"]").val());
    } else {
      // Power = Power - $('p[rel='+id+"]").val().match(/\d+\);
      console.log($('p[rel='+id+"]").val());
    }
    };
});
