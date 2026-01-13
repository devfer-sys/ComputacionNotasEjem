// Esperar a que el DOM esté completamente cargado
document.addEventListener("DOMContentLoaded", () => {
  // Cerrar automáticamente las alertas después de 5 segundos
  const alerts = document.querySelectorAll(".alert")
  alerts.forEach((alert) => {
    setTimeout(() => {
      const closeButton = alert.querySelector(".btn-close")
      if (closeButton) {
        closeButton.click()
      }
    }, 5000)
  })

  // Añadir validación al formulario de búsqueda
  const searchForm = document.querySelector('form[action="/buscar"]')
  if (searchForm) {
    searchForm.addEventListener("submit", (event) => {
      const ciInput = document.getElementById("ci")
      if (ciInput && ciInput.value.trim() === "") {
        event.preventDefault()
        alert("Por favor ingrese un número de CI válido")
      }
    })
  }
})
