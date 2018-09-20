# Ansible Get Device Serial Numbers

This project will query an arbitrary number of Cisco IOS devices, get their hostname, model, and all serial numbers in the stack.

Ansible will generate a text file named `<hostname>-inventory.txt` for each queried hostname in the `configs/inventories` directory.
 
Optionally, use the `merge-files.py` script to merge all individiual output files in `configs/` to a single merged file in named `<source-folder>-merged.txt`

## Getting started

### Initial Setup

- Download or clone from: [Ansible Get Serials](https://github.com/devinbmiller/ansible-get_serials)
  * If cloning via **Git**:
    * Create a directory for the project and change to the new directory
    * Clone the project with `git clone https://github.com/devinbmiller/ansible-get_serials.git`
### Usage
1. Create Ansible Vault file named `vault.yml` for connection credentials variables or generate vault strings and place in `group_vars/all/`
 * **Required Vault Variables**:
   * vault_username
   * vault_password
   * vault_access_secret
   * vault_distro_secret
2. Edit or create a host inventory file to run the play against:
  - A sample inventory with required groups is located in `inventory/hosts`
3. Edit `get_serials.yml` file:
  - confirm that the inventory group next to the `hosts:` key is correct for the inventory you want the play to run against
  - by default it will run against all hosts in the ios group
4. Run the Ansible playbook:
  - `ansible-playbook --ask-vault-pass -i inventory/<inventory_file> get_serials.yml`
  - text files will be generated for each host in the `configs/inventories` directory
5. **Optional**
  - Merge the individual files in `configs/inventories` to a single file named `<source-folder->merged.txt` by running `python merge-files.txt <source-folder>`
