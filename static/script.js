var inputs = document.querySelectorAll('input');
var form = document.querySelector('form');

function checkNum(event){

	event.preventDefault();

	for(var i = 0; i < inputs.length; i++){
		if (inputs[i].value == null || inputs[i].value == "") {
			alert('Oops, you left some fields empty');
			return;
		} else if (isNaN(inputs[i].value)) {
			alert('Check entered number, they are not valid');
			return;
		} 
	}
	form.submit();
}
