How to obtain an RSA key pair

1. Generate a new RSA key pair:

   ssh-keygen -t rsa -b 2048

   This creates the key pair in ~/.ssh/ (private key: id_rsa, public key: id_rsa.pub).

2. View the public key:

   cat ~/.ssh/id_rsa.pub

   Example output:

   ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC... username@yourcomputer

   Copy this public key wherever it needs to be registered (e.g. a server's
   ~/.ssh/authorized_keys file or a Git hosting service). Never share the
   private key (id_rsa).
