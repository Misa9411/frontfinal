(function () {
  // Función para decodificar el token JWT (solo la parte payload en Base64)
  function decodeJWT(token) {
    try {
      const payload = token.split('.')[1];
      return JSON.parse(atob(payload));
    } catch (e) {
      console.error("Error decodificando el token:", e);
      return null;
    }
  }

  // Recupera el token almacenado en localStorage
  const token = localStorage.getItem("token");
  if (!token) {
    window.location.href = "login.html";
    return;
  }

  // Decodifica el token para obtener la información del usuario
  const decoded = decodeJWT(token);
  if (!decoded) {
    window.location.href = "login.html";
    return;
  }

  // Guarda la información del usuario actual
  window.currentUser = {
    username: decoded.username,
    role: decoded.role
  };

  // Función que recorre elementos con data-permissions y, si el usuario no tiene permiso, intercepta el clic
  function checkAccess() {
    const elements = document.querySelectorAll('[data-permissions]');
    elements.forEach(function (el) {
      // Obtén la lista de roles permitidos (en minúsculas)
      const allowedRoles = el.getAttribute('data-permissions')
        .split(',')
        .map(role => role.trim().toLowerCase());
      const userRole = window.currentUser.role.toLowerCase();
      // Si el usuario no tiene permiso para este elemento...
      if (!(userRole === "administrador" || userRole === "gerente" || allowedRoles.includes(userRole))) {
        // No modificamos el estilo para que se vea igual,
        // pero interceptamos el clic en el enlace (si lo hay)
        const link = el.querySelector("a");
        if (link) {
          link.addEventListener("click", function(e) {
            e.preventDefault();
            alert("No tienes permiso para acceder a esta opción.");
          });
        }
      }
    });
  }

  document.addEventListener("DOMContentLoaded", checkAccess);
})();
