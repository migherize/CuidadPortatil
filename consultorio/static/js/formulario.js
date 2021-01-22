const formulario = document.getElementById("formulario");
const inputs = document.querySelectorAll('#formulario input');

const expresiones = {
	usuario: /^[a-zA-Z0-9\_\-]{4,16}$/, // Letras, numeros, guion y guion_bajo
    nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
	cedula: /^\d{7,14}$/, // 7 a 14 numeros.
	edad: /^\d{1,3}$/, // 1 a 3 numeros.
	password: /^.{4,12}$/, // 4 a 12 digitos.
	correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
	telefono: /^\d{7,14}$/ // 7 a 14 numeros.
}

const validarFormulario = (e) => {
    console.log("hola");
    switch (e.target.name) {
		case "Nombre":
            if(expresiones.nombre.test(e.target.value)){
                document.getElementById('Nombre').classList.remove('is-danger');
                document.getElementById('Ncheck').classList.remove('fa-exclamation-triangle');

                document.getElementById('Nombre').classList.add('is-success');
                document.getElementById('Ncheck').classList.add('fa-check');
            } else {
                document.getElementById('Nombre').classList.add('is-danger');
                document.getElementById('Ncheck').classList.add('fa-exclamation-triangle');
            }
        break;
        case "Apellido":
            if(expresiones.nombre.test(e.target.value)){
                document.getElementById('Apellido').classList.remove('is-danger');
                document.getElementById('Acheck').classList.remove('fa-exclamation-triangle');

                document.getElementById('Apellido').classList.add('is-success');
                document.getElementById('Acheck').classList.add('fa-check');
            } else {
                document.getElementById('Apellido').classList.add('is-danger');
                document.getElementById('Acheck').classList.add('fa-exclamation-triangle');
            }
        break;
        case "Cedula":
            console.log("hola");
            if(expresiones.cedula.test(e.target.value)){
                document.getElementById('idPaciente').classList.remove('is-danger');
                document.getElementById('Cecheck').classList.remove('fa-exclamation-triangle');

                document.getElementById('idPaciente').classList.add('is-success');
                document.getElementById('Cecheck').classList.add('fa-check');
            } else {
                document.getElementById('idPaciente').classList.add('is-danger');
                document.getElementById('Cecheck').classList.add('fa-exclamation-triangle');
            }
        break;
        case "Edad":
            if(expresiones.edad.test(e.target.value)){
                document.getElementById('Edad').classList.remove('is-danger');
                document.getElementById('Echeck').classList.remove('fa-exclamation-triangle');

                document.getElementById('Edad').classList.add('is-success');
                document.getElementById('Echeck').classList.add('fa-check');
            } else {
                document.getElementById('Edad').classList.add('is-danger');
                document.getElementById('Echeck').classList.add('fa-exclamation-triangle');
            }
        break;
        case "Direccion":
            if(expresiones.nombre.test(e.target.value)){
                document.getElementById('Direccion').classList.remove('is-danger');
                document.getElementById('Dcheck').classList.remove('fa-exclamation-triangle');

                document.getElementById('Direccion').classList.add('is-success');
                document.getElementById('Dcheck').classList.add('fa-check');
            } else {
                document.getElementById('Direccion').classList.add('is-danger');
                document.getElementById('Dcheck').classList.add('fa-exclamation-triangle');
            }
        break;
        case "Ocupacion":
            if(expresiones.nombre.test(e.target.value)){
                document.getElementById('Ocupacion').classList.remove('is-danger');
                document.getElementById('Ocheck').classList.remove('fa-exclamation-triangle');

                document.getElementById('Ocupacion').classList.add('is-success');
                document.getElementById('Ocheck').classList.add('fa-check');
            } else {
                document.getElementById('Ocupacion').classList.add('is-danger');
                document.getElementById('Ocheck').classList.add('fa-exclamation-triangle');
            }
        break;
		case "password":
			validarCampo(expresiones.password, e.target, 'password');
			validarPassword2();
		break;
		case "password2":
			validarPassword2();
		break;
		case "correo":
			validarCampo(expresiones.correo, e.target, 'correo');
		break;
		case "telefono":
			validarCampo(expresiones.telefono, e.target, 'telefono');
		break;
	}
}


inputs.forEach((input) => {
    input.addEventListener('keyup', validarFormulario);
    input.addEventListener('blur', validarFormulario);
});

const validarCampo = (expresion, input, campo) => {

}