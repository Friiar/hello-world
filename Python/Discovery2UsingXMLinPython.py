xml_str = '<interfaces><interface>Eth1/1</interface></interfaces>'
from lxml import etree
xml_data = etree.fromstring(xml_str)
type(xml_str)
type(xml_data)
print xml_data
intf = xml_data.find('.//interface')
intf
intf.text
#  There is no actual interface Eth 1/1 on this device.  Try 2/1 as an example

show_ver_xml_str = """
<nf:rpc-reply xmlns:nf="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns="http://www.cisco.com/nxos:1.0:sysmgrcli">
 <nf:data>
  <show>
   <version>
    <__XML__OPT_Cmd_sysmgr_show_version___readonly__>
     <__readonly__>
      <header_str>Cisco Nexus Operating System (NX-OS) Software
TAC support: http://www.cisco.com/tac
Documents: http://www.cisco.com/en/US/products/ps9372/tsd_products_support_series_home.html
Copyright (c) 2002-2016, Cisco Systems, Inc. All rights reserved.
The copyrights to certain works contained herein are owned by
other third parties and are used and distributed under license.
Some parts of this software are covered under the GNU Public
License. A copy of the license is available at
http://www.gnu.org/licenses/gpl.html.

NX-OSv is a demo version of the Nexus Operating System
</header_str>
      <loader_ver_str>N/A</loader_ver_str>
      <kickstart_ver_str>7.3(1)D1(1) [build 7.3(1)D1(0.10)]</kickstart_ver_str>
      <sys_ver_str>7.3(1)D1(1) [build 7.3(1)D1(0.10)]</sys_ver_str>
      <kick_file_name>bootflash:///titanium-d1-kickstart.7.3.1.D1.0.10.bin</kick_file_name>
      <kick_cmpl_time> 1/11/2016 16:00:00</kick_cmpl_time>
      <kick_tmstmp>02/22/2016 23:39:33</kick_tmstmp>
      <isan_file_name>bootflash:///titanium-d1.7.3.1.D1.0.10.bin</isan_file_name>
      <isan_cmpl_time> 1/11/2016 16:00:00</isan_cmpl_time>
      <isan_tmstmp>02/23/2016 01:43:36</isan_tmstmp>
      <chassis_id>NX-OSv Chassis</chassis_id>
      <module_id>NX-OSv Supervisor Module</module_id>
      <cpu_name>Intel(R) Xeon(R) CPU E7-4830</cpu_name>
      <memory>3064756</memory>
      <mem_type>kB</mem_type>
      <proc_board_id>TMC008010FB</proc_board_id>
      <host_name>nxosv</host_name>
      <bootflash_size>1582402</bootflash_size>
      <kern_uptm_days>0</kern_uptm_days>
      <kern_uptm_hrs>0</kern_uptm_hrs>
      <kern_uptm_mins>24</kern_uptm_mins>
      <kern_uptm_secs>4</kern_uptm_secs>
      <manufacturer>Cisco Systems, Inc.</manufacturer>
     </__readonly__>
    </__XML__OPT_Cmd_sysmgr_show_version___readonly__>
   </version>
  </show>
 </nf:data>
</nf:rpc-reply>
"""
show_ver_xml_data = etree.fromstring(show_ver_xml_str)
show_ver_xml_data
hostname = show_ver_xml_data.find('.//{http://www.cisco.com/nxos:1.0:sysmgrcli}host_name')

hostname.text
print hostname.text




