filter = document.getElementById('filter');
function show(id) {
    document.getElementById(id).style.display = 'block';
    filter.style.display = 'block';
}
function hide(){
	document.getElementById('new').style.display = 'none';
	document.getElementById('conf').style.display = 'none';
	filter.style.display = 'none';
}
