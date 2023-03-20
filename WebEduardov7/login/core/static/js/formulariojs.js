/**
	 * Método que envía un e-mail a través del cliente que tenga por defecto
	 * @param  {String} insTextoComp Texto que aparecerá dentro del mensaje
	 */
function enviarCorreo(insTextoComp) {
    var sEmail = prompt("Pulsa aceptar para contactar con nosotros", "220252@iessierradeguara.com");
    if(sEmail != null) {
        var sLink = "mailto:" + escape(sEmail)
         + "?subject=" + escape("Te han compartirdo el siguente texto")
         + "&body=" + insTextoComp;
        window.location.href = sLink;
    }
}