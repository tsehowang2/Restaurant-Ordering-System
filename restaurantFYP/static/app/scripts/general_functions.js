function changeModalQuantity(id, i, price) {
    var qty = document.getElementById(id + "_modalCount");
    var qtyvalue = parseInt(qty.getAttribute("value"));
    console.log(qtyvalue+", "+i);
	if (i == 0) {
		qty.setAttribute("class", "text-dark text-center");
		document.getElementById(id + "_total").innerHTML = parseFloat((price)).toFixed(1);
        qty.setAttribute("value", 1);
    }
	else if (parseInt(qtyvalue) + i != 0) {
		qty.setAttribute("class", "text-dark text-center");
		document.getElementById(id + "_total").innerHTML = (parseFloat(price) * (qtyvalue + i)).toFixed(1);
		qty.setAttribute("value", qtyvalue + i);
	}
	else qty.setAttribute("class", "text-danger text-center");
}

function check_bill(token) {
    const g_interval = setInterval(function () {
        $.ajax({
            type: 'POST',
            url: '/force_logout',
            data: {
                csrfmiddlewaretoken: token,
            },
            success: function (data) {
                if (data == 'false') {
                    window.location.href = '/logout';
                }
            }
        });
    }, 5000);

}
