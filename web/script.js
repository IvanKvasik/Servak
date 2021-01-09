let mod = document.getElementById('md'),
	cr = document.getElementById('cr'),
	cf = document.getElementById('cf'),
	success = document.getElementById('success'),
	suc = document.getElementById('suc2'),
	name = document.getElementById('name'),
	pass1 = document.getElementById('password1'),
	pass2 = document.getElementById('password2'),
	btn = document.getElementById('btc'),
	btb = document.getElementById('btb'),
	fil = document.getElementById('fil');

async function Configure(){
	await eel.Configure(pass2.value);
	cf.style.display = 'none';
	cr.style.display = 'block';
	fil.style.display = 'block';
}

async function Create(){
	await eel.Create(name.value, pass1.value);
	success.style.display = 'block';
	fil.style.display = 'block';
	suc.innerHTML = "Success! Visit /home/domains/" + name.value + "/, create your first site file\n and visit http://" + name.value + "\nIf it doesn't work, try again";
}

btn.onclick = () => {
	mod.style.display = 'block';
	fil.style.display = 'block';
};
btb.onclick = () => {
	cf.style.display = "block";
	fil.style.display = "block"
};
fil.onclick = () => {
	cr.style.display = 'none';
	cf.style.display = 'none';
	md.style.display = 'none';
	success.style.display = 'none';
	fil.style.display = 'none';
};