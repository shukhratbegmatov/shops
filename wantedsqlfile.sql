-- MySQL dump 10.13  Distrib 8.0.39, for Linux (x86_64)
--
-- Host: localhost    Database: shop_museums
-- ------------------------------------------------------
-- Server version	8.0.39-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add Пользователь',6,'add_customuser'),(22,'Can change Пользователь',6,'change_customuser'),(23,'Can delete Пользователь',6,'delete_customuser'),(24,'Can view Пользователь',6,'view_customuser'),(25,'Can add Информация о проекте',7,'add_companyinfo'),(26,'Can change Информация о проекте',7,'change_companyinfo'),(27,'Can delete Информация о проекте',7,'delete_companyinfo'),(28,'Can view Информация о проекте',7,'view_companyinfo'),(29,'Can add Свяжитесь с нами',8,'add_contactus'),(30,'Can change Свяжитесь с нами',8,'change_contactus'),(31,'Can delete Свяжитесь с нами',8,'delete_contactus'),(32,'Can view Свяжитесь с нами',8,'view_contactus'),(33,'Can add Меню',9,'add_menu'),(34,'Can change Меню',9,'change_menu'),(35,'Can delete Меню',9,'delete_menu'),(36,'Can view Меню',9,'view_menu'),(37,'Can add Организация',10,'add_organization'),(38,'Can change Организация',10,'change_organization'),(39,'Can delete Организация',10,'delete_organization'),(40,'Can view Организация',10,'view_organization'),(41,'Can add Категория продуктов',11,'add_productcategory'),(42,'Can change Категория продуктов',11,'change_productcategory'),(43,'Can delete Категория продуктов',11,'delete_productcategory'),(44,'Can view Категория продуктов',11,'view_productcategory'),(45,'Can add Продукт',12,'add_product'),(46,'Can change Продукт',12,'change_product'),(47,'Can delete Продукт',12,'delete_product'),(48,'Can view Продукт',12,'view_product'),(49,'Can add Изображение продуктов',13,'add_productimage'),(50,'Can change Изображение продуктов',13,'change_productimage'),(51,'Can delete Изображение продуктов',13,'delete_productimage'),(52,'Can view Изображение продуктов',13,'view_productimage'),(53,'Can add blacklisted token',14,'add_blacklistedtoken'),(54,'Can change blacklisted token',14,'change_blacklistedtoken'),(55,'Can delete blacklisted token',14,'delete_blacklistedtoken'),(56,'Can view blacklisted token',14,'view_blacklistedtoken'),(57,'Can add outstanding token',15,'add_outstandingtoken'),(58,'Can change outstanding token',15,'change_outstandingtoken'),(59,'Can delete outstanding token',15,'delete_outstandingtoken'),(60,'Can view outstanding token',15,'view_outstandingtoken');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_info`
--

DROP TABLE IF EXISTS `company_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `company_info` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `logo_title` varchar(255) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `logo_title_uz` varchar(255) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `logo_title_ru` varchar(255) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `logo_title_en` varchar(255) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `logo` varchar(100) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `company_description` longtext COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `company_description_uz` longtext COLLATE utf8mb4_unicode_520_ci,
  `company_description_ru` longtext COLLATE utf8mb4_unicode_520_ci,
  `company_description_en` longtext COLLATE utf8mb4_unicode_520_ci,
  `updated_at` datetime(6) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_info`
--

LOCK TABLES `company_info` WRITE;
/*!40000 ALTER TABLE `company_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `company_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contact_us`
--

DROP TABLE IF EXISTS `contact_us`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contact_us` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `phone_number` varchar(50) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `instagram` varchar(200) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `facebook` varchar(200) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `telegram` varchar(200) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contact_us`
--

LOCK TABLES `contact_us` WRITE;
/*!40000 ALTER TABLE `contact_us` DISABLE KEYS */;
/*!40000 ALTER TABLE `contact_us` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `custom_user`
--

DROP TABLE IF EXISTS `custom_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `custom_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `profile_image` varchar(100) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `role` int NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `phone_number` varchar(128) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `organization_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone_number` (`phone_number`),
  KEY `custom_user_organization_id_4a0548db_fk_organization_id` (`organization_id`),
  CONSTRAINT `custom_user_organization_id_4a0548db_fk_organization_id` FOREIGN KEY (`organization_id`) REFERENCES `organization` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `custom_user`
--

LOCK TABLES `custom_user` WRITE;
/*!40000 ALTER TABLE `custom_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `custom_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `custom_user_groups`
--

DROP TABLE IF EXISTS `custom_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `custom_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `custom_user_groups_customuser_id_group_id_ea14f886_uniq` (`customuser_id`,`group_id`),
  KEY `custom_user_groups_group_id_02874f21_fk_auth_group_id` (`group_id`),
  CONSTRAINT `custom_user_groups_customuser_id_8e3d0338_fk_custom_user_id` FOREIGN KEY (`customuser_id`) REFERENCES `custom_user` (`id`),
  CONSTRAINT `custom_user_groups_group_id_02874f21_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `custom_user_groups`
--

LOCK TABLES `custom_user_groups` WRITE;
/*!40000 ALTER TABLE `custom_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `custom_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `custom_user_user_permissions`
--

DROP TABLE IF EXISTS `custom_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `custom_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `custom_user_user_permiss_customuser_id_permission_f9232336_uniq` (`customuser_id`,`permission_id`),
  KEY `custom_user_user_per_permission_id_f82b5e3f_fk_auth_perm` (`permission_id`),
  CONSTRAINT `custom_user_user_per_customuser_id_ec2da4cb_fk_custom_us` FOREIGN KEY (`customuser_id`) REFERENCES `custom_user` (`id`),
  CONSTRAINT `custom_user_user_per_permission_id_f82b5e3f_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `custom_user_user_permissions`
--

LOCK TABLES `custom_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `custom_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `custom_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_520_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_custom_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_custom_user_id` FOREIGN KEY (`user_id`) REFERENCES `custom_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (6,'account','customuser'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(5,'sessions','session'),(12,'shop','product'),(11,'shop','productcategory'),(13,'shop','productimage'),(7,'system_settings','companyinfo'),(8,'system_settings','contactus'),(9,'system_settings','menu'),(10,'system_settings','organization'),(14,'token_blacklist','blacklistedtoken'),(15,'token_blacklist','outstandingtoken');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'system_settings','0001_initial','2023-10-28 08:52:12.508400'),(2,'contenttypes','0001_initial','2023-10-28 08:52:12.538915'),(3,'contenttypes','0002_remove_content_type_name','2023-10-28 08:52:12.593318'),(4,'auth','0001_initial','2023-10-28 08:52:12.715497'),(5,'auth','0002_alter_permission_name_max_length','2023-10-28 08:52:12.757811'),(6,'auth','0003_alter_user_email_max_length','2023-10-28 08:52:12.768057'),(7,'auth','0004_alter_user_username_opts','2023-10-28 08:52:12.775838'),(8,'auth','0005_alter_user_last_login_null','2023-10-28 08:52:12.782453'),(9,'auth','0006_require_contenttypes_0002','2023-10-28 08:52:12.785927'),(10,'auth','0007_alter_validators_add_error_messages','2023-10-28 08:52:12.791284'),(11,'auth','0008_alter_user_username_max_length','2023-10-28 08:52:12.797872'),(12,'auth','0009_alter_user_last_name_max_length','2023-10-28 08:52:12.803102'),(13,'auth','0010_alter_group_name_max_length','2023-10-28 08:52:12.818557'),(14,'auth','0011_update_proxy_permissions','2023-10-28 08:52:12.858521'),(15,'auth','0012_alter_user_first_name_max_length','2023-10-28 08:52:12.866068'),(16,'account','0001_initial','2023-10-28 08:52:13.050229'),(17,'account','0002_alter_customuser_role','2023-10-28 08:52:13.065625'),(18,'admin','0001_initial','2023-10-28 08:52:13.146884'),(19,'admin','0002_logentry_remove_auto_add','2023-10-28 08:52:13.161991'),(20,'admin','0003_logentry_add_action_flag_choices','2023-10-28 08:52:13.169911'),(21,'sessions','0001_initial','2023-10-28 08:52:13.194320'),(22,'system_settings','0002_organization_logo_organization_subdomain_field','2023-10-28 08:52:13.252482'),(23,'shop','0001_initial','2023-10-28 08:52:13.307813'),(24,'shop','0002_productcategory_title_en_productcategory_title_ru_and_more','2023-10-28 08:52:13.351357'),(25,'shop','0003_product_productimage','2023-10-28 08:52:13.444778'),(26,'shop','0004_product_organization','2023-10-28 08:52:13.511335'),(27,'system_settings','0003_menu_is_main','2023-10-28 08:52:13.529600'),(28,'token_blacklist','0001_initial','2023-10-28 08:52:13.644155'),(29,'token_blacklist','0002_outstandingtoken_jti_hex','2023-10-28 08:52:13.672366'),(30,'token_blacklist','0003_auto_20171017_2007','2023-10-28 08:52:13.689630'),(31,'token_blacklist','0004_auto_20171017_2013','2023-10-28 08:52:13.736165'),(32,'token_blacklist','0005_remove_outstandingtoken_jti','2023-10-28 08:52:13.772487'),(33,'token_blacklist','0006_auto_20171017_2113','2023-10-28 08:52:13.793921'),(34,'token_blacklist','0007_auto_20171017_2214','2023-10-28 08:52:13.913022'),(35,'token_blacklist','0008_migrate_to_bigautofield','2023-10-28 08:52:14.052404'),(36,'token_blacklist','0010_fix_migrate_to_bigautofield','2023-10-28 08:52:14.077638'),(37,'token_blacklist','0011_linearizes_history','2023-10-28 08:52:14.083331'),(38,'token_blacklist','0012_alter_outstandingtoken_user','2023-10-28 08:52:14.112336');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu`
--

DROP TABLE IF EXISTS `menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menu` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `title_uz` varchar(255) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `title_ru` varchar(255) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `title_en` varchar(255) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `url` varchar(500) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `order` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `is_main` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu`
--

LOCK TABLES `menu` WRITE;
/*!40000 ALTER TABLE `menu` DISABLE KEYS */;
/*!40000 ALTER TABLE `menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `organization`
--

DROP TABLE IF EXISTS `organization`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `organization` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `title_uz` varchar(255) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `title_ru` varchar(255) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `title_en` varchar(255) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `file` varchar(100) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `logo` varchar(100) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `subdomain_field` varchar(200) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `organization_subdomain_field_edcd37bc` (`subdomain_field`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `organization`
--

LOCK TABLES `organization` WRITE;
/*!40000 ALTER TABLE `organization` DISABLE KEYS */;
/*!40000 ALTER TABLE `organization` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `title_uz` varchar(255) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `title_ru` varchar(255) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `title_en` varchar(255) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `description` longtext COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `description_uz` longtext COLLATE utf8mb4_unicode_520_ci,
  `description_ru` longtext COLLATE utf8mb4_unicode_520_ci,
  `description_en` longtext COLLATE utf8mb4_unicode_520_ci,
  `is_recommended` tinyint(1) NOT NULL,
  `main_image` varchar(100) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `price` double NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `category_id` bigint NOT NULL,
  `organization_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `product_category_id_640030a0_fk_product_category_id` (`category_id`),
  KEY `product_organization_id_7b6d37dd_fk_organization_id` (`organization_id`),
  CONSTRAINT `product_category_id_640030a0_fk_product_category_id` FOREIGN KEY (`category_id`) REFERENCES `product_category` (`id`),
  CONSTRAINT `product_organization_id_7b6d37dd_fk_organization_id` FOREIGN KEY (`organization_id`) REFERENCES `organization` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_category`
--

DROP TABLE IF EXISTS `product_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `is_main` tinyint(1) NOT NULL,
  `image` varchar(100) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `organization_id` bigint NOT NULL,
  `title_en` varchar(255) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `title_ru` varchar(255) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  `title_uz` varchar(255) COLLATE utf8mb4_unicode_520_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `product_category_organization_id_68b4eca7_fk_organization_id` (`organization_id`),
  CONSTRAINT `product_category_organization_id_68b4eca7_fk_organization_id` FOREIGN KEY (`organization_id`) REFERENCES `organization` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_category`
--

LOCK TABLES `product_category` WRITE;
/*!40000 ALTER TABLE `product_category` DISABLE KEYS */;
/*!40000 ALTER TABLE `product_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_image`
--

DROP TABLE IF EXISTS `products_image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products_image` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `image` varchar(100) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `product_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `products_image_product_id_978188e9_fk_product_id` (`product_id`),
  CONSTRAINT `products_image_product_id_978188e9_fk_product_id` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_image`
--

LOCK TABLES `products_image` WRITE;
/*!40000 ALTER TABLE `products_image` DISABLE KEYS */;
/*!40000 ALTER TABLE `products_image` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `token_blacklist_blacklistedtoken`
--

DROP TABLE IF EXISTS `token_blacklist_blacklistedtoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `token_blacklist_blacklistedtoken` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `blacklisted_at` datetime(6) NOT NULL,
  `token_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token_id` (`token_id`),
  CONSTRAINT `token_blacklist_blacklistedtoken_token_id_3cc7fe56_fk` FOREIGN KEY (`token_id`) REFERENCES `token_blacklist_outstandingtoken` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `token_blacklist_blacklistedtoken`
--

LOCK TABLES `token_blacklist_blacklistedtoken` WRITE;
/*!40000 ALTER TABLE `token_blacklist_blacklistedtoken` DISABLE KEYS */;
/*!40000 ALTER TABLE `token_blacklist_blacklistedtoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `token_blacklist_outstandingtoken`
--

DROP TABLE IF EXISTS `token_blacklist_outstandingtoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `token_blacklist_outstandingtoken` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `token` longtext COLLATE utf8mb4_unicode_520_ci NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `expires_at` datetime(6) NOT NULL,
  `user_id` bigint DEFAULT NULL,
  `jti` varchar(255) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token_blacklist_outstandingtoken_jti_hex_d9bdf6f7_uniq` (`jti`),
  KEY `token_blacklist_outs_user_id_83bc629a_fk_custom_us` (`user_id`),
  CONSTRAINT `token_blacklist_outs_user_id_83bc629a_fk_custom_us` FOREIGN KEY (`user_id`) REFERENCES `custom_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `token_blacklist_outstandingtoken`
--

LOCK TABLES `token_blacklist_outstandingtoken` WRITE;
/*!40000 ALTER TABLE `token_blacklist_outstandingtoken` DISABLE KEYS */;
/*!40000 ALTER TABLE `token_blacklist_outstandingtoken` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-05 18:15:17
