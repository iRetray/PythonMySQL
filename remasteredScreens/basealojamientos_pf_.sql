-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 16-11-2021 a las 03:58:02
-- Versión del servidor: 10.4.21-MariaDB
-- Versión de PHP: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `basealojamientos(pf)`
--

DELIMITER $$
--
-- Procedimientos
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `allactividades` ()  BEGIN
	select*
    from actividad;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `allalojamientos` ()  BEGIN
	select*
    from alojamientos;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `allcronogramas` ()  BEGIN
	select*
    from cronogramas;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `allempleados` ()  BEGIN
	select*
    from empleados;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `allhabitaciones` ()  BEGIN
	select*
    from habitaciones;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `allhuespedes` ()  BEGIN
	select*
    from huespedes;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `allinscripciones` ()  BEGIN
	select*
    from inscripciones;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `allregistros` ()  BEGIN
	select*
    from registros;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `delactividades` (`id` INT)  BEGIN
	delete from actividad
    where idActividad=id ;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `delalojamientos` (`id` INT)  BEGIN
	delete from alojamientos
    where idAlojamiento= id;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `delcronogramas` (IN `idActividad` INT, IN `idAlojamiento` INT)  BEGIN
	delete from cronogramas
    where cronogramas.idactividad = idActividad
    and cronogramas.idalojamiento = idAlojamiento;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `delempleados` (`id` INT)  BEGIN
	delete from empleados
    where idempleado = id;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `delhabitaciones` (`id` INT)  BEGIN
	delete from habitaciones
    where idhabitacion = id;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `delhuespedes` (`id` INT)  BEGIN
	delete from huespedes
    where idhuesped = id;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `delinscripciones` (IN `idActividad` INT, IN `idAlojamiento` INT, IN `idHuesped` INT)  BEGIN
	delete from inscripciones
    where inscripciones.idActividad = idActividad
    and inscripciones.idAlojamiento= idAlojamiento
    and inscripciones.idHuesped = idHuesped;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `delregistros` (IN `idHabitacion` INT, IN `idHuesped` INT)  BEGIN
	delete from registros
    where registros.idHabitacion = idHabitacion
    and registros.idHueped= idHuesped;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `getactividadxid` (`id` INT)  BEGIN
	select *
    from actividad
    where idActividad = id;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `getalojamientosxid` (`id` INT)  BEGIN
	select *
    from alojamientos
    where idAlojamiento = id;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `getcronogramas` (IN `idactividadidActividad ` INT, IN `idalojamientoidAlojamiento ` INT)  BEGIN
	select *
    from cronogramas
    where cronogramas.idActividad = idActividad
    and cronogramas.idAlojamiento= idAlojamiento;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `getempleadosxid` (`id` INT)  BEGIN
	select *
    from empleados
    where idEmpleado = id;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `gethabitacionesxid` (`id` INT)  BEGIN
	select *
    from habitaciones
    where idHabitacion = id;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `gethuespedesxid` (`id` INT)  BEGIN
	select *
    from huespedes
    where idHuesped = id;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `getinscripciones` (IN `idActividad` INT, IN `idAlojamiento` INT, IN `idHuesped` INT)  BEGIN
	select *
    from inscripciones
    where inscripciones.idHuesped = idHuesped
    and inscripciones.idActividad = idActividad
    and inscripciones.idAlojamiento = idAlojamiento;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `getregistros` (IN `idHuesped` INT, IN `idHabitacion` INT)  BEGIN
	select *
    from registros
    where registros.idHabitacion = idHabitacion
    and registros.idHuesped = idHuesped ;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `modactividades` (IN `idactividad` INT, IN `nombre` VARCHAR(45), IN `descripcion` VARCHAR(45), IN `dificultad` VARCHAR(45), IN `coordinador` INT, IN `id` INT)  BEGIN
	update actividad
    set 
    idActividad=idactividad,
    Nombre=nombre,
    Descripcion=descripcion,
    Dificultad=dificultad,
    Coordinador=coordinador
    where actividad.idactividad=id;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `modalojamientos` (`idalojamiento` INT, `nombre` VARCHAR(45), `direccion` VARCHAR(45), `telefono` VARCHAR(45), `num_habitaciones` VARCHAR(45), `contacto` INT, `oldid` INT)  BEGIN
	update alojamientos
    set idAlojamiento=idalojamiento,
    Nombre=nombre,
    Direccion=direccion,
    Telefono=telefono,
    Num_Habitaciones=num_habitaciones,
    Contacto=contacto
    where alojamientos.idAlojamiento=oldid;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `modcronogramas` (IN `idactividad ` INT, IN `idalojamientoidalojamiento ` INT(45), IN `oldidActividad ` INT, IN `oldidAlojamiento ` INT)  BEGIN
	update cronogramas
    set idActividad=idactividad,
    idAlojamiento=idalojamiento,
    Dia=dia
    where cronogramas.idActividad=oldidActividad
    and cronogramas.idAlojamiento=oldidAlojamiento;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `modempleado` (`idempleado` INT, `nombre` VARCHAR(45), `direccion` VARCHAR(45), `telefono` VARCHAR(45), `alojamiento` INT, `cargo` VARCHAR(45), `oldid` INT)  BEGIN
	update empleados
    set idEmpleado=idempleado,
    Nombre=nombre,
    Direccion=direccion,
    Telefono=telefono,
    Alojamiento=alojamiento,
    Cargo=cargo
    where empleados.idEmpleado = oldid ;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `modhabitaciones` (`idhabitacion` INT, `tipo` VARCHAR(45), `regtempe` VARCHAR(45), `precio` VARCHAR(45), `alojamiento` INT, `keeper` INT, `oldid` INT)  BEGIN
	update habitaciones
    set idHabitacion=idhabitacion,
    Tipo=tipo,
    RegTempe=regtempe,
    Precio=Precio,
    Alojamiento=alojamiento,
    Keeper=keeper
    where habitaciones.idHabitacion =oldid ;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `modhuespedes` (`idhuesped` INT, `nombre` VARCHAR(45), `direccion` VARCHAR(45), `telefono` VARCHAR(45), `origen` VARCHAR(45), `oldid` INT)  BEGIN
	update huespedes
    set idHuesped=idhuespes,
    Nombre=nombre,
    Direccion=direccion,
    Telefono=telefono,
    Origen=origen
    where huespedes.idHuesped =oldid ;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `modinscripciones` (IN `idactividad` INT, IN `idalojamiento` INT, IN `idhuesped` INT, IN `oldidoldidActividad` INT, IN `oldidAlojamiento` INT, IN `oldidHuesped` INT)  BEGIN
	update inscripciones
    set idActividad=idactividad,
    idAlojamiento=idalojamiento,
    idHuesped=idhuesped
    where inscripciones.idAlojamiento=oldidAlojamiento
    and inscripciones.idActividad=oldidActividad
    and inscripciones.idHuesped=oldidHuesped;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `modregistro` (IN `idhuesped` INT, IN `idhabitacion` INT, IN `fechain` VARCHAR(45), IN `fechaout` VARCHAR(45), IN `cuenta` VARCHAR(45), IN `oldidhabitacion` INT, IN `oldidhuesped` INT)  BEGIN
	update registros
    set idHuesped=idhuesped,
    idHabitacion=idhabitacion,
    FechaIn=fechain,
    FechaOut=fechaout,
    Cuenta=cuenta
    where registros.idHabitacion=oldidHabitacion
    and registros.idHuesped= oldidHuesped ;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `newactividad` (IN `idactividad` INT, IN `nombre` VARCHAR(50), IN `descripcion` VARCHAR(50), IN `dificultad` VARCHAR(45), IN `coordinador` INT)  BEGIN
	insert into actividad(idActividad,Nombre,Descripcion,Dificultad,coordinador)
    values (idactividad,nombre,descripcion,dificultad,coordinador);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `newalojamiento` (`idalojamiento` INT, `nombre` VARCHAR(45), `direccion` VARCHAR(45), `telefono` VARCHAR(45), `num_habitaciones` VARCHAR(45), `contacto` INT)  BEGIN
	insert into alojamientos (idAlojamiento,Nombre,Direccion,Telefono,Num_Habitaciones,contacto)
    values (idalojamiento ,nombre ,direccion ,telefono ,num_habitaciones ,contacto);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `newcronograma` (`idactividad` INT, `idalojamiento` INT, `dia` VARCHAR(45))  BEGIN
	insert into cronogramas (idActividad,idAlojamiento,Dia)
    values (idactividad ,idalojamiento ,dia);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `newempleado` (`idempleado` INT, `nombre` VARCHAR(50), `direccion` VARCHAR(50), `telefono` VARCHAR(45), `alojamiento` INT, `cargo` VARCHAR(45))  BEGIN	
	insert into empleados (idEmpleado,Nombre,Direccion,Telefono,Alojamiento,Cargo)
    values (idempleado,nombre,direccion,telefono,alojamiento,cargo);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `newhabitacion` (`idhabitacion` INT, `tipo` VARCHAR(45), `regtempe` VARCHAR(45), `precio` VARCHAR(45), `alojamiento` INT, `keeper` INT)  BEGIN
	insert into habitaciones (idHabitacion,Tipo,RegTempe,Precio,Alojamiento,Keeper)
    values (idhabitacion,tipo,regtempe,precio,alojamiento,keeper);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `newhuesped` (`idhuesped` INT, `nombre` VARCHAR(45), `direccion` VARCHAR(45), `telefono` VARCHAR(45), `origen` VARCHAR(45))  BEGIN
	insert into huespedes (idHuesped,Nombre,Direccion,Telefono,Origen)
    values (idhuesped,nombre,direccion,telefono,origen);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `newinscripcion` (`idactividad` INT, `idalojamiento` INT, `idhuesped` INT)  BEGIN
	insert into inscripciones (idActividad,idAlojamiento,idHuesped)
    values (idactividad,idalojamiento,idhuesped);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `newregistro` (`idhuesped` INT, `idhabitacion` INT, `fechain` VARCHAR(45), `fechaout` VARCHAR(45), `cuenta` VARCHAR(45))  BEGIN
	insert into registros (idHuesped,idHabitacion,FechaIn,FechaOut,Cuenta)
    values (idhuesped,idhabitacion,fechain,fechaout,cuenta);
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `actividad`
--

CREATE TABLE `actividad` (
  `idActividad` int(11) NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Descripcion` varchar(50) DEFAULT NULL,
  `Dificultad` varchar(50) NOT NULL,
  `Coordinador` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `actividad`
--

INSERT INTO `actividad` (`idActividad`, `Nombre`, `Descripcion`, `Dificultad`, `Coordinador`) VALUES
(3010, 'Juliancho', 'Coder', '', NULL),
(3110, 'Julian2', 'Otra', 'Too hard', NULL),
(12345, 'Julian', 'descriptiontest', '', NULL),
(45454, '123', 'asda', '', NULL),
(656565, 'asda', 'asdasd', '', NULL),
(895462, 'Davids', 'ssss', '5', NULL),
(5555555, 'fag', 'vdf', '', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alojamientos`
--

CREATE TABLE `alojamientos` (
  `idAlojamiento` int(11) NOT NULL,
  `Nombre` varchar(45) NOT NULL,
  `Direccion` varchar(45) NOT NULL,
  `Telefono` varchar(45) NOT NULL,
  `Num_Habitaciones` varchar(45) NOT NULL,
  `Contacto` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `alojamientos`
--

INSERT INTO `alojamientos` (`idAlojamiento`, `Nombre`, `Direccion`, `Telefono`, `Num_Habitaciones`, `Contacto`) VALUES
(123, 'Julian Camilo', 'Calle4', '1231212312', '123', NULL),
(343433454, 'sequeraalojamiento', 'direcciondesutia', 'telefonodesutia', '5', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cronogramas`
--

CREATE TABLE `cronogramas` (
  `idActividad` int(11) NOT NULL,
  `idAlojamiento` int(11) NOT NULL,
  `Dia` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `cronogramas`
--

INSERT INTO `cronogramas` (`idActividad`, `idAlojamiento`, `Dia`) VALUES
(895462, 343433454, 'noviembresinti');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

CREATE TABLE `empleados` (
  `idEmpleado` int(11) NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Direccion` varchar(70) NOT NULL,
  `Telefono` varchar(45) NOT NULL,
  `Alojamiento` int(11) DEFAULT NULL,
  `Cargo` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleados` (`idEmpleado`, `Nombre`, `Direccion`, `Telefono`, `Alojamiento`, `Cargo`) VALUES
(123, 'Julian camilo', 'Calle4', '12312', NULL, 'Coder'),
(44444, 'daniel', 'ffss', '4345678', NULL, 'ddd');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `habitaciones`
--

CREATE TABLE `habitaciones` (
  `idHabitacion` int(11) NOT NULL,
  `Tipo` varchar(45) NOT NULL,
  `RegTempe` varchar(45) NOT NULL,
  `Precio` varchar(45) NOT NULL,
  `Alojamiento` int(11) DEFAULT NULL,
  `Keeper` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `habitaciones`
--

INSERT INTO `habitaciones` (`idHabitacion`, `Tipo`, `RegTempe`, `Precio`, `Alojamiento`, `Keeper`) VALUES
(5555, 'gtthf', 'ffff', 'ffff', NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `huespedes`
--

CREATE TABLE `huespedes` (
  `idHuesped` int(11) NOT NULL,
  `Nombre` varchar(45) NOT NULL,
  `Direccion` varchar(45) NOT NULL,
  `Telefono` varchar(45) NOT NULL,
  `Origen` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `huespedes`
--

INSERT INTO `huespedes` (`idHuesped`, `Nombre`, `Direccion`, `Telefono`, `Origen`) VALUES
(666, 'hhh', '', '', ''),
(2222, 'www', 'ddd', 'ff', 'fff');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inscripciones`
--

CREATE TABLE `inscripciones` (
  `idActividad` int(11) NOT NULL,
  `idAlojamiento` int(11) NOT NULL,
  `idHuesped` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `inscripciones`
--

INSERT INTO `inscripciones` (`idActividad`, `idAlojamiento`, `idHuesped`) VALUES
(895462, 2506, 666);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `product`
--

CREATE TABLE `product` (
  `cod` varchar(45) NOT NULL,
  `name` varchar(45) NOT NULL,
  `price` varchar(45) NOT NULL,
  `category` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registros`
--

CREATE TABLE `registros` (
  `idHuesped` int(11) DEFAULT NULL,
  `idHabitacion` int(11) DEFAULT NULL,
  `FechaIn` varchar(45) NOT NULL,
  `FechaOut` varchar(45) NOT NULL,
  `Cuenta` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `registros`
--

INSERT INTO `registros` (`idHuesped`, `idHabitacion`, `FechaIn`, `FechaOut`, `Cuenta`) VALUES
(666, 5555, 'jueves', 'sabado', 'VISA');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `actividad`
--
ALTER TABLE `actividad`
  ADD PRIMARY KEY (`idActividad`),
  ADD UNIQUE KEY `Nombre_UNIQUE` (`Nombre`),
  ADD KEY `ActividadxEmpleados_idx` (`Coordinador`);

--
-- Indices de la tabla `alojamientos`
--
ALTER TABLE `alojamientos`
  ADD PRIMARY KEY (`idAlojamiento`),
  ADD KEY `Alojamientosxempleado_idx` (`Contacto`);

--
-- Indices de la tabla `cronogramas`
--
ALTER TABLE `cronogramas`
  ADD PRIMARY KEY (`idActividad`,`idAlojamiento`),
  ADD KEY `CronogramaxAlojamiento_idx` (`idAlojamiento`);

--
-- Indices de la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`idEmpleado`),
  ADD KEY `EmpleadosxAlojamineto_idx` (`Alojamiento`);

--
-- Indices de la tabla `habitaciones`
--
ALTER TABLE `habitaciones`
  ADD PRIMARY KEY (`idHabitacion`),
  ADD KEY `HabitacionesxAlojamineto_idx` (`Alojamiento`),
  ADD KEY `HabitacionesxEmpleado_idx` (`Keeper`);

--
-- Indices de la tabla `huespedes`
--
ALTER TABLE `huespedes`
  ADD PRIMARY KEY (`idHuesped`);

--
-- Indices de la tabla `inscripciones`
--
ALTER TABLE `inscripciones`
  ADD PRIMARY KEY (`idActividad`,`idAlojamiento`,`idHuesped`),
  ADD KEY `InscripcionesxHuespedes_idx` (`idHuesped`);

--
-- Indices de la tabla `registros`
--
ALTER TABLE `registros`
  ADD KEY `RegistroxHuespede_idx` (`idHuesped`),
  ADD KEY `RegistrosxHabitaciones_idx` (`idHabitacion`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `actividad`
--
ALTER TABLE `actividad`
  ADD CONSTRAINT `ActividadxEmpleados` FOREIGN KEY (`Coordinador`) REFERENCES `empleados` (`idEmpleado`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `alojamientos`
--
ALTER TABLE `alojamientos`
  ADD CONSTRAINT `Alojamientosxempleado` FOREIGN KEY (`Contacto`) REFERENCES `empleados` (`idEmpleado`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `cronogramas`
--
ALTER TABLE `cronogramas`
  ADD CONSTRAINT `cronogramaxactividad` FOREIGN KEY (`idActividad`) REFERENCES `actividad` (`idActividad`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `cronogramaxalojamiento` FOREIGN KEY (`idAlojamiento`) REFERENCES `alojamientos` (`idAlojamiento`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD CONSTRAINT `EmpleadosxAlojamineto` FOREIGN KEY (`Alojamiento`) REFERENCES `alojamientos` (`idAlojamiento`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `habitaciones`
--
ALTER TABLE `habitaciones`
  ADD CONSTRAINT `HabitacionesxAlojamineto` FOREIGN KEY (`Alojamiento`) REFERENCES `alojamientos` (`idAlojamiento`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `HabitacionesxEmpleado` FOREIGN KEY (`Keeper`) REFERENCES `empleados` (`idEmpleado`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `inscripciones`
--
ALTER TABLE `inscripciones`
  ADD CONSTRAINT `InscripcionesxCronograma` FOREIGN KEY (`idActividad`) REFERENCES `cronogramas` (`idActividad`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `InscripcionesxHuespedes` FOREIGN KEY (`idHuesped`) REFERENCES `huespedes` (`idHuesped`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `registros`
--
ALTER TABLE `registros`
  ADD CONSTRAINT `RegistrosxHabitaciones` FOREIGN KEY (`idHabitacion`) REFERENCES `habitaciones` (`idHabitacion`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `RegistroxHuespede` FOREIGN KEY (`idHuesped`) REFERENCES `huespedes` (`idHuesped`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
