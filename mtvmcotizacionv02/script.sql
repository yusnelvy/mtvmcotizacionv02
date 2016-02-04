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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ambiente_ambiente`
--

LOCK TABLES `ambiente_ambiente` WRITE;
/*!40000 ALTER TABLE `ambiente_ambiente` DISABLE KEYS */;
INSERT INTO `ambiente_ambiente` VALUES (1,'Ático','Es un ambiente en la parte superior de una casa',0);
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ambiente_ambienteportipodeinmueble`
--

LOCK TABLES `ambiente_ambienteportipodeinmueble` WRITE;
/*!40000 ALTER TABLE `ambiente_ambienteportipodeinmueble` DISABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=208 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add Pais',7,'add_pais'),(20,'Can change Pais',7,'change_pais'),(21,'Can delete Pais',7,'delete_pais'),(22,'Can add Provincia',8,'add_provincia'),(23,'Can change Provincia',8,'change_provincia'),(24,'Can delete Provincia',8,'delete_provincia'),(25,'Can add Ciudad',9,'add_ciudad'),(26,'Can change Ciudad',9,'change_ciudad'),(27,'Can delete Ciudad',9,'delete_ciudad'),(28,'Can add Barrio',10,'add_barrio'),(29,'Can change Barrio',10,'change_barrio'),(30,'Can delete Barrio',10,'delete_barrio'),(31,'Can add Dirección',11,'add_direccion'),(32,'Can change Dirección',11,'change_direccion'),(33,'Can delete Dirección',11,'delete_direccion'),(34,'Can add Tipo de edificación',12,'add_tipodeedificacion'),(35,'Can change Tipo de edificación',12,'change_tipodeedificacion'),(36,'Can delete Tipo de edificación',12,'delete_tipodeedificacion'),(37,'Can add Edificación',13,'add_edificacion'),(38,'Can change Edificación',13,'change_edificacion'),(39,'Can delete Edificación',13,'delete_edificacion'),(40,'Can add Tipo de ascensor',14,'add_tipodeascensor'),(41,'Can change Tipo de ascensor',14,'change_tipodeascensor'),(42,'Can delete Tipo de ascensor',14,'delete_tipodeascensor'),(43,'Can add Ascensor',15,'add_ascensor'),(44,'Can change Ascensor',15,'change_ascensor'),(45,'Can delete Ascensor',15,'delete_ascensor'),(46,'Can add Tipo de inmueble',16,'add_tipodeinmueble'),(47,'Can change Tipo de inmueble',16,'change_tipodeinmueble'),(48,'Can delete Tipo de inmueble',16,'delete_tipodeinmueble'),(49,'Can add Especificación de inmueble',17,'add_especificaciondeinmueble'),(50,'Can change Especificación de inmueble',17,'change_especificaciondeinmueble'),(51,'Can delete Especificación de inmueble',17,'delete_especificaciondeinmueble'),(52,'Can add Inmueble',18,'add_inmueble'),(53,'Can change Inmueble',18,'change_inmueble'),(54,'Can delete Inmueble',18,'delete_inmueble'),(55,'Can add Horario disponible',19,'add_horariodisponible'),(56,'Can change Horario disponible',19,'change_horariodisponible'),(57,'Can delete Horario disponible',19,'delete_horariodisponible'),(58,'Can add Calle',20,'add_calle'),(59,'Can change Calle',20,'change_calle'),(60,'Can delete Calle',20,'delete_calle'),(61,'Can add ambiente',21,'add_ambiente'),(62,'Can change ambiente',21,'change_ambiente'),(63,'Can delete ambiente',21,'delete_ambiente'),(64,'Can add Ambiente por tipo inmueble',22,'add_ambienteportipodeinmueble'),(65,'Can change Ambiente por tipo inmueble',22,'change_ambienteportipodeinmueble'),(66,'Can delete Ambiente por tipo inmueble',22,'delete_ambienteportipodeinmueble'),(67,'Can add Estado de registro de ambiente',23,'add_ambienteestadoderegistro'),(68,'Can change Estado de registro de ambiente',23,'change_ambienteestadoderegistro'),(69,'Can delete Estado de registro de ambiente',23,'delete_ambienteestadoderegistro'),(70,'Can add Sexo',24,'add_sexo'),(71,'Can change Sexo',24,'change_sexo'),(72,'Can delete Sexo',24,'delete_sexo'),(73,'Can add Estado civil',25,'add_estadocivil'),(74,'Can change Estado civil',25,'change_estadocivil'),(75,'Can delete Estado civil',25,'delete_estadocivil'),(76,'Can add Tipo de cliente',26,'add_tipodecliente'),(77,'Can change Tipo de cliente',26,'change_tipodecliente'),(78,'Can delete Tipo de cliente',26,'delete_tipodecliente'),(79,'Can add Tipo de relacion',27,'add_tipoderelacion'),(80,'Can change Tipo de relacion',27,'change_tipoderelacion'),(81,'Can delete Tipo de relacion',27,'delete_tipoderelacion'),(82,'Can add Tipo de información de contacto',28,'add_tipodeinformaciondecontacto'),(83,'Can change Tipo de información de contacto',28,'change_tipodeinformaciondecontacto'),(84,'Can delete Tipo de información de contacto',28,'delete_tipodeinformaciondecontacto'),(85,'Can add Cliente',29,'add_cliente'),(86,'Can change Cliente',29,'change_cliente'),(87,'Can delete Cliente',29,'delete_cliente'),(88,'Can add Contacto',30,'add_contacto'),(89,'Can change Contacto',30,'change_contacto'),(90,'Can delete Contacto',30,'delete_contacto'),(91,'Can add Información de contacto',31,'add_informaciondecontacto'),(92,'Can change Información de contacto',31,'change_informaciondecontacto'),(93,'Can delete Información de contacto',31,'delete_informaciondecontacto'),(94,'Can add Dirección del cliente',32,'add_clientedireccion'),(95,'Can change Dirección del cliente',32,'change_clientedireccion'),(96,'Can delete Dirección del cliente',32,'delete_clientedireccion'),(97,'Can add Estado de registro de cliente',33,'add_clienteestadoderegistro'),(98,'Can change Estado de registro de cliente',33,'change_clienteestadoderegistro'),(99,'Can delete Estado de registro de cliente',33,'delete_clienteestadoderegistro'),(100,'Can add Contenedor',34,'add_contenedor'),(101,'Can change Contenedor',34,'change_contenedor'),(102,'Can delete Contenedor',34,'delete_contenedor'),(103,'Can add Contenedor tipico por mueble',35,'add_contenedortipicopormueble'),(104,'Can change Contenedor tipico por mueble',35,'change_contenedortipicopormueble'),(105,'Can delete Contenedor tipico por mueble',35,'delete_contenedortipicopormueble'),(106,'Can add Tipo de mueble',36,'add_tipodemueble'),(107,'Can change Tipo de mueble',36,'change_tipodemueble'),(108,'Can delete Tipo de mueble',36,'delete_tipodemueble'),(109,'Can add Mueble',37,'add_mueble'),(110,'Can change Mueble',37,'change_mueble'),(111,'Can delete Mueble',37,'delete_mueble'),(112,'Can add Especificación del mueble',38,'add_especificaciondemueble'),(113,'Can change Especificación del mueble',38,'change_especificaciondemueble'),(114,'Can delete Especificación del mueble',38,'delete_especificaciondemueble'),(115,'Can add Mueble por ambiente',39,'add_muebleporambiente'),(116,'Can change Mueble por ambiente',39,'change_muebleporambiente'),(117,'Can delete Mueble por ambiente',39,'delete_muebleporambiente'),(118,'Can add Tipo de documento',40,'add_tipodedocumento'),(119,'Can change Tipo de documento',40,'change_tipodedocumento'),(120,'Can delete Tipo de documento',40,'delete_tipodedocumento'),(121,'Can add Estado de documento',41,'add_estadodedocumento'),(122,'Can change Estado de documento',41,'change_estadodedocumento'),(123,'Can delete Estado de documento',41,'delete_estadodedocumento'),(124,'Can add Estado',42,'add_estado'),(125,'Can change Estado',42,'change_estado'),(126,'Can delete Estado',42,'delete_estado'),(127,'Can add Estado de registro',43,'add_estadoderegistro'),(128,'Can change Estado de registro',43,'change_estadoderegistro'),(129,'Can delete Estado de registro',43,'delete_estadoderegistro'),(130,'Can add Complejidad y riesgo',44,'add_complejidadriesgo'),(131,'Can change Complejidad y riesgo',44,'change_complejidadriesgo'),(132,'Can delete Complejidad y riesgo',44,'delete_complejidadriesgo'),(133,'Can add Nivel de complejidad y riesgo',45,'add_nivelcomplejidadriesgo'),(134,'Can change Nivel de complejidad y riesgo',45,'change_nivelcomplejidadriesgo'),(135,'Can delete Nivel de complejidad y riesgo',45,'delete_nivelcomplejidadriesgo'),(136,'Can add Tipo de mensaje',46,'add_tipodemensaje'),(137,'Can change Tipo de mensaje',46,'change_tipodemensaje'),(138,'Can delete Tipo de mensaje',46,'delete_tipodemensaje'),(139,'Can add Mensaje',47,'add_mensaje'),(140,'Can change Mensaje',47,'change_mensaje'),(141,'Can delete Mensaje',47,'delete_mensaje'),(142,'Can add empresa',48,'add_empresa'),(143,'Can change empresa',48,'change_empresa'),(144,'Can delete empresa',48,'delete_empresa'),(145,'Can add Personalización Visual',49,'add_personalizacionvisual'),(146,'Can change Personalización Visual',49,'change_personalizacionvisual'),(147,'Can delete Personalización Visual',49,'delete_personalizacionvisual'),(148,'Can add Variente Visual',50,'add_variantevisual'),(149,'Can change Variente Visual',50,'change_variantevisual'),(150,'Can delete Variente Visual',50,'delete_variantevisual'),(151,'Can add Detalle de la variente visual',51,'add_variantevisualdetalle'),(152,'Can change Detalle de la variente visual',51,'change_variantevisualdetalle'),(153,'Can delete Detalle de la variente visual',51,'delete_variantevisualdetalle'),(154,'Can add Dato precargado',52,'add_datosprecargado'),(155,'Can change Dato precargado',52,'change_datosprecargado'),(156,'Can delete Dato precargado',52,'delete_datosprecargado'),(157,'Can add Moneda',53,'add_moneda'),(158,'Can change Moneda',53,'change_moneda'),(159,'Can delete Moneda',53,'delete_moneda'),(160,'Can add Medio',54,'add_medio'),(161,'Can change Medio',54,'change_medio'),(162,'Can delete Medio',54,'delete_medio'),(163,'Can add Medio especifico',55,'add_medioespecifico'),(164,'Can change Medio especifico',55,'change_medioespecifico'),(165,'Can delete Medio especifico',55,'delete_medioespecifico'),(166,'Can add Tipo de referido',56,'add_tipodereferido'),(167,'Can change Tipo de referido',56,'change_tipodereferido'),(168,'Can delete Tipo de referido',56,'delete_tipodereferido'),(169,'Can add Alianza',57,'add_alianza'),(170,'Can change Alianza',57,'change_alianza'),(171,'Can delete Alianza',57,'delete_alianza'),(172,'Can add Estado de registro de alianza',58,'add_alianzaestado'),(173,'Can change Estado de registro de alianza',58,'change_alianzaestado'),(174,'Can delete Estado de registro de alianza',58,'delete_alianzaestado'),(175,'Can add Institución',59,'add_institucion'),(176,'Can change Institución',59,'change_institucion'),(177,'Can delete Institución',59,'delete_institucion'),(178,'Can add Persona',60,'add_personaaliado'),(179,'Can change Persona',60,'change_personaaliado'),(180,'Can delete Persona',60,'delete_personaaliado'),(181,'Can add Persona',61,'add_fuentedepromocion'),(182,'Can change Persona',61,'change_fuentedepromocion'),(183,'Can delete Persona',61,'delete_fuentedepromocion'),(184,'Can add menu',62,'add_menu'),(185,'Can change menu',62,'change_menu'),(186,'Can delete menu',62,'delete_menu'),(187,'Can add Menu favorito',63,'add_menufavorito'),(188,'Can change Menu favorito',63,'change_menufavorito'),(189,'Can delete Menu favorito',63,'delete_menufavorito'),(190,'Can add Cargo de trabajador',64,'add_cargotrabajador'),(191,'Can change Cargo de trabajador',64,'change_cargotrabajador'),(192,'Can delete Cargo de trabajador',64,'delete_cargotrabajador'),(193,'Can add Trabajador',65,'add_trabajador'),(194,'Can change Trabajador',65,'change_trabajador'),(195,'Can delete Trabajador',65,'delete_trabajador'),(196,'Can add Vehículo',66,'add_vehiculo'),(197,'Can change Vehículo',66,'change_vehiculo'),(198,'Can delete Vehículo',66,'delete_vehiculo'),(199,'Can add Vehículo',67,'add_detalledevehiculo'),(200,'Can change Vehículo',67,'change_detalledevehiculo'),(201,'Can delete Vehículo',67,'delete_detalledevehiculo'),(202,'Can add Estado de registro de vehículo',68,'add_estadodevehiculo'),(203,'Can change Estado de registro de vehículo',68,'change_estadodevehiculo'),(204,'Can delete Estado de registro de vehículo',68,'delete_estadodevehiculo'),(205,'Can add Chofer asignado',69,'add_choferasignado'),(206,'Can change Chofer asignado',69,'change_choferasignado'),(207,'Can delete Chofer asignado',69,'delete_choferasignado');
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
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$20000$gmTsKWYIalwb$28hXj6/6CuPT7gfGkAWwMxAGwSHxAZLkJW7vBuK0Xv0=','2016-02-04 15:02:43.135609',1,'admin','','','yusnelvy@gmail.com',1,1,'2016-02-02 16:19:15.301642'),(2,'pbkdf2_sha256$20000$j3U2c7T8YCuU$8AJhxiMIMGqZWuWIQIvjWGXgsSfpWo0A0kIFDgnNkPY=',NULL,0,'std','Estandar','Estandar','',0,1,'2016-02-02 19:02:27.000000');
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
  PRIMARY KEY (`id`),
  KEY `cliente_clientedirecci_cliente_id_32bc0fa6_fk_cliente_cliente_id` (`cliente_id`),
  KEY `cliente_cliented_direccion_id_7b41af54_fk_direccion_direccion_id` (`direccion_id`),
  CONSTRAINT `cliente_cliented_direccion_id_7b41af54_fk_direccion_direccion_id` FOREIGN KEY (`direccion_id`) REFERENCES `direccion_direccion` (`id`),
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
  `fecha_nacimiento` date NOT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente_estadocivil`
--

LOCK TABLES `cliente_estadocivil` WRITE;
/*!40000 ALTER TABLE `cliente_estadocivil` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente_sexo`
--

LOCK TABLES `cliente_sexo` WRITE;
/*!40000 ALTER TABLE `cliente_sexo` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente_tipodecliente`
--

LOCK TABLES `cliente_tipodecliente` WRITE;
/*!40000 ALTER TABLE `cliente_tipodecliente` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente_tipodeinformaciondecontacto`
--

LOCK TABLES `cliente_tipodeinformaciondecontacto` WRITE;
/*!40000 ALTER TABLE `cliente_tipodeinformaciondecontacto` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente_tipoderelacion`
--

LOCK TABLES `cliente_tipoderelacion` WRITE;
/*!40000 ALTER TABLE `cliente_tipoderelacion` DISABLE KEYS */;
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
  `porcentaje` decimal(5,2) NOT NULL,
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
  `capacidad_de_volumen` decimal(7,3) NOT NULL,
  `capacidad_de_peso` decimal(7,3) NOT NULL,
  `ancho` int(11) NOT NULL,
  `largo` int(11) NOT NULL,
  `alto` int(11) NOT NULL,
  `volumen_en_camion` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `contenedor` (`contenedor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contenedor_contenedor`
--

LOCK TABLES `contenedor_contenedor` WRITE;
/*!40000 ALTER TABLE `contenedor_contenedor` DISABLE KEYS */;
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
  PRIMARY KEY (`id`),
  KEY `contenedor_co_contenedor_id_2fe1a6a0_fk_contenedor_contenedor_id` (`contenedor_id`),
  KEY `f0858580c71e366be272be91ad1ccac5` (`especificacion_de_mueble_id`),
  CONSTRAINT `contenedor_co_contenedor_id_2fe1a6a0_fk_contenedor_contenedor_id` FOREIGN KEY (`contenedor_id`) REFERENCES `contenedor_contenedor` (`id`),
  CONSTRAINT `f0858580c71e366be272be91ad1ccac5` FOREIGN KEY (`especificacion_de_mueble_id`) REFERENCES `mueble_especificaciondemueble` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contenedor_contenedortipicopormueble`
--

LOCK TABLES `contenedor_contenedortipicopormueble` WRITE;
/*!40000 ALTER TABLE `contenedor_contenedortipicopormueble` DISABLE KEYS */;
/*!40000 ALTER TABLE `contenedor_contenedortipicopormueble` ENABLE KEYS */;
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
  `capacidad_carga` decimal(8,3) NOT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccion_barrio`
--

LOCK TABLES `direccion_barrio` WRITE;
/*!40000 ALTER TABLE `direccion_barrio` DISABLE KEYS */;
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
INSERT INTO `direccion_ciudad` VALUES (1,'Buenos Aires',10,1),(2,'Córdoba',10,7),(3,'Rosario',10,22),(4,'La Plata',10,1),(5,'Mar del Plata',10,1),(6,'San Miguel de Tucumán',10,25),(7,'Ciudad de Salta',10,18),(8,'Ciudad de Santa Fe',10,22),(9,'Ciudad de Corrientes',10,8),(10,'Bahía Blanca',10,1),(11,'Resistencia',10,5),(12,'Vicente López',10,1),(13,'Posadas',10,15),(14,'Merlo',10,1),(15,'Paraná',10,9),(16,'San Salvador de Jujuy',10,11),(17,'Quilmes',10,1),(18,'Ciudad de Santiago del Estero',10,23),(19,'Pilar',10,1),(20,'Banfield',10,1),(21,'Guaymallén',10,14),(22,'José C. Paz',10,1),(23,'Lanús',10,1),(24,'Ciudad de Neuquén',10,16),(25,'Ciudad de Formosa',10,10),(26,'Godoy Cruz',10,14),(27,'Las Heras',10,14),(28,'Gregorio de Laferrere',10,1),(29,'Berazategui',10,1),(30,'González Catán',10,1),(31,'San Miguel',10,1),(32,'Ciudad de Río Cuarto',10,7),(33,'Ciudad de San Luis',10,20),(34,'Moreno',10,1),(35,'Concordia',10,9),(36,'Ciudad de La Rioja',10,13),(37,'San Fernando del Valle de Catamarca',10,4),(38,'Comodoro Rivadavia',10,6),(39,'Isidro Casanova',10,1),(40,'San Rafael',10,14),(41,'Ituzaingó',10,1),(42,'San Nicolás de los Arroyos',10,1),(43,'Florencio Varela',10,1),(44,'Ciudad de San Juan',10,19),(45,'Lomas de Zamora',10,1),(46,'Temperley',10,1),(47,'Ciudad de Mendoza',10,14),(48,'Monte Grande',10,1),(49,'Bernal',10,1),(50,'San Justo',10,1),(51,'San Carlos de Bariloche',10,17),(52,'Pergamino',10,1),(53,'Castelar',10,1),(54,'Rafael Castillo',10,1),(55,'Trelew',10,6),(56,'Santa Rosa',10,12),(57,'Tandil',10,1),(58,'Libertad',10,1),(59,'Ramos Mejía',10,1),(60,'Villa Mercedes',10,20),(61,'Río Gallegos',10,21),(62,'Caseros',10,1),(63,'La Banda',10,23),(64,'Trujui',10,1),(65,'Ezeiza',10,1),(66,'Morón',10,1),(67,'Virrey del Pino',10,1),(68,'Maipú',10,14),(69,'Zárate',10,1),(70,'Burzaco',10,1),(71,'Grand Bourg',10,1),(72,'Monte Chingolo',10,1),(73,'Olavarría',10,1),(74,'Rawson',10,6),(75,'Rafaela',10,22),(76,'Junín',10,1),(77,'Remedios de Escalada (Partido de Lanús)',10,1),(78,'La Tablada',10,1),(79,'Campana',10,1),(80,'Presidencia Roque Sáenz Peña',10,5),(81,'Rivadavia',10,19),(82,'Florida (no es ciudad sino barrio)',10,1),(83,'Villa Madero',10,1),(84,'Olivos (no es ciudad sino barrio)',10,1),(85,'Gualeguaychú',10,9),(86,'Villa Gobernador Gálvez',10,22),(87,'Villa Luzuriaga',10,1),(88,'Boulogne Sur Mer',10,1),(89,'Chimbas',10,19),(90,'Ciudadela',10,1),(91,'Luján de Cuyo',10,14),(92,'Ezpeleta',10,1),(93,'Villa María',10,7),(94,'Alderetes',10,7),(95,'General Roca',10,17),(96,'San Fernando',10,1),(97,'Ciudad Evita',10,1),(98,'Venado Tuerto',10,22),(99,'Bella Vista',10,1),(100,'Luján',10,1),(101,'San Ramón de la Nueva Orán',10,18),(102,'Cipolletti',10,17),(103,'Goya',10,8),(104,'Reconquista',10,22),(105,'Wilde',10,1),(106,'Martínez',10,1),(107,'Necochea',10,1),(108,'Don Torcuato',10,1),(109,'Banda del Río Salí',10,25),(110,'Concepción del Uruguay',10,9),(111,'General Rodríguez',10,1),(112,'Villa Tesei',10,1),(113,'Ciudad Jardín El Libertador',10,1),(114,'Villa Carlos Paz',10,7),(115,'Sarandí',10,1),(116,'Chivilcoy',10,1),(117,'Villa Domínico',10,1),(118,'Béccar',10,1),(119,'San Francisco',10,7),(120,'Glew',10,1),(121,'Puerto Madryn',10,6),(122,'Punta Alta',10,1),(123,'El Palomar',10,1),(124,'Rafael Calzada',10,1),(125,'Tartagal',10,18),(126,'San Pedro de Jujuy',10,11),(127,'Belén de Escobar',10,1),(128,'Berisso',10,1),(129,'Mariano Acosta',10,1),(130,'San Francisco Solano',10,1),(131,'Los Polvorines',10,1),(132,'Azul',10,1),(133,'Lomas del Mirador',10,1),(134,'Río Grande',10,24),(135,'Presidente Perón',10,1),(136,'General Pico',10,12),(137,'Mercedes',10,1),(138,'Bosques',10,1),(139,'Oberá',10,15),(140,'Barranqueras',10,5),(141,'Yerba Buena/Marcos Paz',10,25),(142,'Villa Centenario',10,1),(143,'San Martín',10,14),(144,'Gobernador Julio A Costa',10,1),(145,'William Morris',10,1),(146,'El Jagüel',10,1),(147,'Villa Mariano Moreno-El Colmenar',10,25),(148,'Eldorado',10,15),(149,'Longchamps',10,1),(150,'Clorinda',10,10),(151,'Viedma',10,17),(152,'Concepción',10,25),(153,'Tres Arroyos',10,1),(154,'Ushuaia',10,24),(155,'San Isidro',10,1),(156,'Palpalá',10,11);
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
  `cantidad_de_pisos` int(11) NOT NULL,
  `cantidad_de_inmuebles_por_piso` int(11) NOT NULL,
  `total_inmuebles` int(11) NOT NULL,
  `rampa` tinyint(1) NOT NULL,
  `distancia_del_vehiculo` int(11) NOT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccion_especificaciondeinmueble`
--

LOCK TABLES `direccion_especificaciondeinmueble` WRITE;
/*!40000 ALTER TABLE `direccion_especificaciondeinmueble` DISABLE KEYS */;
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
  `numero_de_pisos` int(11) NOT NULL,
  `nombre_del_piso` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `cantidad_de_ambientes` int(11) NOT NULL,
  `pisos_por_escalera` int(11) NOT NULL,
  `numero_de_plantas` int(11) NOT NULL,
  `total_m2` decimal(7,2) NOT NULL,
  `baulera` tinyint(1) NOT NULL,
  `volumen_baulera` decimal(8,3) NOT NULL,
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
INSERT INTO `direccion_provincia` VALUES (1,'Buenos Aires','',10),(2,'Buenos Aires-GBA','',10),(3,'Capital Federal','',10),(4,'Catamarca','',10),(5,'Chaco','',10),(6,'Chubut','',10),(7,'Córdoba','',10),(8,'Corrientes','',10),(9,'Entre Ríos','',10),(10,'Formosa','',10),(11,'Jujuy','',10),(12,'La Pampa','',10),(13,'La Rioja','',10),(14,'Mendoza','',10),(15,'Misiones','',10),(16,'Neuquén','',10),(17,'Río Negro','',10),(18,'Salta','',10),(19,'San Juan','',10),(20,'San Luis','',10),(21,'Santa Cruz','',10),(22,'Santa Fe','',10),(23,'Santiago del Estero','',10),(24,'Tierra del Fuego','',10),(25,'Tucumán','',10);
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccion_tipodeascensor`
--

LOCK TABLES `direccion_tipodeascensor` WRITE;
/*!40000 ALTER TABLE `direccion_tipodeascensor` DISABLE KEYS */;
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccion_tipodeedificacion`
--

LOCK TABLES `direccion_tipodeedificacion` WRITE;
/*!40000 ALTER TABLE `direccion_tipodeedificacion` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccion_tipodeinmueble`
--

LOCK TABLES `direccion_tipodeinmueble` WRITE;
/*!40000 ALTER TABLE `direccion_tipodeinmueble` DISABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2016-02-02 19:02:27.820200','2','std',1,'',4,1),(2,'2016-02-02 19:03:06.915584','2','std',2,'Changed first_name and last_name.',4,1),(3,'2016-02-02 19:50:35.649799','18','prueba',1,'',35,1),(4,'2016-02-02 19:51:06.258218','18','prueba',2,'No fields changed.',35,1),(5,'2016-02-02 20:00:04.433876','18','prueba',3,'',35,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=70 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(21,'ambiente','ambiente'),(23,'ambiente','ambienteestadoderegistro'),(22,'ambiente','ambienteportipodeinmueble'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(29,'cliente','cliente'),(32,'cliente','clientedireccion'),(33,'cliente','clienteestadoderegistro'),(30,'cliente','contacto'),(25,'cliente','estadocivil'),(31,'cliente','informaciondecontacto'),(24,'cliente','sexo'),(26,'cliente','tipodecliente'),(28,'cliente','tipodeinformaciondecontacto'),(27,'cliente','tipoderelacion'),(44,'complejidadriesgo','complejidadriesgo'),(45,'complejidadriesgo','nivelcomplejidadriesgo'),(34,'contenedor','contenedor'),(35,'contenedor','contenedortipicopormueble'),(5,'contenttypes','contenttype'),(15,'direccion','ascensor'),(10,'direccion','barrio'),(20,'direccion','calle'),(9,'direccion','ciudad'),(11,'direccion','direccion'),(13,'direccion','edificacion'),(17,'direccion','especificaciondeinmueble'),(19,'direccion','horariodisponible'),(18,'direccion','inmueble'),(7,'direccion','pais'),(8,'direccion','provincia'),(14,'direccion','tipodeascensor'),(12,'direccion','tipodeedificacion'),(16,'direccion','tipodeinmueble'),(42,'estadoderegistro','estado'),(43,'estadoderegistro','estadoderegistro'),(41,'gestiondedocumento','estadodedocumento'),(40,'gestiondedocumento','tipodedocumento'),(47,'mensaje','mensaje'),(46,'mensaje','tipodemensaje'),(62,'menu','menu'),(63,'menu','menufavorito'),(38,'mueble','especificaciondemueble'),(37,'mueble','mueble'),(39,'mueble','muebleporambiente'),(36,'mueble','tipodemueble'),(52,'premisas','datosprecargado'),(48,'premisas','empresa'),(53,'premisas','moneda'),(49,'premisas','personalizacionvisual'),(50,'premisas','variantevisual'),(51,'premisas','variantevisualdetalle'),(57,'promocion','alianza'),(58,'promocion','alianzaestado'),(61,'promocion','fuentedepromocion'),(59,'promocion','institucion'),(54,'promocion','medio'),(55,'promocion','medioespecifico'),(60,'promocion','personaaliado'),(56,'promocion','tipodereferido'),(6,'sessions','session'),(64,'trabajador','cargotrabajador'),(65,'trabajador','trabajador'),(69,'vehiculo','choferasignado'),(67,'vehiculo','detalledevehiculo'),(68,'vehiculo','estadodevehiculo'),(66,'vehiculo','vehiculo');
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
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2016-02-04 14:46:36.516781'),(2,'auth','0001_initial','2016-02-04 14:46:45.975581'),(3,'admin','0001_initial','2016-02-04 14:46:48.473012'),(4,'estadoderegistro','0001_initial','2016-02-04 14:46:50.886358'),(5,'direccion','0001_initial','2016-02-04 14:47:39.072245'),(6,'ambiente','0001_initial','2016-02-04 14:47:46.136836'),(7,'contenttypes','0002_remove_content_type_name','2016-02-04 14:47:48.400172'),(8,'auth','0002_alter_permission_name_max_length','2016-02-04 14:47:50.191163'),(9,'auth','0003_alter_user_email_max_length','2016-02-04 14:47:52.096935'),(10,'auth','0004_alter_user_username_opts','2016-02-04 14:47:52.267643'),(11,'auth','0005_alter_user_last_login_null','2016-02-04 14:47:52.997812'),(12,'auth','0006_require_contenttypes_0002','2016-02-04 14:47:53.085118'),(13,'cliente','0001_initial','2016-02-04 14:48:20.392057'),(14,'complejidadriesgo','0001_initial','2016-02-04 14:48:21.553523'),(15,'mueble','0001_initial','2016-02-04 14:48:30.368877'),(16,'contenedor','0001_initial','2016-02-04 14:48:33.539860'),(17,'gestiondedocumento','0001_initial','2016-02-04 14:48:36.550661'),(18,'mensaje','0001_initial','2016-02-04 14:48:39.558215'),(19,'menu','0001_initial','2016-02-04 14:48:43.720499'),(20,'premisas','0001_initial','2016-02-04 14:48:50.241878'),(21,'promocion','0001_initial','2016-02-04 14:49:14.142114'),(22,'sessions','0001_initial','2016-02-04 14:49:14.864986'),(23,'trabajador','0001_initial','2016-02-04 14:49:17.774861'),(24,'vehiculo','0001_initial','2016-02-04 14:49:29.300197');
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
INSERT INTO `django_session` VALUES ('5adjglk0uvfeoj4qxf79bkvnor1emyh5','MmU1NjZhNmM0YWY3MjZkNTJkNjI1MGFkYjBiMTZmNGRiM2UxMmE0Mzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZjRkYTI2ZDkxMTYzYjNkY2IyOTUwZDI2ZWMyZDM4MDIwNjJhZDU5YyIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-02-18 15:02:43.235676'),('mbobyp9renmnrbrq8ijs366pmawhqksg','MDQ0OGI3NDg4YzM3NWFjMjY0ZDE1ZmM0ZGE5NGRlMDRiNTE4ZGI5Mjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZjRkYTI2ZDkxMTYzYjNkY2IyOTUwZDI2ZWMyZDM4MDIwNjJhZDU5YyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2016-02-16 19:01:09.336565');
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estadoderegistro_estadoderegistro`
--

LOCK TABLES `estadoderegistro_estadoderegistro` WRITE;
/*!40000 ALTER TABLE `estadoderegistro_estadoderegistro` DISABLE KEYS */;
INSERT INTO `estadoderegistro_estadoderegistro` VALUES (1,'ambiente','Es el estado que asigna cuando se crea un ambiente nuevo','',1);
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestiondedocumento_estadodedocumento`
--

LOCK TABLES `gestiondedocumento_estadodedocumento` WRITE;
/*!40000 ALTER TABLE `gestiondedocumento_estadodedocumento` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestiondedocumento_tipodedocumento`
--

LOCK TABLES `gestiondedocumento_tipodedocumento` WRITE;
/*!40000 ALTER TABLE `gestiondedocumento_tipodedocumento` DISABLE KEYS */;
/*!40000 ALTER TABLE `gestiondedocumento_tipodedocumento` ENABLE KEYS */;
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
  `menu_padre_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `menu` (`menu`),
  KEY `menu_menu_menu_padre_id_60d51dd5_fk_menu_menu_id` (`menu_padre_id`),
  CONSTRAINT `menu_menu_menu_padre_id_60d51dd5_fk_menu_menu_id` FOREIGN KEY (`menu_padre_id`) REFERENCES `menu_menu` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu_menu`
--

LOCK TABLES `menu_menu` WRITE;
/*!40000 ALTER TABLE `menu_menu` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu_menufavorito`
--

LOCK TABLES `menu_menufavorito` WRITE;
/*!40000 ALTER TABLE `menu_menufavorito` DISABLE KEYS */;
/*!40000 ALTER TABLE `menu_menufavorito` ENABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mueble_especificaciondemueble`
--

LOCK TABLES `mueble_especificaciondemueble` WRITE;
/*!40000 ALTER TABLE `mueble_especificaciondemueble` DISABLE KEYS */;
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
  PRIMARY KEY (`id`),
  UNIQUE KEY `mueble` (`mueble`),
  KEY `mueble_mueble_fd00bd09` (`tipo_de_mueble_id`),
  CONSTRAINT `mueble_mueb_tipo_de_mueble_id_73a78552_fk_mueble_tipodemueble_id` FOREIGN KEY (`tipo_de_mueble_id`) REFERENCES `mueble_tipodemueble` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mueble_mueble`
--

LOCK TABLES `mueble_mueble` WRITE;
/*!40000 ALTER TABLE `mueble_mueble` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mueble_muebleporambiente`
--

LOCK TABLES `mueble_muebleporambiente` WRITE;
/*!40000 ALTER TABLE `mueble_muebleporambiente` DISABLE KEYS */;
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
INSERT INTO `premisas_personalizacionvisual` VALUES (1,'paginacion','10',1),(2,'paginacion','10',2),(3,'sidebarClosedOpen','1',2),(4,'rangopaginacion','3',2);
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `premisas_variantevisual`
--

LOCK TABLES `premisas_variantevisual` WRITE;
/*!40000 ALTER TABLE `premisas_variantevisual` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `premisas_variantevisualdetalle`
--

LOCK TABLES `premisas_variantevisualdetalle` WRITE;
/*!40000 ALTER TABLE `premisas_variantevisualdetalle` DISABLE KEYS */;
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
  `porcentaje_comision` decimal(5,2) NOT NULL,
  `observacion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `fecha_vigencia` date NOT NULL,
  `medio_especifico_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `promocion_alianza_32e34cc2` (`medio_especifico_id`),
  CONSTRAINT `pro_medio_especifico_id_3675f80b_fk_promocion_medioespecifico_id` FOREIGN KEY (`medio_especifico_id`) REFERENCES `promocion_medioespecifico` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promocion_alianza`
--

LOCK TABLES `promocion_alianza` WRITE;
/*!40000 ALTER TABLE `promocion_alianza` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promocion_alianzaestado`
--

LOCK TABLES `promocion_alianzaestado` WRITE;
/*!40000 ALTER TABLE `promocion_alianzaestado` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promocion_institucion`
--

LOCK TABLES `promocion_institucion` WRITE;
/*!40000 ALTER TABLE `promocion_institucion` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promocion_medio`
--

LOCK TABLES `promocion_medio` WRITE;
/*!40000 ALTER TABLE `promocion_medio` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promocion_medioespecifico`
--

LOCK TABLES `promocion_medioespecifico` WRITE;
/*!40000 ALTER TABLE `promocion_medioespecifico` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promocion_personaaliado`
--

LOCK TABLES `promocion_personaaliado` WRITE;
/*!40000 ALTER TABLE `promocion_personaaliado` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promocion_tipodereferido`
--

LOCK TABLES `promocion_tipodereferido` WRITE;
/*!40000 ALTER TABLE `promocion_tipodereferido` DISABLE KEYS */;
/*!40000 ALTER TABLE `promocion_tipodereferido` ENABLE KEYS */;
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
  `cargo_padre_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cargo_trabajador` (`cargo_trabajador`),
  KEY `trabaja_cargo_padre_id_1db19c0f_fk_trabajador_cargotrabajador_id` (`cargo_padre_id`),
  CONSTRAINT `trabaja_cargo_padre_id_1db19c0f_fk_trabajador_cargotrabajador_id` FOREIGN KEY (`cargo_padre_id`) REFERENCES `trabajador_cargotrabajador` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trabajador_cargotrabajador`
--

LOCK TABLES `trabajador_cargotrabajador` WRITE;
/*!40000 ALTER TABLE `trabajador_cargotrabajador` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trabajador_trabajador`
--

LOCK TABLES `trabajador_trabajador` WRITE;
/*!40000 ALTER TABLE `trabajador_trabajador` DISABLE KEYS */;
/*!40000 ALTER TABLE `trabajador_trabajador` ENABLE KEYS */;
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
  `tara_vehiculo` decimal(9,3) NOT NULL,
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
  `volumen_total_carga` decimal(9,3) NOT NULL,
  `peso_total_carga` decimal(9,3) NOT NULL,
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
-- Dumping events for database 'db_mtvmcotizacionv2'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-02-04 10:57:30
