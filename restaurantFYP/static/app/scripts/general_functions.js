function changeModalQuantity(id, i, price) {
    var qty = document.getElementById(id + "_modalCount");
    var qtyvalue = parseInt(qty.getAttribute("value"));
    console.log(qtyvalue+", "+i);
	if (i == 0) {
		qty.setAttribute("class", "text-dark text-center");
		document.getElementById(id + "_total").innerHTML = parseInt((price)).toFixed(1);
        qty.setAttribute("value", 1);
    }
	else if (parseInt(qtyvalue) + i != 0) {
		qty.setAttribute("class", "text-dark text-center");
		document.getElementById(id + "_total").innerHTML = (price * (qtyvalue + i)).toFixed(1);
		qty.setAttribute("value", qtyvalue + i);
	}
	else qty.setAttribute("class", "text-danger text-center");
}