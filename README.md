# Ansible Get Device Serial Numbers

This project will query an arbitrary number of Cisco IOS devices, get their hostname, model, and all serial numbers in the stack.

Ansible will generate a text file named `<hostname>-inventory.txt` for each queried hostname in the `configs` directory.
 

## Getting started

### Initial Setup

- Download or clone from: [Ansible Get Serials](https://github.com/devinbmiller/ansible-get_serials)
  * If cloning via **Git**:
    * Create a directory for the project and change to the new directory
    * Clone the project with `git clone https://github.com/devinbmiller/ansible-get_serials.git`
### Usage
1. Create Ansible Vault file named `vault_creds.yml` for connection credentials variables or generate vault strings and place in `group_vars/all.yml`
 * **Required Vault Variables**
  * vault_username
  * vault_password
  * vault_access_secret
  * vault_distro_secret
2. Edit or create an inventory to run the play against.
  - A sample inventory with required groups is located in `inventory/hosts`
