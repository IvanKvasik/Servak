let mod = document.getElementById('md'),
	cr = document.getElementById('cr'),
	btn = document.getElementById('btc'),
	btb = document.getElementById('btb'),
	fil = document.getElementById('fil');
btn.onclick = () => {
	mod.style.display = 'block';
	fil.style.display = 'block';
};
btb.onclick = () => {
	cr.style.display = 'block';
	fil.style.display = 'block';
};
fil.onclick = () => {
	cr.style.display = 'none';
	md.style.display = 'none';
	fil.style.display = 'none';
};