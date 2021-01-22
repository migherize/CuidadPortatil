var band = false;
var bandC = false;
var bandO = false;

function preguntasF(p){
  if (band){
    console.log("ya existe");
  }
  else{
    lugar_div = document.getElementById('crear_preguntaF');
    lugar = document.createElement("div");
    lugar.setAttribute("id","generalF");
    lugar_div.appendChild(lugar);
    
    pregunta = document.createElement("label"); // crea un elemento html
    contenido_pre = document.createTextNode("Forma: "); // crea un texto para un elemento.
    pregunta.appendChild(contenido_pre); // agrega un texto en un elemento.
    lugar.appendChild(pregunta);
    
    div_input = document.createElement("div");
    div_input.setAttribute("class","control");
    pregunta_texto = document.createElement("input"); // crea un elemento html
    pregunta_texto.setAttribute("type","texto");
    pregunta_texto.setAttribute("name","Forma");
    pregunta_texto.setAttribute("class","input is-sucess");
    div_input.appendChild(pregunta_texto);
    lugar.appendChild(div_input);
    band = true;
  }
    
  };
  function preguntasC(p){    
  lugar_div = document.getElementById('crear_preguntaC');
  lugar = document.createElement("div");
  lugar.setAttribute("id","generalC");
  lugar_div.appendChild(lugar);
  
  pregunta = document.createElement("label"); // crea un elemento html
  contenido_pre = document.createTextNode("Duracion: "); // crea un texto para un elemento.
  pregunta.appendChild(contenido_pre); // agrega un texto en un elemento.
  lugar.appendChild(pregunta);
    
    div_input = document.createElement("div");
    div_input.setAttribute("class","control");
    pregunta_texto = document.createElement("input"); // crea un elemento html
    pregunta_texto.setAttribute("type","texto");
    pregunta_texto.setAttribute("name","Duracion");
    pregunta_texto.setAttribute("class","input is-sucess");
    div_input.appendChild(pregunta_texto);
    
    if (bandC){
      console.log("ya existe");
    }
    else{
      lugar.appendChild(div_input);
      bandC = true;
    }  
  };

  function preguntasO(p){    

    lugar_div = document.getElementById('crear_preguntaO');
  
    lugar = document.createElement("div");
    lugar.setAttribute("id","generalO");
    lugar_div.appendChild(lugar);
  
    pregunta = document.createElement("label"); // crea un elemento html
    contenido_pre = document.createTextNode("Frecuencia: "); // crea un texto para un elemento.
    pregunta.appendChild(contenido_pre); // agrega un texto en un elemento.
    lugar.appendChild(pregunta);
    
    div_input = document.createElement("div");
    div_input.setAttribute("class","control");
    pregunta_texto = document.createElement("input"); // crea un elemento html
    pregunta_texto.setAttribute("type","texto");
    pregunta_texto.setAttribute("name","Frecuencia");
    pregunta_texto.setAttribute("class","input is-sucess");
    div_input.appendChild(pregunta_texto);

    if (bandO){
      console.log("ya existe");
    }
    else{
      lugar.appendChild(div_input);
      bandO = true;
    }  
  };

    function limpiarF(){
      if(band){
        var div = document.getElementById("generalF");
        if(div){
          div.remove();
        }
        band=false;
      }
      if(!band){
        console.log("no fuma");
        lugar_div = document.getElementById('crear_preguntaF');
        lugar = document.createElement("div");
        lugar.setAttribute("id","generalF");
        lugar_div.appendChild(lugar);
        
        div_input = document.createElement("div");
        div_input.setAttribute("class","control");
        pregunta_texto = document.createElement("input"); // crea un elemento html
        pregunta_texto.setAttribute("type","hidden");
        pregunta_texto.setAttribute("name","Forma");
        pregunta_texto.setAttribute("Value","N");
        pregunta_texto.setAttribute("class","input is-sucess");
        div_input.appendChild(pregunta_texto);
        lugar.appendChild(div_input);
        band = true;
        
      }
    };
    function limpiarC(){
      if(bandC){
        var div = document.getElementById("generalC");
        if(div){
          div.remove();
        }
        bandC=false;
      }
      if(!bandC){
      console.log("no existe Cafe");
      lugar_div = document.getElementById('crear_preguntaC');
      lugar = document.createElement("div");
      lugar.setAttribute("id","generalC");
      lugar_div.appendChild(lugar);
      
      div_input = document.createElement("div");
      div_input.setAttribute("class","control");
      pregunta_texto = document.createElement("input"); // crea un elemento html
      pregunta_texto.setAttribute("type","hidden");
      pregunta_texto.setAttribute("name","Duracion");
      pregunta_texto.setAttribute("value","N");
      pregunta_texto.setAttribute("class","input is-sucess");
      div_input.appendChild(pregunta_texto);
      lugar.appendChild(div_input);
      bandC = true;
      }
    };
    function limpiarO(){
      if(bandO){
        var div = document.getElementById("generalO");
        if(div){
          div.remove();
        }
        bandO =false;
      }
      if(!bandO){
        console.log("no existe Otros");
        lugar_div = document.getElementById('crear_preguntaO');
  
        lugar = document.createElement("div");
        lugar.setAttribute("id","generalO");
        lugar_div.appendChild(lugar);

        div_input = document.createElement("div");
        div_input.setAttribute("class","control");
        pregunta_texto = document.createElement("input"); // crea un elemento html
        pregunta_texto.setAttribute("type","hidden");
        pregunta_texto.setAttribute("name","Frecuencia");
        pregunta_texto.setAttribute("value","N");
        pregunta_texto.setAttribute("class","input is-sucess");
        div_input.appendChild(pregunta_texto);
        lugar.appendChild(div_input);
        bandO = true;
      }
    };

    function validacion(){
      valor = document.getElementById("Nombre").value;
      console.log("hola",valor);
          if( valor == null || valor.length == 0 || /^\s+$/.test(valor) ) {
            return false;
          }

        /*
        if (condicion que debe cumplir el primer campo del formulario) {
          // Si no se cumple la condicion...
          alert('[ERROR] El campo debe tener un valor de...');
          return false;
        }
        else if (condicion que debe cumplir el segundo campo del formulario) {
          // Si no se cumple la condicion...
          alert('[ERROR] El campo debe tener un valor de...');
          return false;
        }
        ...
        else if (condicion que debe cumplir el último campo del formulario) {
          // Si no se cumple la condicion...
          alert('[ERROR] El campo debe tener un valor de...');
          return false;
        }
      
        // Si el script ha llegado a este punto, todas las condiciones
        // se han cumplido, por lo que se devuelve el valor true
        return true;
        */
    };


    function pregunta(){
      if (confirm('¿Estas seguro de enviar este formulario?')){
         document.getElementById('formulario').submit();
      }
    };