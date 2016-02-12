-- Script was generated by Devart dbForge Studio for MySQL, Version 5.0.67.0
-- Product Home Page: http://www.devart.com/dbforge/mysql/studio
-- Script date 12-02-2016 09:22:28 a.m.
-- Source server version: 5.6.21
-- Source connection string: User Id=root;Host=localhost;Character Set=utf8;
-- Target server version: 5.6.21
-- Target connection string: User Id=root;Host=localhost;Character Set=utf8;
-- Run this script against db_mtvmcotizacionv2_prd to synchronize it with db_mtvmcotizacionv2
-- Please backup your target database before running this script

--
-- Disable foreign keys
--
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;

SET NAMES 'utf8';
USE db_mtvmcotizacionv2;

--
-- Alter table menu_menu
--
ALTER TABLE menu_menu
  DROP INDEX menu,
  CHANGE COLUMN menu menu VARCHAR(250) NOT NULL,
  CHANGE COLUMN transaccion transaccion VARCHAR(20) NOT NULL;

ALTER TABLE menu_menu
  ADD UNIQUE INDEX menu_menu_transaccion_517a1e01_uniq (transaccion);

ALTER TABLE menu_menu
  DROP FOREIGN KEY menu_menu_menu_padre_id_2e39653d_fk_menu_menu_id;
ALTER TABLE menu_menu
  ADD CONSTRAINT menu_menu_menu_padre_id_2e39653d_fk_menu_menu_id FOREIGN KEY (menu_padre_id)
    REFERENCES menu_menu(id) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Alter table trabajador_cargotrabajador
--
ALTER TABLE trabajador_cargotrabajador
  DROP FOREIGN KEY trabaja_cargo_padre_id_2378121d_fk_trabajador_cargotrabajador_id;
ALTER TABLE trabajador_cargotrabajador
  ADD CONSTRAINT trabaja_cargo_padre_id_2378121d_fk_trabajador_cargotrabajador_id FOREIGN KEY (cargo_padre_id)
    REFERENCES trabajador_cargotrabajador(id) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Create table menu_relacion
--
CREATE TABLE menu_relacion (
  id INT(11) NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(250) NOT NULL,
  item_origen_id INT(11) NOT NULL,
  item_relacion_id INT(11) NOT NULL,
  PRIMARY KEY (id),
  INDEX menu_relacion_26a7734e (item_origen_id),
  INDEX menu_relacion_5fe6c39a (item_relacion_id),
  CONSTRAINT menu_relacion_item_origen_id_70c122bb_fk_menu_menu_id FOREIGN KEY (item_origen_id)
    REFERENCES menu_menu(id) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT menu_relacion_item_relacion_id_2eeafeb1_fk_menu_menu_id FOREIGN KEY (item_relacion_id)
    REFERENCES menu_menu(id) ON DELETE RESTRICT ON UPDATE RESTRICT
)
ENGINE = INNODB
CHARACTER SET utf8
COLLATE utf8_unicode_ci;

--
-- Enable foreign keys
--
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
