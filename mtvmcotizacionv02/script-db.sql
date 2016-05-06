CREATE DATABASE  IF NOT EXISTS `db_mtvmcotizacionv2` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci */;
USE `db_mtvmcotizacionv2`;
-- MySQL dump 10.13  Distrib 5.6.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: db_mtvmcotizacionv2
-- ------------------------------------------------------
-- Server version 5.6.21-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `almacen_almacen`
--

DROP TABLE IF EXISTS `almacen_almacen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `almacen_almacen` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `almacen` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `ventas` tinyint(1) NOT NULL,
  `compras` tinyint(1) NOT NULL,
  `consumo` tinyint(1) NOT NULL,
  `produccion` tinyint(1) NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `almacen` (`almacen`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `almacen_almacen`
--

LOCK TABLES `almacen_almacen` WRITE;
/*!40000 ALTER TABLE `almacen_almacen` DISABLE KEYS */;
/*!40000 ALTER TABLE `almacen_almacen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `almacen_tipodemovimiento`
--

DROP TABLE IF EXISTS `almacen_tipodemovimiento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `almacen_tipodemovimiento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_de_movimiento` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `sentido` tinyint(1) NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tipo_de_movimiento` (`tipo_de_movimiento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `almacen_tipodemovimiento`
--

LOCK TABLES `almacen_tipodemovimiento` WRITE;
/*!40000 ALTER TABLE `almacen_tipodemovimiento` DISABLE KEYS */;
/*!40000 ALTER TABLE `almacen_tipodemovimiento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `almacen_unidad`
--

DROP TABLE IF EXISTS `almacen_unidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `almacen_unidad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `unidad` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `nombre` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unidad` (`unidad`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `almacen_unidad`
--

LOCK TABLES `almacen_unidad` WRITE;
/*!40000 ALTER TABLE `almacen_unidad` DISABLE KEYS */;
INSERT INTO `almacen_unidad` VALUES (1,'Und','Unidad',''),(2,'h/h','Hora hombre',''),(3,'Ser','Servicio',''),(4,'Ton','Tonelada',''),(5,'Kg','Kilogramo',''),(6,'m','Metro',''),(7,'cm','Centímetro',''),(8,'Pqt','Paquete',''),(9,'Rol','Rollo',''),(10,'Caj','Caja',''),(11,'Bul','Bulto',''),(12,'Pza','Pieza',''),(13,'m3','Metros cúbicos','Metros cúbicos'),(14,'km','Kilometros','kilometros');
/*!40000 ALTER TABLE `almacen_unidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ambiente_ambiente`
--

DROP TABLE IF EXISTS `ambiente_ambiente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ambiente_ambiente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ambiente` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `conteo_de_ambientes` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ambiente` (`ambiente`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ambiente_ambiente`
--

LOCK TABLES `ambiente_ambiente` WRITE;
/*!40000 ALTER TABLE `ambiente_ambiente` DISABLE KEYS */;
INSERT INTO `ambiente_ambiente` VALUES (1,'Ático','Es un ambiente en la parte superior de una casa',0),(2,'Baño principal','Es un ambiente',0),(3,'Baño auxiliar','Es un ambiente',0),(4,'Baño de visitas','Es un ambiente',0),(5,'Bodega','b',0),(6,'Cocina','cocina',0),(7,'Comedor principal','b',0),(8,'Comedor diario','b',0),(9,'Escritorio / Oficce','b',1),(10,'Habitación principal','Habitación',1),(11,'Habitación auxiliar','Habitación',1),(12,'Habitación de Servicio','Habitación',1),(13,'Hall de entrada','b',1),(14,'Jardin delantero','b',0),(15,'Jardin trasero','b',0),(16,'Lavadero','b',0),(17,'Living','living',1),(18,'Living - Comedor','b',0),(19,'Patio','b',0),(20,'Playroom','b',0),(21,'Sala de TV / Cine','b',0),(22,'Garage','Es un ambiente',0);
/*!40000 ALTER TABLE `ambiente_ambiente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ambiente_ambienteestadoderegistro`
--

DROP TABLE IF EXISTS `ambiente_ambienteestadoderegistro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ambiente_ambienteestadoderegistro` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `observacion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `predefinido` tinyint(1) NOT NULL,
  `ambiente_id` int(11) NOT NULL,
  `estado_de_registro_id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ambiente_ambientees_ambiente_id_67ba8244_fk_ambiente_ambiente_id` (`ambiente_id`),
  KEY `D93d7cce868903bfea993e76d58ab1bf` (`estado_de_registro_id`),
  KEY `ambiente_ambienteestadodereg_usuario_id_7ecc6c66_fk_auth_user_id` (`usuario_id`),
  CONSTRAINT `D93d7cce868903bfea993e76d58ab1bf` FOREIGN KEY (`estado_de_registro_id`) REFERENCES `estadoderegistro_estadoderegistro` (`id`),
  CONSTRAINT `ambiente_ambientees_ambiente_id_67ba8244_fk_ambiente_ambiente_id` FOREIGN KEY (`ambiente_id`) REFERENCES `ambiente_ambiente` (`id`),
  CONSTRAINT `ambiente_ambienteestadodereg_usuario_id_7ecc6c66_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ambiente_ambienteestadoderegistro`
--

LOCK TABLES `ambiente_ambienteestadoderegistro` WRITE;
/*!40000 ALTER TABLE `ambiente_ambienteestadoderegistro` DISABLE KEYS */;
INSERT INTO `ambiente_ambienteestadoderegistro` VALUES (1,'2016-02-02','',1,1,1,2);
/*!40000 ALTER TABLE `ambiente_ambienteestadoderegistro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ambiente_ambienteportipodeinmueble`
--

DROP TABLE IF EXISTS `ambiente_ambienteportipodeinmueble`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ambiente_ambienteportipodeinmueble` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `predeterminado` tinyint(1) NOT NULL,
  `ambiente_id` int(11) NOT NULL,
  `especificacion_de_inmueble_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ambiente_ambientepo_ambiente_id_54c5d766_fk_ambiente_ambiente_id` (`ambiente_id`),
  KEY `fe059b1ce4f5505b0f091cb268cacc86` (`especificacion_de_inmueble_id`),
  CONSTRAINT `ambiente_ambientepo_ambiente_id_54c5d766_fk_ambiente_ambiente_id` FOREIGN KEY (`ambiente_id`) REFERENCES `ambiente_ambiente` (`id`),
  CONSTRAINT `fe059b1ce4f5505b0f091cb268cacc86` FOREIGN KEY (`especificacion_de_inmueble_id`) REFERENCES `direccion_especificaciondeinmueble` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ambiente_ambienteportipodeinmueble`
--

LOCK TABLES `ambiente_ambienteportipodeinmueble` WRITE;
/*!40000 ALTER TABLE `ambiente_ambienteportipodeinmueble` DISABLE KEYS */;
INSERT INTO `ambiente_ambienteportipodeinmueble` VALUES (1,1,10,1),(2,1,17,1),(3,0,6,1),(4,0,10,3),(5,0,2,3),(6,0,11,3),(7,0,6,3),(8,0,17,3),(9,1,9,2),(10,1,2,2),(11,1,13,2);
/*!40000 ALTER TABLE `ambiente_ambienteportipodeinmueble` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_43977543_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_43977543_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_5984fec9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissio_content_type_id_83dc67c_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=349 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add Pais',7,'add_pais'),(20,'Can change Pais',7,'change_pais'),(21,'Can delete Pais',7,'delete_pais'),(22,'Can add Provincia',8,'add_provincia'),(23,'Can change Provincia',8,'change_provincia'),(24,'Can delete Provincia',8,'delete_provincia'),(25,'Can add Ciudad',9,'add_ciudad'),(26,'Can change Ciudad',9,'change_ciudad'),(27,'Can delete Ciudad',9,'delete_ciudad'),(28,'Can add Barrio',10,'add_barrio'),(29,'Can change Barrio',10,'change_barrio'),(30,'Can delete Barrio',10,'delete_barrio'),(31,'Can add Dirección',11,'add_direccion'),(32,'Can change Dirección',11,'change_direccion'),(33,'Can delete Dirección',11,'delete_direccion'),(34,'Can add Tipo de edificación',12,'add_tipodeedificacion'),(35,'Can change Tipo de edificación',12,'change_tipodeedificacion'),(36,'Can delete Tipo de edificación',12,'delete_tipodeedificacion'),(37,'Can add Edificación',13,'add_edificacion'),(38,'Can change Edificación',13,'change_edificacion'),(39,'Can delete Edificación',13,'delete_edificacion'),(40,'Can add Tipo de ascensor',14,'add_tipodeascensor'),(41,'Can change Tipo de ascensor',14,'change_tipodeascensor'),(42,'Can delete Tipo de ascensor',14,'delete_tipodeascensor'),(43,'Can add Ascensor',15,'add_ascensor'),(44,'Can change Ascensor',15,'change_ascensor'),(45,'Can delete Ascensor',15,'delete_ascensor'),(46,'Can add Tipo de inmueble',16,'add_tipodeinmueble'),(47,'Can change Tipo de inmueble',16,'change_tipodeinmueble'),(48,'Can delete Tipo de inmueble',16,'delete_tipodeinmueble'),(49,'Can add Especificación de inmueble',17,'add_especificaciondeinmueble'),(50,'Can change Especificación de inmueble',17,'change_especificaciondeinmueble'),(51,'Can delete Especificación de inmueble',17,'delete_especificaciondeinmueble'),(52,'Can add Inmueble',18,'add_inmueble'),(53,'Can change Inmueble',18,'change_inmueble'),(54,'Can delete Inmueble',18,'delete_inmueble'),(55,'Can add Horario disponible',19,'add_horariodisponible'),(56,'Can change Horario disponible',19,'change_horariodisponible'),(57,'Can delete Horario disponible',19,'delete_horariodisponible'),(58,'Can add Calle',20,'add_calle'),(59,'Can change Calle',20,'change_calle'),(60,'Can delete Calle',20,'delete_calle'),(61,'Can add ambiente',21,'add_ambiente'),(62,'Can change ambiente',21,'change_ambiente'),(63,'Can delete ambiente',21,'delete_ambiente'),(64,'Can add Ambiente por tipo inmueble',22,'add_ambienteportipodeinmueble'),(65,'Can change Ambiente por tipo inmueble',22,'change_ambienteportipodeinmueble'),(66,'Can delete Ambiente por tipo inmueble',22,'delete_ambienteportipodeinmueble'),(67,'Can add Estado de registro de ambiente',23,'add_ambienteestadoderegistro'),(68,'Can change Estado de registro de ambiente',23,'change_ambienteestadoderegistro'),(69,'Can delete Estado de registro de ambiente',23,'delete_ambienteestadoderegistro'),(70,'Can add Sexo',24,'add_sexo'),(71,'Can change Sexo',24,'change_sexo'),(72,'Can delete Sexo',24,'delete_sexo'),(73,'Can add Estado civil',25,'add_estadocivil'),(74,'Can change Estado civil',25,'change_estadocivil'),(75,'Can delete Estado civil',25,'delete_estadocivil'),(76,'Can add Tipo de cliente',26,'add_tipodecliente'),(77,'Can change Tipo de cliente',26,'change_tipodecliente'),(78,'Can delete Tipo de cliente',26,'delete_tipodecliente'),(79,'Can add Tipo de relacion',27,'add_tipoderelacion'),(80,'Can change Tipo de relacion',27,'change_tipoderelacion'),(81,'Can delete Tipo de relacion',27,'delete_tipoderelacion'),(82,'Can add Tipo de información de contacto',28,'add_tipodeinformaciondecontacto'),(83,'Can change Tipo de información de contacto',28,'change_tipodeinformaciondecontacto'),(84,'Can delete Tipo de información de contacto',28,'delete_tipodeinformaciondecontacto'),(85,'Can add Cliente',29,'add_cliente'),(86,'Can change Cliente',29,'change_cliente'),(87,'Can delete Cliente',29,'delete_cliente'),(88,'Can add Contacto',30,'add_contacto'),(89,'Can change Contacto',30,'change_contacto'),(90,'Can delete Contacto',30,'delete_contacto'),(91,'Can add Información de contacto',31,'add_informaciondecontacto'),(92,'Can change Información de contacto',31,'change_informaciondecontacto'),(93,'Can delete Información de contacto',31,'delete_informaciondecontacto'),(94,'Can add Dirección del cliente',32,'add_clientedireccion'),(95,'Can change Dirección del cliente',32,'change_clientedireccion'),(96,'Can delete Dirección del cliente',32,'delete_clientedireccion'),(97,'Can add Estado de registro de cliente',33,'add_clienteestadoderegistro'),(98,'Can change Estado de registro de cliente',33,'change_clienteestadoderegistro'),(99,'Can delete Estado de registro de cliente',33,'delete_clienteestadoderegistro'),(100,'Can add Contenedor',34,'add_contenedor'),(101,'Can change Contenedor',34,'change_contenedor'),(102,'Can delete Contenedor',34,'delete_contenedor'),(103,'Can add Contenedor tipico por mueble',35,'add_contenedortipicopormueble'),(104,'Can change Contenedor tipico por mueble',35,'change_contenedortipicopormueble'),(105,'Can delete Contenedor tipico por mueble',35,'delete_contenedortipicopormueble'),(106,'Can add Tipo de mueble',36,'add_tipodemueble'),(107,'Can change Tipo de mueble',36,'change_tipodemueble'),(108,'Can delete Tipo de mueble',36,'delete_tipodemueble'),(109,'Can add Mueble',37,'add_mueble'),(110,'Can change Mueble',37,'change_mueble'),(111,'Can delete Mueble',37,'delete_mueble'),(112,'Can add Especificación del mueble',38,'add_especificaciondemueble'),(113,'Can change Especificación del mueble',38,'change_especificaciondemueble'),(114,'Can delete Especificación del mueble',38,'delete_especificaciondemueble'),(115,'Can add Mueble por ambiente',39,'add_muebleporambiente'),(116,'Can change Mueble por ambiente',39,'change_muebleporambiente'),(117,'Can delete Mueble por ambiente',39,'delete_muebleporambiente'),(118,'Can add Tipo de documento',40,'add_tipodedocumento'),(119,'Can change Tipo de documento',40,'change_tipodedocumento'),(120,'Can delete Tipo de documento',40,'delete_tipodedocumento'),(121,'Can add Estado de documento',41,'add_estadodedocumento'),(122,'Can change Estado de documento',41,'change_estadodedocumento'),(123,'Can delete Estado de documento',41,'delete_estadodedocumento'),(124,'Can add Estado',42,'add_estado'),(125,'Can change Estado',42,'change_estado'),(126,'Can delete Estado',42,'delete_estado'),(127,'Can add Estado de registro',43,'add_estadoderegistro'),(128,'Can change Estado de registro',43,'change_estadoderegistro'),(129,'Can delete Estado de registro',43,'delete_estadoderegistro'),(130,'Can add Complejidad y riesgo',44,'add_complejidadriesgo'),(131,'Can change Complejidad y riesgo',44,'change_complejidadriesgo'),(132,'Can delete Complejidad y riesgo',44,'delete_complejidadriesgo'),(133,'Can add Nivel de complejidad y riesgo',45,'add_nivelcomplejidadriesgo'),(134,'Can change Nivel de complejidad y riesgo',45,'change_nivelcomplejidadriesgo'),(135,'Can delete Nivel de complejidad y riesgo',45,'delete_nivelcomplejidadriesgo'),(136,'Can add Tipo de mensaje',46,'add_tipodemensaje'),(137,'Can change Tipo de mensaje',46,'change_tipodemensaje'),(138,'Can delete Tipo de mensaje',46,'delete_tipodemensaje'),(139,'Can add Mensaje',47,'add_mensaje'),(140,'Can change Mensaje',47,'change_mensaje'),(141,'Can delete Mensaje',47,'delete_mensaje'),(142,'Can add empresa',48,'add_empresa'),(143,'Can change empresa',48,'change_empresa'),(144,'Can delete empresa',48,'delete_empresa'),(145,'Can add Personalización Visual',49,'add_personalizacionvisual'),(146,'Can change Personalización Visual',49,'change_personalizacionvisual'),(147,'Can delete Personalización Visual',49,'delete_personalizacionvisual'),(148,'Can add Variente Visual',50,'add_variantevisual'),(149,'Can change Variente Visual',50,'change_variantevisual'),(150,'Can delete Variente Visual',50,'delete_variantevisual'),(151,'Can add Detalle de la variente visual',51,'add_variantevisualdetalle'),(152,'Can change Detalle de la variente visual',51,'change_variantevisualdetalle'),(153,'Can delete Detalle de la variente visual',51,'delete_variantevisualdetalle'),(154,'Can add Dato precargado',52,'add_datosprecargado'),(155,'Can change Dato precargado',52,'change_datosprecargado'),(156,'Can delete Dato precargado',52,'delete_datosprecargado'),(157,'Can add Moneda',53,'add_moneda'),(158,'Can change Moneda',53,'change_moneda'),(159,'Can delete Moneda',53,'delete_moneda'),(160,'Can add Medio',54,'add_medio'),(161,'Can change Medio',54,'change_medio'),(162,'Can delete Medio',54,'delete_medio'),(163,'Can add Medio especifico',55,'add_medioespecifico'),(164,'Can change Medio especifico',55,'change_medioespecifico'),(165,'Can delete Medio especifico',55,'delete_medioespecifico'),(166,'Can add Tipo de referido',56,'add_tipodereferido'),(167,'Can change Tipo de referido',56,'change_tipodereferido'),(168,'Can delete Tipo de referido',56,'delete_tipodereferido'),(169,'Can add Alianza',57,'add_alianza'),(170,'Can change Alianza',57,'change_alianza'),(171,'Can delete Alianza',57,'delete_alianza'),(172,'Can add Estado de registro de alianza',58,'add_alianzaestado'),(173,'Can change Estado de registro de alianza',58,'change_alianzaestado'),(174,'Can delete Estado de registro de alianza',58,'delete_alianzaestado'),(175,'Can add Institución',59,'add_institucion'),(176,'Can change Institución',59,'change_institucion'),(177,'Can delete Institución',59,'delete_institucion'),(178,'Can add Persona',60,'add_personaaliado'),(179,'Can change Persona',60,'change_personaaliado'),(180,'Can delete Persona',60,'delete_personaaliado'),(181,'Can add Persona',61,'add_fuentedepromocion'),(182,'Can change Persona',61,'change_fuentedepromocion'),(183,'Can delete Persona',61,'delete_fuentedepromocion'),(184,'Can add menu',62,'add_menu'),(185,'Can change menu',62,'change_menu'),(186,'Can delete menu',62,'delete_menu'),(187,'Can add Menu favorito',63,'add_menufavorito'),(188,'Can change Menu favorito',63,'change_menufavorito'),(189,'Can delete Menu favorito',63,'delete_menufavorito'),(190,'Can add Cargo de trabajador',64,'add_cargotrabajador'),(191,'Can change Cargo de trabajador',64,'change_cargotrabajador'),(192,'Can delete Cargo de trabajador',64,'delete_cargotrabajador'),(193,'Can add Trabajador',65,'add_trabajador'),(194,'Can change Trabajador',65,'change_trabajador'),(195,'Can delete Trabajador',65,'delete_trabajador'),(196,'Can add Vehículo',66,'add_vehiculo'),(197,'Can change Vehículo',66,'change_vehiculo'),(198,'Can delete Vehículo',66,'delete_vehiculo'),(199,'Can add Vehículo',67,'add_detalledevehiculo'),(200,'Can change Vehículo',67,'change_detalledevehiculo'),(201,'Can delete Vehículo',67,'delete_detalledevehiculo'),(202,'Can add Estado de registro de vehículo',68,'add_estadodevehiculo'),(203,'Can change Estado de registro de vehículo',68,'change_estadodevehiculo'),(204,'Can delete Estado de registro de vehículo',68,'delete_estadodevehiculo'),(205,'Can add Chofer asignado',69,'add_choferasignado'),(206,'Can change Chofer asignado',69,'change_choferasignado'),(207,'Can delete Chofer asignado',69,'delete_choferasignado'),(208,'Can add Relación',70,'add_relacion'),(209,'Can change Relación',70,'change_relacion'),(210,'Can delete Relación',70,'delete_relacion'),(214,'Can add Herramienta',72,'add_herramienta'),(215,'Can change Herramienta',72,'change_herramienta'),(216,'Can delete Herramienta',72,'delete_herramienta'),(217,'Can add Dotación básica de camión',73,'add_dotacionbasicadecamion'),(218,'Can change Dotación básica de camión',73,'change_dotacionbasicadecamion'),(219,'Can delete Dotación básica de camión',73,'delete_dotacionbasicadecamion'),(220,'Can add Tipo de material ',74,'add_tipodematerial'),(221,'Can change Tipo de material ',74,'change_tipodematerial'),(222,'Can delete Tipo de material ',74,'delete_tipodematerial'),(223,'Can add Material ',75,'add_material'),(224,'Can change Material ',75,'change_material'),(225,'Can delete Material ',75,'delete_material'),(226,'Can add Precio del material',76,'add_preciodematerial'),(227,'Can change Precio del material',76,'change_preciodematerial'),(228,'Can delete Precio del material',76,'delete_preciodematerial'),(229,'Can add Material por servicio',77,'add_materialesporservicio'),(230,'Can change Material por servicio',77,'change_materialesporservicio'),(231,'Can delete Material por servicio',77,'delete_materialesporservicio'),(232,'Can add Servicio',78,'add_servicio'),(233,'Can change Servicio',78,'change_servicio'),(234,'Can delete Servicio',78,'delete_servicio'),(235,'Can add Complejidad del servicio',79,'add_complejidadservicio'),(236,'Can change Complejidad del servicio',79,'change_complejidadservicio'),(237,'Can delete Complejidad del servicio',79,'delete_complejidadservicio'),(238,'Can add Precio del servicio',80,'add_preciodeservicio'),(239,'Can change Precio del servicio',80,'change_preciodeservicio'),(240,'Can delete Precio del servicio',80,'delete_preciodeservicio'),(241,'Can add Herramienta por servicio',81,'add_herramientasporservicio'),(242,'Can change Herramienta por servicio',81,'change_herramientasporservicio'),(243,'Can delete Herramienta por servicio',81,'delete_herramientasporservicio'),(244,'Can add Tipo de documento impreso',82,'add_tipodedocumentoimpreso'),(245,'Can change Tipo de documento impreso',82,'change_tipodedocumentoimpreso'),(246,'Can delete Tipo de documento impreso',82,'delete_tipodedocumentoimpreso'),(247,'Can add Talonario',83,'add_talonario'),(248,'Can change Talonario',83,'change_talonario'),(249,'Can delete Talonario',83,'delete_talonario'),(250,'Can add Documento del talonario',84,'add_documentodeltalonario'),(251,'Can change Documento del talonario',84,'change_documentodeltalonario'),(252,'Can delete Documento del talonario',84,'delete_documentodeltalonario'),(253,'Can add Estado del talonario',85,'add_talonarioestado'),(254,'Can change Estado del talonario',85,'change_talonarioestado'),(255,'Can delete Estado del talonario',85,'delete_talonarioestado'),(256,'Can add Trazabilidad del talonario',86,'add_trazabilidadtalonario'),(257,'Can change Trazabilidad del talonario',86,'change_trazabilidadtalonario'),(258,'Can delete Trazabilidad del talonario',86,'delete_trazabilidadtalonario'),(259,'Can add Estado del documento del talonario',87,'add_documentodeltalonarioestado'),(260,'Can change Estado del documento del talonario',87,'change_documentodeltalonarioestado'),(261,'Can delete Estado del documento del talonario',87,'delete_documentodeltalonarioestado'),(262,'Can add Estado de registro de trabajador',88,'add_trabajadorestadoderegistro'),(263,'Can change Estado de registro de trabajador',88,'change_trabajadorestadoderegistro'),(264,'Can delete Estado de registro de trabajador',88,'delete_trabajadorestadoderegistro'),(265,'Can add Widget',89,'add_widget'),(266,'Can change Widget',89,'change_widget'),(267,'Can delete Widget',89,'delete_widget'),(268,'Can add Cotizador',90,'add_cotizador'),(269,'Can change Cotizador',90,'change_cotizador'),(270,'Can delete Cotizador',90,'delete_cotizador'),(271,'Can add Tipo de dirección',91,'add_tipodireccion'),(272,'Can change Tipo de dirección',91,'change_tipodireccion'),(273,'Can delete Tipo de dirección',91,'delete_tipodireccion'),(274,'Can add Fecha de cotización',92,'add_fechadecotizacion'),(275,'Can change Fecha de cotización',92,'change_fechadecotizacion'),(276,'Can delete Fecha de cotización',92,'delete_fechadecotizacion'),(277,'Can add Concepto de cotización',93,'add_conceptodecotizacion'),(278,'Can change Concepto de cotización',93,'change_conceptodecotizacion'),(279,'Can delete Concepto de cotización',93,'delete_conceptodecotizacion'),(280,'Can add Tipo de abono',94,'add_tipoabono'),(281,'Can change Tipo de abono',94,'change_tipoabono'),(282,'Can delete Tipo de abono',94,'delete_tipoabono'),(283,'Can add Cotización',95,'add_cotizacion'),(284,'Can change Cotización',95,'change_cotizacion'),(285,'Can delete Cotización',95,'delete_cotizacion'),(286,'Can add Dirección de la cotización',96,'add_cotizaciondireccion'),(287,'Can change Dirección de la cotización',96,'change_cotizaciondireccion'),(288,'Can delete Dirección de la cotización',96,'delete_cotizaciondireccion'),(289,'Can add Ambiente de la cotización',97,'add_cotizacionambiente'),(290,'Can change Ambiente de la cotización',97,'change_cotizacionambiente'),(291,'Can delete Ambiente de la cotización',97,'delete_cotizacionambiente'),(292,'Can add Mueble de la cotización',98,'add_cotizacionmueble'),(293,'Can change Mueble de la cotización',98,'change_cotizacionmueble'),(294,'Can delete Mueble de la cotización',98,'delete_cotizacionmueble'),(295,'Can add Contenedor del mueble',99,'add_contenedormueble'),(296,'Can change Contenedor del mueble',99,'change_contenedormueble'),(297,'Can delete Contenedor del mueble',99,'delete_contenedormueble'),(298,'Can add Servicio del mueble',100,'add_serviciomueble'),(299,'Can change Servicio del mueble',100,'change_serviciomueble'),(300,'Can delete Servicio del mueble',100,'delete_serviciomueble'),(301,'Can add Servicio de la cotización',101,'add_cotizacionservicio'),(302,'Can change Servicio de la cotización',101,'change_cotizacionservicio'),(303,'Can delete Servicio de la cotización',101,'delete_cotizacionservicio'),(304,'Can add Material de la cotización',102,'add_cotizacionmaterial'),(305,'Can change Material de la cotización',102,'change_cotizacionmaterial'),(306,'Can delete Material de la cotización',102,'delete_cotizacionmaterial'),(307,'Can add Herramienta de la cotización',103,'add_cotizacionherramienta'),(308,'Can change Herramienta de la cotización',103,'change_cotizacionherramienta'),(309,'Can delete Herramienta de la cotización',103,'delete_cotizacionherramienta'),(310,'Can add Concepto de la cotización',104,'add_cotizacionpresupuesto'),(311,'Can change Concepto de la cotización',104,'change_cotizacionpresupuesto'),(312,'Can delete Concepto de la cotización',104,'delete_cotizacionpresupuesto'),(313,'Can add Concepto de la cotización',105,'add_abono'),(314,'Can change Concepto de la cotización',105,'change_abono'),(315,'Can delete Concepto de la cotización',105,'delete_abono'),(316,'Can add Situación de la cotización',106,'add_cotizacioncomplejidadriesgo'),(317,'Can change Situación de la cotización',106,'change_cotizacioncomplejidadriesgo'),(318,'Can delete Situación de la cotización',106,'delete_cotizacioncomplejidadriesgo'),(319,'Can add Observación de la cotización',107,'add_cotizacionbitacora'),(320,'Can change Observación de la cotización',107,'change_cotizacionbitacora'),(321,'Can delete Observación de la cotización',107,'delete_cotizacionbitacora'),(322,'Can add Observación de la cotización',108,'add_cotizacionhistoricofecha'),(323,'Can change Observación de la cotización',108,'change_cotizacionhistoricofecha'),(324,'Can delete Observación de la cotización',108,'delete_cotizacionhistoricofecha'),(325,'Can add Estado de la cotización',109,'add_cotizacionestado'),(326,'Can change Estado de la cotización',109,'change_cotizacionestado'),(327,'Can delete Estado de la cotización',109,'delete_cotizacionestado'),(328,'Can add Argumento de venta',110,'add_argumentodeventa'),(329,'Can change Argumento de venta',110,'change_argumentodeventa'),(330,'Can delete Argumento de venta',110,'delete_argumentodeventa'),(331,'Can add Servicio tipico por mueble',111,'add_serviciotipicopormueble'),(332,'Can change Servicio tipico por mueble',111,'change_serviciotipicopormueble'),(333,'Can delete Servicio tipico por mueble',111,'delete_serviciotipicopormueble'),(334,'Can add Almacen',112,'add_almacen'),(335,'Can change Almacen',112,'change_almacen'),(336,'Can delete Almacen',112,'delete_almacen'),(337,'Can add Tipo de movimiento',113,'add_tipodemovimiento'),(338,'Can change Tipo de movimiento',113,'change_tipodemovimiento'),(339,'Can delete Tipo de movimiento',113,'delete_tipodemovimiento'),(340,'Can add Unidad',114,'add_unidad'),(341,'Can change Unidad',114,'change_unidad'),(342,'Can delete Unidad',114,'delete_unidad'),(343,'Can add cors model',115,'add_corsmodel'),(344,'Can change cors model',115,'change_corsmodel'),(345,'Can delete cors model',115,'delete_corsmodel'),(346,'Can add Tipo de contenido',116,'add_tipodecontenido'),(347,'Can change Tipo de contenido',116,'change_tipodecontenido'),(348,'Can delete Tipo de contenido',116,'delete_tipodecontenido');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `first_name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `last_name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$20000$gmTsKWYIalwb$28hXj6/6CuPT7gfGkAWwMxAGwSHxAZLkJW7vBuK0Xv0=','2016-05-03 13:45:48.648891',1,'admin','','','yusnelvy@gmail.com',1,1,'2016-02-02 16:19:15.301642'),(2,'pbkdf2_sha256$20000$j3U2c7T8YCuU$8AJhxiMIMGqZWuWIQIvjWGXgsSfpWo0A0kIFDgnNkPY=',NULL,0,'std','Estandar','Estandar','',0,1,'2016-02-02 19:02:27.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_3e51de8_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_3e51de8_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_5f9d723b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_31b05428_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_perm_permission_id_31b05428_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_5482c657_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente_cliente`
--

DROP TABLE IF EXISTS `cliente_cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cliente_cliente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_de_cliente_id` int(11) NOT NULL,
  `cuit` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `nombre` varchar(300) COLLATE utf8_unicode_ci NOT NULL,
  `observaciones` longtext COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cliente_cliente_71de9ee1` (`tipo_de_cliente_id`),
  CONSTRAINT `cliente__tipo_de_cliente_id_250b6bc4_fk_cliente_tipodecliente_id` FOREIGN KEY (`tipo_de_cliente_id`) REFERENCES `cliente_tipodecliente` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente_cliente`
--

LOCK TABLES `cliente_cliente` WRITE;
/*!40000 ALTER TABLE `cliente_cliente` DISABLE KEYS */;
/*!40000 ALTER TABLE `cliente_cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente_clientedireccion`
--

DROP TABLE IF EXISTS `cliente_clientedireccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cliente_clientedireccion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cliente_id` int(11) NOT NULL,
  `direccion_id` int(11) NOT NULL,
  `detalle_de_direccion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `titulo_de_direccion` varchar(300) COLLATE utf8_unicode_ci NOT NULL,
  `edificacion_id` int(11) DEFAULT NULL,
  `inmueble_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cliente_clientedireccion_cliente_id_8ef11b5_uniq` (`cliente_id`,`direccion_id`),
  KEY `cliente_clientedirecci_cliente_id_32bc0fa6_fk_cliente_cliente_id` (`cliente_id`),
  KEY `cliente_cliented_direccion_id_7b41af54_fk_direccion_direccion_id` (`direccion_id`),
  KEY `cliente_clientedireccion_1b0d6425` (`edificacion_id`),
  KEY `cliente_clientedireccion_9846f97f` (`inmueble_id`),
  CONSTRAINT `cliente_clie_edificacion_id_3fdfea0c_fk_direccion_edificacion_id` FOREIGN KEY (`edificacion_id`) REFERENCES `direccion_edificacion` (`id`),
  CONSTRAINT `cliente_cliented_direccion_id_7b41af54_fk_direccion_direccion_id` FOREIGN KEY (`direccion_id`) REFERENCES `direccion_direccion` (`id`),
  CONSTRAINT `cliente_clientedire_inmueble_id_770c355_fk_direccion_inmueble_id` FOREIGN KEY (`inmueble_id`) REFERENCES `direccion_inmueble` (`id`),
  CONSTRAINT `cliente_clientedirecci_cliente_id_32bc0fa6_fk_cliente_cliente_id` FOREIGN KEY (`cliente_id`) REFERENCES `cliente_cliente` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente_clientedireccion`
--

LOCK TABLES `cliente_clientedireccion` WRITE;
/*!40000 ALTER TABLE `cliente_clientedireccion` DISABLE KEYS */;
/*!40000 ALTER TABLE `cliente_clientedireccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente_clienteestadoderegistro`
--

DROP TABLE IF EXISTS `cliente_clienteestadoderegistro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cliente_clienteestadoderegistro` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `observacion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `predefinido` tinyint(1) NOT NULL,
  `cliente_id` int(11) NOT NULL,
  `estado_de_registro_id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cliente_clienteestadode_cliente_id_9c11206_fk_cliente_cliente_id` (`cliente_id`),
  KEY `D4d86929a144360114024833a4a6a464` (`estado_de_registro_id`),
  KEY `cliente_clienteestadoderegis_usuario_id_3ee09c27_fk_auth_user_id` (`usuario_id`),
  CONSTRAINT `D4d86929a144360114024833a4a6a464` FOREIGN KEY (`estado_de_registro_id`) REFERENCES `estadoderegistro_estadoderegistro` (`id`),
  CONSTRAINT `cliente_clienteestadode_cliente_id_9c11206_fk_cliente_cliente_id` FOREIGN KEY (`cliente_id`) REFERENCES `cliente_cliente` (`id`),
  CONSTRAINT `cliente_clienteestadoderegis_usuario_id_3ee09c27_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente_clienteestadoderegistro`
--

LOCK TABLES `cliente_clienteestadoderegistro` WRITE;
/*!40000 ALTER TABLE `cliente_clienteestadoderegistro` DISABLE KEYS */;
/*!40000 ALTER TABLE `cliente_clienteestadoderegistro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente_contacto`
--

DROP TABLE IF EXISTS `cliente_contacto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cliente_contacto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dni` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `nombre` varchar(300) COLLATE utf8_unicode_ci NOT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `observaciones` longtext COLLATE utf8_unicode_ci NOT NULL,
  `cliente_id` int(11) NOT NULL,
  `estado_civil_id` int(11) NOT NULL,
  `sexo_id` int(11) NOT NULL,
  `tipo_de_relacion_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cliente_contacto_cliente_id_9788045_fk_cliente_cliente_id` (`cliente_id`),
  KEY `cliente_contacto_5c2a6c5d` (`estado_civil_id`),
  KEY `cliente_contacto_68bc6daa` (`sexo_id`),
  KEY `cliente_contacto_e918cfd2` (`tipo_de_relacion_id`),
  CONSTRAINT `client_tipo_de_relacion_id_428407fc_fk_cliente_tipoderelacion_id` FOREIGN KEY (`tipo_de_relacion_id`) REFERENCES `cliente_tipoderelacion` (`id`),
  CONSTRAINT `cliente_conta_estado_civil_id_3d70fc69_fk_cliente_estadocivil_id` FOREIGN KEY (`estado_civil_id`) REFERENCES `cliente_estadocivil` (`id`),
  CONSTRAINT `cliente_contacto_cliente_id_9788045_fk_cliente_cliente_id` FOREIGN KEY (`cliente_id`) REFERENCES `cliente_cliente` (`id`),
  CONSTRAINT `cliente_contacto_sexo_id_1ad394_fk_cliente_sexo_id` FOREIGN KEY (`sexo_id`) REFERENCES `cliente_sexo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente_contacto`
--

LOCK TABLES `cliente_contacto` WRITE;
/*!40000 ALTER TABLE `cliente_contacto` DISABLE KEYS */;
/*!40000 ALTER TABLE `cliente_contacto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente_estadocivil`
--

DROP TABLE IF EXISTS `cliente_estadocivil`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cliente_estadocivil` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `estado_civil` varchar(25) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `estado_civil` (`estado_civil`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente_estadocivil`
--

LOCK TABLES `cliente_estadocivil` WRITE;
/*!40000 ALTER TABLE `cliente_estadocivil` DISABLE KEYS */;
INSERT INTO `cliente_estadocivil` VALUES (2,'Casado'),(3,'Divorciado'),(1,'Soltero'),(4,'Viudo');
/*!40000 ALTER TABLE `cliente_estadocivil` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente_informaciondecontacto`
--

DROP TABLE IF EXISTS `cliente_informaciondecontacto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cliente_informaciondecontacto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `informacion_de_contacto` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `contacto_id` int(11) NOT NULL,
  `tipo_de_informacion_de_contacto_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cliente_informaciond_contacto_id_2708f1d4_fk_cliente_contacto_id` (`contacto_id`),
  KEY `cliente_informaciondecontacto_6cac9fa7` (`tipo_de_informacion_de_contacto_id`),
  CONSTRAINT `cliente_informaciond_contacto_id_2708f1d4_fk_cliente_contacto_id` FOREIGN KEY (`contacto_id`) REFERENCES `cliente_contacto` (`id`),
  CONSTRAINT `dbe79d3bf1b4128a4db405ed1d89e4e2` FOREIGN KEY (`tipo_de_informacion_de_contacto_id`) REFERENCES `cliente_tipodeinformaciondecontacto` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente_informaciondecontacto`
--

LOCK TABLES `cliente_informaciondecontacto` WRITE;
/*!40000 ALTER TABLE `cliente_informaciondecontacto` DISABLE KEYS */;
/*!40000 ALTER TABLE `cliente_informaciondecontacto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente_sexo`
--

DROP TABLE IF EXISTS `cliente_sexo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cliente_sexo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sexo` varchar(25) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sexo` (`sexo`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente_sexo`
--

LOCK TABLES `cliente_sexo` WRITE;
/*!40000 ALTER TABLE `cliente_sexo` DISABLE KEYS */;
INSERT INTO `cliente_sexo` VALUES (1,'Femenino'),(2,'Masculino');
/*!40000 ALTER TABLE `cliente_sexo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente_tipodecliente`
--

DROP TABLE IF EXISTS `cliente_tipodecliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cliente_tipodecliente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_de_cliente` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tipo_de_cliente` (`tipo_de_cliente`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente_tipodecliente`
--

LOCK TABLES `cliente_tipodecliente` WRITE;
/*!40000 ALTER TABLE `cliente_tipodecliente` DISABLE KEYS */;
INSERT INTO `cliente_tipodecliente` VALUES (1,'Particular','Es una persona'),(2,'Empresa','Es una empresa'),(3,'Otros','Es un tipo de cliente');
/*!40000 ALTER TABLE `cliente_tipodecliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente_tipodeinformaciondecontacto`
--

DROP TABLE IF EXISTS `cliente_tipodeinformaciondecontacto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cliente_tipodeinformaciondecontacto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_de_informacion_de_contacto` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tipo_de_informacion_de_contacto` (`tipo_de_informacion_de_contacto`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente_tipodeinformaciondecontacto`
--

LOCK TABLES `cliente_tipodeinformaciondecontacto` WRITE;
/*!40000 ALTER TABLE `cliente_tipodeinformaciondecontacto` DISABLE KEYS */;
INSERT INTO `cliente_tipodeinformaciondecontacto` VALUES (1,'Teléfono','Teléfono de contacto'),(2,'Email','Email de contacto');
/*!40000 ALTER TABLE `cliente_tipodeinformaciondecontacto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente_tipoderelacion`
--

DROP TABLE IF EXISTS `cliente_tipoderelacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cliente_tipoderelacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_de_relacion` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tipo_de_relacion` (`tipo_de_relacion`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente_tipoderelacion`
--

LOCK TABLES `cliente_tipoderelacion` WRITE;
/*!40000 ALTER TABLE `cliente_tipoderelacion` DISABLE KEYS */;
INSERT INTO `cliente_tipoderelacion` VALUES (1,'cliente','cliente '),(2,'familiar','Familiar del cliente'),(3,'Propietario','Es el dueño de una empresa o institución'),(4,'Empleado','Es un trabajador de una empresa o institución');
/*!40000 ALTER TABLE `cliente_tipoderelacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `complejidadriesgo_complejidadriesgo`
--

DROP TABLE IF EXISTS `complejidadriesgo_complejidadriesgo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `complejidadriesgo_complejidadriesgo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `situacion` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `factor_complejidad` int(11) NOT NULL,
  `factor_riesgo` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `situacion` (`situacion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `complejidadriesgo_complejidadriesgo`
--

LOCK TABLES `complejidadriesgo_complejidadriesgo` WRITE;
/*!40000 ALTER TABLE `complejidadriesgo_complejidadriesgo` DISABLE KEYS */;
/*!40000 ALTER TABLE `complejidadriesgo_complejidadriesgo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `complejidadriesgo_nivelcomplejidadriesgo`
--

DROP TABLE IF EXISTS `complejidadriesgo_nivelcomplejidadriesgo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `complejidadriesgo_nivelcomplejidadriesgo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nivel_complejidad_riesgo` varchar(25) COLLATE utf8_unicode_ci NOT NULL,
  `factor_inicial` int(11) NOT NULL,
  `factor_final` int(11) NOT NULL,
  `porcentaje` decimal(7,2) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nivel_complejidad_riesgo` (`nivel_complejidad_riesgo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `complejidadriesgo_nivelcomplejidadriesgo`
--

LOCK TABLES `complejidadriesgo_nivelcomplejidadriesgo` WRITE;
/*!40000 ALTER TABLE `complejidadriesgo_nivelcomplejidadriesgo` DISABLE KEYS */;
/*!40000 ALTER TABLE `complejidadriesgo_nivelcomplejidadriesgo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contenedor_contenedor`
--

DROP TABLE IF EXISTS `contenedor_contenedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contenedor_contenedor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `contenedor` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `capacidad_de_volumen` decimal(7,2) NOT NULL,
  `capacidad_de_peso` decimal(7,2) NOT NULL,
  `ancho` int(11) NOT NULL,
  `largo` int(11) NOT NULL,
  `alto` int(11) NOT NULL,
  `volumen_en_camion` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `contenedor` (`contenedor`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contenedor_contenedor`
--

LOCK TABLES `contenedor_contenedor` WRITE;
/*!40000 ALTER TABLE `contenedor_contenedor` DISABLE KEYS */;
INSERT INTO `contenedor_contenedor` VALUES (1,'Canasto','canasto',0.12,22.00,40,70,40,1),(2,'Canasto PC','Canasto PC',0.20,22.00,40,40,70,1),(3,'Bolsa / Bulto','Bolsa / Bulto',1.00,1.00,1,1,1,2),(4,'Ropero','Ropero',0.80,25.00,50,50,100,5);
/*!40000 ALTER TABLE `contenedor_contenedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contenedor_contenedortipicopormueble`
--

DROP TABLE IF EXISTS `contenedor_contenedortipicopormueble`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contenedor_contenedortipicopormueble` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cantidad` int(11) NOT NULL,
  `contenedor_id` int(11) NOT NULL,
  `especificacion_de_mueble_id` int(11) NOT NULL,
  `tipo_de_contenido_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `contenedor_co_contenedor_id_2fe1a6a0_fk_contenedor_contenedor_id` (`contenedor_id`),
  KEY `f0858580c71e366be272be91ad1ccac5` (`especificacion_de_mueble_id`),
  KEY `contenedor_contenedortipicopormueble_d504855e` (`tipo_de_contenido_id`),
  CONSTRAINT `c_tipo_de_contenido_id_29692e5f_fk_contenedor_tipodecontenido_id` FOREIGN KEY (`tipo_de_contenido_id`) REFERENCES `contenedor_tipodecontenido` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `contenedor_co_contenedor_id_2fe1a6a0_fk_contenedor_contenedor_id` FOREIGN KEY (`contenedor_id`) REFERENCES `contenedor_contenedor` (`id`),
  CONSTRAINT `f0858580c71e366be272be91ad1ccac5` FOREIGN KEY (`especificacion_de_mueble_id`) REFERENCES `mueble_especificaciondemueble` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contenedor_contenedortipicopormueble`
--

LOCK TABLES `contenedor_contenedortipicopormueble` WRITE;
/*!40000 ALTER TABLE `contenedor_contenedortipicopormueble` DISABLE KEYS */;
INSERT INTO `contenedor_contenedortipicopormueble` VALUES (1,2,1,3,1),(2,1,1,2,1);
/*!40000 ALTER TABLE `contenedor_contenedortipicopormueble` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contenedor_tipodecontenido`
--

DROP TABLE IF EXISTS `contenedor_tipodecontenido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contenedor_tipodecontenido` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contenedor_tipodecontenido`
--

LOCK TABLES `contenedor_tipodecontenido` WRITE;
/*!40000 ALTER TABLE `contenedor_tipodecontenido` DISABLE KEYS */;
INSERT INTO `contenedor_tipodecontenido` VALUES (1,'ropa','');
/*!40000 ALTER TABLE `contenedor_tipodecontenido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `corsheaders_corsmodel`
--

DROP TABLE IF EXISTS `corsheaders_corsmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `corsheaders_corsmodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cors` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `corsheaders_corsmodel`
--

LOCK TABLES `corsheaders_corsmodel` WRITE;
/*!40000 ALTER TABLE `corsheaders_corsmodel` DISABLE KEYS */;
/*!40000 ALTER TABLE `corsheaders_corsmodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacionweb_abono`
--

DROP TABLE IF EXISTS `cotizacionweb_abono`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cotizacionweb_abono` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha_registro` date NOT NULL,
  `hora_registro` time NOT NULL,
  `monto_pagado` decimal(9,2) NOT NULL,
  `monto_cotizacion` decimal(9,2) NOT NULL,
  `banco` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `numero_transaccion` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `cotizacion_id` int(11) NOT NULL,
  `tipo_abono_id` int(11) NOT NULL,
  `usuario_registro_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cotizacionweb_abono_1b44b901` (`cotizacion_id`),
  KEY `cotizacionweb_abono_6bab39c7` (`tipo_abono_id`),
  KEY `cotizacionweb_abono_8a4ba14d` (`usuario_registro_id`),
  CONSTRAINT `cotizacion_cotizacion_id_15c9bd6b_fk_cotizacionweb_cotizacion_id` FOREIGN KEY (`cotizacion_id`) REFERENCES `cotizacionweb_cotizacion` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cotizacionw_tipo_abono_id_72503b5e_fk_cotizacionweb_tipoabono_id` FOREIGN KEY (`tipo_abono_id`) REFERENCES `cotizacionweb_tipoabono` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cotizacionweb_abono_usuario_registro_id_5f7cc074_fk_auth_user_id` FOREIGN KEY (`usuario_registro_id`) REFERENCES `auth_user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacionweb_abono`
--

LOCK TABLES `cotizacionweb_abono` WRITE;
/*!40000 ALTER TABLE `cotizacionweb_abono` DISABLE KEYS */;
/*!40000 ALTER TABLE `cotizacionweb_abono` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacionweb_argumentodeventa`
--

DROP TABLE IF EXISTS `cotizacionweb_argumentodeventa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cotizacionweb_argumentodeventa` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `valor` decimal(9,2) NOT NULL,
  `aplicado` tinyint(1) NOT NULL,
  `cotizacion_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cotizacionweb_argumentodeventa_1b44b901` (`cotizacion_id`),
  CONSTRAINT `cotizacionw_cotizacion_id_943dedc_fk_cotizacionweb_cotizacion_id` FOREIGN KEY (`cotizacion_id`) REFERENCES `cotizacionweb_cotizacion` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacionweb_argumentodeventa`
--

LOCK TABLES `cotizacionweb_argumentodeventa` WRITE;
/*!40000 ALTER TABLE `cotizacionweb_argumentodeventa` DISABLE KEYS */;
/*!40000 ALTER TABLE `cotizacionweb_argumentodeventa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacionweb_conceptodecotizacion`
--

DROP TABLE IF EXISTS `cotizacionweb_conceptodecotizacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cotizacionweb_conceptodecotizacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `concepto` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `positivo` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `concepto` (`concepto`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacionweb_conceptodecotizacion`
--

LOCK TABLES `cotizacionweb_conceptodecotizacion` WRITE;
/*!40000 ALTER TABLE `cotizacionweb_conceptodecotizacion` DISABLE KEYS */;
INSERT INTO `cotizacionweb_conceptodecotizacion` VALUES (1,'Mudanza','mudanza',0);
/*!40000 ALTER TABLE `cotizacionweb_conceptodecotizacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacionweb_contenedormueble`
--

DROP TABLE IF EXISTS `cotizacionweb_contenedormueble`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cotizacionweb_contenedormueble` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_contenedor` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `cantidad` int(11) NOT NULL,
  `contenedor_id` int(11) NOT NULL,
  `cotizacion_mueble_id` int(11) NOT NULL,
  `tipo_de_contenido_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cotizacionweb_contenedormueble_c01c3066` (`cotizacion_mueble_id`),
  KEY `cotizacionweb_contenedor_id_30b38ea8_fk_contenedor_contenedor_id` (`contenedor_id`),
  KEY `cotizacionweb_contenedormueble_d504855e` (`tipo_de_contenido_id`),
  CONSTRAINT `D2ccfd9b63e1a06a74a0f3e32d7460ff` FOREIGN KEY (`cotizacion_mueble_id`) REFERENCES `cotizacionweb_cotizacionmueble` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `co_tipo_de_contenido_id_2a19fcd_fk_contenedor_tipodecontenido_id` FOREIGN KEY (`tipo_de_contenido_id`) REFERENCES `contenedor_tipodecontenido` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cotizacionweb_contenedor_id_30b38ea8_fk_contenedor_contenedor_id` FOREIGN KEY (`contenedor_id`) REFERENCES `contenedor_contenedor` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacionweb_contenedormueble`
--

LOCK TABLES `cotizacionweb_contenedormueble` WRITE;
/*!40000 ALTER TABLE `cotizacionweb_contenedormueble` DISABLE KEYS */;
/*!40000 ALTER TABLE `cotizacionweb_contenedormueble` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacionweb_cotizacion`
--

DROP TABLE IF EXISTS `cotizacionweb_cotizacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cotizacionweb_cotizacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `numero_contrato` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `numero_cotizacion` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `nombre_cliente` varchar(300) COLLATE utf8_unicode_ci NOT NULL,
  `fecha_de_cotizacion` date NOT NULL,
  `hora_de_cotizacion` time NOT NULL,
  `tiempo_carga` decimal(7,2) NOT NULL,
  `total_recorrido_tiempo` decimal(7,2) NOT NULL,
  `total_recorrido_km` decimal(7,2) NOT NULL,
  `nivel_de_complejidad_riesgo` varchar(25) COLLATE utf8_unicode_ci NOT NULL,
  `porcentaje_complejidad_riesgo` decimal(7,2) NOT NULL,
  `cliente_id` int(11) NOT NULL,
  `como_abona_id` int(11) DEFAULT NULL,
  `cotizador_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `cotizacionweb_cotizacion_0f3c5103` (`cotizador_id`),
  KEY `cotizacionweb_cotizacion_af5f3f96` (`como_abona_id`),
  KEY `cotizacionweb_cotizaci_cliente_id_666eca08_fk_cliente_cliente_id` (`cliente_id`),
  CONSTRAINT `cotizacionw_como_abona_id_2d98d780_fk_cotizacionweb_tipoabono_id` FOREIGN KEY (`como_abona_id`) REFERENCES `cotizacionweb_tipoabono` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cotizacionweb_co_cotizador_id_2b7fef0f_fk_cotizador_cotizador_id` FOREIGN KEY (`cotizador_id`) REFERENCES `cotizador_cotizador` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cotizacionweb_cotizaci_cliente_id_666eca08_fk_cliente_cliente_id` FOREIGN KEY (`cliente_id`) REFERENCES `cliente_cliente` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacionweb_cotizacion`
--

LOCK TABLES `cotizacionweb_cotizacion` WRITE;
/*!40000 ALTER TABLE `cotizacionweb_cotizacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `cotizacionweb_cotizacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacionweb_cotizacionambiente`
--

DROP TABLE IF EXISTS `cotizacionweb_cotizacionambiente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cotizacionweb_cotizacionambiente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `observaciones` longtext COLLATE utf8_unicode_ci NOT NULL,
  `ambiente_id` int(11) NOT NULL,
  `direccion_origen_id` int(11) NOT NULL,
  `nombre` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cotizacionweb_cotizacionambiente_c6b82c03` (`direccion_origen_id`),
  KEY `cotizacionweb_cotiz_ambiente_id_3ae16d07_fk_ambiente_ambiente_id` (`ambiente_id`),
  CONSTRAINT `cotizacionweb_cotiz_ambiente_id_3ae16d07_fk_ambiente_ambiente_id` FOREIGN KEY (`ambiente_id`) REFERENCES `ambiente_ambiente` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `f2802a01778778411a3d1cad076278a1` FOREIGN KEY (`direccion_origen_id`) REFERENCES `cotizacionweb_cotizaciondireccion` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacionweb_cotizacionambiente`
--

LOCK TABLES `cotizacionweb_cotizacionambiente` WRITE;
/*!40000 ALTER TABLE `cotizacionweb_cotizacionambiente` DISABLE KEYS */;
/*!40000 ALTER TABLE `cotizacionweb_cotizacionambiente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacionweb_cotizacionbitacora`
--

DROP TABLE IF EXISTS `cotizacionweb_cotizacionbitacora`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cotizacionweb_cotizacionbitacora` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha_registro` date NOT NULL,
  `hora_registro` time NOT NULL,
  `observacion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `cotizacion_id` int(11) NOT NULL,
  `usuario_registro_id` int(11) NOT NULL,
  `origen_de_registro` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cotizacion_cotizacion_id_5e1a934a_fk_cotizacionweb_cotizacion_id` (`cotizacion_id`),
  KEY `cotizacionweb_cotiz_usuario_registro_id_556f26a1_fk_auth_user_id` (`usuario_registro_id`),
  CONSTRAINT `cotizacion_cotizacion_id_5e1a934a_fk_cotizacionweb_cotizacion_id` FOREIGN KEY (`cotizacion_id`) REFERENCES `cotizacionweb_cotizacion` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cotizacionweb_cotiz_usuario_registro_id_556f26a1_fk_auth_user_id` FOREIGN KEY (`usuario_registro_id`) REFERENCES `auth_user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacionweb_cotizacionbitacora`
--

LOCK TABLES `cotizacionweb_cotizacionbitacora` WRITE;
/*!40000 ALTER TABLE `cotizacionweb_cotizacionbitacora` DISABLE KEYS */;
/*!40000 ALTER TABLE `cotizacionweb_cotizacionbitacora` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacionweb_cotizacioncomplejidadriesgo`
--

DROP TABLE IF EXISTS `cotizacionweb_cotizacioncomplejidadriesgo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cotizacionweb_cotizacioncomplejidadriesgo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `situacion` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `factor_complejidad` int(11) NOT NULL,
  `factor_riesgo` int(11) NOT NULL,
  `observacion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `cotizacion_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cotizacion_cotizacion_id_67973ce4_fk_cotizacionweb_cotizacion_id` (`cotizacion_id`),
  CONSTRAINT `cotizacion_cotizacion_id_67973ce4_fk_cotizacionweb_cotizacion_id` FOREIGN KEY (`cotizacion_id`) REFERENCES `cotizacionweb_cotizacion` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacionweb_cotizacioncomplejidadriesgo`
--

LOCK TABLES `cotizacionweb_cotizacioncomplejidadriesgo` WRITE;
/*!40000 ALTER TABLE `cotizacionweb_cotizacioncomplejidadriesgo` DISABLE KEYS */;
/*!40000 ALTER TABLE `cotizacionweb_cotizacioncomplejidadriesgo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacionweb_cotizaciondireccion`
--

DROP TABLE IF EXISTS `cotizacionweb_cotizaciondireccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cotizacionweb_cotizaciondireccion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `direccion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `orden` int(11) NOT NULL,
  `nombre_de_edificio` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `tipo_de_edificacion` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `rampa` tinyint(1) NOT NULL,
  `distancia_del_vehiculo` int(11) NOT NULL,
  `cantidad_pisos` int(11) NOT NULL,
  `escalera_estrecha` tinyint(1) NOT NULL,
  `escalera_inclinada` tinyint(1) NOT NULL,
  `escalon_grande` tinyint(1) NOT NULL,
  `especificacion_de_inmueble` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `numero_de_inmueble` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `numero_de_pisos` int(11) NOT NULL,
  `nombre_piso` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `cantidad_de_ambientes` int(11) NOT NULL,
  `pisos_por_escalera` int(11) NOT NULL,
  `numero_de_plantas` int(11) NOT NULL,
  `total_m2` decimal(7,2) DEFAULT NULL,
  `baulera` tinyint(1) NOT NULL,
  `volumen_baulera` decimal(7,2) DEFAULT NULL,
  `clientedireccion_id` int(11) NOT NULL,
  `cotizacion_id` int(11) NOT NULL,
  `tipo_direccion_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cotizacionweb_cotizaciondireccion_aa27db54` (`tipo_direccion_id`),
  KEY `coti_clientedireccion_id_79150be3_fk_cliente_clientedireccion_id` (`clientedireccion_id`),
  KEY `cotizacionw_cotizacion_id_933f1ff_fk_cotizacionweb_cotizacion_id` (`cotizacion_id`),
  CONSTRAINT `cot_tipo_direccion_id_638481ad_fk_cotizacionweb_tipodireccion_id` FOREIGN KEY (`tipo_direccion_id`) REFERENCES `cotizacionweb_tipodireccion` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `coti_clientedireccion_id_79150be3_fk_cliente_clientedireccion_id` FOREIGN KEY (`clientedireccion_id`) REFERENCES `cliente_clientedireccion` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cotizacionw_cotizacion_id_933f1ff_fk_cotizacionweb_cotizacion_id` FOREIGN KEY (`cotizacion_id`) REFERENCES `cotizacionweb_cotizacion` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacionweb_cotizaciondireccion`
--

LOCK TABLES `cotizacionweb_cotizaciondireccion` WRITE;
/*!40000 ALTER TABLE `cotizacionweb_cotizaciondireccion` DISABLE KEYS */;
/*!40000 ALTER TABLE `cotizacionweb_cotizaciondireccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacionweb_cotizacionestado`
--

DROP TABLE IF EXISTS `cotizacionweb_cotizacionestado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cotizacionweb_cotizacionestado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha_registro` datetime NOT NULL,
  `observacion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `predefinido` tinyint(1) NOT NULL,
  `cotizacion_id` int(11) NOT NULL,
  `estado_de_documento_id` int(11) DEFAULT NULL,
  `estado_de_registro_id` int(11) DEFAULT NULL,
  `usuario_registro_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ace6965b1bb6487bc2291914a281beea` (`estado_de_documento_id`),
  KEY `cotizacion_cotizacion_id_4b862875_fk_cotizacionweb_cotizacion_id` (`cotizacion_id`),
  KEY `cotizacionweb_cotiz_usuario_registro_id_5ce6b26c_fk_auth_user_id` (`usuario_registro_id`),
  KEY `e0745648b4a35fef40096a62e648eaeb` (`estado_de_registro_id`),
  CONSTRAINT `ace6965b1bb6487bc2291914a281beea` FOREIGN KEY (`estado_de_documento_id`) REFERENCES `gestiondedocumento_estadodedocumento` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cotizacion_cotizacion_id_4b862875_fk_cotizacionweb_cotizacion_id` FOREIGN KEY (`cotizacion_id`) REFERENCES `cotizacionweb_cotizacion` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cotizacionweb_cotiz_usuario_registro_id_5ce6b26c_fk_auth_user_id` FOREIGN KEY (`usuario_registro_id`) REFERENCES `auth_user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `e0745648b4a35fef40096a62e648eaeb` FOREIGN KEY (`estado_de_registro_id`) REFERENCES `estadoderegistro_estadoderegistro` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacionweb_cotizacionestado`
--

LOCK TABLES `cotizacionweb_cotizacionestado` WRITE;
/*!40000 ALTER TABLE `cotizacionweb_cotizacionestado` DISABLE KEYS */;
/*!40000 ALTER TABLE `cotizacionweb_cotizacionestado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacionweb_cotizacionherramienta`
--

DROP TABLE IF EXISTS `cotizacionweb_cotizacionherramienta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cotizacionweb_cotizacionherramienta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_herramienta` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `cantidad` decimal(7,2) NOT NULL,
  `descripcion_de_cantidad` longtext COLLATE utf8_unicode_ci NOT NULL,
  `cantidad_asignada` decimal(7,2) NOT NULL,
  `cotizacion_id` int(11) NOT NULL,
  `herramienta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cotizacion_herramienta_id_57af3462_fk_herramienta_herramienta_id` (`herramienta_id`),
  KEY `cotizacionw_cotizacion_id_59ed8fc_fk_cotizacionweb_cotizacion_id` (`cotizacion_id`),
  CONSTRAINT `cotizacion_herramienta_id_57af3462_fk_herramienta_herramienta_id` FOREIGN KEY (`herramienta_id`) REFERENCES `herramienta_herramienta` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cotizacionw_cotizacion_id_59ed8fc_fk_cotizacionweb_cotizacion_id` FOREIGN KEY (`cotizacion_id`) REFERENCES `cotizacionweb_cotizacion` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacionweb_cotizacionherramienta`
--

LOCK TABLES `cotizacionweb_cotizacionherramienta` WRITE;
/*!40000 ALTER TABLE `cotizacionweb_cotizacionherramienta` DISABLE KEYS */;
/*!40000 ALTER TABLE `cotizacionweb_cotizacionherramienta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacionweb_cotizacionhistoricofecha`
--

DROP TABLE IF EXISTS `cotizacionweb_cotizacionhistoricofecha`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cotizacionweb_cotizacionhistoricofecha` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_tipo_fecha` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `observacion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `aplicar` tinyint(1) NOT NULL,
  `cotizacion_id` int(11) NOT NULL,
  `tipo_fecha_id` int(11) NOT NULL,
  `usuario_registro_id` int(11) NOT NULL,
  `fecha` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cotizacionweb_cotizacionhistoricofecha_8a4ba14d` (`usuario_registro_id`),
  KEY `cotizacionweb_cotizacionhistoricofecha_a6c39426` (`tipo_fecha_id`),
  KEY `cotizacion_cotizacion_id_19699f72_fk_cotizacionweb_cotizacion_id` (`cotizacion_id`),
  CONSTRAINT `cot_tipo_fecha_id_5a703083_fk_cotizacionweb_fechadecotizacion_id` FOREIGN KEY (`tipo_fecha_id`) REFERENCES `cotizacionweb_fechadecotizacion` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cotizacion_cotizacion_id_19699f72_fk_cotizacionweb_cotizacion_id` FOREIGN KEY (`cotizacion_id`) REFERENCES `cotizacionweb_cotizacion` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cotizacionweb_cotiz_usuario_registro_id_2e44a585_fk_auth_user_id` FOREIGN KEY (`usuario_registro_id`) REFERENCES `auth_user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacionweb_cotizacionhistoricofecha`
--

LOCK TABLES `cotizacionweb_cotizacionhistoricofecha` WRITE;
/*!40000 ALTER TABLE `cotizacionweb_cotizacionhistoricofecha` DISABLE KEYS */;
/*!40000 ALTER TABLE `cotizacionweb_cotizacionhistoricofecha` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacionweb_cotizacionmaterial`
--

DROP TABLE IF EXISTS `cotizacionweb_cotizacionmaterial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cotizacionweb_cotizacionmaterial` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_material` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `cantidad` decimal(7,2) NOT NULL,
  `descripcion_de_cantidad` longtext COLLATE utf8_unicode_ci NOT NULL,
  `cantidad_asignada` decimal(7,2) NOT NULL,
  `precio_unitario` decimal(9,2) NOT NULL,
  `monto_material` decimal(9,2) NOT NULL,
  `monto_material_asignado` decimal(9,2) NOT NULL,
  `peso_unitario` decimal(7,2) NOT NULL,
  `peso_total` decimal(7,2) NOT NULL,
  `inlcuido` tinyint(1) NOT NULL,
  `basico` tinyint(1) NOT NULL,
  `aplicar` tinyint(1) NOT NULL,
  `observacion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `cotizacion_id` int(11) NOT NULL,
  `material_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cotizacion_cotizacion_id_7414ece4_fk_cotizacionweb_cotizacion_id` (`cotizacion_id`),
  KEY `cotizacionweb_cotiz_material_id_7d423cc2_fk_material_material_id` (`material_id`),
  CONSTRAINT `cotizacion_cotizacion_id_7414ece4_fk_cotizacionweb_cotizacion_id` FOREIGN KEY (`cotizacion_id`) REFERENCES `cotizacionweb_cotizacion` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cotizacionweb_cotiz_material_id_7d423cc2_fk_material_material_id` FOREIGN KEY (`material_id`) REFERENCES `material_material` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacionweb_cotizacionmaterial`
--

LOCK TABLES `cotizacionweb_cotizacionmaterial` WRITE;
/*!40000 ALTER TABLE `cotizacionweb_cotizacionmaterial` DISABLE KEYS */;
/*!40000 ALTER TABLE `cotizacionweb_cotizacionmaterial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacionweb_cotizacionmueble`
--

DROP TABLE IF EXISTS `cotizacionweb_cotizacionmueble`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cotizacionweb_cotizacionmueble` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_especificacion_de_mueble` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `ancho` decimal(7,2) NOT NULL,
  `largo` decimal(7,2) NOT NULL,
  `alto` decimal(7,2) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `volumen_en_camion` int(11) NOT NULL,
  `trasladable` tinyint(1) NOT NULL,
  `observaciones` longtext COLLATE utf8_unicode_ci NOT NULL,
  `cotizacion_ambiente_id` int(11) NOT NULL,
  `direccion_destino_id` int(11) NOT NULL,
  `especificacion_de_mueble_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `D11febba5d67d7fc23bc5817c199d7ed` (`direccion_destino_id`),
  KEY `D95cd2ce0b4477fb0d3370badefb1779` (`cotizacion_ambiente_id`),
  KEY `ffd1f2bdc910a4d639dbef5a7ee13781` (`especificacion_de_mueble_id`),
  CONSTRAINT `D11febba5d67d7fc23bc5817c199d7ed` FOREIGN KEY (`direccion_destino_id`) REFERENCES `cotizacionweb_cotizaciondireccion` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `D95cd2ce0b4477fb0d3370badefb1779` FOREIGN KEY (`cotizacion_ambiente_id`) REFERENCES `cotizacionweb_cotizacionambiente` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ffd1f2bdc910a4d639dbef5a7ee13781` FOREIGN KEY (`especificacion_de_mueble_id`) REFERENCES `mueble_especificaciondemueble` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacionweb_cotizacionmueble`
--

LOCK TABLES `cotizacionweb_cotizacionmueble` WRITE;
/*!40000 ALTER TABLE `cotizacionweb_cotizacionmueble` DISABLE KEYS */;
/*!40000 ALTER TABLE `cotizacionweb_cotizacionmueble` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacionweb_cotizacionpresupuesto`
--

DROP TABLE IF EXISTS `cotizacionweb_cotizacionpresupuesto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cotizacionweb_cotizacionpresupuesto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_concepto` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `cantidad` decimal(7,2) NOT NULL,
  `precio_unitario` decimal(9,2) NOT NULL,
  `precio_total` decimal(9,2) NOT NULL,
  `precio_total_asignado` decimal(9,2) NOT NULL,
  `descripcion_precio_total` longtext COLLATE utf8_unicode_ci NOT NULL,
  `concepto_id` int(11) NOT NULL,
  `cotizacion_id` int(11) NOT NULL,
  `unidad_de_medida_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `co_concepto_id_61830244_fk_cotizacionweb_conceptodecotizacion_id` (`concepto_id`),
  KEY `cotizacion_cotizacion_id_25240d8b_fk_cotizacionweb_cotizacion_id` (`cotizacion_id`),
  KEY `cotizacionweb_cotizacionpresupuesto_e3256343` (`unidad_de_medida_id`),
  CONSTRAINT `co_concepto_id_61830244_fk_cotizacionweb_conceptodecotizacion_id` FOREIGN KEY (`concepto_id`) REFERENCES `cotizacionweb_conceptodecotizacion` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cotizacion_cotizacion_id_25240d8b_fk_cotizacionweb_cotizacion_id` FOREIGN KEY (`cotizacion_id`) REFERENCES `cotizacionweb_cotizacion` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cotizacionweb__unidad_de_medida_id_2440215b_fk_almacen_unidad_id` FOREIGN KEY (`unidad_de_medida_id`) REFERENCES `almacen_unidad` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacionweb_cotizacionpresupuesto`
--

LOCK TABLES `cotizacionweb_cotizacionpresupuesto` WRITE;
/*!40000 ALTER TABLE `cotizacionweb_cotizacionpresupuesto` DISABLE KEYS */;
/*!40000 ALTER TABLE `cotizacionweb_cotizacionpresupuesto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacionweb_cotizacionservicio`
--

DROP TABLE IF EXISTS `cotizacionweb_cotizacionservicio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cotizacionweb_cotizacionservicio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_de_servicio` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `complejidad_servicio` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `porcentaje_complejidad` decimal(7,2) NOT NULL,
  `monto_servicio` decimal(9,2) NOT NULL,
  `descripcion_de_monto_servicio` longtext COLLATE utf8_unicode_ci NOT NULL,
  `monto_servicio_asignado` decimal(9,2) NOT NULL,
  `incluido_en_precio` tinyint(1) NOT NULL,
  `aplicar_servicio` tinyint(1) NOT NULL,
  `basico` tinyint(1) NOT NULL,
  `observacion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `cotizacion_id` int(11) NOT NULL,
  `servicio_id` int(11) NOT NULL,
  `cantidad_servicio` decimal(7,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cotizacion_cotizacion_id_11643b24_fk_cotizacionweb_cotizacion_id` (`cotizacion_id`),
  KEY `cotizacionweb_cotizac_servicio_id_67cfe7_fk_servicio_servicio_id` (`servicio_id`),
  CONSTRAINT `cotizacion_cotizacion_id_11643b24_fk_cotizacionweb_cotizacion_id` FOREIGN KEY (`cotizacion_id`) REFERENCES `cotizacionweb_cotizacion` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `cotizacionweb_cotizac_servicio_id_67cfe7_fk_servicio_servicio_id` FOREIGN KEY (`servicio_id`) REFERENCES `servicio_servicio` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacionweb_cotizacionservicio`
--

LOCK TABLES `cotizacionweb_cotizacionservicio` WRITE;
/*!40000 ALTER TABLE `cotizacionweb_cotizacionservicio` DISABLE KEYS */;
/*!40000 ALTER TABLE `cotizacionweb_cotizacionservicio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacionweb_fechadecotizacion`
--

DROP TABLE IF EXISTS `cotizacionweb_fechadecotizacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cotizacionweb_fechadecotizacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_fecha` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `obligatoria` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre_fecha` (`nombre_fecha`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacionweb_fechadecotizacion`
--

LOCK TABLES `cotizacionweb_fechadecotizacion` WRITE;
/*!40000 ALTER TABLE `cotizacionweb_fechadecotizacion` DISABLE KEYS */;
INSERT INTO `cotizacionweb_fechadecotizacion` VALUES (1,'Mudanza',0),(2,'Visita del cotizador',0);
/*!40000 ALTER TABLE `cotizacionweb_fechadecotizacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacionweb_serviciomueble`
--

DROP TABLE IF EXISTS `cotizacionweb_serviciomueble`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cotizacionweb_serviciomueble` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion_servicio` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `cantidad` decimal(7,2) NOT NULL,
  `descripcion_cantidad` longtext COLLATE utf8_unicode_ci NOT NULL,
  `cotizacion_mueble_id` int(11) NOT NULL,
  `servicio_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cotizacionweb_servi_servicio_id_44c35488_fk_servicio_servicio_id` (`servicio_id`),
  KEY `fc55ccae093057d028d502e4c95cf24e` (`cotizacion_mueble_id`),
  CONSTRAINT `cotizacionweb_servi_servicio_id_44c35488_fk_servicio_servicio_id` FOREIGN KEY (`servicio_id`) REFERENCES `servicio_servicio` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fc55ccae093057d028d502e4c95cf24e` FOREIGN KEY (`cotizacion_mueble_id`) REFERENCES `cotizacionweb_cotizacionmueble` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacionweb_serviciomueble`
--

LOCK TABLES `cotizacionweb_serviciomueble` WRITE;
/*!40000 ALTER TABLE `cotizacionweb_serviciomueble` DISABLE KEYS */;
/*!40000 ALTER TABLE `cotizacionweb_serviciomueble` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacionweb_tipoabono`
--

DROP TABLE IF EXISTS `cotizacionweb_tipoabono`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cotizacionweb_tipoabono` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_abono` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tipo_abono` (`tipo_abono`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacionweb_tipoabono`
--

LOCK TABLES `cotizacionweb_tipoabono` WRITE;
/*!40000 ALTER TABLE `cotizacionweb_tipoabono` DISABLE KEYS */;
/*!40000 ALTER TABLE `cotizacionweb_tipoabono` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizacionweb_tipodireccion`
--

DROP TABLE IF EXISTS `cotizacionweb_tipodireccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cotizacionweb_tipodireccion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_direccion` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tipo_direccion` (`tipo_direccion`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizacionweb_tipodireccion`
--

LOCK TABLES `cotizacionweb_tipodireccion` WRITE;
/*!40000 ALTER TABLE `cotizacionweb_tipodireccion` DISABLE KEYS */;
INSERT INTO `cotizacionweb_tipodireccion` VALUES (1,'Origen','El tipo de dirección origen es la dirección de donde se realizara la mudanza'),(2,'Destino','El tipo de dirección destino es la dirección donde se llevara la mudanza');
/*!40000 ALTER TABLE `cotizacionweb_tipodireccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cotizador_cotizador`
--

DROP TABLE IF EXISTS `cotizador_cotizador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cotizador_cotizador` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_trabajador_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cotizador_c_id_trabajador_id_af23de8_fk_trabajador_trabajador_id` (`id_trabajador_id`),
  CONSTRAINT `cotizador_c_id_trabajador_id_af23de8_fk_trabajador_trabajador_id` FOREIGN KEY (`id_trabajador_id`) REFERENCES `trabajador_trabajador` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cotizador_cotizador`
--

LOCK TABLES `cotizador_cotizador` WRITE;
/*!40000 ALTER TABLE `cotizador_cotizador` DISABLE KEYS */;
INSERT INTO `cotizador_cotizador` VALUES (2,1);
/*!40000 ALTER TABLE `cotizador_cotizador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `direccion_ascensor`
--

DROP TABLE IF EXISTS `direccion_ascensor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `direccion_ascensor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cantidad` int(11) NOT NULL,
  `piso_ascensor` int(11) NOT NULL,
  `velocidad_por_piso` decimal(7,2) NOT NULL,
  `ancho` decimal(7,2) NOT NULL,
  `largo` decimal(7,2) NOT NULL,
  `alto` decimal(7,2) NOT NULL,
  `capacidad_carga` decimal(7,2) DEFAULT NULL,
  `edificacion_id` int(11) NOT NULL,
  `tipo_de_ascensor_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `direccion_ascensor_1b0d6425` (`edificacion_id`),
  KEY `direccion_ascensor_2af49ef9` (`tipo_de_ascensor_id`),
  CONSTRAINT `dire_tipo_de_ascensor_id_354d32f5_fk_direccion_tipodeascensor_id` FOREIGN KEY (`tipo_de_ascensor_id`) REFERENCES `direccion_tipodeascensor` (`id`),
  CONSTRAINT `direccion_as_edificacion_id_7944bfb7_fk_direccion_edificacion_id` FOREIGN KEY (`edificacion_id`) REFERENCES `direccion_edificacion` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccion_ascensor`
--

LOCK TABLES `direccion_ascensor` WRITE;
/*!40000 ALTER TABLE `direccion_ascensor` DISABLE KEYS */;
/*!40000 ALTER TABLE `direccion_ascensor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `direccion_barrio`
--

DROP TABLE IF EXISTS `direccion_barrio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `direccion_barrio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `barrio` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `ciudad_id` int(11) NOT NULL,
  `pais_id` int(11) NOT NULL,
  `provincia_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `direccion_barrio_barrio_31e67e64_uniq` (`barrio`,`ciudad_id`),
  KEY `direccion_barrio_0201ed81` (`ciudad_id`),
  KEY `direccion_barrio_847ec16e` (`pais_id`),
  KEY `direccion_barrio_54bf7e76` (`provincia_id`),
  CONSTRAINT `direccion_barrio_ciudad_id_450b5804_fk_direccion_ciudad_id` FOREIGN KEY (`ciudad_id`) REFERENCES `direccion_ciudad` (`id`),
  CONSTRAINT `direccion_barrio_pais_id_5c45b0f3_fk_direccion_pais_id` FOREIGN KEY (`pais_id`) REFERENCES `direccion_pais` (`id`),
  CONSTRAINT `direccion_barrio_provincia_id_6be7d54e_fk_direccion_provincia_id` FOREIGN KEY (`provincia_id`) REFERENCES `direccion_provincia` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccion_barrio`
--

LOCK TABLES `direccion_barrio` WRITE;
/*!40000 ALTER TABLE `direccion_barrio` DISABLE KEYS */;
INSERT INTO `direccion_barrio` VALUES (1,'Agronomía',1,10,1),(2,'Almagro',1,10,1),(3,'Balvanera',1,10,1),(4,'Barracas',1,10,1),(5,'Belgrano',1,10,1),(6,'Boedo',1,10,1),(7,'Caballito',1,10,1),(8,'Chacarita',1,10,1),(9,'Coghlan',1,10,1),(10,'Colegiales',1,10,1),(11,'Constitución',1,10,1),(12,'Flores',1,10,1),(13,'Floresta',1,10,1),(14,'La Boca',1,10,1),(15,'La Paternal',1,10,1),(16,'Liniers',1,10,1),(17,'Mataderos',1,10,1),(18,'Monte Castro',1,10,1),(19,'Monserrat (originalmente llamado Montserrat).',1,10,1),(20,'Nueva Pompeya',1,10,1),(21,'Núñez',1,10,1),(22,'Palermo',1,10,1),(23,'Parque Avellaneda',1,10,1),(24,'Parque Chacabuco',1,10,1),(25,'Parque Chas',1,10,1),(26,'Parque Patricios',1,10,1);
/*!40000 ALTER TABLE `direccion_barrio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `direccion_calle`
--

DROP TABLE IF EXISTS `direccion_calle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `direccion_calle` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `calle` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `ciudad_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `direccion_calle_calle_5c410cfc_uniq` (`calle`,`ciudad_id`),
  KEY `direccion_calle_0201ed81` (`ciudad_id`),
  CONSTRAINT `direccion_calle_ciudad_id_35669a32_fk_direccion_ciudad_id` FOREIGN KEY (`ciudad_id`) REFERENCES `direccion_ciudad` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccion_calle`
--

LOCK TABLES `direccion_calle` WRITE;
/*!40000 ALTER TABLE `direccion_calle` DISABLE KEYS */;
/*!40000 ALTER TABLE `direccion_calle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `direccion_ciudad`
--

DROP TABLE IF EXISTS `direccion_ciudad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `direccion_ciudad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ciudad` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `pais_id` int(11) NOT NULL,
  `provincia_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `direccion_ciudad_ciudad_245cdfbd_uniq` (`ciudad`,`provincia_id`),
  KEY `direccion_ciudad_847ec16e` (`pais_id`),
  KEY `direccion_ciudad_54bf7e76` (`provincia_id`),
  CONSTRAINT `direccion_ciudad_pais_id_652cf141_fk_direccion_pais_id` FOREIGN KEY (`pais_id`) REFERENCES `direccion_pais` (`id`),
  CONSTRAINT `direccion_ciudad_provincia_id_7e6ea766_fk_direccion_provincia_id` FOREIGN KEY (`provincia_id`) REFERENCES `direccion_provincia` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=157 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccion_ciudad`
--

LOCK TABLES `direccion_ciudad` WRITE;
/*!40000 ALTER TABLE `direccion_ciudad` DISABLE KEYS */;
INSERT INTO `direccion_ciudad` VALUES (1,'Buenos Aires',10,2),(2,'Córdoba',10,7),(3,'Rosario',10,22),(4,'La Plata',10,1),(5,'Mar del Plata',10,1),(6,'San Miguel de Tucumán',10,25),(7,'Ciudad de Salta',10,18),(8,'Ciudad de Santa Fe',10,22),(9,'Ciudad de Corrientes',10,8),(10,'Bahía Blanca',10,1),(11,'Resistencia',10,5),(12,'Vicente López',10,1),(13,'Posadas',10,15),(14,'Merlo',10,1),(15,'Paraná',10,9),(16,'San Salvador de Jujuy',10,11),(17,'Quilmes',10,1),(18,'Ciudad de Santiago del Estero',10,23),(19,'Pilar',10,1),(20,'Banfield',10,1),(21,'Guaymallén',10,14),(22,'José C. Paz',10,1),(23,'Lanús',10,1),(24,'Ciudad de Neuquén',10,16),(25,'Ciudad de Formosa',10,10),(26,'Godoy Cruz',10,14),(27,'Las Heras',10,14),(28,'Gregorio de Laferrere',10,1),(29,'Berazategui',10,1),(30,'González Catán',10,1),(31,'San Miguel',10,1),(32,'Ciudad de Río Cuarto',10,7),(33,'Ciudad de San Luis',10,20),(34,'Moreno',10,1),(35,'Concordia',10,9),(36,'Ciudad de La Rioja',10,13),(37,'San Fernando del Valle de Catamarca',10,4),(38,'Comodoro Rivadavia',10,6),(39,'Isidro Casanova',10,1),(40,'San Rafael',10,14),(41,'Ituzaingó',10,1),(42,'San Nicolás de los Arroyos',10,1),(43,'Florencio Varela',10,1),(44,'Ciudad de San Juan',10,19),(45,'Lomas de Zamora',10,1),(46,'Temperley',10,1),(47,'Ciudad de Mendoza',10,14),(48,'Monte Grande',10,1),(49,'Bernal',10,1),(50,'San Justo',10,1),(51,'San Carlos de Bariloche',10,17),(52,'Pergamino',10,1),(53,'Castelar',10,1),(54,'Rafael Castillo',10,1),(55,'Trelew',10,6),(56,'Santa Rosa',10,12),(57,'Tandil',10,1),(58,'Libertad',10,1),(59,'Ramos Mejía',10,1),(60,'Villa Mercedes',10,20),(61,'Río Gallegos',10,21),(62,'Caseros',10,1),(63,'La Banda',10,23),(64,'Trujui',10,1),(65,'Ezeiza',10,1),(66,'Morón',10,1),(67,'Virrey del Pino',10,1),(68,'Maipú',10,14),(69,'Zárate',10,1),(70,'Burzaco',10,1),(71,'Grand Bourg',10,1),(72,'Monte Chingolo',10,1),(73,'Olavarría',10,1),(74,'Rawson',10,6),(75,'Rafaela',10,22),(76,'Junín',10,1),(77,'Remedios de Escalada (Partido de Lanús)',10,1),(78,'La Tablada',10,1),(79,'Campana',10,1),(80,'Presidencia Roque Sáenz Peña',10,5),(81,'Rivadavia',10,19),(82,'Florida (no es ciudad sino barrio)',10,1),(83,'Villa Madero',10,1),(84,'Olivos (no es ciudad sino barrio)',10,1),(85,'Gualeguaychú',10,9),(86,'Villa Gobernador Gálvez',10,22),(87,'Villa Luzuriaga',10,1),(88,'Boulogne Sur Mer',10,1),(89,'Chimbas',10,19),(90,'Ciudadela',10,1),(91,'Luján de Cuyo',10,14),(92,'Ezpeleta',10,1),(93,'Villa María',10,7),(94,'Alderetes',10,7),(95,'General Roca',10,17),(96,'San Fernando',10,1),(97,'Ciudad Evita',10,1),(98,'Venado Tuerto',10,22),(99,'Bella Vista',10,1),(100,'Luján',10,1),(101,'San Ramón de la Nueva Orán',10,18),(102,'Cipolletti',10,17),(103,'Goya',10,8),(104,'Reconquista',10,22),(105,'Wilde',10,1),(106,'Martínez',10,1),(107,'Necochea',10,1),(108,'Don Torcuato',10,1),(109,'Banda del Río Salí',10,25),(110,'Concepción del Uruguay',10,9),(111,'General Rodríguez',10,1),(112,'Villa Tesei',10,1),(113,'Ciudad Jardín El Libertador',10,1),(114,'Villa Carlos Paz',10,7),(115,'Sarandí',10,1),(116,'Chivilcoy',10,1),(117,'Villa Domínico',10,1),(118,'Béccar',10,1),(119,'San Francisco',10,7),(120,'Glew',10,1),(121,'Puerto Madryn',10,6),(122,'Punta Alta',10,1),(123,'El Palomar',10,1),(124,'Rafael Calzada',10,1),(125,'Tartagal',10,18),(126,'San Pedro de Jujuy',10,11),(127,'Belén de Escobar',10,1),(128,'Berisso',10,1),(129,'Mariano Acosta',10,1),(130,'San Francisco Solano',10,1),(131,'Los Polvorines',10,1),(132,'Azul',10,1),(133,'Lomas del Mirador',10,1),(134,'Río Grande',10,24),(135,'Presidente Perón',10,1),(136,'General Pico',10,12),(137,'Mercedes',10,1),(138,'Bosques',10,1),(139,'Oberá',10,15),(140,'Barranqueras',10,5),(141,'Yerba Buena/Marcos Paz',10,25),(142,'Villa Centenario',10,1),(143,'San Martín',10,14),(144,'Gobernador Julio A Costa',10,1),(145,'William Morris',10,1),(146,'El Jagüel',10,1),(147,'Villa Mariano Moreno-El Colmenar',10,25),(148,'Eldorado',10,15),(149,'Longchamps',10,1),(150,'Clorinda',10,10),(151,'Viedma',10,17),(152,'Concepción',10,25),(153,'Tres Arroyos',10,1),(154,'Ushuaia',10,24),(155,'San Isidro',10,1),(156,'Palpalá',10,11);
/*!40000 ALTER TABLE `direccion_ciudad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `direccion_direccion`
--

DROP TABLE IF EXISTS `direccion_direccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `direccion_direccion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `calle` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `altura` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `zip` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `punto_referencia` longtext COLLATE utf8_unicode_ci NOT NULL,
  `observacion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `barrio_id` int(11) NOT NULL,
  `ciudad_id` int(11) NOT NULL,
  `pais_id` int(11) NOT NULL,
  `provincia_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `direccion_direccion_d2d7294b` (`barrio_id`),
  KEY `direccion_direccion_0201ed81` (`ciudad_id`),
  KEY `direccion_direccion_847ec16e` (`pais_id`),
  KEY `direccion_direccion_54bf7e76` (`provincia_id`),
  CONSTRAINT `direccion_direcc_provincia_id_74244344_fk_direccion_provincia_id` FOREIGN KEY (`provincia_id`) REFERENCES `direccion_provincia` (`id`),
  CONSTRAINT `direccion_direccion_barrio_id_9ae9e9_fk_direccion_barrio_id` FOREIGN KEY (`barrio_id`) REFERENCES `direccion_barrio` (`id`),
  CONSTRAINT `direccion_direccion_ciudad_id_2abb8df2_fk_direccion_ciudad_id` FOREIGN KEY (`ciudad_id`) REFERENCES `direccion_ciudad` (`id`),
  CONSTRAINT `direccion_direccion_pais_id_24c11b63_fk_direccion_pais_id` FOREIGN KEY (`pais_id`) REFERENCES `direccion_pais` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccion_direccion`
--

LOCK TABLES `direccion_direccion` WRITE;
/*!40000 ALTER TABLE `direccion_direccion` DISABLE KEYS */;
/*!40000 ALTER TABLE `direccion_direccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `direccion_edificacion`
--

DROP TABLE IF EXISTS `direccion_edificacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `direccion_edificacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_de_edificio` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `cantidad_de_pisos` int(11) DEFAULT NULL,
  `cantidad_de_inmuebles_por_piso` int(11) DEFAULT NULL,
  `total_inmuebles` int(11) DEFAULT NULL,
  `rampa` tinyint(1) NOT NULL,
  `distancia_del_vehiculo` int(11) DEFAULT NULL,
  `escalera_estrecha` tinyint(1) NOT NULL,
  `escalera_inclinada` tinyint(1) NOT NULL,
  `escalon_grande` tinyint(1) NOT NULL,
  `direccion_id` int(11) NOT NULL,
  `tipo_de_edificacion_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `direccion_edific_direccion_id_2f0f822c_fk_direccion_direccion_id` (`direccion_id`),
  KEY `direccion_edificacion_ac1f730e` (`tipo_de_edificacion_id`),
  CONSTRAINT `D62457c79e1bd9996b3241bd43b68787` FOREIGN KEY (`tipo_de_edificacion_id`) REFERENCES `direccion_tipodeedificacion` (`id`),
  CONSTRAINT `direccion_edific_direccion_id_2f0f822c_fk_direccion_direccion_id` FOREIGN KEY (`direccion_id`) REFERENCES `direccion_direccion` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccion_edificacion`
--

LOCK TABLES `direccion_edificacion` WRITE;
/*!40000 ALTER TABLE `direccion_edificacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `direccion_edificacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `direccion_especificaciondeinmueble`
--

DROP TABLE IF EXISTS `direccion_especificaciondeinmueble`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `direccion_especificaciondeinmueble` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `especificacion_de_inmueble` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `predeterminado` tinyint(1) NOT NULL,
  `tipo_de_inmueble_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `direccion_especificaciondeinmueble_e1ed7001` (`tipo_de_inmueble_id`),
  CONSTRAINT `dire_tipo_de_inmueble_id_106d1bf2_fk_direccion_tipodeinmueble_id` FOREIGN KEY (`tipo_de_inmueble_id`) REFERENCES `direccion_tipodeinmueble` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccion_especificaciondeinmueble`
--

LOCK TABLES `direccion_especificaciondeinmueble` WRITE;
/*!40000 ALTER TABLE `direccion_especificaciondeinmueble` DISABLE KEYS */;
INSERT INTO `direccion_especificaciondeinmueble` VALUES (1,'Casa de 2 Ambientes','casa con 2 ambientes',1,1),(2,'Oficina con 4 ambientes','Oficina con 4 ambientes',0,2),(3,'Casa de 3 Ambientes','Casa de 3 Ambientes',0,1);
/*!40000 ALTER TABLE `direccion_especificaciondeinmueble` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `direccion_horariodisponible`
--

DROP TABLE IF EXISTS `direccion_horariodisponible`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `direccion_horariodisponible` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lunes` tinyint(1) NOT NULL,
  `martes` tinyint(1) NOT NULL,
  `miercoles` tinyint(1) NOT NULL,
  `jueves` tinyint(1) NOT NULL,
  `viernes` tinyint(1) NOT NULL,
  `sabado` tinyint(1) NOT NULL,
  `domingo` tinyint(1) NOT NULL,
  `hora_desde` time(6) NOT NULL,
  `hora_hasta` time(6) NOT NULL,
  `edificio` tinyint(1) NOT NULL,
  `ascensor` tinyint(1) NOT NULL,
  `observacion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `edificacion_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `direccion_ho_edificacion_id_4846b6b6_fk_direccion_edificacion_id` (`edificacion_id`),
  CONSTRAINT `direccion_ho_edificacion_id_4846b6b6_fk_direccion_edificacion_id` FOREIGN KEY (`edificacion_id`) REFERENCES `direccion_edificacion` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccion_horariodisponible`
--

LOCK TABLES `direccion_horariodisponible` WRITE;
/*!40000 ALTER TABLE `direccion_horariodisponible` DISABLE KEYS */;
/*!40000 ALTER TABLE `direccion_horariodisponible` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `direccion_inmueble`
--

DROP TABLE IF EXISTS `direccion_inmueble`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `direccion_inmueble` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `numero_de_inmueble` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `numero_de_pisos` int(11) DEFAULT NULL,
  `nombre_del_piso` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `cantidad_de_ambientes` int(11) NOT NULL,
  `pisos_por_escalera` int(11) NOT NULL,
  `numero_de_plantas` int(11) NOT NULL,
  `total_m2` decimal(7,2) DEFAULT NULL,
  `baulera` tinyint(1) NOT NULL,
  `volumen_baulera` decimal(7,2) DEFAULT NULL,
  `edificacion_id` int(11) NOT NULL,
  `especificacion_de_inmueble_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `direccion_in_edificacion_id_69097183_fk_direccion_edificacion_id` (`edificacion_id`),
  KEY `c579c5dbb7e8080d192db976e7c6346e` (`especificacion_de_inmueble_id`),
  CONSTRAINT `c579c5dbb7e8080d192db976e7c6346e` FOREIGN KEY (`especificacion_de_inmueble_id`) REFERENCES `direccion_especificaciondeinmueble` (`id`),
  CONSTRAINT `direccion_in_edificacion_id_69097183_fk_direccion_edificacion_id` FOREIGN KEY (`edificacion_id`) REFERENCES `direccion_edificacion` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccion_inmueble`
--

LOCK TABLES `direccion_inmueble` WRITE;
/*!40000 ALTER TABLE `direccion_inmueble` DISABLE KEYS */;
/*!40000 ALTER TABLE `direccion_inmueble` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `direccion_pais`
--

DROP TABLE IF EXISTS `direccion_pais`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `direccion_pais` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pais` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `codigo_telefonico` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `pais` (`pais`)
) ENGINE=InnoDB AUTO_INCREMENT=265 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccion_pais`
--

LOCK TABLES `direccion_pais` WRITE;
/*!40000 ALTER TABLE `direccion_pais` DISABLE KEYS */;
INSERT INTO `direccion_pais` VALUES (1,'Afghanistan (AF)',''),(2,'Albania (AL)',''),(3,'Algeria (DZ)',''),(4,'American Samoa (AS)',''),(5,'Andorra (AD)',''),(6,'Angola (AO)',''),(7,'Anguilla (AI)',''),(8,'Antarctica (AQ)',''),(9,'Antigua and Barbuda (AG)',''),(10,'Argentina (AR)','+54'),(11,'Armenia (AM)',''),(12,'Aruba (AW)',''),(13,'Australia (AU)',''),(14,'Austria (AT)',''),(15,'Azerbaijan (AZ)',''),(16,'Bahamas (BS)',''),(17,'Bahrain (BH)',''),(18,'Bangladesh (BD)',''),(19,'Barbados (BB)',''),(20,'Belarus (BY)',''),(21,'Belgium (BE)',''),(22,'Belize (BZ)',''),(23,'Benin (BJ)',''),(24,'Bermuda (BM)',''),(25,'Bhutan (BT)',''),(26,'Bolivia (BO)',''),(27,'Bosnia and Herzegovina (BA)',''),(28,'Botswana (BW)',''),(29,'Bouvet Island (BV)',''),(30,'Brazil (BR)',''),(31,'British Antarctic Territory (BQ)',''),(32,'British Indian Ocean Territory (IO)',''),(33,'British Virgin Islands (VG)',''),(34,'Brunei (BN)',''),(35,'Bulgaria (BG)',''),(36,'Burkina Faso (BF)',''),(37,'Burundi (BI)',''),(38,'Cambodia (KH)',''),(39,'Cameroon (CM)',''),(40,'Canada (CA)',''),(41,'Canton and Enderbury Islands (CT)',''),(42,'Cape Verde (CV)',''),(43,'Cayman Islands (KY)',''),(44,'Central African Republic (CF)',''),(45,'Chad (TD)',''),(46,'Chile (CL)',''),(47,'China (CN)',''),(48,'Christmas Island (CX)',''),(49,'Cocos [Keeling] Islands (CC)',''),(50,'Colombia (CO)',''),(51,'Comoros (KM)',''),(52,'Congo - Brazzaville (CG)',''),(53,'Congo - Kinshasa (CD)',''),(54,'Cook Islands (CK)',''),(55,'Costa Rica (CR)',''),(56,'Croatia (HR)',''),(57,'Cuba (CU)',''),(58,'Cyprus (CY)',''),(59,'Czech Republic (CZ)',''),(60,'C?te d?Ivoire (CI)',''),(61,'Denmark (DK)',''),(62,'Djibouti (DJ)',''),(63,'Dominica (DM)',''),(64,'Dominican Republic (DO)',''),(65,'Dronning Maud Land (NQ)',''),(66,'East Germany (DD)',''),(67,'Ecuador (EC)',''),(68,'Egypt (EG)',''),(69,'El Salvador (SV)',''),(70,'Equatorial Guinea (GQ)',''),(71,'Eritrea (ER)',''),(72,'Estonia (EE)',''),(73,'Ethiopia (ET)',''),(74,'Falkland Islands (FK)',''),(75,'Faroe Islands (FO)',''),(76,'Fiji (FJ)',''),(77,'Finland (FI)',''),(78,'France (FR)',''),(79,'French Guiana (GF)',''),(80,'French Polynesia (PF)',''),(81,'French Southern Territories (TF)',''),(82,'French Southern and Antarctic Territories (FQ)',''),(83,'Gabon (GA)',''),(84,'Gambia (GM)',''),(85,'Georgia (GE)',''),(86,'Germany (DE)',''),(87,'Ghana (GH)',''),(88,'Gibraltar (GI)',''),(89,'Greece (GR)',''),(90,'Greenland (GL)',''),(91,'Grenada (GD)',''),(92,'Guadeloupe (GP)',''),(93,'Guam (GU)',''),(94,'Guatemala (GT)',''),(95,'Guernsey (GG)',''),(96,'Guinea (GN)',''),(97,'Guinea-Bissau (GW)',''),(98,'Guyana (GY)',''),(99,'Haiti (HT)',''),(100,'Heard Island and McDonald Islands (HM)',''),(101,'Honduras (HN)',''),(102,'Hong Kong SAR China (HK)',''),(103,'Hungary (HU)',''),(104,'Iceland (IS)',''),(105,'India (IN)',''),(106,'Indonesia (ID)',''),(107,'Iran (IR)',''),(108,'Iraq (IQ)',''),(109,'Ireland (IE)',''),(110,'Isle of Man (IM)',''),(111,'Israel (IL)',''),(112,'Italy (IT)',''),(113,'Jamaica (JM)',''),(114,'Japan (JP)',''),(115,'Jersey (JE)',''),(116,'Johnston Island (JT)',''),(117,'Jordan (JO)',''),(118,'Kazakhstan (KZ)',''),(119,'Kenya (KE)',''),(120,'Kiribati (KI)',''),(121,'Kuwait (KW)',''),(122,'Kyrgyzstan (KG)',''),(123,'Laos (LA)',''),(124,'Latvia (LV)',''),(125,'Lebanon (LB)',''),(126,'Lesotho (LS)',''),(127,'Liberia (LR)',''),(128,'Libya (LY)',''),(129,'Liechtenstein (LI)',''),(130,'Lithuania (LT)',''),(131,'Luxembourg (LU)',''),(132,'Macau SAR China (MO)',''),(133,'Macedonia (MK)',''),(134,'Madagascar (MG)',''),(135,'Malawi (MW)',''),(136,'Malaysia (MY)',''),(137,'Maldives (MV)',''),(138,'Mali (ML)',''),(139,'Malta (MT)',''),(140,'Marshall Islands (MH)',''),(141,'Martinique (MQ)',''),(142,'Mauritania (MR)',''),(143,'Mauritius (MU)',''),(144,'Mayotte (YT)',''),(145,'Metropolitan France (FX)',''),(146,'Mexico (MX)',''),(147,'Micronesia (FM)',''),(148,'Midway Islands (MI)',''),(149,'Moldova (MD)',''),(150,'Monaco (MC)',''),(151,'Mongolia (MN)',''),(152,'Montenegro (ME)',''),(153,'Montserrat (MS)',''),(154,'Morocco (MA)',''),(155,'Mozambique (MZ)',''),(156,'Myanmar [Burma] (MM)',''),(157,'Namibia (NA)',''),(158,'Nauru (NR)',''),(159,'Nepal (NP)',''),(160,'Netherlands (NL)',''),(161,'Netherlands Antilles (AN)',''),(162,'Neutral Zone (NT)',''),(163,'New Caledonia (NC)',''),(164,'New Zealand (NZ)',''),(165,'Nicaragua (NI)',''),(166,'Niger (NE)',''),(167,'Nigeria (NG)',''),(168,'Niue (NU)',''),(169,'Norfolk Island (NF)',''),(170,'North Korea (KP)',''),(171,'North Vietnam (VD)',''),(172,'Northern Mariana Islands (MP)',''),(173,'Norway (NO)',''),(174,'Oman (OM)',''),(175,'Pacific Islands Trust Territory (PC)',''),(176,'Pakistan (PK)',''),(177,'Palau (PW)',''),(178,'Palestinian Territories (PS)',''),(179,'Panama (PA)',''),(180,'Panama Canal Zone (PZ)',''),(181,'Papua New Guinea (PG)',''),(182,'Paraguay (PY)',''),(183,'People s Democratic Republic of Yemen (YD)',''),(184,'Peru (PE)',''),(185,'Philippines (PH)',''),(186,'Pitcairn Islands (PN)',''),(187,'Poland (PL)',''),(188,'Portugal (PT)',''),(189,'Puerto Rico (PR)',''),(190,'Qatar (QA)',''),(191,'Romania (RO)',''),(192,'Russia (RU)',''),(193,'Rwanda (RW)',''),(194,'R?union (RE)',''),(195,'Saint Barth?lemy (BL)',''),(196,'Saint Helena (SH)',''),(197,'Saint Kitts and Nevis (KN)',''),(198,'Saint Lucia (LC)',''),(199,'Saint Martin (MF)',''),(200,'Saint Pierre and Miquelon (PM)',''),(201,'Saint Vincent and the Grenadines (VC)',''),(202,'Samoa (WS)',''),(203,'San Marino (SM)',''),(204,'Saudi Arabia (SA)',''),(205,'Senegal (SN)',''),(206,'Serbia (RS)',''),(207,'Serbia and Montenegro (CS)',''),(208,'Seychelles (SC)',''),(209,'Sierra Leone (SL)',''),(210,'Singapore (SG)',''),(211,'Slovakia (SK)',''),(212,'Slovenia (SI)',''),(213,'Solomon Islands (SB)',''),(214,'Somalia (SO)',''),(215,'South Africa (ZA)',''),(216,'South Georgia and the South Sandwich Islands (GS)',''),(217,'South Korea (KR)',''),(218,'Spain (ES)',''),(219,'Sri Lanka (LK)',''),(220,'Sudan (SD)',''),(221,'Suriname (SR)',''),(222,'Svalbard and Jan Mayen (SJ)',''),(223,'Swaziland (SZ)',''),(224,'Sweden (SE)',''),(225,'Switzerland (CH)',''),(226,'Syria (SY)',''),(227,'S?o Tom? and Pr?ncipe (ST)',''),(228,'Taiwan (TW)',''),(229,'Tajikistan (TJ)',''),(230,'Tanzania (TZ)',''),(231,'Thailand (TH)',''),(232,'Timor-Leste (TL)',''),(233,'Togo (TG)',''),(234,'Tokelau (TK)',''),(235,'Tonga (TO)',''),(236,'Trinidad and Tobago (TT)',''),(237,'Tunisia (TN)',''),(238,'Turkey (TR)',''),(239,'Turkmenistan (TM)',''),(240,'Turks and Caicos Islands (TC)',''),(241,'Tuvalu (TV)',''),(242,'U.S. Minor Outlying Islands (UM)',''),(243,'U.S. Miscellaneous Pacific Islands (PU)',''),(244,'U.S. Virgin Islands (VI)',''),(245,'Uganda (UG)',''),(246,'Ukraine (UA)',''),(247,'Union of Soviet Socialist Republics (SU)',''),(248,'United Arab Emirates (AE)',''),(249,'United Kingdom (GB)',''),(250,'United States (US)',''),(251,'Unknown or Invalid Region (ZZ)',''),(252,'Uruguay (UY)',''),(253,'Uzbekistan (UZ)',''),(254,'Vanuatu (VU)',''),(255,'Vatican City (VA)',''),(256,'Venezuela (VE)','+58'),(257,'Vietnam (VN)',''),(258,'Wake Island (WK)',''),(259,'Wallis and Futuna (WF)',''),(260,'Western Sahara (EH)',''),(261,'Yemen (YE)',''),(262,'Zambia (ZM)',''),(263,'Zimbabwe (ZW)',''),(264,'Aland Islands (AX)','');
/*!40000 ALTER TABLE `direccion_pais` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `direccion_provincia`
--

DROP TABLE IF EXISTS `direccion_provincia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `direccion_provincia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `provincia` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `codigo_telefonico` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `pais_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `direccion_provincia_provincia_4ff3f3d4_uniq` (`provincia`,`pais_id`),
  KEY `direccion_provincia_pais_id_4226634a_fk_direccion_pais_id` (`pais_id`),
  CONSTRAINT `direccion_provincia_pais_id_4226634a_fk_direccion_pais_id` FOREIGN KEY (`pais_id`) REFERENCES `direccion_pais` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccion_provincia`
--

LOCK TABLES `direccion_provincia` WRITE;
/*!40000 ALTER TABLE `direccion_provincia` DISABLE KEYS */;
INSERT INTO `direccion_provincia` VALUES (1,'Buenos Aires','',1),(2,'Buenos Aires-GBA','',10),(3,'Capital Federal','',10),(4,'Catamarca','',10),(5,'Chaco','',10),(6,'Chubut','',10),(7,'Córdoba','',10),(8,'Corrientes','',10),(9,'Entre Ríos','',10),(10,'Formosa','',10),(11,'Jujuy','',10),(12,'La Pampa','',10),(13,'La Rioja','',10),(14,'Mendoza','',10),(15,'Misiones','',10),(16,'Neuquén','',10),(17,'Río Negro','',10),(18,'Salta','',10),(19,'San Juan','',10),(20,'San Luis','',10),(21,'Santa Cruz','',10),(22,'Santa Fe','',10),(23,'Santiago del Estero','',10),(24,'Tierra del Fuego','',10),(25,'Tucumán','',10);
/*!40000 ALTER TABLE `direccion_provincia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `direccion_tipodeascensor`
--

DROP TABLE IF EXISTS `direccion_tipodeascensor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `direccion_tipodeascensor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_de_ascensor` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccion_tipodeascensor`
--

LOCK TABLES `direccion_tipodeascensor` WRITE;
/*!40000 ALTER TABLE `direccion_tipodeascensor` DISABLE KEYS */;
INSERT INTO `direccion_tipodeascensor` VALUES (1,'Principal','Ascensor principal'),(2,'Servicio','Ascensor de servicio'),(3,'Camillero','Ascensor camillero ');
/*!40000 ALTER TABLE `direccion_tipodeascensor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `direccion_tipodeedificacion`
--

DROP TABLE IF EXISTS `direccion_tipodeedificacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `direccion_tipodeedificacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_de_edificacion` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `nombre` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccion_tipodeedificacion`
--

LOCK TABLES `direccion_tipodeedificacion` WRITE;
/*!40000 ALTER TABLE `direccion_tipodeedificacion` DISABLE KEYS */;
INSERT INTO `direccion_tipodeedificacion` VALUES (1,'Casa','casa ',0),(2,'Conjunto residencial','Edificación con varios inmuebles',1),(3,'Edificio','Edificación con varias oficinas o departamentos',0);
/*!40000 ALTER TABLE `direccion_tipodeedificacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `direccion_tipodeinmueble`
--

DROP TABLE IF EXISTS `direccion_tipodeinmueble`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `direccion_tipodeinmueble` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_de_inmueble` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccion_tipodeinmueble`
--

LOCK TABLES `direccion_tipodeinmueble` WRITE;
/*!40000 ALTER TABLE `direccion_tipodeinmueble` DISABLE KEYS */;
INSERT INTO `direccion_tipodeinmueble` VALUES (1,'Casa','casa'),(2,'Oficina','oficina'),(3,'Departamento','departamento');
/*!40000 ALTER TABLE `direccion_tipodeinmueble` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_20878280_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_374d1025_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_20878280_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_374d1025_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2016-02-02 19:02:27.820200','2','std',1,'',4,1),(2,'2016-02-02 19:03:06.915584','2','std',2,'Changed first_name and last_name.',4,1),(3,'2016-02-02 19:50:35.649799','18','prueba',1,'',35,1),(4,'2016-02-02 19:51:06.258218','18','prueba',2,'No fields changed.',35,1),(5,'2016-02-02 20:00:04.433876','18','prueba',3,'',35,1),(6,'2016-02-04 19:21:19.000000','1','prueba',1,'',62,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_5316f01b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=117 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(112,'almacen','almacen'),(113,'almacen','tipodemovimiento'),(114,'almacen','unidad'),(21,'ambiente','ambiente'),(23,'ambiente','ambienteestadoderegistro'),(22,'ambiente','ambienteportipodeinmueble'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(29,'cliente','cliente'),(32,'cliente','clientedireccion'),(33,'cliente','clienteestadoderegistro'),(30,'cliente','contacto'),(25,'cliente','estadocivil'),(31,'cliente','informaciondecontacto'),(24,'cliente','sexo'),(26,'cliente','tipodecliente'),(28,'cliente','tipodeinformaciondecontacto'),(27,'cliente','tipoderelacion'),(44,'complejidadriesgo','complejidadriesgo'),(45,'complejidadriesgo','nivelcomplejidadriesgo'),(34,'contenedor','contenedor'),(35,'contenedor','contenedortipicopormueble'),(116,'contenedor','tipodecontenido'),(5,'contenttypes','contenttype'),(115,'corsheaders','corsmodel'),(105,'cotizacionweb','abono'),(110,'cotizacionweb','argumentodeventa'),(93,'cotizacionweb','conceptodecotizacion'),(99,'cotizacionweb','contenedormueble'),(95,'cotizacionweb','cotizacion'),(97,'cotizacionweb','cotizacionambiente'),(107,'cotizacionweb','cotizacionbitacora'),(106,'cotizacionweb','cotizacioncomplejidadriesgo'),(96,'cotizacionweb','cotizaciondireccion'),(109,'cotizacionweb','cotizacionestado'),(103,'cotizacionweb','cotizacionherramienta'),(108,'cotizacionweb','cotizacionhistoricofecha'),(102,'cotizacionweb','cotizacionmaterial'),(98,'cotizacionweb','cotizacionmueble'),(104,'cotizacionweb','cotizacionpresupuesto'),(101,'cotizacionweb','cotizacionservicio'),(92,'cotizacionweb','fechadecotizacion'),(100,'cotizacionweb','serviciomueble'),(94,'cotizacionweb','tipoabono'),(91,'cotizacionweb','tipodireccion'),(90,'cotizador','cotizador'),(15,'direccion','ascensor'),(10,'direccion','barrio'),(20,'direccion','calle'),(9,'direccion','ciudad'),(11,'direccion','direccion'),(13,'direccion','edificacion'),(17,'direccion','especificaciondeinmueble'),(19,'direccion','horariodisponible'),(18,'direccion','inmueble'),(7,'direccion','pais'),(8,'direccion','provincia'),(14,'direccion','tipodeascensor'),(12,'direccion','tipodeedificacion'),(16,'direccion','tipodeinmueble'),(42,'estadoderegistro','estado'),(43,'estadoderegistro','estadoderegistro'),(41,'gestiondedocumento','estadodedocumento'),(40,'gestiondedocumento','tipodedocumento'),(73,'herramienta','dotacionbasicadecamion'),(72,'herramienta','herramienta'),(75,'material','material'),(77,'material','materialesporservicio'),(76,'material','preciodematerial'),(74,'material','tipodematerial'),(47,'mensaje','mensaje'),(46,'mensaje','tipodemensaje'),(62,'menu','menu'),(63,'menu','menufavorito'),(70,'menu','relacion'),(38,'mueble','especificaciondemueble'),(37,'mueble','mueble'),(39,'mueble','muebleporambiente'),(36,'mueble','tipodemueble'),(52,'premisas','datosprecargado'),(48,'premisas','empresa'),(53,'premisas','moneda'),(49,'premisas','personalizacionvisual'),(50,'premisas','variantevisual'),(51,'premisas','variantevisualdetalle'),(57,'promocion','alianza'),(58,'promocion','alianzaestado'),(61,'promocion','fuentedepromocion'),(59,'promocion','institucion'),(54,'promocion','medio'),(55,'promocion','medioespecifico'),(60,'promocion','personaaliado'),(56,'promocion','tipodereferido'),(79,'servicio','complejidadservicio'),(81,'servicio','herramientasporservicio'),(80,'servicio','preciodeservicio'),(78,'servicio','servicio'),(111,'servicio','serviciotipicopormueble'),(6,'sessions','session'),(84,'talonario','documentodeltalonario'),(87,'talonario','documentodeltalonarioestado'),(83,'talonario','talonario'),(85,'talonario','talonarioestado'),(82,'talonario','tipodedocumentoimpreso'),(86,'talonario','trazabilidadtalonario'),(64,'trabajador','cargotrabajador'),(65,'trabajador','trabajador'),(88,'trabajador','trabajadorestadoderegistro'),(69,'vehiculo','choferasignado'),(67,'vehiculo','detalledevehiculo'),(68,'vehiculo','estadodevehiculo'),(66,'vehiculo','vehiculo'),(89,'widget','widget');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=87 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2016-02-04 14:46:36.516781'),(2,'auth','0001_initial','2016-02-04 14:46:45.975581'),(3,'admin','0001_initial','2016-02-04 14:46:48.473012'),(4,'estadoderegistro','0001_initial','2016-02-04 14:46:50.886358'),(5,'direccion','0001_initial','2016-02-04 14:47:39.072245'),(6,'ambiente','0001_initial','2016-02-04 14:47:46.136836'),(7,'contenttypes','0002_remove_content_type_name','2016-02-04 14:47:48.400172'),(8,'auth','0002_alter_permission_name_max_length','2016-02-04 14:47:50.191163'),(9,'auth','0003_alter_user_email_max_length','2016-02-04 14:47:52.096935'),(10,'auth','0004_alter_user_username_opts','2016-02-04 14:47:52.267643'),(11,'auth','0005_alter_user_last_login_null','2016-02-04 14:47:52.997812'),(12,'auth','0006_require_contenttypes_0002','2016-02-04 14:47:53.085118'),(13,'cliente','0001_initial','2016-02-04 14:48:20.392057'),(14,'complejidadriesgo','0001_initial','2016-02-04 14:48:21.553523'),(15,'mueble','0001_initial','2016-02-04 14:48:30.368877'),(16,'contenedor','0001_initial','2016-02-04 14:48:33.539860'),(17,'gestiondedocumento','0001_initial','2016-02-04 14:48:36.550661'),(18,'mensaje','0001_initial','2016-02-04 14:48:39.558215'),(19,'menu','0001_initial','2016-02-04 14:48:43.720499'),(20,'premisas','0001_initial','2016-02-04 14:48:50.241878'),(21,'promocion','0001_initial','2016-02-04 14:49:14.142114'),(22,'sessions','0001_initial','2016-02-04 14:49:14.864986'),(23,'trabajador','0001_initial','2016-02-04 14:49:17.774861'),(24,'vehiculo','0001_initial','2016-02-04 14:49:29.300197'),(25,'menu','0002_auto_20160204_1450','2016-02-04 19:20:53.000000'),(26,'trabajador','0002_auto_20160204_1453','2016-02-04 19:23:15.000000'),(27,'menu','0003_auto_20160212_0910','2016-02-12 13:41:18.000000'),(28,'premisas','0002_unidad','2016-02-15 19:30:54.000000'),(29,'herramienta','0001_initial','2016-02-15 19:30:59.000000'),(30,'servicio','0001_initial','2016-02-15 19:31:17.000000'),(31,'material','0001_initial','2016-02-15 19:31:23.000000'),(32,'material','0002_auto_20160215_1500','2016-02-15 19:31:32.000000'),(33,'talonario','0001_initial','2016-02-15 19:31:49.000000'),(34,'talonario','0002_auto_20160217_1458','2016-02-17 19:29:15.000000'),(35,'trabajador','0003_trabajadorestadoderegistro','2016-02-17 19:29:20.000000'),(36,'cliente','0002_auto_20160301_0825','2016-03-01 12:58:37.000000'),(37,'premisas','0003_auto_20160301_0825','2016-03-01 12:58:38.000000'),(38,'promocion','0002_auto_20160301_0825','2016-03-01 12:58:38.000000'),(39,'cliente','0003_auto_20160301_1634','2016-03-01 21:04:28.000000'),(40,'direccion','0002_auto_20160301_1634','2016-03-01 21:04:31.000000'),(41,'servicio','0002_auto_20160302_1335','2016-03-02 18:05:31.000000'),(42,'talonario','0003_auto_20160302_1335','2016-03-02 18:05:32.000000'),(43,'direccion','0003_auto_20160303_1401','2016-03-03 18:31:53.000000'),(44,'cliente','0004_auto_20160303_1401','2016-03-03 18:31:59.000000'),(45,'direccion','0004_auto_20160303_1403','2016-03-03 18:33:16.000000'),(46,'direccion','0005_auto_20160304_1558','2016-03-04 20:32:37.000000'),(47,'widget','0001_initial','2016-03-14 19:29:32.000000'),(48,'widget','0002_remove_widget_desplegable','2016-03-14 19:33:38.000000'),(49,'talonario','0004_auto_20160318_1403','2016-03-18 18:33:56.000000'),(50,'complejidadriesgo','0002_auto_20160331_1430','2016-03-31 19:02:05.000000'),(51,'contenedor','0002_auto_20160331_1430','2016-03-31 19:02:07.000000'),(52,'direccion','0006_auto_20160331_1430','2016-03-31 19:02:09.000000'),(53,'material','0003_auto_20160331_1430','2016-03-31 19:02:11.000000'),(54,'promocion','0003_auto_20160331_1430','2016-03-31 19:02:12.000000'),(55,'servicio','0003_auto_20160331_1430','2016-03-31 19:02:14.000000'),(56,'vehiculo','0002_auto_20160331_1430','2016-03-31 19:02:19.000000'),(57,'cotizador','0001_initial','2016-03-31 19:05:16.000000'),(61,'direccion','0007_auto_20160401_1206','2016-04-01 16:36:46.000000'),(63,'direccion','0008_auto_20160404_1616','2016-04-04 20:47:07.000000'),(64,'servicio','0004_serviciotipicopormueble','2016-04-08 20:05:10.000000'),(65,'cotizacionweb','0001_initial','2016-04-08 20:06:17.000000'),(66,'promocion','0004_auto_20160408_1524','2016-04-08 20:06:19.000000'),(67,'almacen','0001_initial','2016-04-08 20:13:06.000000'),(68,'cotizacionweb','0002_cotizacionpresupuesto_unidad_de_medida','2016-04-08 20:13:09.000000'),(69,'material','0004_auto_20160408_1540','2016-04-08 20:13:12.000000'),(70,'herramienta','0002_auto_20160408_1548','2016-04-08 20:18:24.000000'),(71,'servicio','0005_auto_20160408_1548','2016-04-08 20:18:25.000000'),(72,'premisas','0004_delete_unidad','2016-04-08 20:19:22.000000'),(73,'contenedor','0003_contenedortipicopormueble_predefinido','2016-04-11 14:13:30.000000'),(74,'servicio','0006_serviciotipicopormueble_predefinido','2016-04-11 14:13:32.000000'),(75,'cliente','0005_auto_20160412_1106','2016-04-12 15:37:18.000000'),(76,'cotizacionweb','0003_cotizacionbitacora_origen_de_registro','2016-04-12 15:37:20.000000'),(77,'cotizacionweb','0004_auto_20160414_1529','2016-04-14 20:00:12.000000'),(78,'servicio','0007_preciodeservicio_precio_marginal','2016-04-14 20:00:13.000000'),(79,'servicio','0008_auto_20160414_1544','2016-04-14 20:14:40.000000'),(80,'contenedor','0004_tipodecontenido','2016-04-18 17:55:38.000000'),(81,'direccion','0009_auto_20160418_1152','2016-04-18 17:55:39.000000'),(82,'mueble','0002_auto_20160415_1617','2016-04-18 17:55:43.000000'),(83,'contenedor','0005_contenedortipicopormueble_tipo_de_contenido','2016-04-18 17:58:46.000000'),(84,'cotizacionweb','0005_auto_20160420_1104','2016-04-20 15:39:04.000000'),(85,'cotizacionweb','0006_cotizacionambiente_nombre','2016-04-20 16:18:18.000000'),(86,'contenedor','0006_remove_contenedortipicopormueble_predefinido','2016-04-22 12:55:49.000000');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('5adjglk0uvfeoj4qxf79bkvnor1emyh5','MmU1NjZhNmM0YWY3MjZkNTJkNjI1MGFkYjBiMTZmNGRiM2UxMmE0Mzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZjRkYTI2ZDkxMTYzYjNkY2IyOTUwZDI2ZWMyZDM4MDIwNjJhZDU5YyIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-02-18 15:02:43.235676'),('64vgx9tyun5s5etomjs3dsoayolac21b','OTRjYWY1ZDQ0ZTc5MjkxN2Y5NjVkNDhiMTE2YTQ0MzFlZGMyMGMzNjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjEiLCJfYXV0aF91c2VyX2hhc2giOiJmNGRhMjZkOTExNjNiM2RjYjI5NTBkMjZlYzJkMzgwMjA2MmFkNTljIn0=','2016-05-17 13:45:48.780910'),('iqy7x3jawyqz0evq4jh0ntk4qo0qe1d4','ZGQ5MGNlMzBlNTEyNWM3Yjg0NTdkN2RhZTRjZGIzZDIxNjY2YTdkNDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJmNGRhMjZkOTExNjNiM2RjYjI5NTBkMjZlYzJkMzgwMjA2MmFkNTljIn0=','2016-03-01 20:59:56.000000'),('mbobyp9renmnrbrq8ijs366pmawhqksg','MDQ0OGI3NDg4YzM3NWFjMjY0ZDE1ZmM0ZGE5NGRlMDRiNTE4ZGI5Mjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZjRkYTI2ZDkxMTYzYjNkY2IyOTUwZDI2ZWMyZDM4MDIwNjJhZDU5YyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2016-02-16 19:01:09.336565'),('qds5wgrdrsaufw6224y51kxognuv4x7b','MDQ0OGI3NDg4YzM3NWFjMjY0ZDE1ZmM0ZGE5NGRlMDRiNTE4ZGI5Mjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZjRkYTI2ZDkxMTYzYjNkY2IyOTUwZDI2ZWMyZDM4MDIwNjJhZDU5YyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2016-02-25 18:52:07.000000');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estadoderegistro_estado`
--

DROP TABLE IF EXISTS `estadoderegistro_estado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `estadoderegistro_estado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `estado` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `estado` (`estado`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estadoderegistro_estado`
--

LOCK TABLES `estadoderegistro_estado` WRITE;
/*!40000 ALTER TABLE `estadoderegistro_estado` DISABLE KEYS */;
INSERT INTO `estadoderegistro_estado` VALUES (1,'Activo','Es el estado que indica que el registro esta disponible para su uso'),(2,'Inactivo','Es el estado que indica que el registro no esta disponible para su uso'),(3,'Papelera','Es el estado que indica que el registro esta en papelera a la espera de la eliminación');
/*!40000 ALTER TABLE `estadoderegistro_estado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estadoderegistro_estadoderegistro`
--

DROP TABLE IF EXISTS `estadoderegistro_estadoderegistro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `estadoderegistro_estadoderegistro` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `model` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `observacion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `estado_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `estadoderegistr_estado_id_2a6b6ba7_fk_estadoderegistro_estado_id` (`estado_id`),
  CONSTRAINT `estadoderegistr_estado_id_2a6b6ba7_fk_estadoderegistro_estado_id` FOREIGN KEY (`estado_id`) REFERENCES `estadoderegistro_estado` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estadoderegistro_estadoderegistro`
--

LOCK TABLES `estadoderegistro_estadoderegistro` WRITE;
/*!40000 ALTER TABLE `estadoderegistro_estadoderegistro` DISABLE KEYS */;
INSERT INTO `estadoderegistro_estadoderegistro` VALUES (1,'ambiente','Es el estado que asigna cuando se crea un ambiente nuevo','',1),(2,'trabajador','Es el estado que asigna cuando se crea un trabajador','',1),(3,'talonario','Es el estado que asigna cuando se crea un talonario','',1),(4,'cotizacion','Es el estado que asigna cuando se crea una cotización','',1),(5,'alianza','Es el estado que asigna cuando se crea una alianza','',1),(6,'vehiculo','Es el estado que se asigna cuando se crea un vehículo','',1);
/*!40000 ALTER TABLE `estadoderegistro_estadoderegistro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gestiondedocumento_estadodedocumento`
--

DROP TABLE IF EXISTS `gestiondedocumento_estadodedocumento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gestiondedocumento_estadodedocumento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `estado_de_documento` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `orden` int(11) NOT NULL,
  `observacion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `tipo_de_documento_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `gestiondedocumento_estadodedocumento_ced3756a` (`tipo_de_documento_id`),
  CONSTRAINT `D52306614f011f0aa043644bbc723adf` FOREIGN KEY (`tipo_de_documento_id`) REFERENCES `gestiondedocumento_tipodedocumento` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestiondedocumento_estadodedocumento`
--

LOCK TABLES `gestiondedocumento_estadodedocumento` WRITE;
/*!40000 ALTER TABLE `gestiondedocumento_estadodedocumento` DISABLE KEYS */;
INSERT INTO `gestiondedocumento_estadodedocumento` VALUES (1,'creado','creación del talonario',0,'',1),(2,'creado','creación de un item perteneciente a un talonario',0,'',2),(3,'Carga Inicial','Es el estado que asigna cuando se esta cargando la data inicial de una cotización',1,'',3),(4,'Por cotizar','Es el estado que asigna cuando se cargaron todo los datos básicos de una cotización',2,'',3),(5,'Agendada','Es el estado que asigna cuando se agenda una visita a un cliente para capturar los datos del inmueble a cotizar',3,'',3),(6,'Carga de datos del cliente','Es el estado que asigna cuando se realizo la visita a un cliente para capturar los datos del inmueble a cotizar',4,'',3),(7,'Carga de direcciones','asociar direcciones a la cotización',5,'',3),(8,'Carga de muebles','Es el estado que se asigna cuando se cierra la carga de direcciones',6,'',3),(9,'Verificación de servicios','Es el estado que se asigna cuando se cierra la carga de muebles',7,'',3),(10,'Verificación de contenedores','Es el estado que se asigna cuando se cierra la verificación de servicios',8,'',3),(11,'Verificación de materiales','Es el estado que se asigna cuando se cierra la verificación de contenedores',9,'',3),(12,'Verificación de herramientas','Es el estado que se asigna cuando se cierra la verificación de materiales',10,'',3),(13,'Verificación de complejidad y riesgos','Es el estado que se asigna cuando se cierra la verificación de herramientas',11,'',3),(14,'Revisión de presupuesto','Es el estado que se asigna cuando se cierra verificación de complejidad y riesgos',12,'',3),(15,'Cierre de cotización','Es el estado que se asigna cuando revisión de presupuesto',13,'',3),(16,'Orden de envío colocada','Es el estado que se asigna se hace la petición de enviar la cotización por correo',14,'',3),(17,'Orden de envío ejecutada','Es el estado que se asigna cuando la petición de envío de correo se realizo correctamente',15,'',3),(18,'Cotizada','Es el estado que se asigna cuando se verifica la recepción del correo con el cliente',16,'',3),(19,'Ejecución del seguimiento','Es el estado que se asigna cuando se realiza el primer seguimiento',17,'',3),(20,'Confirmación de cotización','Es el estado que se asigna cuando el cliente indique su confirmación para realizar los servicios',18,'',3),(21,'Realizada','Es el estado que se asigna cuando se pulsa el botón \"cotización realizada\"',19,'',3),(22,'Cancelación de cotización','Es el estado que se asigna cuando se pulsa el botón \"cancelada\" y exista al menos un seguimiento',20,'',3),(23,'Negocio perdido','Es el estado que se asigna cuando se pulsa el botón \"cancelada\" y no hay ningún seguimiento',21,'',3);
/*!40000 ALTER TABLE `gestiondedocumento_estadodedocumento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gestiondedocumento_tipodedocumento`
--

DROP TABLE IF EXISTS `gestiondedocumento_tipodedocumento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gestiondedocumento_tipodedocumento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_de_documento` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tipo_de_documento` (`tipo_de_documento`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestiondedocumento_tipodedocumento`
--

LOCK TABLES `gestiondedocumento_tipodedocumento` WRITE;
/*!40000 ALTER TABLE `gestiondedocumento_tipodedocumento` DISABLE KEYS */;
INSERT INTO `gestiondedocumento_tipodedocumento` VALUES (1,'talonario','talonario físico tales como cheques, facturas entre otros documentos impresos'),(2,'documento del talonario','documento de un talonario'),(3,'cotizacion','cotización');
/*!40000 ALTER TABLE `gestiondedocumento_tipodedocumento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `herramienta_dotacionbasicadecamion`
--

DROP TABLE IF EXISTS `herramienta_dotacionbasicadecamion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `herramienta_dotacionbasicadecamion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cantidad` int(11) NOT NULL,
  `detalle_de_vehiculo_id` int(11) NOT NULL,
  `herramienta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `e27bd33f475ef5319887eb066f3cca57` (`detalle_de_vehiculo_id`),
  KEY `herramienta_dotacionbasicadecamion_590f1392` (`herramienta_id`),
  CONSTRAINT `e27bd33f475ef5319887eb066f3cca57` FOREIGN KEY (`detalle_de_vehiculo_id`) REFERENCES `vehiculo_detalledevehiculo` (`id`),
  CONSTRAINT `herramient_herramienta_id_6eff8704_fk_herramienta_herramienta_id` FOREIGN KEY (`herramienta_id`) REFERENCES `herramienta_herramienta` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `herramienta_dotacionbasicadecamion`
--

LOCK TABLES `herramienta_dotacionbasicadecamion` WRITE;
/*!40000 ALTER TABLE `herramienta_dotacionbasicadecamion` DISABLE KEYS */;
/*!40000 ALTER TABLE `herramienta_dotacionbasicadecamion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `herramienta_herramienta`
--

DROP TABLE IF EXISTS `herramienta_herramienta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `herramienta_herramienta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `herramienta` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `volumen_en_camion` int(11) NOT NULL,
  `peso_kg` decimal(9,2) NOT NULL,
  `unidad_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `herramienta` (`herramienta`),
  KEY `herramienta_herramienta_unidad_id_2275d2a3_fk_premisas_unidad_id` (`unidad_id`),
  CONSTRAINT `herramienta_herramienta_unidad_id_272edb2_fk_almacen_unidad_id` FOREIGN KEY (`unidad_id`) REFERENCES `almacen_unidad` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `herramienta_herramienta`
--

LOCK TABLES `herramienta_herramienta` WRITE;
/*!40000 ALTER TABLE `herramienta_herramienta` DISABLE KEYS */;
/*!40000 ALTER TABLE `herramienta_herramienta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `material_material`
--

DROP TABLE IF EXISTS `material_material`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `material_material` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `material` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `relacion_consumo_venta` decimal(9,2) NOT NULL,
  `ancho` decimal(7,2) NOT NULL,
  `largo` decimal(7,2) NOT NULL,
  `alto` decimal(7,2) NOT NULL,
  `peso_unidad_consumo_kg` decimal(7,2) NOT NULL,
  `cotizable` tinyint(1) NOT NULL,
  `tipo_de_material_id` int(11) NOT NULL,
  `unidad_de_consumo_id` int(11) NOT NULL,
  `unidad_de_venta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `material_material_03520e42` (`unidad_de_consumo_id`),
  KEY `material_material_ce7badf3` (`unidad_de_venta_id`),
  KEY `material_material_fcceed0b` (`tipo_de_material_id`),
  CONSTRAINT `mater_tipo_de_material_id_46fee1b5_fk_material_tipodematerial_id` FOREIGN KEY (`tipo_de_material_id`) REFERENCES `material_tipodematerial` (`id`),
  CONSTRAINT `material_mate_unidad_de_consumo_id_1c639de1_fk_almacen_unidad_id` FOREIGN KEY (`unidad_de_consumo_id`) REFERENCES `almacen_unidad` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `material_materi_unidad_de_venta_id_513cb613_fk_almacen_unidad_id` FOREIGN KEY (`unidad_de_venta_id`) REFERENCES `almacen_unidad` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `material_material`
--

LOCK TABLES `material_material` WRITE;
/*!40000 ALTER TABLE `material_material` DISABLE KEYS */;
/*!40000 ALTER TABLE `material_material` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `material_materialesporservicio`
--

DROP TABLE IF EXISTS `material_materialesporservicio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `material_materialesporservicio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cantidad` decimal(9,2) NOT NULL,
  `calculo` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `material_id` int(11) NOT NULL,
  `servicio_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `material_materiales_material_id_53bf5842_fk_material_material_id` (`material_id`),
  KEY `material_materialesporservicio_4bb699dc` (`servicio_id`),
  CONSTRAINT `material_materiales_material_id_53bf5842_fk_material_material_id` FOREIGN KEY (`material_id`) REFERENCES `material_material` (`id`),
  CONSTRAINT `material_materiales_servicio_id_220e584a_fk_servicio_servicio_id` FOREIGN KEY (`servicio_id`) REFERENCES `servicio_servicio` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `material_materialesporservicio`
--

LOCK TABLES `material_materialesporservicio` WRITE;
/*!40000 ALTER TABLE `material_materialesporservicio` DISABLE KEYS */;
/*!40000 ALTER TABLE `material_materialesporservicio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `material_preciodematerial`
--

DROP TABLE IF EXISTS `material_preciodematerial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `material_preciodematerial` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `precio` decimal(9,2) NOT NULL,
  `fecha_desde` date NOT NULL,
  `fecha_hasta` date NOT NULL,
  `infinito` tinyint(1) NOT NULL,
  `fecha_preparacion` date NOT NULL,
  `fecha_aprobacion` date NOT NULL,
  `aprobado` tinyint(1) NOT NULL,
  `material_id` int(11) NOT NULL,
  `user_aprobador_id` int(11) DEFAULT NULL,
  `user_preparador_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `material_preciodema_material_id_583392c6_fk_material_material_id` (`material_id`),
  KEY `material_preciodemat_user_preparador_id_28467901_fk_auth_user_id` (`user_preparador_id`),
  KEY `material_preciodemate_user_aprobador_id_7e8fd742_fk_auth_user_id` (`user_aprobador_id`),
  CONSTRAINT `material_preciodema_material_id_583392c6_fk_material_material_id` FOREIGN KEY (`material_id`) REFERENCES `material_material` (`id`),
  CONSTRAINT `material_preciodemat_user_preparador_id_28467901_fk_auth_user_id` FOREIGN KEY (`user_preparador_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `material_preciodemate_user_aprobador_id_7e8fd742_fk_auth_user_id` FOREIGN KEY (`user_aprobador_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `material_preciodematerial`
--

LOCK TABLES `material_preciodematerial` WRITE;
/*!40000 ALTER TABLE `material_preciodematerial` DISABLE KEYS */;
/*!40000 ALTER TABLE `material_preciodematerial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `material_tipodematerial`
--

DROP TABLE IF EXISTS `material_tipodematerial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `material_tipodematerial` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_de_material` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `material_tipodematerial`
--

LOCK TABLES `material_tipodematerial` WRITE;
/*!40000 ALTER TABLE `material_tipodematerial` DISABLE KEYS */;
/*!40000 ALTER TABLE `material_tipodematerial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mensaje_mensaje`
--

DROP TABLE IF EXISTS `mensaje_mensaje`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mensaje_mensaje` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `mensaje` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `tipo_de_mensaje_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mensaje_mensaje_cd5aca77` (`tipo_de_mensaje_id`),
  CONSTRAINT `mensaje__tipo_de_mensaje_id_739058f2_fk_mensaje_tipodemensaje_id` FOREIGN KEY (`tipo_de_mensaje_id`) REFERENCES `mensaje_tipodemensaje` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mensaje_mensaje`
--

LOCK TABLES `mensaje_mensaje` WRITE;
/*!40000 ALTER TABLE `mensaje_mensaje` DISABLE KEYS */;
/*!40000 ALTER TABLE `mensaje_mensaje` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mensaje_tipodemensaje`
--

DROP TABLE IF EXISTS `mensaje_tipodemensaje`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mensaje_tipodemensaje` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_de_mensaje` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tipo_de_mensaje` (`tipo_de_mensaje`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mensaje_tipodemensaje`
--

LOCK TABLES `mensaje_tipodemensaje` WRITE;
/*!40000 ALTER TABLE `mensaje_tipodemensaje` DISABLE KEYS */;
/*!40000 ALTER TABLE `mensaje_tipodemensaje` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu_menu`
--

DROP TABLE IF EXISTS `menu_menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `menu_menu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `menu` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `transaccion` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `namespace` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `nivel` int(11) NOT NULL,
  `padre` tinyint(1) NOT NULL,
  `menu_padre_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `menu_menu_transaccion_517a1e01_uniq` (`transaccion`),
  KEY `menu_menu_menu_padre_id_2e39653d_fk_menu_menu_id` (`menu_padre_id`),
  CONSTRAINT `menu_menu_menu_padre_id_2e39653d_fk_menu_menu_id` FOREIGN KEY (`menu_padre_id`) REFERENCES `menu_menu` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=228 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu_menu`
--

LOCK TABLES `menu_menu` WRITE;
/*!40000 ALTER TABLE `menu_menu` DISABLE KEYS */;
INSERT INTO `menu_menu` VALUES (1,'Dirección','DIR01','','',1,1,NULL),(2,'Barrio','BAR01','','',2,1,1),(3,'Agregar Barrio','BAR02','udirecciones','add_barrio',3,0,2),(4,'Ciudad','CIU01','udirecciones','add_ciudad',2,1,1),(7,'Ambiente','AMB01','','',1,1,NULL),(8,'Ambiente','AMB02','','',2,1,7),(9,'Agregar Ambiente','AMB03','uambientes','add_ambiente',3,0,8),(12,'Lista de Ambiente','AMB04','uambientes','list_ambiente',3,0,8),(13,'Lista de Barrio','BAR03','udirecciones','list_barrio',3,0,2),(14,'Agregar Ciudad','CIU02','udirecciones','add_ciudad',3,0,4),(15,'Lista de Ciudad','CIU03','udirecciones','list_ciudad',3,0,4),(16,'Pais','PAI01','','',2,1,1),(17,'Agregar Pais','PAI02','udirecciones','add_pais',3,0,16),(18,'Lista de Pais','PAI03','udirecciones','list_pais',3,0,16),(19,'Ambiente por tipo de Inmueble','AMB05','','',2,1,7),(20,'Agregar Ambiente por Tipo de Inmueble','AMB06','uambientes','add_ambienteportipoinmueble',3,0,19),(21,'Lista de Ambientes por tipo de Inmueble','AMB07','uambientes','list_ambienteportipoinmueble',3,0,19),(22,'Cliente','CLI01','','',1,1,NULL),(23,'Cliente','CLI02','','',2,1,22),(24,'Agregar Cliente','CLI03','uclientes','add_cliente',3,0,23),(25,'Lista de Cliente','CLI04','uclientes','list_cliente',3,0,23),(26,'Estado Civil','EST01','','',2,1,22),(27,'Agregar Estado Civil','EST02','uclientes','add_estado_civil',3,0,26),(28,'Lista de Estados Civiles','EST03','uclientes','list_estado_civil',3,0,26),(29,'Sexo','SEX01','','',2,1,22),(30,'Agregar Sexo','SEX02','uclientes','add_sexo',3,0,29),(31,'Lista de Sexos','SEX03','uclientes','list_sexo',3,0,29),(32,'Tipo de Cliente','TDC01','','',2,1,22),(33,'Agregar Tipo de Cliente','TDC02','uclientes','add_tipo_de_cliente',3,0,32),(34,'Lista de Tipos de Clientes','TDC03','uclientes','list_tipo_de_cliente',3,0,32),(35,'Tipo de Relacion','TDR01','','',2,1,22),(36,'Agregar Tipo de Relacion','TDR02','uclientes','add_tipo_de_relacion',3,0,35),(37,'Lista de Tipos de Relacion','TDR03','uclientes','list_tipo_de_relacion',3,0,35),(38,'Tipo de Información de Contacto','TDI01','','',2,1,22),(39,'Agregar Tipo Información de Contacto','TDI02','uclientes','add_tipo_de_informacion_de_contacto',3,0,38),(40,'Lista de Tipos de Información de Contacto','TDI03','uclientes','list_tipo_de_informacion_de_contacto',3,0,38),(41,'Complejidad de Riesgo','COM01','','',1,1,NULL),(42,'Complejidad de Riesgo','COM02','','',2,1,41),(43,'Agregar Complejidad de Riesgo','COM03','ucomplejidadriesgos','add_complejidadriesgo',3,0,42),(44,'Lista de Cpmplejidades de Riesgos','COM04','ucomplejidadriesgos','list_complejidadriesgo',3,0,42),(45,'Nivel de Complejidad de Riesgo','NDC01','','',2,1,41),(46,'Agregar Nivel de Complejidad de Riesgo','NDC02','ucomplejidadriesgos','add_nivelcomplejidadriesgo',3,0,45),(47,'Lista de Niveles de Complejidad de Riesgo','NDC03','ucomplejidadriesgos','list_nivelcomplejidadriesgo',3,0,45),(48,'Contenedor','CON01','','',1,1,NULL),(49,'Contenedor','CON02','','',2,1,48),(50,'Agregar Contenedor','CON03','ucontenedores','add_contenedor',3,0,49),(51,'Lista de Contenedores','CON04','ucontenedores','list_contenedor',3,0,49),(52,'Contenedor Típico','CON05','','',2,1,48),(53,'Agregar Contenedor Típico','CON06','ucontenedores','add_contenedortipico',3,0,52),(54,'Lista de Contenedores Típicos','CON07','ucontenedores','list_contenedortipico',3,0,52),(55,'Especificación de Inmueble','EDI01','','',2,1,1),(56,'Agregar Especificación de Inmueble','EDI02','udirecciones','add_especificaciondeinmueble',3,0,55),(57,'Lista de Especificaciones de Inmuebles','EDI03','udirecciones','list_especificaciondeinmueble',3,0,55),(58,'Provincia','PRO01','','',2,1,1),(59,'Agregar Provincia','PRO02','udirecciones','add_provincia',3,0,58),(60,'Lista de Provincias','PRO03','udirecciones','list_provincia',3,0,58),(61,'Tipo de Ascensor','TDA01','','',2,1,1),(86,'Agregar Tipo de Ascensor','TDA02','udirecciones','add_tipo_de_ascensor',3,0,61),(87,'Lista de Tipos de Ascensor','TDA03','udirecciones','list_tipo_de_ascensor',3,0,61),(88,'Tipo de Edificación','TDE01','','',2,1,1),(89,'Agregar Tipo de Edificación','TDE02','udirecciones','add_tipo_de_edificacion',3,0,88),(90,'Lista de Tipos de Especificaciones','TDE03','udirecciones','list_tipo_de_edificacion',3,0,88),(91,'Tipo de Inmueble','TIN01','','',2,1,1),(92,'Agregar Tipo de Inmueble','TIN02','udirecciones','add_tipo_de_inmueble',3,0,91),(93,'Lista de Tipos de Inmuebles','TIN03','udirecciones','list_tipo_de_inmueble',3,0,91),(94,'Estado de Registro','EDR01','','',1,1,NULL),(95,'Estado','EDO01','','',2,1,94),(96,'Agregar Estado','EDO02','uestadoderegistros','add_estado',3,0,95),(97,'Lista de Estados','EDO03','uestadoderegistros','list_estado',3,0,95),(98,'Estado de Registro','EDR02','','',2,1,94),(99,'Agregar Estado de Registro','EDR03','uestadoderegistros','add_estadoderegistro',3,0,98),(100,'Lista de Estados de Registros','EDR04','uestadoderegistros','list_estadoderegistro',3,0,98),(101,'Gestión de Documento','GES01','','',1,1,NULL),(102,'Estado de Documento','EDD01','','',2,1,101),(103,'Agregar Estado de Documento','EDD02','ugestiondedocumentos','add_estadodedocumento',3,0,102),(104,'Lista de Estado de Documento','EDD03','ugestiondedocumentos','list_estadodedocumento',3,0,102),(105,'Tipo de Documento','TDD01','','',2,1,101),(106,'Agregar Tipo de Documento','TDD02','ugestiondedocumentos','add_tipodedocumento',3,0,105),(107,'Lista de Tipos de Documentos','TDD03','ugestiondedocumentos','list_tipodedocumento',3,0,105),(108,'Herramienta','HER01','','',1,1,NULL),(109,'Herramienta','HER02','','',2,1,108),(110,'Agregar Herramienta','HER03','uherramientas','add_herramienta',3,0,109),(111,'Lista de Herramientas','HER04','uherramientas','list_herramienta',3,0,109),(112,'Dotación Básica de Camión','DBC01','','',2,1,108),(113,'Agregar Dotación Básica de Camión','DBC02','uherramientas','add_dotacionbasicadecamion',3,0,112),(114,'Lista de Dotaciones Básicas de Camión','DBC03','uherramientas','list_dotacionbasicadecamion',3,0,112),(115,'Material','MAT01','','',1,1,NULL),(116,'Material','MAT02','','',2,1,115),(117,'Agregar Material','MAT03','umateriales','add_material',3,0,116),(118,'Lista de Materiales','MAT04','umateriales','list_material',3,0,116),(119,'Tipo de Material','TDM01','','',2,1,115),(120,'Agregar Tipo de Material','TDM02','umateriales','add_tipodematerial',3,0,119),(121,'Lista de Tipos de Materiales','TDM03','umateriales','list_tipodematerial',3,0,119),(122,'Mensaje','MEN01','','',1,1,NULL),(123,'Mensaje','MEN02','','',2,1,122),(124,'Agregar Mensaje','MEN03','umensajes','add_mensaje',3,0,123),(125,'Lista de Mensajes','MEN04','umensajes','list_mensaje',3,0,123),(126,'Tipo de Mensaje','TMJ01','','',2,1,122),(127,'Agregar Tipo de Mensajes','TMJ02','umensajes','add_tipodemensaje',3,0,126),(128,'Lista de Tipos de Mensajes','TMJ03','umensajes','list_tipodemensaje',3,0,126),(129,'Menú','MNU01','','',1,1,NULL),(130,'Menú','MNU02','','',2,1,129),(131,'Agregar Menú','MNU03','umenus','add_menu',3,0,130),(132,'Lista de Menús','MNU04','umenus','list_menu',3,0,130),(133,'Favoritos','FAV01','','',2,1,129),(134,'Agregar Favoritos','FAV02','umenus','add_menufavorito',3,0,133),(135,'Lista de Favoritos','FAV03','umenus','list_menufavorito',3,0,133),(136,'Relación','REL01','','',2,1,129),(137,'Agregar Relación','REL02','umenus','add_relacion',3,0,136),(138,'Lista de Relaciones','REL03','umenus','list_relacion',3,0,136),(139,'Mueble','MUE01','','',1,1,NULL),(140,'Mueble','MUE02','','',2,1,139),(141,'Agregar Mueble','MUE03','umuebles','add_mueble',3,0,140),(142,'Lista de Muebles','MUE04','umuebles','list_mueble',3,0,140),(143,'Especificación de Mueble','ESM01','','',2,1,139),(144,'Agregar Especificación de Mueble','ESM02','umuebles','add_especificaciondemueble',3,0,143),(145,'Lista de Especificaciones de Mueble','ESM03','umuebles','list_especificaciondemueble',3,0,143),(146,'Mueble por Ambiente','MPA01','','',2,1,139),(147,'Agregar Mueble por Ambiente','MPA02','umuebles','add_muebleporambiente',3,0,146),(148,'Lista de Muebles por Ambientes','MPA03','umuebles','list_muebleporambiente',3,0,146),(149,'Tipo de Mueble','TMU01','','',2,1,139),(150,'Agregar Tipo de Mueble','TMU02','umuebles','add_tipodemueble',3,0,149),(151,'Lista de Tipos de Muebles','TMU03','umuebles','list_tipodemueble',3,0,149),(152,'Premisas','PRE01','','',1,1,NULL),(153,'Datos Precargados','DPR01','','',2,1,152),(154,'Agregar Datos Precargados','DPR02','upremisas','add_datosprecargado',3,0,153),(155,'Lista de Datos Precargados','DPR03','upremisas','list_datosprecargado',3,0,153),(156,'Empresa','EMP01','','',2,1,152),(157,'Agregar Empresa','EMP02','upremisas','add_empresa',3,0,156),(158,'Lista de Empresas','EMP03','upremisas','list_empresa',3,0,156),(159,'Personalización Visual','PVI01','','',2,1,152),(160,'Agregar Personalización Visual','PVI02','upremisas','add_personalizacionvisual',3,0,159),(161,'Listas de Personalizaciones Visuales','PVI03','upremisas','list_personalizacionvisual',3,0,159),(162,'Variante Visual','VAV01','','',2,1,152),(163,'Agregar Variante Visual','VAV02','upremisas','add_variantevisual',3,0,162),(164,'Lista de Variantes Visuales','VAV03','upremisas','list_variantevisual',3,0,162),(165,'Promoción','PRM01','','',1,1,NULL),(166,'Alianza','ALI01','','',2,1,165),(167,'Agregar Alianza','ALI02','upromociones','add_alianza',3,0,166),(168,'Lista de Alianzas','ALI03','upromociones','list_alianza',3,0,166),(169,'Fuente de Promoción','FDP01','','',2,1,165),(170,'Agregar Fuente de Promoción','FDP02','upromociones','add_fuentedepromocion',3,0,169),(171,'Lista de Fuentes de Promociones','FDP03','upromociones','list_fuentedepromocion',3,0,169),(172,'Institución','INS01','','',2,1,165),(173,'Agregar Institución','INS02','upromociones','add_institucion',3,0,172),(174,'Lista de Instituciones','INS03','upromociones','list_institucion',3,0,172),(175,'Medio','MED01','','',2,1,165),(176,'Agregar Medio','MED02','upromociones','add_medio',3,0,175),(177,'Lista de Medios','MED03','upromociones','list_medio',3,0,175),(178,'Medio Especifico','MES01','','',2,1,165),(179,'Agregar Medio Especifico','MES02','upromociones','add_medioespecifico',3,0,178),(180,'Lista de Medios Especificos','MES03','upromociones','list_medioespecifico',3,0,178),(181,'Personalizado','PES01','','',2,1,165),(182,'Agregar Personalizado','PES02','upromociones','add_personaaliado',3,0,181),(183,'Lista de Personalizados','PES03','upromociones','list_personaaliado',3,0,181),(184,'Tipo de Referido','TRF01','','',2,1,165),(185,'Agregar Tipo de Referido','TRF02','upromociones','add_tipodereferido',3,0,184),(186,'Lista de Tipos de Referidos','TRF03','upromociones','list_tipodereferido',3,0,184),(187,'Servicio','SER01','','',1,1,NULL),(188,'Servicio ','SER02','','',2,1,187),(189,'Agregar Servicio','SER03','uservicios','add_servicio',3,0,188),(190,'Lista de Servicios','SER04','uservicios','list_servicio',3,0,188),(191,'Complejidad del Servicio','CDS01','','',2,1,187),(192,'Agregar Complejidad de Servicio','CDS02','uservicios','add_complejidadservicio',3,0,191),(193,'Lista de Complejiades de Servicios','CDS03','uservicios','list_complejidadservicio',3,0,191),(194,'Herramienta por Servicio','HPS01','','',2,1,187),(195,'Agregar Herramienta por Servicio','HPS02','uservicios','add_herramientaporservicio',3,0,194),(196,'Lista de Herramientas por Servicios','HPS03','uservicios','list_herramientaporservicio',3,0,194),(197,'Precio de Servicio','PDS01','','',2,1,187),(198,'Agregar Precio de Servicio','PDS02','uservicios','add_preciodeservicio',3,0,197),(199,'Lista de Precios de Servicios','PDS03','uservicios','list_preciodeservicio',3,0,197),(200,'Talonario','TAL01','','',1,1,NULL),(201,'Talonario','TAL02','','',2,1,200),(202,'Agregar Talonario','TAL03','utalonarios','add_talonario',3,0,201),(203,'Lista de Talonarios','TAL04','utalonarios','list_talonario',3,0,201),(204,'Documento del Talonario','DDT01','','',2,1,200),(205,'Agregar Document del Talonario','DDT02','utalonarios','add_documentodeltalonario',3,0,204),(206,'Lista de Documentos del Talonario','DDT03','utalonarios','list_documentodeltalonario',3,0,204),(207,'Tipo de Documento Impreso','TPI01','','',2,1,200),(208,'Agregar Tipo de Documento Impreso','TPI02','utalonarios','add_tipodedocumentoimpreso',3,0,207),(209,'Lista de Tipos de Documentos Impresos','TPI03','utalonarios','list_tipodedocumentoimpreso',3,0,207),(210,'Trabajador','TRA01','','',1,1,NULL),(211,'Cargo Trabajador','CTR01','','',2,1,210),(212,'Agregar Cargo','CTR02','utrabajadores','add_cargotrabajador',3,0,211),(213,'Lista de Cargos','CTR03','utrabajadores','list_cargotrabajador',3,0,211),(214,'Trabajador','TRA02','','',2,1,210),(215,'Agregar Trabajador','TRA03','utrabajadores','add_trabajador',3,0,214),(216,'Lista de Trabajadores','TRA04','utrabajadores','list_trabajador',3,0,214),(217,'Vehiculo','VEH01','','',1,1,NULL),(218,'Vehiculo','VEH02','','',2,1,217),(219,'Agregar Vehiculo','VEH03','uvehiculos','add_vehiculo',3,0,218),(220,'Lista de Vehiculos','VEH04','uvehiculos','list_vehiculo',3,0,218),(221,'Chofer Asignado','CHO01','','',2,1,217),(222,'Agregar Chofer Asignado','CHO02','uvehiculos','add_choferasignado',3,0,221),(223,'Lista de Choferes Asignados','CHO03','uvehiculos','list_choferasignado',3,0,221),(224,'Detalle de Vehiculo','DDV01','','',2,1,217),(225,'Agregar Detalle de Vehiculo','DDV02','uvehiculos','add_detalledevehiculo',3,0,224),(226,'Lista de Detalles de Vehiculos','DDV03','uvehiculos','list_detalledevehiculo',3,0,224),(227,'aaaaaaaaa','aaaaaaaaaa','aaaaaaaa','aaaaaaaaa',1,0,167);
/*!40000 ALTER TABLE `menu_menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu_menufavorito`
--

DROP TABLE IF EXISTS `menu_menufavorito`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `menu_menufavorito` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `grupo` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `orden` int(11) NOT NULL,
  `menu_id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `menu_menufavorito_menu_id_51cd3e22_fk_menu_menu_id` (`menu_id`),
  KEY `menu_menufavorito_usuario_id_1770ec7e_fk_auth_user_id` (`usuario_id`),
  CONSTRAINT `menu_menufavorito_menu_id_51cd3e22_fk_menu_menu_id` FOREIGN KEY (`menu_id`) REFERENCES `menu_menu` (`id`),
  CONSTRAINT `menu_menufavorito_usuario_id_1770ec7e_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu_menufavorito`
--

LOCK TABLES `menu_menufavorito` WRITE;
/*!40000 ALTER TABLE `menu_menufavorito` DISABLE KEYS */;
INSERT INTO `menu_menufavorito` VALUES (1,'Grupo1',3,9,1),(2,'Grupo1',2,3,1),(3,'Grupo2',1,14,1);
/*!40000 ALTER TABLE `menu_menufavorito` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu_relacion`
--

DROP TABLE IF EXISTS `menu_relacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `menu_relacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `item_origen_id` int(11) NOT NULL,
  `item_relacion_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `menu_relacion_26a7734e` (`item_origen_id`),
  KEY `menu_relacion_5fe6c39a` (`item_relacion_id`),
  CONSTRAINT `menu_relacion_item_origen_id_70c122bb_fk_menu_menu_id` FOREIGN KEY (`item_origen_id`) REFERENCES `menu_menu` (`id`),
  CONSTRAINT `menu_relacion_item_relacion_id_2eeafeb1_fk_menu_menu_id` FOREIGN KEY (`item_relacion_id`) REFERENCES `menu_menu` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=175 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu_relacion`
--

LOCK TABLES `menu_relacion` WRITE;
/*!40000 ALTER TABLE `menu_relacion` DISABLE KEYS */;
INSERT INTO `menu_relacion` VALUES (1,'Ciudad',3,15),(2,'Barrio',14,13),(3,'Ciudad',13,15),(4,'Pais',3,18),(5,'Pais',13,18),(6,'Barrio',15,13),(7,'Pais',14,18),(8,'Pais',15,18),(9,'Barrio',17,13),(10,'Barrio',18,13),(11,'Ciudad',18,15),(12,'Ciudad',17,15),(13,'Provincia',3,60),(14,'Provincia',15,60),(15,'Provincia',14,60),(16,'Pais',59,18),(17,'Pais',60,18),(18,'Ciudad',59,15),(19,'Ciudad',60,15),(20,'Ambientes por Tipo de Inmueble',9,21),(21,'Ambiente por tipo de Inmuebles',12,21),(22,'Ambiente',20,12),(23,'Ambiente',21,12),(24,'Muebles por ambiente',20,148),(25,'Muebles por Ambiente',21,148),(26,'Especificación de Inmueble',20,57),(27,'Especificación de Inmueble',21,57),(28,'Ambiente por Tipo de Inmueble',56,21),(29,'Ambiente por tipo de Inmueble',57,21),(30,'Ambiente por tipo de Inmueble',147,21),(31,'Ambiente por tipo de Inmueble',148,21),(32,'Tipo de Cliente',24,34),(33,'Tipo de Cliente',25,34),(34,'Cliente',33,25),(35,'Cliente',34,25),(36,'Contenedores Tipicos',50,54),(37,'Contenedores Tipicos',51,54),(38,'Contenedor',53,51),(39,'Contenedor',54,51),(40,'Estado de Registro',96,100),(41,'Estado de Registro',97,100),(42,'Estado',99,97),(43,'Estado',100,97),(44,'Tipos de Documentos',103,107),(45,'Tipos de Documentos',104,107),(46,'Estado de Documento',106,104),(47,'Estado de Documento',107,104),(48,'Dotación Básica de Camión',110,114),(49,'Dotación Básica de Camión',111,114),(50,'Herramienta',113,111),(51,'Herramienta',114,111),(52,'Tipo de Material',117,121),(53,'Tipo de Material',118,121),(54,'Material',120,118),(55,'Material',121,118),(56,'Tipo de Mensaje',124,128),(57,'Tipo de Mensaje',125,128),(58,'Mensaje',127,125),(59,'Mensaje',128,125),(79,'Tipo de Mueble',141,151),(80,'Tipo de Mueble',142,151),(81,'Mueble',150,142),(82,'Mueble',151,142),(83,'Especificación de Mueble',141,145),(84,'Especificación de Mueble',142,145),(85,'Mueble',144,142),(86,'Mueble',145,142),(87,'Mueble por Ambiente',144,148),(88,'Muebles por Ambiente',145,148),(89,'Especificación de Mueble',147,145),(90,'Especificación de Mueble',148,145),(91,'Ambiente por Tipo de Inmueble',147,21),(92,'Ambiente por Tipo de Inmueble',148,21),(93,'Muebles por Ambiente',20,148),(94,'Muebles por Ambiente',21,148),(95,'Medio Especifico',167,180),(96,'Medio Especifico',168,180),(97,'Alianza',179,168),(98,'Alianza',180,168),(99,'Medio Especifico',176,180),(100,'Medio Especifico',177,180),(101,'Medio',179,177),(102,'Medio',180,177),(103,'Medio Especifico',185,180),(104,'Medio Especifico',186,180),(105,'Tipo de Referido',179,186),(106,'Tipo de Referido',180,186),(107,'Alianza',173,168),(108,'Alianza',174,168),(109,'Institución ',167,174),(110,'Institución',168,174),(111,'Institución',182,174),(112,'Institución',183,174),(113,'Persona Aliada',173,183),(114,'Persona Aliada',174,183),(115,'Persona Aliada',170,183),(116,'Persona Aliada',171,183),(117,'Fuente de Promoción',182,171),(118,'Fuente de Promoción',183,171),(119,'Medio Especifico',170,180),(120,'Medio Especifico',171,180),(121,'Fuente de Promoción',179,171),(122,'Fuente de Promoción',180,171),(123,'Fuente de Promoción',185,171),(124,'Fuente de Promoción',186,171),(125,'Tipo de Referido',170,186),(126,'Tipo de Referido',171,186),(127,'Cliente',179,25),(128,'Cliente',180,25),(129,'Barrio',179,13),(130,'Barrio',180,13),(131,'Complejidad del Servicio',189,193),(132,'Complejidad del Servicio',190,193),(133,'Servicio',192,190),(134,'Servicio',193,190),(135,'Servicio',198,190),(136,'Servicio',199,190),(137,'Precio del Servicio',189,199),(138,'Precio del Servicio',190,199),(139,'Servicio',195,190),(140,'Servicio',196,190),(141,'Herramientas por Servicio',189,196),(142,'Herramientas por Servicio',190,196),(143,'Herramientas por Servicio',110,196),(144,'Herramientas por Servicio',111,196),(145,'Herramienta',195,111),(146,'Herramienta',196,111),(147,'Documentos del Talonario',202,206),(148,'Documentos del Talonario',203,206),(149,'Talonario',205,203),(150,'Talonario',206,203),(151,'Talonario',208,203),(152,'Talonario',209,203),(153,'Tipo de Documentos Impresos',202,209),(154,'Tipo de Documentos Impresos',203,209),(155,'Cargo',215,213),(156,'Cargo',216,213),(157,'Trabajador',212,216),(158,'Trabajador',213,216),(159,'Detalle del Vehiculo',219,226),(160,'Detalle del Vehiculo',220,226),(161,'Vehiculo',225,220),(162,'Vehiculo',226,220),(163,'Detalle del Vehiculo',222,226),(164,'Detalle del Vehiculo',223,226),(165,'Chofer Asignado',225,223),(166,'Chofer Asignado',226,223),(167,'Menú',134,132),(168,'Menú',135,132),(169,'Favoritos',131,135),(170,'Favoritos',132,135),(171,'Menú',137,132),(172,'Menú',138,132),(173,'Relación',131,138),(174,'Relación',132,138);
/*!40000 ALTER TABLE `menu_relacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mueble_especificaciondemueble`
--

DROP TABLE IF EXISTS `mueble_especificaciondemueble`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mueble_especificaciondemueble` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `especificacion_de_mueble` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `ancho` decimal(7,2) NOT NULL,
  `largo` decimal(7,2) NOT NULL,
  `alto` decimal(7,2) NOT NULL,
  `volumen_en_camion` int(11) NOT NULL,
  `predefinido` tinyint(1) NOT NULL,
  `mueble_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mueble_especificaciondemueble_49933347` (`mueble_id`),
  CONSTRAINT `mueble_especificaciondemueb_mueble_id_bbf1a9_fk_mueble_mueble_id` FOREIGN KEY (`mueble_id`) REFERENCES `mueble_mueble` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mueble_especificaciondemueble`
--

LOCK TABLES `mueble_especificaciondemueble` WRITE;
/*!40000 ALTER TABLE `mueble_especificaciondemueble` DISABLE KEYS */;
INSERT INTO `mueble_especificaciondemueble` VALUES (1,'Cama matrimonial','',1.40,2.00,0.60,13,1,2),(2,'Mesa de luz pequeña 40 ','',0.40,0.40,0.50,1,1,3),(3,'Biblioteca pequeña ','',0.40,0.40,1.00,2,1,5),(4,'Mesa de comedor redonda','',0.60,0.60,0.90,6,1,7),(5,'Silla de comedor sin asas','',0.30,0.30,0.40,8,1,8),(6,'Sofá de 1 puesto','',0.90,0.70,0.90,7,1,1),(7,'Nevera de 2 puertas','',0.52,0.60,1.24,7,1,4);
/*!40000 ALTER TABLE `mueble_especificaciondemueble` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mueble_mueble`
--

DROP TABLE IF EXISTS `mueble_mueble`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mueble_mueble` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mueble` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `trasladable` tinyint(1) NOT NULL,
  `tipo_de_mueble_id` int(11) NOT NULL,
  `contenido_fragil` tinyint(1) NOT NULL,
  `contenido_textil` tinyint(1) NOT NULL,
  `fragil` tinyint(1) NOT NULL,
  `pesado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mueble` (`mueble`),
  KEY `mueble_mueble_fd00bd09` (`tipo_de_mueble_id`),
  CONSTRAINT `mueble_mueb_tipo_de_mueble_id_73a78552_fk_mueble_tipodemueble_id` FOREIGN KEY (`tipo_de_mueble_id`) REFERENCES `mueble_tipodemueble` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mueble_mueble`
--

LOCK TABLES `mueble_mueble` WRITE;
/*!40000 ALTER TABLE `mueble_mueble` DISABLE KEYS */;
INSERT INTO `mueble_mueble` VALUES (1,'Sofá','Sofá',1,4,0,0,0,0),(2,'Cama','Cama',1,2,0,0,0,0),(3,'Mesa de luz','mesa de noche',1,1,0,0,0,0),(4,'Nevera','nevera',1,3,0,0,0,0),(5,'Biblioteca','Biblioteca',0,9,0,0,0,0),(6,'Sillón de living','Sillón de living',1,10,0,0,0,0),(7,'Mesa de comedor','Mesa de comedor',1,1,0,0,0,0),(8,'Sillas de comedor                 ','Sillas de comedor',1,10,0,0,0,0);
/*!40000 ALTER TABLE `mueble_mueble` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mueble_muebleporambiente`
--

DROP TABLE IF EXISTS `mueble_muebleporambiente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mueble_muebleporambiente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `predefinido` tinyint(1) NOT NULL,
  `ambiente_por_tipo_de_inmueble_id` int(11) NOT NULL,
  `especificacion_de_mueble_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `D6ecdfbc704ea0855e52e5bb4f3926fb` (`ambiente_por_tipo_de_inmueble_id`),
  KEY `D67df0f1ac7cf05b8e7382323cf459c4` (`especificacion_de_mueble_id`),
  CONSTRAINT `D67df0f1ac7cf05b8e7382323cf459c4` FOREIGN KEY (`especificacion_de_mueble_id`) REFERENCES `mueble_especificaciondemueble` (`id`),
  CONSTRAINT `D6ecdfbc704ea0855e52e5bb4f3926fb` FOREIGN KEY (`ambiente_por_tipo_de_inmueble_id`) REFERENCES `ambiente_ambienteportipodeinmueble` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mueble_muebleporambiente`
--

LOCK TABLES `mueble_muebleporambiente` WRITE;
/*!40000 ALTER TABLE `mueble_muebleporambiente` DISABLE KEYS */;
INSERT INTO `mueble_muebleporambiente` VALUES (1,1,9,3),(2,1,9,1),(3,1,11,4),(4,1,11,6),(5,1,11,5),(6,1,1,1),(7,1,1,2),(8,1,2,4),(9,1,2,5),(10,1,2,6),(11,1,3,7);
/*!40000 ALTER TABLE `mueble_muebleporambiente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mueble_tipodemueble`
--

DROP TABLE IF EXISTS `mueble_tipodemueble`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mueble_tipodemueble` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_de_mueble` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tipo_de_mueble` (`tipo_de_mueble`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mueble_tipodemueble`
--

LOCK TABLES `mueble_tipodemueble` WRITE;
/*!40000 ALTER TABLE `mueble_tipodemueble` DISABLE KEYS */;
INSERT INTO `mueble_tipodemueble` VALUES (1,'Mesas y mesones',''),(2,'Camas',''),(3,'Línea blanca',''),(4,'Sofás',''),(5,'Electrodomésticos',''),(6,'Adornos de pared',''),(7,'Percheros y colgadores',''),(8,'Armarios y roperos',''),(9,'Estanterias y gavinetes',''),(10,'Sillas y sillones',''),(11,'Muebles de cocina',''),(12,'Sobre pisos',''),(13,'Adornos de piso',''),(14,'Adornos - Otros',''),(15,'Divisores de área',''),(16,'Jardinería',''),(17,'Gimnasio','');
/*!40000 ALTER TABLE `mueble_tipodemueble` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `premisas_datosprecargado`
--

DROP TABLE IF EXISTS `premisas_datosprecargado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `premisas_datosprecargado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_app` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `dato` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `tipo_de_dato` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `valor` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `premisas_datosprecargado`
--

LOCK TABLES `premisas_datosprecargado` WRITE;
/*!40000 ALTER TABLE `premisas_datosprecargado` DISABLE KEYS */;
/*!40000 ALTER TABLE `premisas_datosprecargado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `premisas_empresa`
--

DROP TABLE IF EXISTS `premisas_empresa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `premisas_empresa` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `empresa` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `telefonos` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `direccion` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `sitio_web` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `correo` varchar(254) COLLATE utf8_unicode_ci NOT NULL,
  `responsable` varchar(250) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cuit` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `logo` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `telefono_call_center` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `premisas_empresa`
--

LOCK TABLES `premisas_empresa` WRITE;
/*!40000 ALTER TABLE `premisas_empresa` DISABLE KEYS */;
/*!40000 ALTER TABLE `premisas_empresa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `premisas_moneda`
--

DROP TABLE IF EXISTS `premisas_moneda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `premisas_moneda` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `moneda` varchar(5) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `moneda` (`moneda`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `premisas_moneda`
--

LOCK TABLES `premisas_moneda` WRITE;
/*!40000 ALTER TABLE `premisas_moneda` DISABLE KEYS */;
/*!40000 ALTER TABLE `premisas_moneda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `premisas_personalizacionvisual`
--

DROP TABLE IF EXISTS `premisas_personalizacionvisual`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `premisas_personalizacionvisual` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `valor` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `usuario_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `premisas_personalizacionvisual_usuario_id_3a06fdb4_uniq` (`usuario_id`,`tipo`),
  CONSTRAINT `premisas_personalizacionvisu_usuario_id_7d294bef_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `premisas_personalizacionvisual`
--

LOCK TABLES `premisas_personalizacionvisual` WRITE;
/*!40000 ALTER TABLE `premisas_personalizacionvisual` DISABLE KEYS */;
INSERT INTO `premisas_personalizacionvisual` VALUES (1,'paginacion','10',1),(2,'paginacion','10',2),(3,'sidebarClosedOpen','2',2),(4,'rangopaginacion','3',2);
/*!40000 ALTER TABLE `premisas_personalizacionvisual` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `premisas_variantevisual`
--

DROP TABLE IF EXISTS `premisas_variantevisual`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `premisas_variantevisual` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `usuario_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  KEY `premisas_variantevisual_usuario_id_3f1c3811_fk_auth_user_id` (`usuario_id`),
  CONSTRAINT `premisas_variantevisual_usuario_id_3f1c3811_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `premisas_variantevisual`
--

LOCK TABLES `premisas_variantevisual` WRITE;
/*!40000 ALTER TABLE `premisas_variantevisual` DISABLE KEYS */;
INSERT INTO `premisas_variantevisual` VALUES (1,'ciudad001','ciudad',1),(2,'ciudad002','ciudad',2);
/*!40000 ALTER TABLE `premisas_variantevisual` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `premisas_variantevisualdetalle`
--

DROP TABLE IF EXISTS `premisas_variantevisualdetalle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `premisas_variantevisualdetalle` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `campo` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `visibilidad` int(11) NOT NULL,
  `variante_visual_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `premis_variante_visual_id_696537b8_fk_premisas_variantevisual_id` (`variante_visual_id`),
  CONSTRAINT `premis_variante_visual_id_696537b8_fk_premisas_variantevisual_id` FOREIGN KEY (`variante_visual_id`) REFERENCES `premisas_variantevisual` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `premisas_variantevisualdetalle`
--

LOCK TABLES `premisas_variantevisualdetalle` WRITE;
/*!40000 ALTER TABLE `premisas_variantevisualdetalle` DISABLE KEYS */;
INSERT INTO `premisas_variantevisualdetalle` VALUES (1,'pais',1,1),(2,'provincia',1,1),(3,'pais',1,2),(4,'provincia',1,2),(5,'ciudad',1,2);
/*!40000 ALTER TABLE `premisas_variantevisualdetalle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `promocion_alianza`
--

DROP TABLE IF EXISTS `promocion_alianza`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `promocion_alianza` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `alianza` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `porcentaje_comision` decimal(7,2) NOT NULL,
  `observacion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `fecha_vigencia` date NOT NULL,
  `medio_especifico_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `promocion_alianza_32e34cc2` (`medio_especifico_id`),
  CONSTRAINT `pro_medio_especifico_id_3675f80b_fk_promocion_medioespecifico_id` FOREIGN KEY (`medio_especifico_id`) REFERENCES `promocion_medioespecifico` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promocion_alianza`
--

LOCK TABLES `promocion_alianza` WRITE;
/*!40000 ALTER TABLE `promocion_alianza` DISABLE KEYS */;
INSERT INTO `promocion_alianza` VALUES (1,'Acuerdo comercial',0.20,'alianza','2016-05-24',1);
/*!40000 ALTER TABLE `promocion_alianza` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `promocion_alianzaestado`
--

DROP TABLE IF EXISTS `promocion_alianzaestado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `promocion_alianzaestado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `observacion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `predefinido` tinyint(1) NOT NULL,
  `alianza_id` int(11) NOT NULL,
  `estado_de_registro_id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `promocion_alianzaest_alianza_id_2b1ca378_fk_promocion_alianza_id` (`alianza_id`),
  KEY `dbcb0d1c318338ecefa1b80d420aba50` (`estado_de_registro_id`),
  KEY `promocion_alianzaestado_usuario_id_6e8a892c_fk_auth_user_id` (`usuario_id`),
  CONSTRAINT `dbcb0d1c318338ecefa1b80d420aba50` FOREIGN KEY (`estado_de_registro_id`) REFERENCES `estadoderegistro_estadoderegistro` (`id`),
  CONSTRAINT `promocion_alianzaest_alianza_id_2b1ca378_fk_promocion_alianza_id` FOREIGN KEY (`alianza_id`) REFERENCES `promocion_alianza` (`id`),
  CONSTRAINT `promocion_alianzaestado_usuario_id_6e8a892c_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promocion_alianzaestado`
--

LOCK TABLES `promocion_alianzaestado` WRITE;
/*!40000 ALTER TABLE `promocion_alianzaestado` DISABLE KEYS */;
INSERT INTO `promocion_alianzaestado` VALUES (1,'2016-04-06','Creación de una alianza',1,1,5,2);
/*!40000 ALTER TABLE `promocion_alianzaestado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `promocion_fuentedepromocion`
--

DROP TABLE IF EXISTS `promocion_fuentedepromocion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `promocion_fuentedepromocion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_referido` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `telefono_referido` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `institucion_aliado` longtext COLLATE utf8_unicode_ci NOT NULL,
  `alianza` longtext COLLATE utf8_unicode_ci NOT NULL,
  `condiciones_de_calculo_alianza` longtext COLLATE utf8_unicode_ci NOT NULL,
  `barrio_id` int(11) NOT NULL,
  `cliente_id` int(11) NOT NULL,
  `medio_especifico_id` int(11) NOT NULL,
  `persona_aliado_id` int(11) NOT NULL,
  `tipo_de_referido_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `promocion_fuentedeprom_barrio_id_7471cf98_fk_direccion_barrio_id` (`barrio_id`),
  KEY `promocion_fuentedeprom_cliente_id_77024b95_fk_cliente_cliente_id` (`cliente_id`),
  KEY `promocion_fuentedepromocion_32e34cc2` (`medio_especifico_id`),
  KEY `promocion_fuentedepromocion_e62a12ff` (`persona_aliado_id`),
  KEY `promocion_fuentedepromocion_76b0e50c` (`tipo_de_referido_id`),
  CONSTRAINT `pro_medio_especifico_id_44794512_fk_promocion_medioespecifico_id` FOREIGN KEY (`medio_especifico_id`) REFERENCES `promocion_medioespecifico` (`id`),
  CONSTRAINT `prom_tipo_de_referido_id_4cba41e4_fk_promocion_tipodereferido_id` FOREIGN KEY (`tipo_de_referido_id`) REFERENCES `promocion_tipodereferido` (`id`),
  CONSTRAINT `promoci_persona_aliado_id_5a89b769_fk_promocion_personaaliado_id` FOREIGN KEY (`persona_aliado_id`) REFERENCES `promocion_personaaliado` (`id`),
  CONSTRAINT `promocion_fuentedeprom_barrio_id_7471cf98_fk_direccion_barrio_id` FOREIGN KEY (`barrio_id`) REFERENCES `direccion_barrio` (`id`),
  CONSTRAINT `promocion_fuentedeprom_cliente_id_77024b95_fk_cliente_cliente_id` FOREIGN KEY (`cliente_id`) REFERENCES `cliente_cliente` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promocion_fuentedepromocion`
--

LOCK TABLES `promocion_fuentedepromocion` WRITE;
/*!40000 ALTER TABLE `promocion_fuentedepromocion` DISABLE KEYS */;
/*!40000 ALTER TABLE `promocion_fuentedepromocion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `promocion_institucion`
--

DROP TABLE IF EXISTS `promocion_institucion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `promocion_institucion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `cuit` varchar(25) COLLATE utf8_unicode_ci NOT NULL,
  `pagina_web` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `persona_contacto` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `telefono` varchar(25) COLLATE utf8_unicode_ci NOT NULL,
  `telefono_movil` varchar(25) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `alianza_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `promocion_institucio_alianza_id_4b248997_fk_promocion_alianza_id` (`alianza_id`),
  CONSTRAINT `promocion_institucio_alianza_id_4b248997_fk_promocion_alianza_id` FOREIGN KEY (`alianza_id`) REFERENCES `promocion_alianza` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promocion_institucion`
--

LOCK TABLES `promocion_institucion` WRITE;
/*!40000 ALTER TABLE `promocion_institucion` DISABLE KEYS */;
INSERT INTO `promocion_institucion` VALUES (1,'institución','12','http://','Luis alvarez','0256090290','0412985784','inst@gm.com',1);
/*!40000 ALTER TABLE `promocion_institucion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `promocion_medio`
--

DROP TABLE IF EXISTS `promocion_medio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `promocion_medio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `medio` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `medio` (`medio`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promocion_medio`
--

LOCK TABLES `promocion_medio` WRITE;
/*!40000 ALTER TABLE `promocion_medio` DISABLE KEYS */;
INSERT INTO `promocion_medio` VALUES (1,'Prensa/Diario','medio de información impreso'),(2,'TV','televisión'),(3,'Radio','radio'),(4,'Vía pública','vía pública'),(5,'Internet','internet');
/*!40000 ALTER TABLE `promocion_medio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `promocion_medioespecifico`
--

DROP TABLE IF EXISTS `promocion_medioespecifico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `promocion_medioespecifico` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `medio_especifico` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `medio_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `promocion_medioespecific_medio_id_77e60134_fk_promocion_medio_id` (`medio_id`),
  CONSTRAINT `promocion_medioespecific_medio_id_77e60134_fk_promocion_medio_id` FOREIGN KEY (`medio_id`) REFERENCES `promocion_medio` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promocion_medioespecifico`
--

LOCK TABLES `promocion_medioespecifico` WRITE;
/*!40000 ALTER TABLE `promocion_medioespecifico` DISABLE KEYS */;
INSERT INTO `promocion_medioespecifico` VALUES (1,'Diario la nación','Diario la nación',1),(2,'Camión mudarte','Camión en la vía pública',4),(3,'Facebook','facebook',5),(4,'Google','google',5);
/*!40000 ALTER TABLE `promocion_medioespecifico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `promocion_personaaliado`
--

DROP TABLE IF EXISTS `promocion_personaaliado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `promocion_personaaliado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dni` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `nombre` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `telefono` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `telefono_movil_1` varchar(25) COLLATE utf8_unicode_ci NOT NULL,
  `telefono_movil_2` varchar(25) COLLATE utf8_unicode_ci NOT NULL,
  `email_principal` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `email_secundario` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `observacion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `institucion_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `promocion_pe_institucion_id_27c51def_fk_promocion_institucion_id` (`institucion_id`),
  CONSTRAINT `promocion_pe_institucion_id_27c51def_fk_promocion_institucion_id` FOREIGN KEY (`institucion_id`) REFERENCES `promocion_institucion` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promocion_personaaliado`
--

LOCK TABLES `promocion_personaaliado` WRITE;
/*!40000 ALTER TABLE `promocion_personaaliado` DISABLE KEYS */;
INSERT INTO `promocion_personaaliado` VALUES (1,'182938','Andrea Barco','04128478584','041498757009','','andrea@gn.com','','',1);
/*!40000 ALTER TABLE `promocion_personaaliado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `promocion_tipodereferido`
--

DROP TABLE IF EXISTS `promocion_tipodereferido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `promocion_tipodereferido` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_de_referido` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `medio_especifico_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `pro_medio_especifico_id_72098d6c_fk_promocion_medioespecifico_id` (`medio_especifico_id`),
  CONSTRAINT `pro_medio_especifico_id_72098d6c_fk_promocion_medioespecifico_id` FOREIGN KEY (`medio_especifico_id`) REFERENCES `promocion_medioespecifico` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promocion_tipodereferido`
--

LOCK TABLES `promocion_tipodereferido` WRITE;
/*!40000 ALTER TABLE `promocion_tipodereferido` DISABLE KEYS */;
INSERT INTO `promocion_tipodereferido` VALUES (1,'Familiar','Tipo de referido',1),(2,'Relación comercial','relación comercial',2);
/*!40000 ALTER TABLE `promocion_tipodereferido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servicio_complejidadservicio`
--

DROP TABLE IF EXISTS `servicio_complejidadservicio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `servicio_complejidadservicio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `porcentaje` decimal(7,2) NOT NULL,
  `predefinido` tinyint(1) NOT NULL,
  `servicio_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `servicio_complejidadservicio_4bb699dc` (`servicio_id`),
  CONSTRAINT `servicio_complejidad_servicio_id_adc12fc_fk_servicio_servicio_id` FOREIGN KEY (`servicio_id`) REFERENCES `servicio_servicio` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicio_complejidadservicio`
--

LOCK TABLES `servicio_complejidadservicio` WRITE;
/*!40000 ALTER TABLE `servicio_complejidadservicio` DISABLE KEYS */;
INSERT INTO `servicio_complejidadservicio` VALUES (1,'Normal',0.00,1,2),(2,'Complejo',20.00,0,2),(3,'Muy complejo',50.00,0,2),(4,'Normal',0.00,1,3),(5,'Normal',0.00,1,1),(6,'Normal',0.00,1,7),(7,'Normal',0.00,1,4),(8,'Normal',0.00,1,5),(9,'Normal',0.00,1,9),(10,'Normal',0.00,1,6),(11,'Normal',0.00,1,8),(12,'Normal',0.00,1,11),(13,'Normal',0.00,1,10);
/*!40000 ALTER TABLE `servicio_complejidadservicio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servicio_herramientasporservicio`
--

DROP TABLE IF EXISTS `servicio_herramientasporservicio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `servicio_herramientasporservicio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cantidad` decimal(9,2) NOT NULL,
  `calculo` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `herramienta_id` int(11) NOT NULL,
  `servicio_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `servicio_h_herramienta_id_4b303ac1_fk_herramienta_herramienta_id` (`herramienta_id`),
  KEY `servicio_herramientasporservicio_4bb699dc` (`servicio_id`),
  CONSTRAINT `servicio_h_herramienta_id_4b303ac1_fk_herramienta_herramienta_id` FOREIGN KEY (`herramienta_id`) REFERENCES `herramienta_herramienta` (`id`),
  CONSTRAINT `servicio_herramient_servicio_id_755b5145_fk_servicio_servicio_id` FOREIGN KEY (`servicio_id`) REFERENCES `servicio_servicio` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicio_herramientasporservicio`
--

LOCK TABLES `servicio_herramientasporservicio` WRITE;
/*!40000 ALTER TABLE `servicio_herramientasporservicio` DISABLE KEYS */;
/*!40000 ALTER TABLE `servicio_herramientasporservicio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servicio_preciodeservicio`
--

DROP TABLE IF EXISTS `servicio_preciodeservicio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `servicio_preciodeservicio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `precio_base` decimal(9,2) NOT NULL,
  `cantidad_de_gracia` decimal(9,2) NOT NULL,
  `intervalo_1` decimal(9,2) NOT NULL,
  `porcentaje_1` decimal(9,2) NOT NULL,
  `intervalo_2` decimal(9,2) NOT NULL,
  `porcentaje_2` decimal(9,2) NOT NULL,
  `intervalo_3` decimal(9,2) NOT NULL,
  `porcentaje_3` decimal(9,2) NOT NULL,
  `redondeo` decimal(9,2) NOT NULL,
  `fecha_desde` date NOT NULL,
  `fecha_hasta` date NOT NULL,
  `infinito` tinyint(1) NOT NULL,
  `fecha_preparacion` date NOT NULL,
  `fecha_aprobacion` date NOT NULL,
  `aprobado` tinyint(1) NOT NULL,
  `servicio_id` int(11) NOT NULL,
  `user_aprobador_id` int(11) DEFAULT NULL,
  `user_preparador_id` int(11) NOT NULL,
  `precio_marginal` decimal(9,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `servicio_preciodeservicio_4bb699dc` (`servicio_id`),
  KEY `servicio_preciodeservicio_76e3b4be` (`user_preparador_id`),
  KEY `servicio_preciodeservicio_7af25b10` (`user_aprobador_id`),
  CONSTRAINT `servicio_preciodese_servicio_id_64c592a1_fk_servicio_servicio_id` FOREIGN KEY (`servicio_id`) REFERENCES `servicio_servicio` (`id`),
  CONSTRAINT `servicio_preciodeser_user_preparador_id_5cd6c1ce_fk_auth_user_id` FOREIGN KEY (`user_preparador_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `servicio_preciodeserv_user_aprobador_id_6f3f9ecb_fk_auth_user_id` FOREIGN KEY (`user_aprobador_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicio_preciodeservicio`
--

LOCK TABLES `servicio_preciodeservicio` WRITE;
/*!40000 ALTER TABLE `servicio_preciodeservicio` DISABLE KEYS */;
INSERT INTO `servicio_preciodeservicio` VALUES (1,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,1.00,'2016-01-01','2016-12-31',1,'2016-04-14','2016-01-01',1,1,1,1,400.00),(2,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,1.00,'2016-01-01','2016-12-31',1,'2016-04-14','2016-01-01',1,2,1,1,400.00),(3,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,'2016-01-01','2016-12-31',1,'2016-04-14','2016-01-01',1,5,1,1,400.00),(4,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,1.00,'2016-01-01','2016-12-31',1,'2016-04-14','2016-01-01',1,10,1,1,400.00),(5,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,1.00,'2016-01-01','2016-12-31',1,'2016-04-14','2016-01-01',1,4,1,1,400.00),(6,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,1.00,'2016-01-01','2016-12-31',1,'2016-04-14','2016-01-01',1,3,1,1,400.00),(7,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,1.00,'2016-01-01','2016-12-31',1,'2016-04-14','2016-01-01',1,9,1,1,400.00),(8,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,1.00,'2016-01-01','2016-12-31',1,'2016-04-14','2016-01-01',1,6,1,1,8000.00),(9,1200.00,0.00,1.00,0.05,10.00,0.15,0.00,0.00,1.00,'2016-01-01','2016-12-31',1,'2016-04-14','2016-01-01',1,8,1,1,200.00),(10,30.00,25.00,10.00,0.30,0.00,0.00,0.00,0.00,1.00,'2016-01-01','2016-12-31',1,'2016-04-14','2016-01-01',1,11,1,1,30.00),(11,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,1.00,'2016-01-01','2016-12-31',1,'2016-04-14','2016-01-01',1,7,1,1,8000.00);
/*!40000 ALTER TABLE `servicio_preciodeservicio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servicio_servicio`
--

DROP TABLE IF EXISTS `servicio_servicio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `servicio_servicio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `servicio` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `unidad_de_venta_id` int(11) NOT NULL,
  `unidad_de_consumo_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `servicio_servi_unidad_de_venta_id_497a28bc_fk_premisas_unidad_id` (`unidad_de_venta_id`),
  KEY `servicio_servicio_03520e42` (`unidad_de_consumo_id`),
  CONSTRAINT `servicio_serv_unidad_de_consumo_id_334a1b70_fk_almacen_unidad_id` FOREIGN KEY (`unidad_de_consumo_id`) REFERENCES `almacen_unidad` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `servicio_servic_unidad_de_venta_id_41fb160a_fk_almacen_unidad_id` FOREIGN KEY (`unidad_de_venta_id`) REFERENCES `almacen_unidad` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicio_servicio`
--

LOCK TABLES `servicio_servicio` WRITE;
/*!40000 ALTER TABLE `servicio_servicio` DISABLE KEYS */;
INSERT INTO `servicio_servicio` VALUES (1,'(AR) Armar','Servicio de armar un mueble',3,1),(2,'(DE) Desarmar','Servicio de desarmar mueble',3,2),(3,'(EC) Embalaje de contenidos','Embalaje',3,2),(4,'(DC) Desembalaje de contenidos','Desembalaje',3,2),(5,'(EP) Embalaje premium de muebles','Embalaje de muebles',3,2),(6,'(PI) Piano','Piano',3,4),(7,'(CF) Caja fuerte','Caja Fuerte',3,4),(8,'(SO) Trabajo de soga','soga',3,1),(9,'(MU) Mudanza','Mudanza',3,13),(10,'(DP) Desembalaje premium de mueble','Desembalaje',3,2),(11,'(TRA) Traslado','Traslado',3,14);
/*!40000 ALTER TABLE `servicio_servicio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servicio_serviciotipicopormueble`
--

DROP TABLE IF EXISTS `servicio_serviciotipicopormueble`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `servicio_serviciotipicopormueble` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cantidad` int(11) NOT NULL,
  `especificacion_de_mueble_id` int(11) NOT NULL,
  `servicio_id` int(11) NOT NULL,
  `predefinido` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `D0021180033e02db09537d078aad0316` (`especificacion_de_mueble_id`),
  KEY `servicio_servicioti_servicio_id_6d4f09bd_fk_servicio_servicio_id` (`servicio_id`),
  CONSTRAINT `D0021180033e02db09537d078aad0316` FOREIGN KEY (`especificacion_de_mueble_id`) REFERENCES `mueble_especificaciondemueble` (`id`),
  CONSTRAINT `servicio_servicioti_servicio_id_6d4f09bd_fk_servicio_servicio_id` FOREIGN KEY (`servicio_id`) REFERENCES `servicio_servicio` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicio_serviciotipicopormueble`
--

LOCK TABLES `servicio_serviciotipicopormueble` WRITE;
/*!40000 ALTER TABLE `servicio_serviciotipicopormueble` DISABLE KEYS */;
INSERT INTO `servicio_serviciotipicopormueble` VALUES (1,1,3,1,0),(2,1,1,2,1),(3,1,3,3,1),(4,1,7,5,1);
/*!40000 ALTER TABLE `servicio_serviciotipicopormueble` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `talonario_documentodeltalonario`
--

DROP TABLE IF EXISTS `talonario_documentodeltalonario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `talonario_documentodeltalonario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `numero` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `estado` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `informacion_de_proceso` longtext COLLATE utf8_unicode_ci NOT NULL,
  `informacion_de_beneficiario` longtext COLLATE utf8_unicode_ci NOT NULL,
  `numero_final` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `talonario_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `talonario_documentodeltalonario_e7d1d01e` (`talonario_id`),
  CONSTRAINT `talonario_docume_talonario_id_6cd80c98_fk_talonario_talonario_id` FOREIGN KEY (`talonario_id`) REFERENCES `talonario_talonario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `talonario_documentodeltalonario`
--

LOCK TABLES `talonario_documentodeltalonario` WRITE;
/*!40000 ALTER TABLE `talonario_documentodeltalonario` DISABLE KEYS */;
/*!40000 ALTER TABLE `talonario_documentodeltalonario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `talonario_documentodeltalonarioestado`
--

DROP TABLE IF EXISTS `talonario_documentodeltalonarioestado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `talonario_documentodeltalonarioestado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha_registro` date NOT NULL,
  `observacion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `predefinido` tinyint(1) NOT NULL,
  `documento_del_talonario_id` int(11) NOT NULL,
  `estado_de_documento_id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `b58b327d7bd223e0ebe372d7fc817701` (`documento_del_talonario_id`),
  KEY `D202d4d0caa705f7a449ec3571cf1402` (`estado_de_documento_id`),
  KEY `talonario_documentodeltalona_usuario_id_11e221f6_fk_auth_user_id` (`usuario_id`),
  CONSTRAINT `D202d4d0caa705f7a449ec3571cf1402` FOREIGN KEY (`estado_de_documento_id`) REFERENCES `estadoderegistro_estadoderegistro` (`id`),
  CONSTRAINT `b58b327d7bd223e0ebe372d7fc817701` FOREIGN KEY (`documento_del_talonario_id`) REFERENCES `talonario_documentodeltalonario` (`id`),
  CONSTRAINT `talonario_documentodeltalona_usuario_id_11e221f6_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `talonario_documentodeltalonarioestado`
--

LOCK TABLES `talonario_documentodeltalonarioestado` WRITE;
/*!40000 ALTER TABLE `talonario_documentodeltalonarioestado` DISABLE KEYS */;
/*!40000 ALTER TABLE `talonario_documentodeltalonarioestado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `talonario_talonario`
--

DROP TABLE IF EXISTS `talonario_talonario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `talonario_talonario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `talonario` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `prefijo` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `separador` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `numero_desde` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `numero_hasta` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `separado_sufijo` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `sufijo` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `numeracion_correlativa` tinyint(1) NOT NULL,
  `numero_de_documento` int(11) NOT NULL,
  `cantidad_fija` tinyint(1) NOT NULL,
  `tipo_de_documento_impreso_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `talonario_talonario_a2d0f438` (`tipo_de_documento_impreso_id`),
  CONSTRAINT `c9a1dc01832a89b93a05ee5dea392c58` FOREIGN KEY (`tipo_de_documento_impreso_id`) REFERENCES `talonario_tipodedocumentoimpreso` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `talonario_talonario`
--

LOCK TABLES `talonario_talonario` WRITE;
/*!40000 ALTER TABLE `talonario_talonario` DISABLE KEYS */;
INSERT INTO `talonario_talonario` VALUES (3,'nuevo','talonario','0','0','0','0','0','0',0,0,0,2),(4,'nuevo','talonario','0','0','0','0','0','0',0,0,0,2),(5,'nuevo','talonario','0','0','0','0','0','0',0,0,0,2),(6,'nuevo','talonario','0','0','0','0','0','0',0,0,0,2),(7,'nuevo','talonario','0','0','0','0','0','0',0,0,0,2);
/*!40000 ALTER TABLE `talonario_talonario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `talonario_talonarioestado`
--

DROP TABLE IF EXISTS `talonario_talonarioestado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `talonario_talonarioestado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha_registro` date NOT NULL,
  `observacion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `predefinido` tinyint(1) NOT NULL,
  `estado_de_documento_id` int(11) NOT NULL,
  `talonario_id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cf3e0692596746ef628e19d433f2be69` (`estado_de_documento_id`),
  KEY `talonario_talona_talonario_id_33bf11c6_fk_talonario_talonario_id` (`talonario_id`),
  KEY `talonario_talonarioestado_usuario_id_63d03632_fk_auth_user_id` (`usuario_id`),
  CONSTRAINT `cf3e0692596746ef628e19d433f2be69` FOREIGN KEY (`estado_de_documento_id`) REFERENCES `estadoderegistro_estadoderegistro` (`id`),
  CONSTRAINT `talonario_talona_talonario_id_33bf11c6_fk_talonario_talonario_id` FOREIGN KEY (`talonario_id`) REFERENCES `talonario_talonario` (`id`),
  CONSTRAINT `talonario_talonarioestado_usuario_id_63d03632_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `talonario_talonarioestado`
--

LOCK TABLES `talonario_talonarioestado` WRITE;
/*!40000 ALTER TABLE `talonario_talonarioestado` DISABLE KEYS */;
INSERT INTO `talonario_talonarioestado` VALUES (1,'2016-03-02','Creación del talonario',1,1,7,2);
/*!40000 ALTER TABLE `talonario_talonarioestado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `talonario_tipodedocumentoimpreso`
--

DROP TABLE IF EXISTS `talonario_tipodedocumentoimpreso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `talonario_tipodedocumentoimpreso` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_de_documento_impreso` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `talonario_tipodedocumentoimpreso`
--

LOCK TABLES `talonario_tipodedocumentoimpreso` WRITE;
/*!40000 ALTER TABLE `talonario_tipodedocumentoimpreso` DISABLE KEYS */;
INSERT INTO `talonario_tipodedocumentoimpreso` VALUES (1,'prueba','prueba'),(2,'prueba','prueba');
/*!40000 ALTER TABLE `talonario_tipodedocumentoimpreso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `talonario_trazabilidadtalonario`
--

DROP TABLE IF EXISTS `talonario_trazabilidadtalonario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `talonario_trazabilidadtalonario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha_registro` date NOT NULL,
  `fecha_modificacion` date DEFAULT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `talonario_id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `talonario_trazab_talonario_id_7290cdb7_fk_talonario_talonario_id` (`talonario_id`),
  KEY `talonario_trazabilidadtalona_usuario_id_68fa1fef_fk_auth_user_id` (`usuario_id`),
  CONSTRAINT `talonario_trazab_talonario_id_7290cdb7_fk_talonario_talonario_id` FOREIGN KEY (`talonario_id`) REFERENCES `talonario_talonario` (`id`),
  CONSTRAINT `talonario_trazabilidadtalona_usuario_id_68fa1fef_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `talonario_trazabilidadtalonario`
--

LOCK TABLES `talonario_trazabilidadtalonario` WRITE;
/*!40000 ALTER TABLE `talonario_trazabilidadtalonario` DISABLE KEYS */;
INSERT INTO `talonario_trazabilidadtalonario` VALUES (1,'2016-03-02','2016-03-02','Actualización del talonario: nuevo',7,2),(2,'2016-03-02','2016-03-02','Actualización del talonario: nuevo',7,2);
/*!40000 ALTER TABLE `talonario_trazabilidadtalonario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trabajador_cargotrabajador`
--

DROP TABLE IF EXISTS `trabajador_cargotrabajador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `trabajador_cargotrabajador` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cargo_trabajador` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `cargo_padre_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cargo_trabajador` (`cargo_trabajador`),
  KEY `trabaja_cargo_padre_id_2378121d_fk_trabajador_cargotrabajador_id` (`cargo_padre_id`),
  CONSTRAINT `trabaja_cargo_padre_id_2378121d_fk_trabajador_cargotrabajador_id` FOREIGN KEY (`cargo_padre_id`) REFERENCES `trabajador_cargotrabajador` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trabajador_cargotrabajador`
--

LOCK TABLES `trabajador_cargotrabajador` WRITE;
/*!40000 ALTER TABLE `trabajador_cargotrabajador` DISABLE KEYS */;
INSERT INTO `trabajador_cargotrabajador` VALUES (1,'Chofer','Chofer tipo 1',NULL),(2,'Ayudante de mudanza','Ayudante de mudanza',NULL),(3,'Cotizador','Cotizador',NULL);
/*!40000 ALTER TABLE `trabajador_cargotrabajador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trabajador_trabajador`
--

DROP TABLE IF EXISTS `trabajador_trabajador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `trabajador_trabajador` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dni` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `nombre` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `apellido` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `direccion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `telefono` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `volumen_en_camion` int(11) NOT NULL,
  `cargo_trabajador_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tr_cargo_trabajador_id_6e276986_fk_trabajador_cargotrabajador_id` (`cargo_trabajador_id`),
  CONSTRAINT `tr_cargo_trabajador_id_6e276986_fk_trabajador_cargotrabajador_id` FOREIGN KEY (`cargo_trabajador_id`) REFERENCES `trabajador_cargotrabajador` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trabajador_trabajador`
--

LOCK TABLES `trabajador_trabajador` WRITE;
/*!40000 ALTER TABLE `trabajador_trabajador` DISABLE KEYS */;
INSERT INTO `trabajador_trabajador` VALUES (1,'123','Andres','Alvarez','Av vargas','04149837929','andres@gdh.com',0,3);
/*!40000 ALTER TABLE `trabajador_trabajador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trabajador_trabajadorestadoderegistro`
--

DROP TABLE IF EXISTS `trabajador_trabajadorestadoderegistro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `trabajador_trabajadorestadoderegistro` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `observacion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `predefinido` tinyint(1) NOT NULL,
  `estado_de_registro_id` int(11) NOT NULL,
  `trabajador_id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `D154d3c7508c39b0a90a480b70f2a87b` (`estado_de_registro_id`),
  KEY `trabajador_tra_trabajador_id_fcfee4e_fk_trabajador_trabajador_id` (`trabajador_id`),
  KEY `trabajador_trabajadorestadod_usuario_id_1e14d6d6_fk_auth_user_id` (`usuario_id`),
  CONSTRAINT `D154d3c7508c39b0a90a480b70f2a87b` FOREIGN KEY (`estado_de_registro_id`) REFERENCES `estadoderegistro_estadoderegistro` (`id`),
  CONSTRAINT `trabajador_tra_trabajador_id_fcfee4e_fk_trabajador_trabajador_id` FOREIGN KEY (`trabajador_id`) REFERENCES `trabajador_trabajador` (`id`),
  CONSTRAINT `trabajador_trabajadorestadod_usuario_id_1e14d6d6_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trabajador_trabajadorestadoderegistro`
--

LOCK TABLES `trabajador_trabajadorestadoderegistro` WRITE;
/*!40000 ALTER TABLE `trabajador_trabajadorestadoderegistro` DISABLE KEYS */;
INSERT INTO `trabajador_trabajadorestadoderegistro` VALUES (1,'2016-04-06','Creación de trabajador',1,2,1,2);
/*!40000 ALTER TABLE `trabajador_trabajadorestadoderegistro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vehiculo_choferasignado`
--

DROP TABLE IF EXISTS `vehiculo_choferasignado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vehiculo_choferasignado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha_desde` date NOT NULL,
  `fecha_hasta` date NOT NULL,
  `detalle_de_vehiculo_id` int(11) NOT NULL,
  `trabajador_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `vehiculo_choferasignado_b8492fc2` (`detalle_de_vehiculo_id`),
  KEY `vehiculo_choferasignado_12b1cd18` (`trabajador_id`),
  CONSTRAINT `D6a129485d01c7720d0b5531995afb35` FOREIGN KEY (`detalle_de_vehiculo_id`) REFERENCES `vehiculo_detalledevehiculo` (`id`),
  CONSTRAINT `vehiculo_chof_trabajador_id_30247261_fk_trabajador_trabajador_id` FOREIGN KEY (`trabajador_id`) REFERENCES `trabajador_trabajador` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehiculo_choferasignado`
--

LOCK TABLES `vehiculo_choferasignado` WRITE;
/*!40000 ALTER TABLE `vehiculo_choferasignado` DISABLE KEYS */;
/*!40000 ALTER TABLE `vehiculo_choferasignado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vehiculo_detalledevehiculo`
--

DROP TABLE IF EXISTS `vehiculo_detalledevehiculo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vehiculo_detalledevehiculo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `numero_de_camion` int(11) NOT NULL,
  `ancho` decimal(7,2) NOT NULL,
  `largo` decimal(7,2) NOT NULL,
  `alto` decimal(7,2) NOT NULL,
  `ancho_aux` decimal(7,2) NOT NULL,
  `largo_aux` decimal(7,2) NOT NULL,
  `alto_aux` decimal(7,2) NOT NULL,
  `tara_vehiculo` decimal(7,2) NOT NULL,
  `observacion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `vehiculo_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `vehiculo_detalledevehiculo_31609bf9` (`vehiculo_id`),
  CONSTRAINT `vehiculo_detalledeve_vehiculo_id_437c950_fk_vehiculo_vehiculo_id` FOREIGN KEY (`vehiculo_id`) REFERENCES `vehiculo_vehiculo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehiculo_detalledevehiculo`
--

LOCK TABLES `vehiculo_detalledevehiculo` WRITE;
/*!40000 ALTER TABLE `vehiculo_detalledevehiculo` DISABLE KEYS */;
/*!40000 ALTER TABLE `vehiculo_detalledevehiculo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vehiculo_estadodevehiculo`
--

DROP TABLE IF EXISTS `vehiculo_estadodevehiculo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vehiculo_estadodevehiculo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `observacion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `predefinido` tinyint(1) NOT NULL,
  `detalle_especifico_id` int(11) NOT NULL,
  `estado_de_registro_id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ve_detalle_especifico_id_e6e611_fk_vehiculo_detalledevehiculo_id` (`detalle_especifico_id`),
  KEY `D92ce076bf43a11eddc8834983887649` (`estado_de_registro_id`),
  KEY `vehiculo_estadodevehiculo_usuario_id_5b41916f_fk_auth_user_id` (`usuario_id`),
  CONSTRAINT `D92ce076bf43a11eddc8834983887649` FOREIGN KEY (`estado_de_registro_id`) REFERENCES `estadoderegistro_estadoderegistro` (`id`),
  CONSTRAINT `ve_detalle_especifico_id_e6e611_fk_vehiculo_detalledevehiculo_id` FOREIGN KEY (`detalle_especifico_id`) REFERENCES `vehiculo_detalledevehiculo` (`id`),
  CONSTRAINT `vehiculo_estadodevehiculo_usuario_id_5b41916f_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehiculo_estadodevehiculo`
--

LOCK TABLES `vehiculo_estadodevehiculo` WRITE;
/*!40000 ALTER TABLE `vehiculo_estadodevehiculo` DISABLE KEYS */;
/*!40000 ALTER TABLE `vehiculo_estadodevehiculo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vehiculo_vehiculo`
--

DROP TABLE IF EXISTS `vehiculo_vehiculo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vehiculo_vehiculo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `marca` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `modelo` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `transmision` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `motor` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `volumen_total_carga` decimal(7,2) NOT NULL,
  `peso_total_carga` decimal(7,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehiculo_vehiculo`
--

LOCK TABLES `vehiculo_vehiculo` WRITE;
/*!40000 ALTER TABLE `vehiculo_vehiculo` DISABLE KEYS */;
/*!40000 ALTER TABLE `vehiculo_vehiculo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `widget_widget`
--

DROP TABLE IF EXISTS `widget_widget`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `widget_widget` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_id` int(11) NOT NULL,
  `nombre` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `visible` tinyint(1) NOT NULL,
  `desplegable` int(11) NOT NULL,
  `numero_de_columna` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `color` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `orden` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuario_id` (`usuario_id`,`nombre`),
  CONSTRAINT `widget_widget_usuario_id_165f0770_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `widget_widget`
--

LOCK TABLES `widget_widget` WRITE;
/*!40000 ALTER TABLE `widget_widget` DISABLE KEYS */;
INSERT INTO `widget_widget` VALUES (1,1,'Autofiltros',0,1,'2x3','Rojo',1),(2,1,'Filtros Rápidos',0,2,'1x0','Verde',4),(3,2,'Autofiltros',0,2,'2x3','red',1),(4,1,'Menú',1,1,'2x3','Azul',2),(5,1,'Tablas Relacionadas',0,1,'2x3','Azul',5),(7,1,'Ficha',1,1,'2x3','Azul',1),(8,1,'Fases del Proceso',0,1,'2x3','Azul',3);
/*!40000 ALTER TABLE `widget_widget` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'db_mtvmcotizacionv2_prd'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-05-03 16:57:12
