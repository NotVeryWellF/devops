# Vagrant
By using vagrant and vagrant virtualbox provider we can easily create VM for our needs.

We can also use other features of the vagrant, for example: \
- We can start a new vm from Vagrantfile by `vagrant up`
- Connect to the VM by `vagrand ssh`
- Stop VM by `vagrant halt`
- Check status of the VM by `vagrant status`
- Destroy VM by `vagrant destroy` \
And many more.

In my Vagrantfile I used `bento/ubuntu-18.04` (it was used in the tutorial I've read), VM has 1024 Mb of ram and 1 cpu.