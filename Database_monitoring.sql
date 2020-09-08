/*
 Navicat Premium Data Transfer

 Source Server         : 192.168.4.89
 Source Server Type    : PostgreSQL
 Source Server Version : 90224
 Source Host           : 192.168.4.89:5432
 Source Catalog        : postgres
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 90224
 File Encoding         : 65001

 Date: 14/08/2020 09:40:12
*/


-- ----------------------------
-- Table structure for Database_monitoring
-- ----------------------------
DROP TABLE IF EXISTS "public"."Database_monitoring";
CREATE TABLE "public"."Database_monitoring" (
  "sysID" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "sysName" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "reportTime" date DEFAULT NULL,
  "dBList" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "dBName" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "dBMSName" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "dBVer" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "dBObj" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "dBConn" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "dBCreateTime" text COLLATE "pg_catalog"."default" DEFAULT NULL,
  "dBMacName" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "dBStartTime" date DEFAULT NULL,
  "dBAllUser" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "userCreateTime" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "userExpirdTime" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "cpuMaxExe" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "cpuMaxMacName" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "cpuRatePerT" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "cpuRate" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "curUserConnects" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "permitMaxConnects" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "totalConnects" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "parConnects" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "activeConnects" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "dBSpace" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "dBLoadMem" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "id" int4 NOT NULL DEFAULT NULL
)
;

-- ----------------------------
-- Primary Key structure for table Database_monitoring
-- ----------------------------
ALTER TABLE "public"."Database_monitoring" ADD CONSTRAINT "Database_monitoring_pkey" PRIMARY KEY ("id");

# test code views
