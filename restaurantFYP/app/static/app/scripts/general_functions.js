
/*function changeModalQuantity(id, i, price) {
    var qty = document.getElementById(id + "_modalCount");
    var qtyvalue = parseInt(qty.getAttribute("value"));
    console.log(qtyvalue+", "+i);
    if (i == '0') {
        qty.setAttribute("class", "text-dark text-center");
        document.getElementById(id + "_total").innerHTML = parseFloat((price)).toFixed(1);
        qty.setAttribute("value", 1);
    }
    else if (parseInt(qtyvalue) + i == 0 || parseInt(qtyvalue) + i == 31) {
        qty.setAttribute("class", "text-danger text-center");
    }
    else {
		qty.setAttribute("class", "text-dark text-center");
		document.getElementById(id + "_total").innerHTML = (parseFloat(price) * (qtyvalue + i)).toFixed(1);
		qty.setAttribute("value", qtyvalue + i);
	}
}
//why this page doesn't changed?*/