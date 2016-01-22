-- MySQL dump 10.13  Distrib 5.6.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: db_mtvmcotizacionv2
-- ------------------------------------------------------
-- Server version   5.6.21-log

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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ambiente_ambiente`
--

LOCK TABLES `ambiente_ambiente` WRITE;
/*!40000 ALTER TABLE `ambiente_ambiente` DISABLE KEYS */;
/*!40000 ALTER TABLE `ambiente_ambiente` ENABLE KEYS */;
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
  KEY `auth_group_permissi_permission_id_66d15eb6_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_66d15eb6_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_76c2798f_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
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
  CONSTRAINT `auth_permissi_content_type_id_76c32374_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=94 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add Pais',7,'add_pais'),(20,'Can change Pais',7,'change_pais'),(21,'Can delete Pais',7,'delete_pais'),(22,'Can add Provincia',8,'add_provincia'),(23,'Can change Provincia',8,'change_provincia'),(24,'Can delete Provincia',8,'delete_provincia'),(25,'Can add Ciudad',9,'add_ciudad'),(26,'Can change Ciudad',9,'change_ciudad'),(27,'Can delete Ciudad',9,'delete_ciudad'),(28,'Can add Barrio',10,'add_barrio'),(29,'Can change Barrio',10,'change_barrio'),(30,'Can delete Barrio',10,'delete_barrio'),(31,'Can add Direccion',11,'add_direccion'),(32,'Can change Direccion',11,'change_direccion'),(33,'Can delete Direccion',11,'delete_direccion'),(34,'Can add Tipo de edificación',12,'add_tipodeedificacion'),(35,'Can change Tipo de edificación',12,'change_tipodeedificacion'),(36,'Can delete Tipo de edificación',12,'delete_tipodeedificacion'),(37,'Can add Tipo de edificación',13,'add_edificio'),(38,'Can change Tipo de edificación',13,'change_edificio'),(39,'Can delete Tipo de edificación',13,'delete_edificio'),(40,'Can add Tipo de ascensor',14,'add_tipodeascensor'),(41,'Can change Tipo de ascensor',14,'change_tipodeascensor'),(42,'Can delete Tipo de ascensor',14,'delete_tipodeascensor'),(43,'Can add Ascensor',15,'add_ascensor'),(44,'Can change Ascensor',15,'change_ascensor'),(45,'Can delete Ascensor',15,'delete_ascensor'),(46,'Can add Tipo de inmueble',16,'add_tipodeinmueble'),(47,'Can change Tipo de inmueble',16,'change_tipodeinmueble'),(48,'Can delete Tipo de inmueble',16,'delete_tipodeinmueble'),(49,'Can add Especificación de inmueble',17,'add_especificaciondeinmueble'),(50,'Can change Especificación de inmueble',17,'change_especificaciondeinmueble'),(51,'Can delete Especificación de inmueble',17,'delete_especificaciondeinmueble'),(52,'Can add Inmueble',18,'add_inmueble'),(53,'Can change Inmueble',18,'change_inmueble'),(54,'Can delete Inmueble',18,'delete_inmueble'),(55,'Can add Ambiente',19,'add_ambiente'),(56,'Can change Ambiente',19,'change_ambiente'),(57,'Can delete Ambiente',19,'delete_ambiente'),(58,'Can add Sexo',20,'add_sexo'),(59,'Can change Sexo',20,'change_sexo'),(60,'Can delete Sexo',20,'delete_sexo'),(61,'Can add Estado civil',21,'add_estadocivil'),(62,'Can change Estado civil',21,'change_estadocivil'),(63,'Can delete Estado civil',21,'delete_estadocivil'),(64,'Can add Tipo de cliente',22,'add_tipodecliente'),(65,'Can change Tipo de cliente',22,'change_tipodecliente'),(66,'Can delete Tipo de cliente',22,'delete_tipodecliente'),(67,'Can add Tipo de contacto',23,'add_tipodecontacto'),(68,'Can change Tipo de contacto',23,'change_tipodecontacto'),(69,'Can delete Tipo de contacto',23,'delete_tipodecontacto'),(70,'Can add Tipo de información de contacto',24,'add_tipodeinformaciondecontacto'),(71,'Can change Tipo de información de contacto',24,'change_tipodeinformaciondecontacto'),(72,'Can delete Tipo de información de contacto',24,'delete_tipodeinformaciondecontacto'),(73,'Can add Contenedor',25,'add_contenedor'),(74,'Can change Contenedor',25,'change_contenedor'),(75,'Can delete Contenedor',25,'delete_contenedor'),(76,'Can add Tipo de mueble',26,'add_tipodemueble'),(77,'Can change Tipo de mueble',26,'change_tipodemueble'),(78,'Can delete Tipo de mueble',26,'delete_tipodemueble'),(79,'Can add Tipo de documento',27,'add_tipodedocumento'),(80,'Can change Tipo de documento',27,'change_tipodedocumento'),(81,'Can delete Tipo de documento',27,'delete_tipodedocumento'),(82,'Can add Estado de documento',28,'add_estadodedocumento'),(83,'Can change Estado de documento',28,'change_estadodedocumento'),(84,'Can delete Estado de documento',28,'delete_estadodedocumento'),(85,'Can add Estado',29,'add_estado'),(86,'Can change Estado',29,'change_estado'),(87,'Can delete Estado',29,'delete_estado'),(88,'Can add Tipo de Registro',30,'add_tipoderegistro'),(89,'Can change Tipo de Registro',30,'change_tipoderegistro'),(90,'Can delete Tipo de Registro',30,'delete_tipoderegistro'),(91,'Can add Estado de registro',31,'add_estadoderegistro'),(92,'Can change Estado de registro',31,'change_estadoderegistro'),(93,'Can delete Estado de registro',31,'delete_estadoderegistro');
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$20000$BNYRtK9HrFRA$rLwocCQ1n/FhAXXl60euvoNdbub6nBmzgiWum4sRIa0=',NULL,1,'admin','','','yusnelvy@gmail.com',1,1,'2016-01-22 13:43:06.556419');
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
  KEY `auth_user_groups_group_id_2e67f35b_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_2e67f35b_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_11a89054_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
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
  KEY `auth_user_user_perm_permission_id_2a84541f_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_perm_permission_id_2a84541f_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_184b152b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
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
  PRIMARY KEY (`id`)
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
-- Table structure for table `cliente_tipodecontacto`
--

DROP TABLE IF EXISTS `cliente_tipodecontacto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cliente_tipodecontacto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_de_contacto` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente_tipodecontacto`
--

LOCK TABLES `cliente_tipodecontacto` WRITE;
/*!40000 ALTER TABLE `cliente_tipodecontacto` DISABLE KEYS */;
/*!40000 ALTER TABLE `cliente_tipodecontacto` ENABLE KEYS */;
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
  PRIMARY KEY (`id`)
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
  PRIMARY KEY (`id`)
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
  `edificio_id` int(11) NOT NULL,
  `tipo_de_ascensor_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `direccion_ascensor_8a1efaf1` (`edificio_id`),
  KEY `direccion_ascensor_2af49ef9` (`tipo_de_ascensor_id`),
  CONSTRAINT `dire_tipo_de_ascensor_id_49dac27e_fk_direccion_tipodeascensor_id` FOREIGN KEY (`tipo_de_ascensor_id`) REFERENCES `direccion_tipodeascensor` (`id`),
  CONSTRAINT `direccion_ascensor_edificio_id_54bb93bd_fk_direccion_edificio_id` FOREIGN KEY (`edificio_id`) REFERENCES `direccion_edificio` (`id`)
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
  UNIQUE KEY `direccion_barrio_barrio_7705804e_uniq` (`barrio`,`ciudad_id`),
  KEY `direccion_barrio_0201ed81` (`ciudad_id`),
  KEY `direccion_barrio_847ec16e` (`pais_id`),
  KEY `direccion_barrio_54bf7e76` (`provincia_id`),
  CONSTRAINT `direccion_barrio_ciudad_id_5740c46a_fk_direccion_ciudad_id` FOREIGN KEY (`ciudad_id`) REFERENCES `direccion_ciudad` (`id`),
  CONSTRAINT `direccion_barrio_pais_id_30aa6f8e_fk_direccion_pais_id` FOREIGN KEY (`pais_id`) REFERENCES `direccion_pais` (`id`),
  CONSTRAINT `direccion_barrio_provincia_id_385c7858_fk_direccion_provincia_id` FOREIGN KEY (`provincia_id`) REFERENCES `direccion_provincia` (`id`)
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
  UNIQUE KEY `direccion_ciudad_ciudad_63311a1a_uniq` (`ciudad`,`provincia_id`),
  KEY `direccion_ciudad_847ec16e` (`pais_id`),
  KEY `direccion_ciudad_54bf7e76` (`provincia_id`),
  CONSTRAINT `direccion_ciudad_pais_id_15e58ffe_fk_direccion_pais_id` FOREIGN KEY (`pais_id`) REFERENCES `direccion_pais` (`id`),
  CONSTRAINT `direccion_ciudad_provincia_id_20cc84cc_fk_direccion_provincia_id` FOREIGN KEY (`provincia_id`) REFERENCES `direccion_provincia` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccion_ciudad`
--

LOCK TABLES `direccion_ciudad` WRITE;
/*!40000 ALTER TABLE `direccion_ciudad` DISABLE KEYS */;
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
  `punto_referencia` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `adicional` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `barrio_id` int(11) NOT NULL,
  `ciudad_id` int(11) NOT NULL,
  `pais_id` int(11) NOT NULL,
  `provincia_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `direccion_direccion_d2d7294b` (`barrio_id`),
  KEY `direccion_direccion_0201ed81` (`ciudad_id`),
  KEY `direccion_direccion_847ec16e` (`pais_id`),
  KEY `direccion_direccion_54bf7e76` (`provincia_id`),
  CONSTRAINT `direccion_direcc_provincia_id_4ae4e479_fk_direccion_provincia_id` FOREIGN KEY (`provincia_id`) REFERENCES `direccion_provincia` (`id`),
  CONSTRAINT `direccion_direccion_barrio_id_79c54395_fk_direccion_barrio_id` FOREIGN KEY (`barrio_id`) REFERENCES `direccion_barrio` (`id`),
  CONSTRAINT `direccion_direccion_ciudad_id_4056b739_fk_direccion_ciudad_id` FOREIGN KEY (`ciudad_id`) REFERENCES `direccion_ciudad` (`id`),
  CONSTRAINT `direccion_direccion_pais_id_64048f03_fk_direccion_pais_id` FOREIGN KEY (`pais_id`) REFERENCES `direccion_pais` (`id`)
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
-- Table structure for table `direccion_edificio`
--

DROP TABLE IF EXISTS `direccion_edificio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `direccion_edificio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_de_edificio` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `cantidad_de_pisos` int(11) NOT NULL,
  `cantidad_de_inmuebles_por_piso` int(11) NOT NULL,
  `total_inmuebles` int(11) NOT NULL,
  `rampa` tinyint(1) NOT NULL,
  `distancia_del_vehiculo` int(11) NOT NULL,
  `escalera_estrecha` tinyint(1) NOT NULL,
  `escalera_inclinada` tinyint(1) NOT NULL,
  `escalon_grande` tinyint(1) NOT NULL,
  `tipo_de_edificacion_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `direccion_edificio_ac1f730e` (`tipo_de_edificacion_id`),
  CONSTRAINT `c08ca9b169877709e9acf6c5b52d0c1e` FOREIGN KEY (`tipo_de_edificacion_id`) REFERENCES `direccion_tipodeedificacion` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccion_edificio`
--

LOCK TABLES `direccion_edificio` WRITE;
/*!40000 ALTER TABLE `direccion_edificio` DISABLE KEYS */;
/*!40000 ALTER TABLE `direccion_edificio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `direccion_especificaciondeinmueble`
--

DROP TABLE IF EXISTS `direccion_especificaciondeinmueble`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `direccion_especificaciondeinmueble` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `especificacion_de_inmueble` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `tipo_de_inmueble_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `direccion_especificaciondeinmueble_e1ed7001` (`tipo_de_inmueble_id`),
  CONSTRAINT `dire_tipo_de_inmueble_id_43b75e84_fk_direccion_tipodeinmueble_id` FOREIGN KEY (`tipo_de_inmueble_id`) REFERENCES `direccion_tipodeinmueble` (`id`)
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
-- Table structure for table `direccion_inmueble`
--

DROP TABLE IF EXISTS `direccion_inmueble`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `direccion_inmueble` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `numero_de_inmueble` int(11) NOT NULL,
  `numero_de_pisos` int(11) NOT NULL,
  `nombre_del_piso` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `cantidad_de_ambientes` int(11) NOT NULL,
  `pisos_por_escalera` int(11) NOT NULL,
  `numero_de_plantas` int(11) NOT NULL,
  `total_m2` decimal(7,2) NOT NULL,
  `baulera` tinyint(1) NOT NULL,
  `volumen_baulera` decimal(8,3) NOT NULL,
  `edificio_id` int(11) NOT NULL,
  `especificacion_de_inmueble_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `direccion_inmueble_edificio_id_5817320d_fk_direccion_edificio_id` (`edificio_id`),
  KEY `ab391cd9376409bfe1c0ed2ff1c8f6c8` (`especificacion_de_inmueble_id`),
  CONSTRAINT `ab391cd9376409bfe1c0ed2ff1c8f6c8` FOREIGN KEY (`especificacion_de_inmueble_id`) REFERENCES `direccion_especificaciondeinmueble` (`id`),
  CONSTRAINT `direccion_inmueble_edificio_id_5817320d_fk_direccion_edificio_id` FOREIGN KEY (`edificio_id`) REFERENCES `direccion_edificio` (`id`)
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
  `pais` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `pais` (`pais`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccion_pais`
--

LOCK TABLES `direccion_pais` WRITE;
/*!40000 ALTER TABLE `direccion_pais` DISABLE KEYS */;
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
  `pais_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `direccion_provincia_provincia_6124bde5_uniq` (`provincia`,`pais_id`),
  KEY `direccion_provincia_pais_id_3792779d_fk_direccion_pais_id` (`pais_id`),
  CONSTRAINT `direccion_provincia_pais_id_3792779d_fk_direccion_pais_id` FOREIGN KEY (`pais_id`) REFERENCES `direccion_pais` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direccion_provincia`
--

LOCK TABLES `direccion_provincia` WRITE;
/*!40000 ALTER TABLE `direccion_provincia` DISABLE KEYS */;
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
  KEY `django_admin__content_type_id_67f62513_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_13503fd2_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_67f62513_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_13503fd2_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
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
  UNIQUE KEY `django_content_type_app_label_e9877d0_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(19,'ambiente','ambiente'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(21,'cliente','estadocivil'),(20,'cliente','sexo'),(22,'cliente','tipodecliente'),(23,'cliente','tipodecontacto'),(24,'cliente','tipodeinformaciondecontacto'),(25,'contenedor','contenedor'),(5,'contenttypes','contenttype'),(15,'direccion','ascensor'),(10,'direccion','barrio'),(9,'direccion','ciudad'),(11,'direccion','direccion'),(13,'direccion','edificio'),(17,'direccion','especificaciondeinmueble'),(18,'direccion','inmueble'),(7,'direccion','pais'),(8,'direccion','provincia'),(14,'direccion','tipodeascensor'),(12,'direccion','tipodeedificacion'),(16,'direccion','tipodeinmueble'),(29,'estadoderegistro','estado'),(31,'estadoderegistro','estadoderegistro'),(30,'estadoderegistro','tipoderegistro'),(28,'gestiondedocumento','estadodedocumento'),(27,'gestiondedocumento','tipodedocumento'),(26,'mueble','tipodemueble'),(6,'sessions','session');
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
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2016-01-22 13:42:03.094685'),(2,'auth','0001_initial','2016-01-22 13:42:12.457234'),(3,'admin','0001_initial','2016-01-22 13:42:14.085434'),(4,'contenttypes','0002_remove_content_type_name','2016-01-22 13:42:15.375760'),(5,'auth','0002_alter_permission_name_max_length','2016-01-22 13:42:16.698474'),(6,'auth','0003_alter_user_email_max_length','2016-01-22 13:42:17.723237'),(7,'auth','0004_alter_user_username_opts','2016-01-22 13:42:17.832459'),(8,'auth','0005_alter_user_last_login_null','2016-01-22 13:42:18.552446'),(9,'auth','0006_require_contenttypes_0002','2016-01-22 13:42:18.618842'),(10,'sessions','0001_initial','2016-01-22 13:42:20.154448'),(11,'ambiente','0001_initial','2016-01-22 13:44:24.291778'),(12,'cliente','0001_initial','2016-01-22 13:44:25.660492'),(13,'contenedor','0001_initial','2016-01-22 13:44:26.008239'),(14,'direccion','0001_initial','2016-01-22 13:44:59.679130'),(15,'estadoderegistro','0001_initial','2016-01-22 13:45:04.144673'),(16,'gestiondedocumento','0001_initial','2016-01-22 13:45:07.476318'),(17,'mueble','0001_initial','2016-01-22 13:45:08.084226');
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estadoderegistro_estado`
--

LOCK TABLES `estadoderegistro_estado` WRITE;
/*!40000 ALTER TABLE `estadoderegistro_estado` DISABLE KEYS */;
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
  `orden` int(11) NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `observacion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `estado_id` int(11) NOT NULL,
  `tipo_de_registro_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `estadoderegistr_estado_id_6705e1f4_fk_estadoderegistro_estado_id` (`estado_id`),
  KEY `estadoderegistro_estadoderegistro_b214a833` (`tipo_de_registro_id`),
  CONSTRAINT `D1573d6306f3b45cc4e102fbc2a5dd6f` FOREIGN KEY (`tipo_de_registro_id`) REFERENCES `estadoderegistro_tipoderegistro` (`id`),
  CONSTRAINT `estadoderegistr_estado_id_6705e1f4_fk_estadoderegistro_estado_id` FOREIGN KEY (`estado_id`) REFERENCES `estadoderegistro_estado` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estadoderegistro_estadoderegistro`
--

LOCK TABLES `estadoderegistro_estadoderegistro` WRITE;
/*!40000 ALTER TABLE `estadoderegistro_estadoderegistro` DISABLE KEYS */;
/*!40000 ALTER TABLE `estadoderegistro_estadoderegistro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estadoderegistro_tipoderegistro`
--

DROP TABLE IF EXISTS `estadoderegistro_tipoderegistro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `estadoderegistro_tipoderegistro` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_de_registro` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tipo_de_registro` (`tipo_de_registro`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estadoderegistro_tipoderegistro`
--

LOCK TABLES `estadoderegistro_tipoderegistro` WRITE;
/*!40000 ALTER TABLE `estadoderegistro_tipoderegistro` DISABLE KEYS */;
/*!40000 ALTER TABLE `estadoderegistro_tipoderegistro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gestiondedocumento_estadodedocumento`
--

DROP TABLE IF EXISTS `gestiondedocumento_estadodedocumento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gestiondedocumento_estadodedocumento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `orden` int(11) NOT NULL,
  `estado_de_documento` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `observacion` longtext COLLATE utf8_unicode_ci NOT NULL,
  `tipo_de_documento_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `gestiondedocumento_estadodedocumento_ced3756a` (`tipo_de_documento_id`),
  CONSTRAINT `D117740eec0c29a7de2fb03ee00fe355` FOREIGN KEY (`tipo_de_documento_id`) REFERENCES `gestiondedocumento_tipodedocumento` (`id`)
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mueble_tipodemueble`
--

LOCK TABLES `mueble_tipodemueble` WRITE;
/*!40000 ALTER TABLE `mueble_tipodemueble` DISABLE KEYS */;
/*!40000 ALTER TABLE `mueble_tipodemueble` ENABLE KEYS */;
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

-- Dump completed on 2016-01-22  9:16:38
