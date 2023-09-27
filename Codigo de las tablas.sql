-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS JugueteriaDB;
USE JugueteriaDB;

-- Tabla Proveedor
CREATE TABLE IF NOT EXISTS Proveedor (
  idProveedor INT NOT NULL AUTO_INCREMENT,
  Nombre VARCHAR(45) NOT NULL,
  Apellido VARCHAR(45) NOT NULL,
  Telefono INT(8),
  Direccion VARCHAR(100),
   Empresa varchar(45)
  PRIMARY KEY (idProveedor)
);
ALTER TABLE Proveedor ADD Empresa varchar(45);
ALTER TABLE Proveedor MODIFY Telefono INT NULL;
DELETE FROM Proveedor WHERE idProveedor = 3;
SELECT *FROM Proveedor;
ALTER TABLE Proveedor AUTO_INCREMENT = 3;

INSERT INTO Proveedor (Nombre, Apellido, Telefono, Direccion, Empresa) VALUES ('Juan', 'Hernandez','12345678','9-36 zona 5','Empres1');

-- Tabla Producto
CREATE TABLE IF NOT EXISTS Producto (
  idProducto INT NOT NULL AUTO_INCREMENT,
  Nombre VARCHAR(100) NOT NULL,
  Precio DECIMAL(10, 2) NOT NULL,
  Cantidad INT NOT NULL,
  PRIMARY KEY (idProducto)
);

-- Tabla Proveedor_Producto (Relación N:M entre Proveedor y Producto)
CREATE TABLE IF NOT EXISTS Proveedor_Producto (
  Proveedor_idProveedor INT NOT NULL,
  Producto_idProducto INT NOT NULL,
  PRIMARY KEY (Proveedor_idProveedor, Producto_idProducto),
  FOREIGN KEY (Proveedor_idProveedor) REFERENCES Proveedor(idProveedor),
  FOREIGN KEY (Producto_idProducto) REFERENCES Producto(idProducto)
);

-- Tabla Cliente
CREATE TABLE IF NOT EXISTS Cliente (
  idCliente INT NOT NULL AUTO_INCREMENT,
  Nombre VARCHAR(45) NOT NULL,
  Apellido VARCHAR(45) NOT NULL,
  Telefono INT(8),
  Direccion VARCHAR(100),
  PRIMARY KEY (idCliente)
);

-- Tabla Usuario
CREATE TABLE IF NOT EXISTS Usuario (
  idUsuario INT NOT NULL AUTO_INCREMENT,
  NombreUsuario VARCHAR(45) NOT NULL,
  Contraseña VARCHAR(100) NOT NULL,
  PRIMARY KEY (idUsuario)
);

INSERT INTO Rol (NombreRol) VALUES ('Administrador');
INSERT INTO Rol (NombreRol) VALUES ('Cajero');
INSERT INTO Usuario (NombreUsuario, Contraseña) VALUES ('Admin', 'Admin123');
SELECT *FROM Usuario
SET @idUsuario = LAST_INSERT_ID();
SET @idRol = (SELECT idRol FROM Rol WHERE NombreRol = 'Administrador');
INSERT INTO Usuario_Rol (Usuario_idUsuario, Rol_idRol) VALUES (@idUsuario, @idRol);
USE JugueteriaDB;
SELECT *FROM usuario_rol;
SELECT *FROM rol;
SELECT *FROM usuario;
DELETE FROM Usuario WHERE idUsuario = 2;
ALTER TABLE Usuario AUTO_INCREMENT = 2;
SELECT *FROM Proveedor;


-- Tabla Rol
CREATE TABLE IF NOT EXISTS Rol (
  idRol INT NOT NULL AUTO_INCREMENT,
  NombreRol VARCHAR(45) NOT NULL,
  PRIMARY KEY (idRol)
);

-- Tabla Usuario_Rol (Relación N:M entre Usuario y Rol)
CREATE TABLE IF NOT EXISTS Usuario_Rol (
  Usuario_idUsuario INT NOT NULL,
  Rol_idRol INT NOT NULL,
  PRIMARY KEY (Usuario_idUsuario, Rol_idRol),
  FOREIGN KEY (Usuario_idUsuario) REFERENCES Usuario(idUsuario),
  FOREIGN KEY (Rol_idRol) REFERENCES Rol(idRol)
);

-- Tabla Compra
CREATE TABLE IF NOT EXISTS Compra (
  idCompra INT NOT NULL AUTO_INCREMENT,
  Total DECIMAL(10, 2) NOT NULL,
  FechaCompra DATE NOT NULL,
  Usuario_idUsuario INT NOT NULL,
  Detalle VARCHAR(200),
  PRIMARY KEY (idCompra),
  FOREIGN KEY (Usuario_idUsuario) REFERENCES Usuario(idUsuario)
);

-- Tabla Venta
CREATE TABLE IF NOT EXISTS Venta (
  idVenta INT NOT NULL AUTO_INCREMENT,
  Monto DECIMAL(10, 2) NOT NULL,
  Total DECIMAL(10, 2) NOT NULL,
  FechaVenta DATE NOT NULL,
  Detalle VARCHAR(200),
  Cliente_idCliente INT NOT NULL,
  Usuario_idUsuario INT NOT NULL,
  PRIMARY KEY (idVenta),
  FOREIGN KEY (Cliente_idCliente) REFERENCES Cliente(idCliente),
  FOREIGN KEY (Usuario_idUsuario) REFERENCES Usuario(idUsuario)
);

-- Tabla Combo
CREATE TABLE IF NOT EXISTS Combo (
  idCombo INT NOT NULL AUTO_INCREMENT,
  NombreCombo VARCHAR(100) NOT NULL,
  Descuento DECIMAL(10, 2) NOT NULL,
  PrecioTotal DECIMAL(10, 2) NOT NULL,
  FechaValida DATE NOT NULL,
  PRIMARY KEY (idCombo)
);

-- Tabla Combo_Producto (Relación N:M entre Combo y Producto)
CREATE TABLE IF NOT EXISTS Combo_Producto (
  Combo_idCombo INT NOT NULL,
  Producto_idProducto INT NOT NULL,
  PRIMARY KEY (Combo_idCombo, Producto_idProducto),
  FOREIGN KEY (Combo_idCombo) REFERENCES Combo(idCombo),
  FOREIGN KEY (Producto_idProducto) REFERENCES Producto(idProducto)
);

-- Tabla Detalle_Venta
CREATE TABLE IF NOT EXISTS Detalle_Venta (
  idDetalle INT NOT NULL AUTO_INCREMENT,
  PrecioUnitario DECIMAL(10, 2) NOT NULL,
  Cantidad INT NOT NULL,
  Descripcion VARCHAR(200),
  Venta_idVenta INT NOT NULL,
  PRIMARY KEY (idDetalle),
  FOREIGN KEY (Venta_idVenta) REFERENCES Venta(idVenta)
);

-- Tabla Combo_Venta (Relación N:M entre Combo y Venta)
CREATE TABLE IF NOT EXISTS Combo_Venta (
  Combo_idCombo INT NOT NULL,
  Venta_idVenta INT NOT NULL,
  PRIMARY KEY (Combo_idCombo, Venta_idVenta),
  FOREIGN KEY (Combo_idCombo) REFERENCES Combo(idCombo),
  FOREIGN KEY (Venta_idVenta) REFERENCES Venta(idVenta)
);
-- Tabla Ticket
CREATE TABLE IF NOT EXISTS Ticket (
  idTicket INT NOT NULL AUTO_INCREMENT,
  FechaEmision DATE NOT NULL,
  Venta_idVenta INT NOT NULL,
  PRIMARY KEY (idTicket),
  FOREIGN KEY (Venta_idVenta) REFERENCES Venta(idVenta)
);


