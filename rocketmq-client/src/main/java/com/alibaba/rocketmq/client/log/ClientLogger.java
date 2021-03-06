/**
 * Copyright (C) 2010-2013 Alibaba Group Holding Limited
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package com.alibaba.rocketmq.client.log;

import com.alibaba.rocketmq.common.constant.LoggerName;
import org.slf4j.ILoggerFactory;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.lang.reflect.Method;
import java.net.URL;


/**
 * Client通过反射来初始化客户端日志
 * 
 * @author 菱叶<jin.qian@alipay.com>
 * @since 2013-7-24
 */
public class ClientLogger {

    private static Logger log;

    static {
        // 初始化Logger
        initLogger();
        log = LoggerFactory.getLogger(LoggerName.ClientLoggerName);
    }

    private static void initLogger() {
        String logConfigFilePath = System.getProperty("rocketmq.client.log.configFile", System.getenv("ROCKETMQ_CLIENT_LOG_CONFIGFILE"));
        Boolean loadCustomConfig = Boolean.parseBoolean(System.getProperty("rocketmq.client.log.loadconfig", "true"));

        final String log4jResourceFile = System.getProperty("rocketmq.client.log4j.resource.fileName", "log4j_rocketmq_client.xml");

        final String logbackResourceFile = System.getProperty("rocketmq.client.logback.resource.fileName", "logback_rocketmq_client.xml");

        String logHome = System.getProperty("log.home", "${user.home}");
        System.setProperty("log.home", logHome);

        if (loadCustomConfig) {
            try {
                ILoggerFactory iLoggerFactory = LoggerFactory.getILoggerFactory();
                Class classType = iLoggerFactory.getClass();
                if (classType.getName().equals("org.slf4j.impl.Log4jLoggerFactory")) {
                    Class<?> DOMConfigurator = null;
                    Object DOMConfiguratorObj = null;
                    DOMConfigurator = Class.forName("org.apache.log4j.xml.DOMConfigurator");
                    DOMConfiguratorObj = DOMConfigurator.newInstance();
                    if (null == logConfigFilePath) {
                        // 如果应用没有配置，则使用jar包内置配置
                        Method configure = DOMConfiguratorObj.getClass().getMethod("configure", URL.class);
                        URL url = ClientLogger.class.getClassLoader().getResource(log4jResourceFile);
                        configure.invoke(DOMConfiguratorObj, url);
                    } else {
                        Method configure = DOMConfiguratorObj.getClass().getMethod("configure", String.class);
                        configure.invoke(DOMConfiguratorObj, logConfigFilePath);
                    }

                } else if (classType.getName().equals("ch.qos.logback.classic.LoggerContext")) {
                    Class<?> joranConfigurator = null;
                    Class<?> context = Class.forName("ch.qos.logback.core.Context");
                    Object joranConfiguratoroObj = null;
                    joranConfigurator = Class.forName("ch.qos.logback.classic.joran.JoranConfigurator");
                    joranConfiguratoroObj = joranConfigurator.newInstance();
                    Method setContext = joranConfiguratoroObj.getClass().getMethod("setContext", context);
                    setContext.invoke(joranConfiguratoroObj, iLoggerFactory);
                    if (null == logConfigFilePath) {
                        // 如果应用没有配置，则使用jar包内置配置
                        URL url = ClientLogger.class.getClassLoader().getResource(logbackResourceFile);
                        Method doConfigure = joranConfiguratoroObj.getClass().getMethod("doConfigure", URL.class);
                        doConfigure.invoke(joranConfiguratoroObj, url);
                    } else {
                        Method doConfigure = joranConfiguratoroObj.getClass().getMethod("doConfigure", String.class);
                        doConfigure.invoke(joranConfiguratoroObj, logConfigFilePath);
                    }
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }


    public static Logger getLog() {
        return log;
    }

    public static Logger getLog(String name){
        return LoggerFactory.getLogger(name);
    }


    public static void setLog(Logger log) {
        ClientLogger.log = log;
    }
}
