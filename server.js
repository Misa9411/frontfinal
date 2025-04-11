// server.js
const express = require("express");
const cors = require("cors");
const jwt = require("jsonwebtoken");
const argon2 = require("argon2");
const path = require("path");

const app = express();

// Middleware para parsear JSON y permitir CORS
app.use(express.json());
app.use(cors());

// Rutas personalizadas para redirigir a login
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "login.html"));
});

app.get("/login", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "login.html"));
});

// Sirve archivos estáticos desde la carpeta "public" sin usar el index predeterminado
app.use(express.static("public", { index: false }));

// Clave secreta para firmar el JWT (en producción, usa una variable de entorno)
const JWT_SECRET = "mi_clave_secreta";

// Ejemplo de hash para "admin123" generado con Argon2.
// Genera el hash ejecutando en la terminal:
// node -e "require('argon2').hash('admin123').then(console.log).catch(console.error)"
const adminHash = "$argon2id$v=19$m=65536,t=3,p=4$tr/SZBsvbtxdcvLwuF2Gfg$DicbzTnFghleL1Gq9JkiAlg1Ue/58Hs+L0Axij2Xnoc";

    const users = [
        {
          id: 1,
          username: 'admin',
          email: 'admin@example.com',
          password: adminHash,
          role: 'administrador'
        },
        {
          id: 2,
          username: 'comercialRetail',
          email: 'retail@example.com',
          // Reemplaza el hash de abajo por el que generaste para "retail123"
          password: '$argon2id$v=19$m=65536,t=3,p=4$nn3ERTyNTWkO05Rgig7rMA$lHmnLlJqqAj1I1+teyZb5NK2ZoPNSgYigAmsuVYMi0E',
          role: 'comercial_retail'
        }
      ];
      

app.post("/api/login", async (req, res) => {
  const { email, password } = req.body;

  const user = users.find((u) => u.email === email);
  if (!user) {
    return res.status(400).json({ message: "Credenciales inválidas" });
  }

  try {
    const isMatch = await argon2.verify(user.password, password);
    if (!isMatch) {
      return res.status(400).json({ message: "Credenciales inválidas" });
    }

    const token = jwt.sign(
      { id: user.id, username: user.username, role: user.role },
      JWT_SECRET,
      { expiresIn: "1h" }
    );

    res.json({ token });
  } catch (err) {
    console.error("Error en argon2.verify:", err);
    res.status(500).json({ message: "Error interno" });
  }
});

app.get("/prueba", (req, res) => {
  res.send("Servidor funcionando correctamente.");
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Servidor corriendo en el puerto ${PORT}`);
});
