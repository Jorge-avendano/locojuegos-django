// Funcionalidad para las compras

document.getElementById("compraModal").addEventListener("shown.bs.modal", function () {
    document.body.style.overflow = "hidden"; // Evita que la página haga scroll cuando el modal aparece
});

document.getElementById("compraModal").addEventListener("hidden.bs.modal", function () {
    document.body.style.overflow = ""; // Restaura el scroll cuando se cierra el modal
});

document.querySelectorAll(".btn-comprar").forEach(boton => {
    boton.addEventListener("click", (event) => {
        event.preventDefault(); // Solo previene el comportamiento por si acaso
        let modal = new bootstrap.Modal(document.getElementById("compraModal"));
        modal.show();
    });
});



// Acción al finalizar compra con validaciones
document.getElementById("finalizarCompra").addEventListener("click", () => {
    let name = document.getElementById("name").value.trim();
    let email = document.getElementById("email").value.trim();
    let cantidad = document.getElementById("cantidad").value.trim();
    // Expresión regular para validar un correo electrónico
    
    if (name === "") {
        alert("⚠️ Falta completar el campo de Nombre.");

    } 

    // Validar correo
    else if (!email.includes("@")) {
        alert("Por favor, ingresa un correo electrónico válido.");
        return;
    }
    else if (!email.includes(".com")) {
        alert("Por favor, ingresa el dominio de tu correo electrónico después de @.\n@example.com");
        return;
    }

    else if (cantidad < 1) {
        alert("Por favor, ingresa una cantidad válida");
        return;
    }
    
    
    else {
        alert("✅ ¡Compra exitosa!\n👉Nos pondremos en contacto contigo");
        document.getElementById("formCompra").reset(); // Limpia el formulario
        let modal = bootstrap.Modal.getInstance(document.getElementById("compraModal"));
        modal.hide(); // Cierra el modal
    }
});




// Navegacion suave a id de otras paginas

document.addEventListener("DOMContentLoaded", function() {
    if (window.location.hash) {
        let target = document.querySelector(window.location.hash);
        if (target) {
            target.scrollIntoView({ behavior: "smooth" });
        }
    }
});