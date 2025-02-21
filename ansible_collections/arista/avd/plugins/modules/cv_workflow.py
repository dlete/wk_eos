# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

DOCUMENTATION = r"""
---
module: cv_workflow
version_added: "4.7.0"
author: Arista Ansible Team (@aristanetworks)
short_description: Deploy various objects to CloudVision
description: |-
  The `arista.avd.cv_workflow` module is an Ansible Action Plugin providing the following capabilities:

  - Verify Devices are in the CloudVision inventory.
  - Verify Devices are in the Inventory & Topology Studio.
  - Update the Device hostname in the Inventory & Topology Studio as needed.
  - Create Workspace and build, submit, abandon as needed.
  - Deploy EOS configurations using "Static Configlet Studio".
  - Create and associate Device and Interface Tags.
  - Approve, run, cancel Change Controls as needed.
options:
  cv_servers:
    description: List of hostnames or IP addresses for CloudVision instance to deploy to.
    type: list
    elements: str
    required: true
  cv_token:
    description: Service account token. It is strongly recommended to use Vault for this.
    type: str
    required: true
  cv_verify_certs:
    description: Verifies CloudVison server certificates.
    type: bool
    default: true
  configuration_dir:
    description: Path to directory containing .cfg files with EOS configurations.
    required: true
    type: str
  structured_config_dir:
    description: |-
      Path to directory containing files with AVD structured configurations.
      If found, the `serial_number` or `system_mac_address` will be used to identify the Device on CloudVision.
      Any tags found in the structured configuration metadata will be applied to the Device and/or Interfaces.
    required: true
    type: str
  structured_config_suffix:
    description: File suffix for AVD structured configuration files.
    default: "yml"
    type: str
  device_list:
    description: List of devices to deploy. The names are used to find AVD structured configuration and EOS configuration files.
    type: list
    required: true
    elements: str
  strict_tags:
    description: If `true` other tags associated with the devices will get removed. Otherwise other tags will be left as-is.
    type: bool
    default: false
  skip_missing_devices:
    description: If `true` anything that can be deployed will get deployed. Otherwise the Workspace will be abandoned on any issue.
    type: bool
    default: false
  configlet_name_template:
    description: Python String Template to use for creating the configlet name for each device configuration.
    type: str
    default: "AVD-${hostname}"
  workspace:
    description: CloudVision Workspace to create or use for the deployment.
    type: dict
    suboptions:
      name:
        description: Optional name to use for the created Workspace. By default the name will be `AVD <timestamp>`.
        type: str
      description:
        description: Optional description to use for the created Workspace.
        type: str
      id:
        description: Optional ID to use for the created Workspace. If there is already a workspace with the same ID, it must be in the 'pending' state.
        type: str
      requested_state:
        description: |-
          The requested state for the Workspace.

          - `pending`: Leave the Workspace in pending state.
          - `built`: Build the Workspace but do not submit.
          - `submitted` (default): Build and submit the Workspace.
          - `abandoned`: Build and then abandon the Workspace.
              Used for dry-run where no changes will be committed to CloudVision.
          - `deleted`: Build, abort and then delete the Workspace.
              Used for dry-run where no changes will be committed to CloudVision and the temporary Workspace will be removed to avoid "clutter".
        type: str
        default: built
        choices: ["pending", "built", "submitted", "abandoned", "deleted"]
      force:
        description: Force submit the workspace even if some devices are not actively streaming to CloudVision.
        type: bool
        default: false
  change_control:
    description: CloudVision Change Control to create for the deployment.
    type: dict
    suboptions:
      name:
        description: Optional name to use for the created Change Control. By default the name generated by CloudVision will be kept.
        type: str
      description:
        description: Optional description to use for the created Change Control.
        type: str
      requested_state:
        description: |-
          The requested state for the Change Control.

          - `pending approval` (default): Leave the Change Control in "pending approval" state.
          - `approved`: Approve the Change Control but do not start.
          - `running`: Approve and start the Change Control. Do not wait for the Change Control to be completed or failed.
          - `completed`: Approve and start the Change Control. Wait for the Change Control to be completed.
        type: str
        default: pending approval
        choices: ["pending approval", "approved", "running", "completed"]
  timeouts:
    description: Timeouts for long running operations. May need to be adjusted for large inventories.
    type: dict
    suboptions:
      workspace_build_timeout:
        description: Time to wait for Workspace build before failing.
        type: float
        default: 300.0
      change_control_creation_timeout:
        description: Time to wait for Change Control creation before failing.
        type: float
        default: 300.0
  return_details:
    description: |-
      If `true` all details will be returned to Ansible and can be registered.
      For large inventories this can affect performance, so it is disabled by default.
    type: bool
    default: false
notes:
  - |-
    When interacting with CVaaS the regional URL where the tenant is deployed should be used, e.g:
    `cv_servers: [ www.cv-prod-euwest-2.arista.io ]`
    To see the full list of regional URLs, please visit the [cv_deploy](../../../roles/cv_deploy/README.md#overview)
    role documentation.
  - |-
    To generate service accounts check [cv_deploy](../../../roles/cv_deploy/README.md#steps-to-create-service-accounts-on-cloudvision)
    role documentation or the CloudVision Help Center.
"""

EXAMPLES = r"""
---
- name: Configuration deployment with CVP
  hosts: FABRIC
  connection: local
  gather_facts: false
  tasks:
    - name: Provision CVP with AVD configuration
      run_once: true
      delegate_to: localhost
      arista.avd.cv_workflow:
        cv_servers: [ "www.arista.io" ]
        cv_token: "<insert vaulted service account token here>"
        # cv_verify_certs: True
        configuration_dir: "{{ inventory_dir }}/intended/configs"
        structured_config_dir: "{{ inventory_dir }}/intended/structured_configs"
        # structured_config_suffix: "yml"
        device_list: "{{ ansible_play_hosts }}"
        # strict_tags: false
        # skip_missing_devices: false
        # configlet_name_template: "AVD-${hostname}"
        workspace:
        #   name:
        #   description:
        #   id: <uuid or similar>
          requested_state: submitted
          force: True
        change_control:
        #   name:
        #   description:
          requested_state: "approved"
        # timeouts:
        #   workspace_build_timeout: 300.0
        #   change_control_creation_timeout: 300.0
        # return_details: false
"""

# TODO: RETURN
