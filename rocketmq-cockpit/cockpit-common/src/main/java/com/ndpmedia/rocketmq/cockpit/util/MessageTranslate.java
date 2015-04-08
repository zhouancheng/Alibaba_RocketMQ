package com.ndpmedia.rocketmq.cockpit.util;

import com.alibaba.rocketmq.common.message.*;
import com.ndpmedia.rocketmq.cockpit.model.CockpitMessage;

/**
 * Created by robert.xu on 2015/4/8.
 */
public class MessageTranslate {

    public static CockpitMessage translateFrom(MessageExt message){
        CockpitMessage cockpitMessage = new CockpitMessage();
        cockpitMessage.setMsgId(message.getMsgId());
        cockpitMessage.setTags(message.getTags());
        cockpitMessage.setKeys(message.getKeys());
        cockpitMessage.setTopic(message.getTopic());
        cockpitMessage.setStorTime(message.getStoreTimestamp());
        cockpitMessage.setBody(message.getBody());
        cockpitMessage.setProperties(message.getProperties());
        return cockpitMessage;
    }
}
