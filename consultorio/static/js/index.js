function preguntasF(p){    

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
    pregunta_texto.setAttribute("class","input is-sucess");
    div_input.appendChild(pregunta_texto);
    lugar.appendChild(div_input);
  
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
    pregunta_texto.setAttribute("class","input is-sucess");
    div_input.appendChild(pregunta_texto);
    lugar.appendChild(div_input);
  
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
    pregunta_texto.setAttribute("class","input is-sucess");
    div_input.appendChild(pregunta_texto);
    lugar.appendChild(div_input);
  
  };

    function limpiarF(){
      var div = document.getElementById("generalF");
      if(div){
        div.remove();
      }
    };
    function limpiarC(){
      var div = document.getElementById("generalC");
      if(div){
        div.remove();
      }
    };
    function limpiarO(){
      var div = document.getElementById("generalO");
      if(div){
        div.remove();
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