#
# This file is part of amplet2.
#
# Copyright (c) 2013-2016 The University of Waikato, Hamilton, New Zealand.
#
# Author: Brendon Jones
#
# All rights reserved.
#
# This code has been developed by the University of Waikato WAND
# research group. For further information please see http://www.wand.net.nz/
#
# amplet2 is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# In addition, as a special exception, the copyright holders give
# permission to link the code of portions of this program with the
# OpenSSL library under certain conditions as described in each
# individual source file, and distribute linked combinations including
# the two.
#
# You must obey the GNU General Public License in all respects for all
# of the code used other than OpenSSL. If you modify file(s) with this
# exception, you may extend this exception to your version of the
# file(s), but you are not obligated to do so. If you do not wish to do
# so, delete this exception statement from your version. If you delete
# this exception statement from all source files in the program, then
# also delete it here.
#
# amplet2 is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with amplet2. If not, see <http://www.gnu.org/licenses/>.
#

import ampsave.tests.tcpping_pb2
from ampsave.common import getPrintableAddress, getPrintableDscp

def get_data(data):
    """
    Extract the test results from the protocol buffer data.
    """

    results = []
    msg = ampsave.tests.tcpping_pb2.Report()
    msg.ParseFromString(data)

    for i in msg.reports:
        results.append(
            {
                "target": i.name if len(i.name) > 0 else "unknown",
                "port": msg.header.port,
                "address": getPrintableAddress(i.family, i.address),
                "rtt": i.rtt if i.HasField("rtt") else None,
                "replyflags": {
                    "fin": i.flags.fin,
                    "syn": i.flags.syn,
                    "rst": i.flags.rst,
                    "psh": i.flags.psh,
                    "ack": i.flags.ack,
                    "urg": i.flags.urg,
                } if i.HasField("rtt") else None,
                "icmptype": i.icmptype if i.HasField("icmptype") else None,
                "icmpcode": i.icmpcode if i.HasField("icmpcode") else None,
                "packet_size": msg.header.packet_size,
                "random": msg.header.random,
                "loss": 0 if i.HasField("rtt") or i.HasField("icmptype") or i.HasField("icmpcode") else 1,
                "dscp": getPrintableDscp(msg.header.dscp),
            }
        )

    return results

# vim: set sw=4 tabstop=4 softtabstop=4 expandtab :
