CREATE DATABASE  IF NOT EXISTS `db_mtvmcotizacionv2` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci */;
USE `db_mtvmcotizacionv2`;
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
-- Dumping data for table `ambiente_ambiente`
--

LOCK TABLES `ambiente_ambiente` WRITE;
/*!40000 ALTER TABLE `ambiente_ambiente` DISABLE KEYS */;
/*!40000 ALTER TABLE `ambiente_ambiente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add Pais',7,'add_pais'),(20,'Can change Pais',7,'change_pais'),(21,'Can delete Pais',7,'delete_pais'),(22,'Can add Provincia',8,'add_provincia'),(23,'Can change Provincia',8,'change_provincia'),(24,'Can delete Provincia',8,'delete_provincia'),(25,'Can add Ciudad',9,'add_ciudad'),(26,'Can change Ciudad',9,'change_ciudad'),(27,'Can delete Ciudad',9,'delete_ciudad'),(28,'Can add Barrio',10,'add_barrio'),(29,'Can change Barrio',10,'change_barrio'),(30,'Can delete Barrio',10,'delete_barrio'),(31,'Can add Direccion',11,'add_direccion'),(32,'Can change Direccion',11,'change_direccion'),(33,'Can delete Direccion',11,'delete_direccion'),(34,'Can add Tipo de edificación',12,'add_tipodeedificacion'),(35,'Can change Tipo de edificación',12,'change_tipodeedificacion'),(36,'Can delete Tipo de edificación',12,'delete_tipodeedificacion'),(37,'Can add Tipo de edificación',13,'add_edificio'),(38,'Can change Tipo de edificación',13,'change_edificio'),(39,'Can delete Tipo de edificación',13,'delete_edificio'),(40,'Can add Tipo de ascensor',14,'add_tipodeascensor'),(41,'Can change Tipo de ascensor',14,'change_tipodeascensor'),(42,'Can delete Tipo de ascensor',14,'delete_tipodeascensor'),(43,'Can add Ascensor',15,'add_ascensor'),(44,'Can change Ascensor',15,'change_ascensor'),(45,'Can delete Ascensor',15,'delete_ascensor'),(46,'Can add Tipo de inmueble',16,'add_tipodeinmueble'),(47,'Can change Tipo de inmueble',16,'change_tipodeinmueble'),(48,'Can delete Tipo de inmueble',16,'delete_tipodeinmueble'),(49,'Can add Especificación de inmueble',17,'add_especificaciondeinmueble'),(50,'Can change Especificación de inmueble',17,'change_especificaciondeinmueble'),(51,'Can delete Especificación de inmueble',17,'delete_especificaciondeinmueble'),(52,'Can add Inmueble',18,'add_inmueble'),(53,'Can change Inmueble',18,'change_inmueble'),(54,'Can delete Inmueble',18,'delete_inmueble'),(55,'Can add Ambiente',19,'add_ambiente'),(56,'Can change Ambiente',19,'change_ambiente'),(57,'Can delete Ambiente',19,'delete_ambiente'),(58,'Can add Sexo',20,'add_sexo'),(59,'Can change Sexo',20,'change_sexo'),(60,'Can delete Sexo',20,'delete_sexo'),(61,'Can add Estado civil',21,'add_estadocivil'),(62,'Can change Estado civil',21,'change_estadocivil'),(63,'Can delete Estado civil',21,'delete_estadocivil'),(64,'Can add Tipo de cliente',22,'add_tipodecliente'),(65,'Can change Tipo de cliente',22,'change_tipodecliente'),(66,'Can delete Tipo de cliente',22,'delete_tipodecliente'),(67,'Can add Tipo de contacto',23,'add_tipodecontacto'),(68,'Can change Tipo de contacto',23,'change_tipodecontacto'),(69,'Can delete Tipo de contacto',23,'delete_tipodecontacto'),(70,'Can add Tipo de información de contacto',24,'add_tipodeinformaciondecontacto'),(71,'Can change Tipo de información de contacto',24,'change_tipodeinformaciondecontacto'),(72,'Can delete Tipo de información de contacto',24,'delete_tipodeinformaciondecontacto'),(73,'Can add Contenedor',25,'add_contenedor'),(74,'Can change Contenedor',25,'change_contenedor'),(75,'Can delete Contenedor',25,'delete_contenedor'),(76,'Can add Tipo de mueble',26,'add_tipodemueble'),(77,'Can change Tipo de mueble',26,'change_tipodemueble'),(78,'Can delete Tipo de mueble',26,'delete_tipodemueble'),(79,'Can add Tipo de documento',27,'add_tipodedocumento'),(80,'Can change Tipo de documento',27,'change_tipodedocumento'),(81,'Can delete Tipo de documento',27,'delete_tipodedocumento'),(82,'Can add Estado de documento',28,'add_estadodedocumento'),(83,'Can change Estado de documento',28,'change_estadodedocumento'),(84,'Can delete Estado de documento',28,'delete_estadodedocumento'),(85,'Can add Estado',29,'add_estado'),(86,'Can change Estado',29,'change_estado'),(87,'Can delete Estado',29,'delete_estado'),(88,'Can add Tipo de Registro',30,'add_tipoderegistro'),(89,'Can change Tipo de Registro',30,'change_tipoderegistro'),(90,'Can delete Tipo de Registro',30,'delete_tipoderegistro'),(91,'Can add Estado de registro',31,'add_estadoderegistro'),(92,'Can change Estado de registro',31,'change_estadoderegistro'),(93,'Can delete Estado de registro',31,'delete_estadoderegistro');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$20000$RlTIUgYCW3nq$YCWK5z9rBOvWDZ6POlu4DsaLHDgQbT43s61Cwni2c+s=',NULL,1,'admin','','','yusnelvy@gmail.com',1,1,'2016-01-21 20:34:04.469134');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `cliente_estadocivil`
--

LOCK TABLES `cliente_estadocivil` WRITE;
/*!40000 ALTER TABLE `cliente_estadocivil` DISABLE KEYS */;
/*!40000 ALTER TABLE `cliente_estadocivil` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `cliente_sexo`
--

LOCK TABLES `cliente_sexo` WRITE;
/*!40000 ALTER TABLE `cliente_sexo` DISABLE KEYS */;
/*!40000 ALTER TABLE `cliente_sexo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `cliente_tipodecliente`
--

LOCK TABLES `cliente_tipodecliente` WRITE;
/*!40000 ALTER TABLE `cliente_tipodecliente` DISABLE KEYS */;
/*!40000 ALTER TABLE `cliente_tipodecliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `cliente_tipodecontacto`
--

LOCK TABLES `cliente_tipodecontacto` WRITE;
/*!40000 ALTER TABLE `cliente_tipodecontacto` DISABLE KEYS */;
/*!40000 ALTER TABLE `cliente_tipodecontacto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `cliente_tipodeinformaciondecontacto`
--

LOCK TABLES `cliente_tipodeinformaciondecontacto` WRITE;
/*!40000 ALTER TABLE `cliente_tipodeinformaciondecontacto` DISABLE KEYS */;
/*!40000 ALTER TABLE `cliente_tipodeinformaciondecontacto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `contenedor_contenedor`
--

LOCK TABLES `contenedor_contenedor` WRITE;
/*!40000 ALTER TABLE `contenedor_contenedor` DISABLE KEYS */;
/*!40000 ALTER TABLE `contenedor_contenedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `direccion_ascensor`
--

LOCK TABLES `direccion_ascensor` WRITE;
/*!40000 ALTER TABLE `direccion_ascensor` DISABLE KEYS */;
/*!40000 ALTER TABLE `direccion_ascensor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `direccion_barrio`
--

LOCK TABLES `direccion_barrio` WRITE;
/*!40000 ALTER TABLE `direccion_barrio` DISABLE KEYS */;
/*!40000 ALTER TABLE `direccion_barrio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `direccion_ciudad`
--

LOCK TABLES `direccion_ciudad` WRITE;
/*!40000 ALTER TABLE `direccion_ciudad` DISABLE KEYS */;
/*!40000 ALTER TABLE `direccion_ciudad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `direccion_direccion`
--

LOCK TABLES `direccion_direccion` WRITE;
/*!40000 ALTER TABLE `direccion_direccion` DISABLE KEYS */;
/*!40000 ALTER TABLE `direccion_direccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `direccion_edificio`
--

LOCK TABLES `direccion_edificio` WRITE;
/*!40000 ALTER TABLE `direccion_edificio` DISABLE KEYS */;
/*!40000 ALTER TABLE `direccion_edificio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `direccion_especificaciondeinmueble`
--

LOCK TABLES `direccion_especificaciondeinmueble` WRITE;
/*!40000 ALTER TABLE `direccion_especificaciondeinmueble` DISABLE KEYS */;
/*!40000 ALTER TABLE `direccion_especificaciondeinmueble` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `direccion_inmueble`
--

LOCK TABLES `direccion_inmueble` WRITE;
/*!40000 ALTER TABLE `direccion_inmueble` DISABLE KEYS */;
/*!40000 ALTER TABLE `direccion_inmueble` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `direccion_pais`
--

LOCK TABLES `direccion_pais` WRITE;
/*!40000 ALTER TABLE `direccion_pais` DISABLE KEYS */;
/*!40000 ALTER TABLE `direccion_pais` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `direccion_provincia`
--

LOCK TABLES `direccion_provincia` WRITE;
/*!40000 ALTER TABLE `direccion_provincia` DISABLE KEYS */;
/*!40000 ALTER TABLE `direccion_provincia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `direccion_tipodeascensor`
--

LOCK TABLES `direccion_tipodeascensor` WRITE;
/*!40000 ALTER TABLE `direccion_tipodeascensor` DISABLE KEYS */;
/*!40000 ALTER TABLE `direccion_tipodeascensor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `direccion_tipodeedificacion`
--

LOCK TABLES `direccion_tipodeedificacion` WRITE;
/*!40000 ALTER TABLE `direccion_tipodeedificacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `direccion_tipodeedificacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `direccion_tipodeinmueble`
--

LOCK TABLES `direccion_tipodeinmueble` WRITE;
/*!40000 ALTER TABLE `direccion_tipodeinmueble` DISABLE KEYS */;
/*!40000 ALTER TABLE `direccion_tipodeinmueble` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(19,'ambiente','ambiente'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(21,'cliente','estadocivil'),(20,'cliente','sexo'),(22,'cliente','tipodecliente'),(23,'cliente','tipodecontacto'),(24,'cliente','tipodeinformaciondecontacto'),(25,'contenedor','contenedor'),(5,'contenttypes','contenttype'),(15,'direccion','ascensor'),(10,'direccion','barrio'),(9,'direccion','ciudad'),(11,'direccion','direccion'),(13,'direccion','edificio'),(17,'direccion','especificaciondeinmueble'),(18,'direccion','inmueble'),(7,'direccion','pais'),(8,'direccion','provincia'),(14,'direccion','tipodeascensor'),(12,'direccion','tipodeedificacion'),(16,'direccion','tipodeinmueble'),(29,'estadoderegistro','estado'),(31,'estadoderegistro','estadoderegistro'),(30,'estadoderegistro','tipoderegistro'),(28,'gestiondedocumento','estadodedocumento'),(27,'gestiondedocumento','tipodedocumento'),(26,'mueble','tipodemueble'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2016-01-21 20:33:21.358100'),(2,'auth','0001_initial','2016-01-21 20:33:30.328893'),(3,'admin','0001_initial','2016-01-21 20:33:33.506733'),(4,'contenttypes','0002_remove_content_type_name','2016-01-21 20:33:35.503942'),(5,'auth','0002_alter_permission_name_max_length','2016-01-21 20:33:36.617362'),(6,'auth','0003_alter_user_email_max_length','2016-01-21 20:33:37.636286'),(7,'auth','0004_alter_user_username_opts','2016-01-21 20:33:37.717138'),(8,'auth','0005_alter_user_last_login_null','2016-01-21 20:33:38.570587'),(9,'auth','0006_require_contenttypes_0002','2016-01-21 20:33:38.632874'),(10,'sessions','0001_initial','2016-01-21 20:33:39.235126'),(11,'ambiente','0001_initial','2016-01-21 20:34:23.897847'),(12,'cliente','0001_initial','2016-01-21 20:34:25.267342'),(13,'contenedor','0001_initial','2016-01-21 20:34:25.643186'),(14,'direccion','0001_initial','2016-01-21 20:35:02.000574'),(15,'estadoderegistro','0001_initial','2016-01-21 20:35:06.683676'),(16,'gestiondedocumento','0001_initial','2016-01-21 20:35:08.933791'),(17,'mueble','0001_initial','2016-01-21 20:35:09.477402');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `estadoderegistro_estado`
--

LOCK TABLES `estadoderegistro_estado` WRITE;
/*!40000 ALTER TABLE `estadoderegistro_estado` DISABLE KEYS */;
/*!40000 ALTER TABLE `estadoderegistro_estado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `estadoderegistro_estadoderegistro`
--

LOCK TABLES `estadoderegistro_estadoderegistro` WRITE;
/*!40000 ALTER TABLE `estadoderegistro_estadoderegistro` DISABLE KEYS */;
/*!40000 ALTER TABLE `estadoderegistro_estadoderegistro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `estadoderegistro_tipoderegistro`
--

LOCK TABLES `estadoderegistro_tipoderegistro` WRITE;
/*!40000 ALTER TABLE `estadoderegistro_tipoderegistro` DISABLE KEYS */;
/*!40000 ALTER TABLE `estadoderegistro_tipoderegistro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `gestiondedocumento_estadodedocumento`
--

LOCK TABLES `gestiondedocumento_estadodedocumento` WRITE;
/*!40000 ALTER TABLE `gestiondedocumento_estadodedocumento` DISABLE KEYS */;
/*!40000 ALTER TABLE `gestiondedocumento_estadodedocumento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `gestiondedocumento_tipodedocumento`
--

LOCK TABLES `gestiondedocumento_tipodedocumento` WRITE;
/*!40000 ALTER TABLE `gestiondedocumento_tipodedocumento` DISABLE KEYS */;
/*!40000 ALTER TABLE `gestiondedocumento_tipodedocumento` ENABLE KEYS */;
UNLOCK TABLES;

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

-- Dump completed on 2016-01-21 16:10:57
