# About this file
Operation instructions.
Source: [Arista Netdevops Community](https://github.com/arista-netdevops-community/avd-quickstart-containerlab)

My understanding:
Can run with, or without, starting the containerlab container.
* If not starting. 
  * starts containerlab container, issues command and leaves. and so on.
* If starting.
  * containerlabs is run from the container
  * ansible is run from the container

Follow steps in page up to #5 
## Option 1
Run container with containerlabs and ansible in interactive mode
execute #8 make run(start containerlab container in interactive mode, applies ip .1)
sudo containerlab deploy --reconfigure -t avd_lab/clab/avd_lab.clab.yml

manage the nodes
option A
ssh to the nodes

option B
issue: make avd_build_eapi
or manually:
➜  (AVD 🐳) anc_avd-quickstart-containerlab make avd_build_eapi
if [ "True" = "True" ]; then \
        cd /workspace/wk_eos/containerlabs/anc_avd-quickstart-containerlab/avd_lab; ansible-playbook playbooks/fabric-deploy-eapi.yml ; \
else \
        docker run --rm -it --privileged \
                --network host \
                -v /var/run/docker.sock:/var/run/docker.sock \
                -v /etc/hosts:/etc/hosts \
                --pid="host" \
                -w /workspace/wk_eos/containerlabs/anc_avd-quickstart-containerlab/avd_lab \
                -v /workspace/wk_eos/containerlabs/anc_avd-quickstart-containerlab:/workspace/wk_eos/containerlabs/anc_avd-quickstart-containerlab \
                -v /workspace/wk_eos/containerlabs/anc_avd-quickstart-containerlab/99-zceos.conf:/etc/sysctl.d/99-zceos.conf:ro \
                -e AVD_GIT_USER="Daniel Lete" \
                -e AVD_GIT_EMAIL="daniel.lete@heanet.ie" \
                avd-quickstart:latest ansible-playbook playbooks/fabric-deploy-eapi.yml ; \
fi

make clab_destroy
exit the contianerlab

## Option 2
Do not run container with containerlabs and ansible in interactive mode
#11: make clab_deploy

