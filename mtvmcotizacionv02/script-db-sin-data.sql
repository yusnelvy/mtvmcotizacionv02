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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  KEY `ambiente_ambientepo_ambiente_id_73ad5624_fk_ambiente_ambiente_id` (`ambiente_id`),
  KEY `c804ffca241dc6a8ea55ea4144c7a00c` (`especificacion_de_inmueble_id`),
  CONSTRAINT `ambiente_ambientepo_ambiente_id_73ad5624_fk_ambiente_ambiente_id` FOREIGN KEY (`ambiente_id`) REFERENCES `ambiente_ambiente` (`id`),
  CONSTRAINT `c804ffca241dc6a8ea55ea4144c7a00c` FOREIGN KEY (`especificacion_de_inmueble_id`) REFERENCES `direccion_especificaciondeinmueble` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=106 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  CONSTRAINT `mueble_especificaciondemu_mueble_id_771e6d97_fk_mueble_mueble_id` FOREIGN KEY (`mueble_id`) REFERENCES `mueble_mueble` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  KEY `mueble_mueb_tipo_de_mueble_id_7e72d3b4_fk_mueble_tipodemueble_id` (`tipo_de_mueble_id`),
  CONSTRAINT `mueble_mueb_tipo_de_mueble_id_7e72d3b4_fk_mueble_tipodemueble_id` FOREIGN KEY (`tipo_de_mueble_id`) REFERENCES `mueble_tipodemueble` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  KEY `D949a3fd63be7f5d7af8532da369314e` (`ambiente_por_tipo_de_inmueble_id`),
  KEY `b9f138942889768994a59045f2fadb23` (`especificacion_de_mueble_id`),
  CONSTRAINT `D949a3fd63be7f5d7af8532da369314e` FOREIGN KEY (`ambiente_por_tipo_de_inmueble_id`) REFERENCES `ambiente_ambienteportipodeinmueble` (`id`),
  CONSTRAINT `b9f138942889768994a59045f2fadb23` FOREIGN KEY (`especificacion_de_mueble_id`) REFERENCES `mueble_especificaciondemueble` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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

-- Dump completed on 2016-01-25 15:11:49
