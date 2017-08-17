# -*- coding: utf-8 -*-
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def test_functions_get_nodes_of_type_unknown(parser):
    parser.parse_literal("""
tosca_definitions_version: tosca_simple_yaml_1_0
node_types:
  MyType:
    properties:
      my_parameter:
        type: string
topology_template:
  node_templates:
    my_node:
      type: MyType
      properties:
        my_parameter: { get_nodes_of_type: unknown }
""", import_profile=True).assert_failure()


def test_functions_get_nodes_of_type(parser):
    parser.parse_literal("""
tosca_definitions_version: tosca_simple_yaml_1_0
node_types:
  MyType:
    properties:
      my_parameter:
        type: list
        entry_schema: string
topology_template:
  node_templates:
    my_node:
      type: MyType
      properties:
        my_parameter: { get_nodes_of_type: MyType }
""", import_profile=True).assert_success()


# Unicode

def test_functions_get_nodes_of_type_unicode(parser):
    parser.parse_literal("""
tosca_definitions_version: tosca_simple_yaml_1_0
node_types:
  類型:
    properties:
      參數:
        type: list
        entry_schema: string
topology_template:
  node_templates:
    模板:
      type: 類型
      properties:
        參數: { get_nodes_of_type: 類型 }
""", import_profile=True).assert_success()