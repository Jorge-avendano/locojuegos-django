// Validación del formulario de contacto
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("contact-form").addEventListener("click", function (event) {
        event.preventDefault();

        // Obtener los valores del formulario
        let nombre = document.getElementById("name-contacto").value.trim();
        let correo = document.getElementById("email-contacto").value.trim();
        let mensaje = document.getElementById("message").value.trim();

        // Función para mostrar el modal de alerta
        function mostrarModal(mensaje) {
            document.getElementById("alertMessage").innerText = mensaje;
            let modal = new bootstrap.Modal(document.getElementById("alertModal"));
            modal.show();
        }

        // Validar nombre
        if (nombre === "") {
            mostrarModal("Por favor, ingresa tu nombre.");
            return;
        }

        // Validar correo
        if (!correo.includes("@") || !correo.includes(".")) {
            mostrarModal("Por favor, ingresa un correo electrónico válido.");
            return;
        }

        // Validar mensaje
        if (mensaje === "") {
            mostrarModal("Por favor, escribe un mensaje.");
            return;
        }

        // Si todo es correcto
        mostrarModal("Mensaje enviado con éxito.");
    });
});
