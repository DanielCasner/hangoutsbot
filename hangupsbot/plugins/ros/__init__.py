"""
Hangoutsbot plugin for interacting with the Robot Operating System (ROS)
When loaded, this plugin makes hangoutsbot into a ROS node which can subscribe to and also publish topics.
Most configuration is done through the environmental variables which control ROS nodes in general but hangoutsbot
specific functionality is done through bot commands.
"""
__LICENSE__ = """
The BSD License
Copyright (c) 2016, Daniel Casner
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
__author__ = "Daniel Casner <www.artificelab.com>"

import time
import aiohttp, asyncio, io, logging
import plugins
import rospy, std_msgs

logger = logging.getLogger(__name__)

def _initalize(bot):
    rospy.init_node("Hangoutsbot")
    plugins.register_user_command(["rostopic"])
    
def showme(bot, event, *args):
    """Implement rostopic command line tool like functionality through the bot"""
    yield from bot.coro_send_message(event.conv, _("Nothing implemented yet"))
